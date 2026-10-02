### Rendered layout feedback (preview experiment)

Copilot is enabled in this development environment. Once the view first renders,
run `layout-check` before manual geometry tuning, alongside screenshots and browser interaction checks, to inspect
geometry, clipping, spacing, and repeated structures. Fix only observations that
conflict with the requested design. A warning count is not a quality score.

Start the app with `mvn spring-boot:run`, then capture the task route with a CSS selector
that proves your view's data is ready, for example:

```sh
layout-check http://localhost:8080/employees --ready 'vaadin-grid' --state initial --width 1440 --height 1024
```

Use your actual route and a meaningful readiness selector, including loaded rows
when needed. `--ready` requires a visible element, not just an HTTP response.
The command prints Markdown and a unique report directory under
`/logs/agent/layout/`; JSON, a screenshot, and capture metadata are retained there.
Capture again after edits and at the mobile viewport specified by the task.

For a drawer, tab, filter, or authenticated state, write a module exporting
`async function prepare(page)` and pass `--prepare /absolute/path/state.mjs`.
Use Playwright locators to navigate into the state and wait for its actual data
before returning. `--state drawer-open` records its name. Each invocation starts
a fresh browser context; it does not reuse playwright-cli's session.

The report covers only the current viewport and rendered state. Hidden panels
and virtualized rows are not fully inspected. Check `coverage` and truncation;
source references may be unavailable, so use component paths. A successful,
stable capture can still omit visible virtual children (including the employee
detail panel on the pinned Copilot). A warning is printed and recorded in
`capture.json` when your readiness subtree is absent from Copilot's tree. This
check is conservative; it does not prove every child is measured. Copilot Inspect
mode is restored before the screenshot. Heuristic findings and matching peer
structures do not establish design intent. Screenshots and the task's checks
remain necessary. Do not change dependencies or the target design to silence
this experimental analyzer. If capture fails, read its error and continue with
the ordinary tools; repeated unsuccessful captures waste time.
