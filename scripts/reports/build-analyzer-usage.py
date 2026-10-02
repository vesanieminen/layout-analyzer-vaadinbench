"""Build the public, allowlisted evidence report from the local completed study."""
import collections, hashlib, html, json, re, shlex, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / 'jobs/reports-luna6-repeats-20261001-195010'
PILOT = ROOT / 'jobs/reports-luna6-pilot-20261001-180419'
OUT = ROOT / 'site/analyzer-usage'
OUT.mkdir(parents=True, exist_ok=True)
summary = json.loads((STUDY / 'combined-summary.json').read_text())
runs = []
for row in sorted(summary['trials'], key=lambda r:r['pair']):
    if row['mode'] != 'full': continue
    trial = (PILOT if row['pair'] == 1 else STUDY) / row['job'] / row['trial']
    commands, capture_commands, reads = [], {}, []
    for line in (trial / 'agent/codex.txt').read_text().splitlines():
        try: event = json.loads(line)
        except json.JSONDecodeError: continue
        item = event.get('item', {})
        if event.get('type') != 'item.completed' or item.get('type') != 'command_execution': continue
        command = item['command']; commands.append(command)
        if 'layout-check http://localhost:8080/reports' in command:
            match = re.search(r'Layout artifacts: /logs/agent/layout/(capture-\w+)', item.get('aggregated_output',''))
            assert match, command
            parts = shlex.split(command)
            capture_commands[match[1]] = {'shellCommand': parts[-1], 'completedShellCommandOrdinal': len(commands), 'exitCode': item.get('exit_code')}
        elif '/logs/agent/layout/' in command:
            reads.append({'ordinal':len(commands),'command':shlex.split(command)[-1]})
    trajectory = json.loads((trial/'agent/trajectory.json').read_text())
    views = []
    for step in trajectory['steps']:
        for call in step.get('tool_calls',[]) or []:
            args = call.get('arguments',{})
            raw = json.dumps(args)
            if 'view_image' in raw:
                for path in re.findall(r'/logs/agent/layout/capture-[\w]+/[\w.-]+',raw):
                    views.append({'step':step['step_id'],'path':path,'artifactExists':(trial/'agent/layout'/Path(path).parent.name/Path(path).name).exists()})
    captures=[]
    for folder in (trial/'agent/layout').glob('capture-*'):
        meta=json.loads((folder/'capture.json').read_text()); layout=json.loads((folder/'layout.json').read_text())
        target=OUT/'evidence'/f'pair-{row["pair"]}'/folder.name; target.mkdir(parents=True,exist_ok=True)
        for name in ['layout.md','page.png']: shutil.copyfile(folder/name,target/name)
        # Explicit allowlist: no agent logs, environment, browser session files or push URLs.
        public={k:meta.get(k) for k in ['url','state','viewport','mode','ready','prepareSource','capturedAt','status','copilotAvailable','coverage','readyElementInTree','coverageWarnings','reportChars','analyzerVersion','totalDurationMs','reportTruncated']}
        (target/'capture.json').write_text(json.dumps(public,indent=2)+'\n')
        boxes=layout['model']['boxes']; byid={b['index']:b for b in boxes}
        findings=[dict(f, label=byid.get(f.get('box'),{}).get('label')) for f in layout['model']['findings']]
        c=dict(public,artifact=folder.name, evidencePath=str(target.relative_to(OUT)), findings=findings,
               geometry=[{k:b.get(k) for k in ['index','label','tag','x','y','width','height']} for b in boxes],
               markdownSha256=hashlib.sha256((folder/'layout.md').read_bytes()).hexdigest(),**capture_commands[folder.name])
        captures.append(c)
    captures.sort(key=lambda c:c['capturedAt'])
    assert len(captures)==len(capture_commands)
    runs.append({'pair':row['pair'],'trial':row['trial'],'shellCommandEvents':len(commands),
                 'playwrightShellEvents':sum('playwright-cli' in c for c in commands),
                 'helpShellEvents':sum('layout-check --help' in c for c in commands),
                 'artifactReadCommands':reads,'analyzerImageViewReferences':views,'captures':captures})
allcaps=[c for r in runs for c in r['captures']]
assert len(allcaps)==37 and all(c['status']=='ok' for c in allcaps)
data={'sourceCommit':'b78e016e138014909c0a81fc43008d2389623834','model':'openai/gpt-6-luna','effort':'xhigh','runs':runs}
(OUT/'usage.json').write_text(json.dumps(data,indent=2)+'\n')
# Compact outcome data excludes local filesystem and cache manifest paths.
outcomes=[{k:r[k] for k in ['pair','mode','agentSeconds','visualAggregate','reward','uncachedInputTokens','outputTokens']} for r in summary['trials']]
(OUT/'outcomes.json').write_text(json.dumps(outcomes,indent=2)+'\n')
esc=lambda s:html.escape(str(s))
parts=['''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>What the layout analyzer actually did — VaadinBench</title><style>
:root{color-scheme:light}body{font:17px/1.6 system-ui,sans-serif;color:#182b3a;background:#f4f7fa;margin:0}main{max-width:1150px;margin:auto;padding:36px 24px 80px}h1{font-size:clamp(2rem,5vw,3.3rem);line-height:1.15}h2{margin-top:48px}h3{margin-top:30px}a{color:#0759ac}code,pre{font-size:13px}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#edf2f7;padding:16px;border-radius:8px}table{border-collapse:collapse;width:100%;font-size:15px}td,th{padding:12px;text-align:left;border-bottom:1px solid #cbd5df;vertical-align:top}.scroll{overflow:auto}.card{background:white;border:1px solid #d8e1ea;padding:24px;border-radius:12px;margin:20px 0}.metrics{display:flex;flex-wrap:wrap;gap:14px}.metric{flex:1;min-width:150px;background:#e3edf7;padding:18px;border-radius:10px}.metric b{display:block;font-size:30px}small,.muted{color:#506273}summary{cursor:pointer;font-weight:600;padding:12px 0}.images{display:grid;grid-template-columns:1fr 1fr;gap:20px}.images img{width:100%;max-height:650px;object-fit:contain;object-position:top;background:#e9eef2}figure{margin:0}nav a{margin-right:16px}li{margin:8px 0}@media(max-width:650px){.images{grid-template-columns:1fr}main{padding:24px 14px}}
</style></head><body><main><p class="muted">VaadinBench · Evidence report · 2 October 2026</p><h1>What the layout analyzer actually did</h1><p>The analyzer gave the agent a component geometry report and a screenshot of its running Reports view. The agent used that feedback during layout corrections. It did not implement fixes, compare the page to the reference design, or prove the view passed its tests.</p><nav><a href="#usage">Usage counts</a><a href="#changes">Measured changes</a><a href="#commands">Every command</a><a href="#outcomes">Outcomes</a><a href="usage.json">Download usage JSON</a></nav>
<div class="metrics"><div class="metric"><b>37 / 37</b>Successful captures</div><div class="metric"><b>4</b>Analyzer trials</div><div class="metric"><b>21 + 16</b>Desktop + mobile</div><div class="metric"><b>0 / 4</b>Passing analyzer trials</div></div>
<section class="card"><h2 style="margin-top:0">What this establishes</h2><p><strong>The integration worked, and the reports supplied useful layout measurements.</strong> Recorded changes include moving mobile filters almost 500 pixels upward, reducing filter control heights, removing a root-height overflow warning, and correcting a mobile summary overlap.</p><p><strong>The experiment does not establish a consistent quality or speed improvement.</strong> The analyzer runs beat the control on time and visual score in two of four pairs. All eight implementations failed the final verifier. The evidence below distinguishes measured changes from claims about what caused them.</p></section>
<h2>Experiment and method</h2><p>One task, <code>flow-reports-strict</code>, with four independent attempts per arm: vanilla control and analyzer-enabled vanilla. All used <code>openai/gpt-6-luna</code> at <code>xhigh</code>, Vaadin 25.3.0, Copilot enabled, and no agent-facing <code>ui-check</code>. Harbor trials ran sequentially. Pair labels do not imply matched random seeds. The analyzer was preview 0.1.1, with full relationship reports enabled.</p><p>Source commit: <code>b78e016e138014909c0a81fc43008d2389623834</code>. This report audits completed shell events, trajectory image references, capture metadata, geometry reports and final verifier results. Command ordinals are completion order, which can differ from invocation order when an agent starts desktop and mobile captures together.</p>
<h2>How the agent used it</h2><ol><li>Implemented and started the application, then waited for report cards to render.</li><li>Ran <code>layout-check</code> against <code>http://localhost:8080/reports</code> at desktop (1440 × 1024) and mobile (390 × 844) sizes.</li><li>Received the Markdown report directly in command output. Each capture also wrote <code>layout.md</code>, <code>layout.json</code>, <code>capture.json</code> and <code>page.png</code>.</li><li>Read geometry/findings and sometimes opened the generated screenshot or searched a saved report.</li><li>Edited Java/CSS with ordinary coding tools, then captured again to inspect the result.</li></ol><p>The wrapper uses <code>captureLayout</code> from <code>@vaadin/layout-analyzer-preview/playwright</code>. It checks Copilot availability and the ready element’s presence in the component tree. Each call gets a fresh browser context. <code>--state</code> is only a label; it does not interact with the UI.</p>
<h2 id="usage">Exactly how much it was used</h2><div class="scroll"><table><thead><tr><th>Trial</th><th>Captures D / M</th><th>Capture time</th><th>Report characters</th><th>Prepare calls</th><th>Repeated report text¹</th><th>Shell events / Playwright²</th></tr></thead><tbody>''']
for r in runs:
    cs=r['captures'];d=sum(c['viewport']['width']==1440 for c in cs)
    parts.append(f'<tr><td>Pair {r["pair"]}{" (pilot)" if r["pair"]==1 else ""}</td><td>{len(cs)} ({d} / {len(cs)-d})</td><td>{sum(c["totalDurationMs"] for c in cs)/1000:.3f}s</td><td>{sum(c["reportChars"] for c in cs):,}</td><td>{sum(bool(c["prepareSource"]) for c in cs)}</td><td>{len(cs)-len(set(c["markdownSha256"] for c in cs))}</td><td>{r["shellCommandEvents"]} / {r["playwrightShellEvents"]}</td></tr>')
parts.append(f'''</tbody></table></div><p>Total: <strong>{sum(c['totalDurationMs'] for c in allcaps)/1000:.3f} capture seconds</strong> and <strong>{sum(c['reportChars'] for c in allcaps):,} report characters</strong>. This is summed capture duration, not necessarily additional wall time. One extra shell event requested analyzer help/availability (pair 2). There were {sum(r['shellCommandEvents'] for r in runs)} completed shell events across analyzer trials.</p><p><small>¹ Captures beyond the first occurrence of an identical Markdown SHA-256 within a trial. Identical text does not prove the screenshot or application state was identical. ² Shell events containing <code>playwright-cli</code>, not individual CLI invocations; a shell event may chain several commands. Counts overlap with other activity.</small></p><p>All 37 captures reported Copilot available, a ready element in the tree, no coverage warnings and no truncation. <strong>All had zero source references</strong>, so this experiment did not exercise source-location navigation.</p><p>Only pair 3 used <code>--prepare</code> (9 of its 11 captures). Its hook dismissed the development notice, later also checking “Don’t show again.” No hook applied report filters or opened the date calendar. All captures examined the baseline reports page; <code>final</code> labels were sometimes reused before further edits.</p>
<h2 id="changes">What changed while the analyzer was being used</h2><p>These are measurements from the actual captures, supported by agent notes about report or screenshot use. They establish before/after changes within the workflow, not that the analyzer alone caused the improvements. The agents also used ordinary browser screenshots and DOM inspection.</p>''')

def case(title,description,pair,before,after,labels):
    r=next(r for r in runs if r['pair']==pair);a=next(c for c in r['captures'] if c['artifact']==before);b=next(c for c in r['captures'] if c['artifact']==after)
    parts.append(f'<section class="card"><h3>{esc(title)}</h3><p>{description}</p><div class="images">')
    for caption,c in [('Before',a),('After',b)]:
        parts.append(f'<figure><a href="{c["evidencePath"]}/page.png"><img loading="lazy" src="{c["evidencePath"]}/page.png" alt="{caption}, pair {pair}, {esc(c["state"])}"></a><figcaption>{caption}: <a href="{c["evidencePath"]}/layout.md">geometry report</a> · <a href="{c["evidencePath"]}/capture.json">metadata</a></figcaption></figure>')
    parts.append('</div><details><summary>Selected measured boxes (x, y, width, height)</summary><pre>')
    for caption,c in [('Before',a),('After',b)]:
        selected=[x for x in c['geometry'] if any(label in x['label'] for label in labels)]
        parts.append(esc(caption+'\n'+'\n'.join(f'{x["label"]}: {x["x"]}, {x["y"]}, {x["width"]}, {x["height"]}' for x in selected)))
    parts.append('</pre></details></section>')
case('Pair 1: mobile summary overlap','An intermediate mobile capture reported an overflow involving the New report button. The agent said it changed the summary to grow naturally on narrow screens. In the later capture, that button overflow finding was absent, and the page grew by 43 pixels. Separately, the desktop account avatar moved from y=1119.25 (below the 1024px viewport) to y=968 after sidebar sizing changes.',1,'capture-4x95LL','capture-G1Bat9',['New report','Filters','ReportsView'])
case('Pair 2: excess control height','The agent explicitly identified hidden label-row space in the report and moved labels into the Vaadin controls. Desktop TextField height fell from 68 to 48px; MultiSelectComboBox from 76 to 48px; DatePickers from 68 to 48px. The dates moved from y=495 to y=441. This is a concrete geometry improvement, although the final view still failed the visual threshold.',2,'capture-9tzNNq','capture-XsCx2d',['TextField','MultiSelectComboBox','DatePicker'])
case('Pair 3: fixed-height mobile root','The first mobile report showed a 390×844 root with a much taller child and an ESCAPES finding extending 2940px beyond its parent. The agent removed the fixed root height. The final root was 390×3778.47, and that escape finding disappeared. Subsequent screenshot inspection also caught a desktop sidebar-footer regression, requiring another correction.',3,'capture-y2lu4N','capture-xcfXcl',['ReportsView'])
case('Pair 4: mobile filters moved into view','The initial mobile shell remained vertically stacked. Filters started at y=805.33 and its text field at y=871.33, beyond the 844px viewport. After the shell was changed to a flex Div, Filters started at y=308 and the text field at y=374: 497.33px upward. The agent used the initial geometry/screenshot feedback, but the initial mobile report had no findings classified as broken—showing why warning count is not a quality score.',4,'capture-zkA14H','capture-dhXHXN',['Filters','TextField','New report'])
parts.append('''<h2>What should not be credited to the analyzer</h2><ul><li>Search/filter/calendar interactions were exercised with ordinary Playwright commands. Capturing the initial page does not verify those behaviors.</li><li>Java API mismatches, multi-select chip configuration, compilation, server restarts and stale styles/bundles required ordinary development and browser tools.</li><li>The analyzer never received the reference image as an input and never produced a similarity score. Reference matching remained agent judgment; the independent final verifier supplied visual scores.</li><li>No analyzer command repaired code. The agent made every source edit.</li></ul><h2>Friction and limits observed</h2><ul><li>Recurring Avatar CUT findings persisted after other improvements. Agents treated some as geometry noise; do not assume every clipping finding is a real visual defect, or dismiss all avatar problems as false positives.</li><li>Many captures repeated identical report text. Large reports added context volume: median uncached input was about 52.5% higher in analyzer runs.</li><li>Development notice overlays required special handling. Only one trial adopted a prepare hook; other agents also used ordinary browser screenshots to inspect a clean page.</li><li>The pilot tried to open <code>screenshot.png</code> once, but the saved filename is <code>page.png</code>; the agent then corrected it.</li><li>Geometry applies only to the captured viewport and current UI state. No source references were available; readiness checks cannot prove all future asynchronous updates are complete.</li></ul>
<h2 id="commands">Exact capture command ledger</h2><p>All 37 shell commands are below, with their actual labels and ready selectors. Expand a trial for the full commands, capture timing and linked reports. Commands that create a prepare hook include that script verbatim. The downloadable <a href="usage.json">usage JSON</a> also contains findings, measured boxes, image-view references and explicit artifact-read commands. Raw trajectories are deliberately excluded from the public report.</p>''')
for r in runs:
    parts.append(f'<details class="card"><summary>Pair {r["pair"]}: {len(r["captures"])} captures — {esc(r["trial"])}</summary>')
    for n,c in enumerate(r['captures'],1):
        vp=c['viewport'];parts.append(f'<h3>{n}. {esc(c["artifact"])} · {vp["width"]} × {vp["height"]}</h3><p>{esc(c["capturedAt"])} · {c["totalDurationMs"]/1000:.3f}s · shell completion #{c["completedShellCommandOrdinal"]} · exit {c["exitCode"]}</p><pre>{esc(c["shellCommand"])}</pre><p><a href="{c["evidencePath"]}/layout.md">Report</a> · <a href="{c["evidencePath"]}/page.png">Screenshot</a> · <a href="{c["evidencePath"]}/capture.json">Metadata</a></p>')
    parts.append('<h3>Explicit artifact reads</h3><p>Reports were also returned automatically on stdout for every capture; these reads are additional activity.</p>')
    for c in r['artifactReadCommands']:parts.append(f'<pre>#{c["ordinal"]}: {esc(c["command"])}</pre>')
    parts.append('</details>')
parts.append('<h2 id="outcomes">Did this translate into better results?</h2><div class="scroll"><table><tr><th>Pair</th><th>Control time</th><th>Analyzer time</th><th>Control visual</th><th>Analyzer visual</th></tr>')
for pair in range(1,5):
    a=next(r for r in outcomes if r['pair']==pair and r['mode']=='control');b=next(r for r in outcomes if r['pair']==pair and r['mode']=='full')
    parts.append(f'<tr><td>{pair}</td><td>{a["agentSeconds"]/60:.2f} min</td><td>{b["agentSeconds"]/60:.2f} min</td><td>{a["visualAggregate"]:.4f}</td><td>{b["visualAggregate"]:.4f}</td></tr>')
parts.append('''</table></div><p>Median agent time was 40m27s control versus 36m28s analyzer (9.8% lower). Median visual aggregate was 0.8173 versus 0.8159, essentially unchanged. These are four samples per arm on one task; the time difference is not a reliable estimate of a general speedup. Agent timing excludes image setup and final verification.</p><p>All eight attempts failed all three verifier categories. Visual grading required aggregate ≥0.90 plus regional floors. Every implementation omitted <code>vaadin-card</code>, which blocked component checks and the interaction verifier’s card locator. That does not establish that every implemented filter was broken. The task requested suitable standard Vaadin components generally, without explicitly naming <code>vaadin-card</code>.</p><p><a href="outcomes.json">Download outcome metrics</a>.</p><h2>Recommendation</h2><p>Keep the analyzer available as an optional diagnostic aid. Its strongest demonstrated contribution is concrete geometry feedback during responsive layout repair. The next useful test is a working canonical Vaadin view with known layout defects: compare diagnosis and repair time with and without the tool, hold component correctness constant, and capture the specific broken states using prepare hooks. That would isolate its value more clearly than another full view implementation.</p><footer><p class="muted">Generated from local completed study artifacts. Evidence includes 37 geometry reports, metadata files and unmodified screenshots. No new benchmark trials were run to produce this report.</p></footer></main></body></html>''')
(OUT/'index.html').write_text('\n'.join(parts))
(ROOT/'site/index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>VaadinBench reports</title><h1>VaadinBench reports</h1><p><a href="analyzer-usage/">What the layout analyzer actually did — full usage and evidence report</a></p></html>\n')
print(json.dumps([{k:v for k,v in r.items() if k not in ['captures','artifactReadCommands','analyzerImageViewReferences']} for r in runs],indent=2))
print('Report:',OUT/'index.html')
