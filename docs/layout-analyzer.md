# Layout analyzer preview experiment

The root `vaadin-layout-analyzer-preview-0.1.1.tgz` is an unmodified Apache-2.0
preview. It measures rendered Vaadin components using Copilot's internal Inspect
API and returns geometry, heuristic findings and structural peer comparisons.
It needs development mode, Copilot, Node >=22 and Chromium. It neither reads the
reference screenshot nor knows the intended design, so it supplements screenshots
and `ui-check`; it must not become the grading oracle.

## Run a controlled comparison

```sh
# API-key users export OPENAI_API_KEY. For an existing Codex subscription:
export CODEX_FORCE_AUTH_JSON=1

# Start with one task. Each arm runs with Copilot enabled.
for mode in control geometry full; do
  uv run vaadin-bench.py -c vanilla -m luna -t flow-employee-list-strict \
    -k 1 -n 1 --layout-analyzer "$mode" -- --ak reasoning_effort=xhigh
done

# Once the pilot works, cover all eight visual tasks (strict and lenient).
uv run vaadin-bench.py -c vanilla -m luna -k 1 -n 2 \
  --layout-analyzer full -- --ak reasoning_effort=xhigh
```

`control` enables Copilot without installing or mentioning the analyzer.
`geometry` supplies the report without relationships. `full` includes
relationships. They all keep the same ordinary browser tools, task requirements,
grader and resource limits. Normal runs without the flag keep Copilot disabled.
The experiment defaults to one concurrent trial and accepts at most three.
Account for other Harbor processes when selecting concurrency. Luna resolves to
the model pinned by this repository's model table, currently GPT-5.6 Luna.

The option stages content-addressed copies under `.layout-analyzer/<mode>/<hash>`
and prints the resulting plain Harbor command with `--dry-run`. The adjacent
`manifest.json` records SHA-256s of the tasks, helper code and archive. Only the
agent Dockerfile and its instruction change; the original task files and all
verifier files stay intact. npm dependencies are locked and installed during the
image build. Captures use the task's existing Chromium and browser settings,
without a second browser download or runtime package installation. Reports live
under `/logs/agent/layout`, outside the submitted `/app`.

The supported tasks are the employee-list, payroll, orders and reports pairs.
The project-generation, migration, basic new-view and filtering tasks have
different toolchains or goals and are not silently included in this experiment.

## Use the report during implementation

```sh
app-start
layout-check http://localhost:8080/employees \
  --ready '[data-testid="employee-grid"]' --state initial \
  --width 1440 --height 1024
```

Readiness belongs to the caller: choose a visible selector that establishes the
required data is loaded, or wait for it in a `--prepare state.mjs` module exporting
`async function prepare(page)`. That function can open a panel, change a filter,
or sign in. Each command opens a fresh context. Capture the relevant mobile
viewport separately. Markdown goes to stdout; JSON, metadata and a screenshot
go to a unique report directory (or the explicit `--out` directory).

`capture.json` records mode, URL, viewport, UI-state label, preparation source,
coverage, report length, truncation, analyzer version, browser version and timing.
Failures return nonzero and retain diagnostic metadata. The complete geometry
remains in `layout.json` when the Markdown budget is exceeded. Copilot's previous
mode is restored by the package, including after capture errors.

## What this can improve, and what to measure

Geometry can answer concrete debugging questions without manually querying each
element: which parent clips a control, which width stays fixed on mobile, or
which repeated card has a different inset. Structural relationships may help the
card-heavy reports view more than a virtualized employee Grid. This is a
hypothesis to test, not an established speed or quality improvement.

Compare the same model/effort, task/profile, attempt count and ordinary condition
across all three arms. Record reward, region SSIM/geometry and interaction
failures from the unchanged verifier, agent duration and token usage from Harbor,
and successful/failed capture counts and report sizes. Review whether edits
actually follow the report and whether they damage intended designs. Count
capture time and extra context as costs. One attempt per arm is a smoke trial;
it cannot establish a causal improvement or a stable success rate.

## Compatibility and limitations

The package README only claims testing on Vaadin/Copilot 25.3.0-beta3. The initial
local employee-list reference smoke also succeeded on this benchmark's Vaadin
25.2.6 / Copilot 25.2.5 with Lumo. Desktop and mobile reports had stable geometry
and loaded fonts, but no source references and no repeated relationships. The
smoke exercises geometry-only/full reports, truncation, restoration after an
error and recapture after introducing horizontal overflow. It is a compatibility
test against a reference solution, separate from held-out agent trials.

Source-line lookup is unavailable on this Copilot version. Hidden states and
virtualized Grid contents are incomplete, and stable geometry does not prove
asynchronous work is complete. Intentional whitespace, ellipsis and scrolling
can trigger findings. Relationship matching is structural, with physical-edge
assumptions, not semantic design knowledge. Copilot also attempts background
release-note downloads on the restricted network; these can add noise and cost,
which is why all three comparison arms enable it.

The `layout-analyzer` CI workflow builds the actual experiment image, applies
the employee-list reference solution, and captures through real Copilot offline.
It also verifies that disabling Copilot makes the adapter fail explicitly. The
regular validation job checks staging isolation and resolves generated commands
through pinned Harbor.
