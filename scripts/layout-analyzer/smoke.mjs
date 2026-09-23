// Run inside an experiment image against the employee-list reference solution.
// No model is involved: exercise the real Copilot runtime and unmodified package.
import assert from 'node:assert/strict';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { chromium } from 'playwright';
import { captureLayout } from '@vaadin/layout-analyzer-preview/playwright';
import { main as captureWithAdapter } from './capture.mjs';

const config = JSON.parse(await readFile(process.env.PLAYWRIGHT_MCP_CONFIG, 'utf8')).browser;
const browser = await chromium.launch({ ...config.launchOptions, headless: true });
const out = process.argv[3] || '/logs/agent/layout-smoke';
await mkdir(out, { recursive: true });
const results = [];
try {
  const page = await browser.newPage(config.contextOptions);
  await page.goto(process.argv[2] || 'http://localhost:8080/employees');
  await page.getByTestId('employee-grid').waitFor();
  await page.waitForFunction(() => Boolean(window.Vaadin?.copilot?._uiState?.setActiveMode));
  const previousMode = await page.evaluate(() => window.Vaadin.copilot._uiState.activeMode);
  for (const [state, width, height] of [['desktop', 1440, 1024], ['mobile', 720, 900]]) {
    await page.setViewportSize({ width, height });
    for (const includeRelationships of [false, true]) {
      const report = await captureLayout(page, { includeRelationships });
      assert.equal(report.analyzerVersion, '0.1.1');
      assert.ok(report.coverage.visibleComponents > 10);
      assert.ok(report.coverage.geometryStable);
      assert.ok(report.coverage.fontsReady);
      assert.equal(await page.evaluate(() => window.Vaadin.copilot._uiState.activeMode), previousMode);
      assert.equal(report.markdown.includes('## Repeated relationships'), includeRelationships);
      results.push({ state, width, height, includeRelationships,
        coverage: report.coverage, durationMs: report.durationMs,
        reportChars: report.markdown.length, relationships: report.relationships.length });
      await writeFile(`${out}/${state}-${includeRelationships ? 'full' : 'geometry'}.json`, JSON.stringify(report, null, 2));
    }
  }
  await page.setViewportSize({ width: 1440, height: 1024 });
  const bounded = await captureLayout(page, { maxReportChars: 1000 });
  assert.ok(bounded.reportTruncated);
  assert.ok(bounded.markdown.length <= 1000);
  assert.ok(bounded.model.boxes.length > 10);
  // A malformed option throws after entering Inspect mode; it must still restore it.
  await assert.rejects(captureLayout(page, { maxReportChars: 1 }), /maxReportChars/);
  assert.equal(await page.evaluate(() => window.Vaadin.copilot._uiState.activeMode), previousMode);
  // A fresh capture must reflect a real geometry change, not a cached report.
  const before = await captureLayout(page);
  await page.getByTestId('employee-grid').evaluate(el => el.style.width = '2000px');
  const after = await captureLayout(page);
  assert.notDeepEqual(before.model.boxes, after.model.boxes);
  assert.ok(after.model.findings.some(f => /OVERFLOW|ESCAPES|CUT|CLIPPED|SIDEWAYS/.test(f.kind)));
  // The adapter must prepare a real interactive state in its fresh context.
  const prepare = `${out}/open-detail.mjs`;
  await writeFile(prepare, `export async function prepare(page) {
    await page.getByTestId('employee-grid').locator('[part~="body-row"]').nth(1).click();
    await page.getByTestId('employee-detail').waitFor();
  }`);
  await captureWithAdapter([process.argv[2] || 'http://localhost:8080/employees',
    '--prepare', prepare, '--state', 'detail-open',
    '--ready', '[data-testid="employee-detail"]', '--out', `${out}/detail`]);
  const detail = JSON.parse(await readFile(`${out}/detail/capture.json`, 'utf8'));
  assert.equal(detail.status, 'ok');
  assert.equal(detail.state, 'detail-open');
  // Copilot 25.2.5 omits this visible virtual child. Do not mistake stable
  // geometry for complete coverage; keep the omission visible to the agent.
  assert.equal(detail.readyElementInTree, false);
  assert.equal(detail.coverageWarnings.length, 1);
  await writeFile(`${out}/summary.json`, JSON.stringify({ results, truncation: true, restorationAfterError: true, recapture: true, preparedState: true }, null, 2));
  console.log(JSON.stringify(results, null, 2));
} finally {
  await browser.close();
}
