#!/usr/bin/env node
// VaadinBench adapter; the preview archive itself is unmodified.
import { chromium } from 'playwright';
import { captureLayout } from '@vaadin/layout-analyzer-preview/playwright';
import { mkdir, mkdtemp, readFile, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { parseArgs } from 'node:util';

const help = `Usage: layout-check URL --ready CSS [--prepare state.mjs] [--state NAME]
  [--width 1440] [--height 1024] [--out DIRECTORY] [--timeout 30000]
  [--max-report-chars 24000]
Captures the current state after prepare(page) and a visible readiness selector.
Prints Markdown; saves JSON, screenshot, and metadata under /logs/agent/layout/.
VB_LAYOUT_MODE=geometry omits relationships; full is the default.
Uses the task's PLAYWRIGHT_MCP_CONFIG and its preinstalled Chromium.
`;

function positive(value, name, minimum = 1) {
  const number = Number(value);
  if (!Number.isSafeInteger(number) || number < minimum)
    throw new Error(`${name} must be an integer >= ${minimum}`);
  return number;
}

export async function main(args = process.argv.slice(2)) {
  const { values, positionals } = parseArgs({ args, allowPositionals: true, options: {
    help: { type: 'boolean' }, ready: { type: 'string' }, prepare: { type: 'string' },
    state: { type: 'string', default: 'initial' }, out: { type: 'string' },
    width: { type: 'string', default: '1440' }, height: { type: 'string', default: '1024' },
    timeout: { type: 'string', default: '30000' },
    'max-report-chars': { type: 'string', default: '24000' },
  } });
  if (values.help) { process.stdout.write(help); return; }
  if (positionals.length !== 1 || !values.ready) throw new Error(help);
  const url = new URL(positionals[0]);
  if (!['http:', 'https:'].includes(url.protocol)) throw new Error('URL must use HTTP(S)');
  const viewport = { width: positive(values.width, 'width'), height: positive(values.height, 'height') };
  const timeout = positive(values.timeout, 'timeout');
  const maxReportChars = positive(values['max-report-chars'], 'max-report-chars', 1000);
  const mode = process.env.VB_LAYOUT_MODE || 'full';
  if (!['geometry', 'full'].includes(mode)) throw new Error(`Invalid VB_LAYOUT_MODE: ${mode}`);
  const configPath = process.env.PLAYWRIGHT_MCP_CONFIG;
  if (!configPath) throw new Error('PLAYWRIGHT_MCP_CONFIG must point to the task browser config');
  const config = JSON.parse(await readFile(configPath, 'utf8')).browser;
  const prepareSource = values.prepare ? await readFile(resolve(values.prepare), 'utf8') : null;
  const started = performance.now();
  const base = '/logs/agent/layout';
  await mkdir(values.out ? resolve(values.out) : base, { recursive: true });
  const out = values.out ? resolve(values.out) : await mkdtemp(`${base}/capture-`);
  const metadata = {
    url: url.href, state: values.state, viewport, mode, ready: values.ready,
    prepareSource, capturedAt: new Date().toISOString(), status: 'error',
  };
  let browser;
  try {
    browser = await chromium.launch({ ...config.launchOptions, headless: true });
    metadata.browserVersion = browser.version();
    const page = await browser.newPage({ ...config.contextOptions, viewport });
    page.setDefaultTimeout(timeout);
    await page.goto(url.href, { waitUntil: 'domcontentloaded', timeout });
    if (values.prepare) {
      const module = await import(pathToFileURL(resolve(values.prepare)).href);
      if (typeof module.prepare !== 'function') throw new Error('State module must export prepare(page)');
      await module.prepare(page);
    }
    await page.locator(values.ready).first().waitFor({ state: 'visible', timeout });
    metadata.copilotAvailable = await page.evaluate(() => Boolean(
      window.Vaadin?.copilot?._uiState?.setActiveMode && window.Vaadin?.copilot?.tree));
    // captureLayout also waits for asynchronous Copilot initialization.
    const report = await captureLayout(page, {
      timeoutMs: timeout, maxReportChars, includeRelationships: mode === 'full',
    });
    if (!report.coverage.visibleComponents) throw new Error('Copilot returned no visible components');
    metadata.copilotAvailable = true;
    metadata.finalUrl = page.url();
    metadata.coverage = report.coverage;
    metadata.reportChars = report.markdown.length;
    metadata.analyzerVersion = report.analyzerVersion;
    metadata.captureDurationMs = report.durationMs;
    metadata.reportTruncated = report.reportTruncated;
    await writeFile(`${out}/layout.json`, JSON.stringify(report, null, 2) + '\n');
    await writeFile(`${out}/layout.md`, report.markdown + '\n');
    await page.screenshot({ path: `${out}/page.png` });
    metadata.status = 'ok';
    process.stdout.write(report.markdown + '\n');
  } catch (error) {
    metadata.error = error.message;
    throw new Error(`Layout capture failed: ${error.message}\nCheck app readiness and development mode with JAVA_TOOL_OPTIONS=-Dvaadin.copilot.enable=true. Metadata: ${out}/capture.json`, { cause: error });
  } finally {
    metadata.totalDurationMs = Math.round(performance.now() - started);
    await writeFile(`${out}/capture.json`, JSON.stringify(metadata, null, 2) + '\n');
    await browser?.close();
    process.stderr.write(`Layout artifacts: ${out}\n`);
  }
}

// Resolve symlinks because /usr/local/bin/layout-check points at this file.
import { realpathSync } from 'node:fs';
if (process.argv[1] && realpathSync(process.argv[1]) === realpathSync(new URL(import.meta.url))) {
  main().catch(error => { console.error(error.message); process.exitCode = 1; });
}
