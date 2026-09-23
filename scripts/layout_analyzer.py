"""Stage opt-in layout experiments without changing the canonical tasks or grader."""

import hashlib
import json
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "vaadin-layout-analyzer-preview-0.1.1.tgz"
TOOLS = ROOT / "scripts/layout-analyzer"
SUPPORTED = tuple(
    f"flow-{view}-{profile}"
    for view in ("employee-list", "orders", "payroll", "reports")
    for profile in ("strict", "lenient")
)
MODES = ("control", "geometry", "full")


def source_files(directory):
    # Match the repository's build exclusions; never stage local dependencies.
    return sorted(
        p for p in directory.rglob("*") if p.is_file()
        and not set(p.relative_to(directory).parts).intersection(
            {"node_modules", "target", "__pycache__", ".git"}
        )
    )


def stage_tasks(tasks, mode, root=ROOT):
    """Return an immutable, content-addressed Harbor dataset directory.

    Docker builds still use each task's original pinned base and browser tools.
    Only the agent image and instruction gain the experiment. Tests, solution,
    artifact transfer and time/resource limits are copied byte for byte.
    """
    if mode not in MODES:
        raise ValueError(f"Unknown layout analyzer mode: {mode}")
    unsupported = sorted(set(tasks) - set(SUPPORTED))
    if unsupported:
        raise ValueError("Layout experiments support the eight visual tasks; unsupported: "
                         + ", ".join(unsupported))
    inputs = {}
    for name in sorted(tasks):
        directory = root / "tasks" / name
        for path in source_files(directory):
            inputs[str(path.relative_to(root))] = path
    for path in source_files(TOOLS):
        inputs[str(path.relative_to(ROOT))] = path
    inputs[PACKAGE.name] = PACKAGE
    inputs["scripts/layout_analyzer.py"] = Path(__file__)
    hashes = {name: hashlib.sha256(path.read_bytes()).hexdigest()
              for name, path in inputs.items()}
    manifest = {"mode": mode, "inputs": hashes}
    encoded = json.dumps(manifest, sort_keys=True, indent=2) + "\n"
    digest = hashlib.sha256(encoded.encode()).hexdigest()
    cache = root / ".layout-analyzer"
    destination = cache / mode / digest
    if destination.exists():
        return destination / "tasks"
    cache.mkdir(exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".stage-", dir=cache))
    try:
        for name, source in inputs.items():
            if not name.startswith("tasks/"):
                continue
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        for name in tasks:
            task = staging / "tasks" / name
            environment = task / "environment"
            with (environment / "Dockerfile").open("a") as dockerfile:
                dockerfile.write("\n# Opt-in layout experiment; the verifier is unchanged.\n"
                                 "ENV JAVA_TOOL_OPTIONS=-Dvaadin.copilot.enable=true\n")
                if mode != "control":
                    tools = environment / "layout-analyzer"
                    tools.mkdir()
                    for source in source_files(TOOLS):
                        target = tools / source.relative_to(TOOLS)
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(source, target)
                    shutil.copy2(PACKAGE, tools / "preview.tgz")
                    dockerfile.write(
                        "COPY layout-analyzer /opt/vaadinbench/layout-analyzer\n"
                        "RUN cd /opt/vaadinbench/layout-analyzer "
                        "&& PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm ci --ignore-scripts --no-audit --no-fund "
                        "&& ln -s /opt/vaadinbench/layout-analyzer/capture.mjs /usr/local/bin/layout-check "
                        "&& layout-check --help\n"
                        f"ENV VB_LAYOUT_MODE={mode}\n"
                    )
            if mode != "control":
                instruction = task / "instruction.md"
                instruction.write_text(
                    "Layout experiment: run `layout-check` after the first working render, "
                    "before manual geometry tuning. Capture the task's desktop and mobile "
                    "states, then use the report alongside screenshots and `ui-check`. "
                    "The command guide follows the task below.\n\n"
                    + instruction.read_text() + "\n\n" + (TOOLS / "instructions.md").read_text()
                )
        (staging / "manifest.json").write_text(encoded)
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            staging.rename(destination)
        except OSError:
            if not destination.exists():
                raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return destination / "tasks"
