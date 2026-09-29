# Luna 6 xhigh: vanilla versus layout analyzer

On 2026-09-29, one sequential pair on `flow-reports-strict` showed that the
analyzer works and is used, but did not establish a development speed or overall
quality improvement. Both trials exhausted the one-hour agent budget and scored
0. The analyzer trial improved whole-page screenshot similarity, but retained a
mobile drawer interaction failure that the baseline did not have.

## Controlled setup

Source commit: `d09a6aaaf9c9a297e6f5b35720c4fac8e82e2c7e`. Both arms used the
locally validated Vaadin 25.3.0 images, Codex `openai/gpt-6-luna`, `xhigh`, the
`vanilla` condition, one attempt, two CPUs, 4 GiB RAM, and a 3600-second agent
budget. The baseline ran first, then the analyzer arm; no trials in this pair
overlapped. Two pre-existing containers belonged to another benchmark workspace
at launch, so this was not a globally idle host.

Both arms enabled Copilot and retained ordinary browser tools and `ui-check`.
`control` provided no analyzer; `full` added preview 0.1.1 with relationships.
Only agent instructions, agent image setup, and six analyzer support files
differed between staged tasks. Task content and verifier files matched. The
paused analyzer-only feedback changes in the working tree were not included.
The vanilla baseline here is Copilot-enabled to isolate analyzer availability.

Commands, executed from the validated checkout with local image pins:

```sh
export CODEX_FORCE_AUTH_JSON=1
for mode in control full; do
  python3 vaadin-bench.py -c vanilla -m openai/gpt-6-luna \
    -t flow-reports-strict -k 1 -n 1 --layout-analyzer "$mode" \
    --job-name "luna6-visual-$mode" \
    -o /tmp/luna6-visual-comparison-20260929 \
    -- --ak reasoning_effort=xhigh
done
```

The saved Harbor configuration and actual Codex invocation confirmed `xhigh`.

## Final verifier results

| Measurement | Vanilla / control | Analyzer / full |
|---|---:|---:|
| Reward | 0 | 0 |
| Agent outcome | Timeout | Timeout |
| Agent time, including timeout cleanup | 3604.58 s | 3604.70 s |
| Browser tests passing | 6/7 | 5/7 |
| Explicit design/geometry checks passing | 224/224 | 224/224 |
| Whole-page SSIM (required ≥0.95) | 0.924132 | 0.934716 |
| Screenshot regions passing | 1/8 | 1/8 |
| Completed UI-check commands | 6 | 2 |
| Completed Playwright commands | 32 | 30 |
| Successful analyzer captures | 0 | 9 |
| Input tokens, including cache | 9,528,176 | 20,262,364 |
| Cached input tokens | 9,219,584 | 19,954,048 |
| Uncached input tokens | 308,592 | 308,316 |
| Output tokens | 77,636 | 113,100 |
| Harbor estimated cost, USD | 0.161873 | 0.286922 |

Cost figures are Harbor estimates, not verified charges; both runs used Codex
subscription authentication. Aggregate input includes repeated cached context.
Output increased 45.7%; uncached input was essentially unchanged. Both runs
were censored at the time limit, so neither establishes time to completion.

The analyzer arm improved sidebar, header, summary and filter similarity, but
all three card-row regions were slightly worse. Both arms failed strict visual
fidelity. All five behavior tests passed in both. Only the analyzer arm failed
responsive live resizing: the open drawer intercepted clicks on the menu toggle.
These are model-output failures, not failures of the benchmark reference controls.

## Actual use and issues

- Nine captures succeeded: five desktop, three mobile closed-drawer, and one
  mobile open-drawer state using a prepare module. The agent captured before
  geometry changes and recaptured afterward. Total capture time was 119.483 s;
  reports totaled 62,751 characters. No report was truncated, all readiness
  elements appeared in the Copilot tree, and all captures confirmed Copilot.
  This readiness check does not prove complete component coverage.
- Every capture had zero source references. The agent still used direct DOM and
  shadow-DOM queries to investigate component styling. The tool did not replace
  those inspections.
- The agent explicitly credited layout feedback for noticing the footer avatar's
  outer size. Later reports continued to mark avatar content as clipped: 39 px
  of content in a 32 px inner box, despite the outer avatar matching 36 px. The
  agent treated this as internal SVG text bounds rather than visible overflow.
  This is a suspected noisy heuristic, not a proven analyzer bug.
- Reports also flagged intentional internal scrolling, a 25 px gap off the
  theme spacing scale, and unequal summary widths. These must be checked against
  design intent, not automatically “fixed.”
- The analyzer agent spent multiple calls investigating a Copilot development
  notice and added `hidePopover()`/MutationObserver code to the submitted view,
  plus CSS hiding `copilot-main`. This is unwanted development-tool coupling in
  application code. Copilot was enabled in both arms, so the pair does not prove
  the analyzer caused that detour. Capture/UI-check integration should handle
  overlays consistently, without asking agents to patch application code.
- The prepared drawer-open capture succeeded but did not establish clickability.
  The final interaction verifier found the blocked menu toggle. Layout analysis
  is not a replacement for interaction tests or screenshot comparison.

## Recommendation

Keep the analyzer opt-in. It supplies usable geometry and supports iterative
captures, but this pair is not evidence to roll it out across all tasks or remove
`ui-check`. Before a broader experiment, address the overlay distraction and
investigate the avatar warning, then repeat several sequential matched trials.
A single pair on one hard task cannot separate a tool effect from model variation,
run order, or host load.

[Machine-readable results](layout-analyzer-luna6-results.json) include trial IDs,
region scores, capture metadata, token counts, and artifact paths. Raw trajectories,
patches, screenshots and verifier reports remain under
`/tmp/luna6-visual-comparison-20260929`. The executable local runner is
`/tmp/run-luna6-visual-comparison-20260929.sh`.
