# Layout analyzer preview experiment

The root `vaadin-layout-analyzer-preview-0.1.1.tgz` is an unmodified Apache-2.0
preview. It measures rendered Vaadin components using Copilot's internal Inspect
API and returns geometry, heuristic findings and structural peer comparisons.
It needs development mode, Copilot, Node >=22 and Chromium. It neither reads the
reference screenshot nor knows the intended design, so it supplements screenshots
and browser interaction checks; it must not become the grading oracle.

Upstream alignment (2026-10-01): the visual tasks now use the upstream
Vaadin 25.3.0 / Spring Boot 4.1.1 starter and standard Playwright CLI.
Agents have no `ui-check`, grading contracts, or custom `app-start` helpers.
The recorded Luna pilot predates these task and grading changes; repeat both
arms on the current tasks before comparing results.

## Run a controlled comparison

```sh
# API-key users export OPENAI_API_KEY. For an existing Codex subscription:
export CODEX_FORCE_AUTH_JSON=1

# Start with one task. Each arm runs with Copilot enabled.
for mode in control geometry full; do
  uv run vaadin-bench.py -c vanilla -m openai/gpt-6-luna -t flow-employee-list-strict \
    -k 1 -n 1 --layout-analyzer "$mode" -- --ak reasoning_effort=xhigh
done

# Once the pilot works, cover all eight visual tasks (strict and lenient).
uv run vaadin-bench.py -c vanilla -m openai/gpt-6-luna -k 1 -n 2 \
  --layout-analyzer full -- --ak reasoning_effort=xhigh
```

`control` enables Copilot without installing or mentioning the analyzer.
`geometry` supplies the report without relationships. `full` includes
relationships. They all keep the same ordinary browser tools, task requirements,
grader and resource limits. Normal runs without the flag keep Copilot disabled.
The experiment defaults to one concurrent trial and accepts at most three.
Account for other Harbor processes when selecting concurrency. Use an explicit model ID such as `-m openai/gpt-6-luna` to select only
GPT-6 Luna; the substring `luna` can match multiple generations in the model table.

The option stages content-addressed copies under `.layout-analyzer/<mode>/<hash>`
and prints the resulting plain Harbor command with `--dry-run`. The adjacent
`manifest.json` records SHA-256s of the tasks, helper code and archive. Only the
agent Dockerfile and its instruction change; the original task files and all
verifier files stay intact. npm dependencies are locked and installed during the
image build. The image build installs the Chromium revision required by the adapter’s pinned
Playwright version. The upstream CLI can use a different browser revision;
captures must not depend on that revision being compatible. No runtime package
installation or network access is needed. Reports live
under `/logs/agent/layout`, outside the submitted `/app`.

The supported tasks are the employee-list, payroll, orders and reports pairs.
The project-generation, migration, basic new-view and filtering tasks have
different toolchains or goals and are not silently included in this experiment.

Report arms put a short first-render reminder before the task and the detailed
command guide after it. The intended loop is implement → render → capture →
check the design and fix relevant issues. Offering a report only after completing
the view can miss the part of development where geometry feedback is useful.

## Use the report during implementation

```sh
# In a separate terminal, start the application:
mvn spring-boot:run
# Once the view is ready, capture it from another terminal:
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

Export trial-level outcomes, token usage, capture costs, individual browser-test
outcomes and the verifier's design checks without averaging unlike tasks:

```sh
uv run python scripts/summarize-layout-experiment.py jobs > layout-results.json
```

Keep the staged manifests when moving results; the exporter uses their recorded
mode, not a guessed label. Missing rewards and token counts stay null, and capture
failures remain visible alongside successful captures.

## Agent trials

[Per-trial measurements](layout-analyzer-agent-results.json) record Luna/xhigh
runs, including failures and missing analyzer usage. These are single attempts
on a shared host. Copilot was enabled in every arm.

The first employee-list strict trial used full reports with an appended command
guide. The agent never invoked the analyzer and reached the one-hour limit.
Its final reward was 0: all 431 measured geometry/style assertions passed, but
14 of 16 screenshot regions failed, selection returned the wrong employee, and
the closed Grid overflowed at 900 px. This is evidence of an adoption problem,
not an analyzer quality result. It also shows why measured geometry alone cannot
replace interaction, breakpoint and screenshot checks.

Subsequent runs prepended a first-render reminder and retained detailed commands
after the task. The experiment was stopped before a completed comparison was
available. The snapshots record this protocol change; these trials do not
establish a development benefit.

## Compatibility and limitations

The modern benchmark stack now targets Vaadin 25.3.0. The measurements below and
the recorded agent trials are historical 25.2 results; upgrading the runtime is
a separate change from adding the analyzer. Future comparisons must use the same
runtime in both arms. The upgrade retains Lumo and the existing design references.

The employee reference smoke also passes on Vaadin / Flow / Copilot 25.3.0:
desktop/mobile captures, truncation, restoration after errors, new overflow
detection, prepared state and explicit failure with Copilot disabled. The reports
still contain 33/16 visible components and zero source references; the visible
detail subtree remains absent, so the partial-coverage warning is still needed.

The package README only claims testing on Vaadin/Copilot 25.3.0-beta3. The initial
local employee-list reference smoke also succeeded on this benchmark's Vaadin
25.2.6 / Copilot 25.2.5 with Lumo. Desktop and mobile reports had stable geometry
and loaded fonts, but no source references and no repeated relationships. The
smoke exercises geometry-only/full reports, truncation, restoration after an
error and recapture after introducing horizontal overflow. It is a compatibility
test against a reference solution, separate from held-out agent trials.

The [recorded reference captures](layout-analyzer-smoke-results.json) also cover
Orders, Payroll and Reports at 1440×1024 and 720×900, in both report modes:

| View | Visible components, desktop/mobile | Full report characters, desktop/mobile | Relationships |
| --- | ---: | ---: | --- |
| Employee list | 33 / 16 | 4,758 / 3,037 | none |
| Orders | 52 / 35 | 6,101 / 5,296 | none |
| Payroll | 42 / 25 | 5,618 / 4,267 | none |
| Reports | 58 / 41 | 6,941 / 5,424 | one consistent summary-metric inset; no exceptions |

All 16 captures had stable geometry, ready fonts and zero source references.
The extra views' cold captures took 13–22 seconds end to end on a shared host;
employee recaptures reused one page and should not be compared to those cold
starts. The reference designs still generated 3–7 findings each. Reports'
relationship concerns its three summary metrics, not its repeated cards.
A separate prepared-state capture filtered Reports to Sweden and correctly
captured the two remaining cards. These observations support using geometry for
targeted debugging; they do not establish a development-time or quality gain.

Source-line lookup is unavailable on this Copilot version. Hidden states and
virtualized Grid contents are incomplete, and stable geometry does not prove
asynchronous work is complete. Intentional whitespace, ellipsis and scrolling
can trigger findings. Relationship matching is structural, with physical-edge
assumptions, not semantic design knowledge. Copilot also attempts background
release-note downloads on the restricted network; these can add noise and cost,
which is why all three comparison arms enable it.

The prepared employee drawer exposed an additional compatibility issue:
Copilot 25.2.5 omits the visible dynamic `MasterDetailLayout` detail subtree.
The report still marks geometry stable and measures 33 components, while the
screenshot shows the fields. The adapter now checks whether the readiness
element or any of its descendants appears in Copilot's tree; if absent, it
prints a partial-coverage warning and records it in `capture.json`. This check
does not prove coverage of all descendants when the readiness root is present.
The full screenshot and ordinary tools remain essential for dynamic panels.

The `layout-analyzer` CI workflow builds the actual experiment image, applies
the employee-list reference solution, and captures through real Copilot offline.
It also verifies that disabling Copilot makes the adapter fail explicitly. The
regular validation job checks staging isolation and resolves generated commands
through pinned Harbor.

Fork CI validates the published `ghcr.io/vaadin` images by default. A fork that
publishes its own stack should set the repository Actions variable
`VAADINBENCH_IMAGE_OWNER` to that publisher's namespace; the digest and consistent
stack checks still apply.

## Luna 6 xhigh comparison on Vaadin 25.3

The [2026-09-29 sequential Reports-strict comparison](layout-analyzer-luna6-results.md)
completed with nine successful analyzer captures. Both arms timed out and scored
0. Whole-page similarity improved slightly with the analyzer, but a mobile drawer
interaction failed and token use increased. This pair establishes tool usability,
not a development speed or overall quality improvement.
