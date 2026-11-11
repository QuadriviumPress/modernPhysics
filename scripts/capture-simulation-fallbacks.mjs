/**
 * Capture the selected public OpenLyceum screens for PDF, DOCX and print.
 *
 * npm install --prefix /tmp/modernphysics-browser playwright
 * PLAYWRIGHT_MODULE=/tmp/modernphysics-browser/node_modules/playwright/index.mjs \
 *   node scripts/capture-simulation-fallbacks.mjs
 *
 * Install Chromium with Playwright if it is not already available. Captures
 * reflect the deployed simulation version; inspect the images after refreshing.
 * Pass capture filenames as arguments to refresh only those entries.
 * The manifest may specify keyboard actions to select a teaching preset.
 */
import { readFile, mkdir } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const directory = path.join(root, 'images/simulations');
const { captures } = JSON.parse(await readFile(path.join(directory, 'manifest.json'), 'utf8'));
const moduleName = process.env.PLAYWRIGHT_MODULE;
const { chromium } = await import(moduleName ? pathToFileURL(moduleName).href : 'playwright');
const selectedFiles = new Set(process.argv.slice(2));
const browser = await chromium.launch({
  headless: true,
  args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'],
});
await mkdir(directory, { recursive: true });
try {
  for (const capture of captures) {
    if (selectedFiles.size && !selectedFiles.has(capture.file)) continue;
    const page = await browser.newPage({ viewport: { width: 1024, height: 618 }, deviceScaleFactor: 1 });
    const exceptions = [];
    page.on('pageerror', error => exceptions.push(error.message));
    const params = new URLSearchParams({
      screens: capture.screens,
      initialScreen: capture.initialScreen ?? capture.screens.split(',')[0],
      seed: '173',
    });
    // Exercise the renderer available even on machines without a WebGPU device.
    if (capture.repository === 'QuantumAtom3D') params.set('forceCpu', 'true');
    const url = `https://openlyceum.github.io/${capture.repository}/?${params}`;
    const response = await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    if (!response?.ok()) throw new Error(`${url}: HTTP ${response?.status()}`);
    await page.waitForFunction(() => Boolean(window.phet?.joist?.sim), undefined, { timeout: 60000 });
    await page.locator('#sim').waitFor({ state: 'visible', timeout: 60000 });
    await page.evaluate(() => document.fonts.ready);
    for (const action of capture.actions ?? []) {
      await page.getByRole(action.role, { name: action.name, exact: true }).press(action.key ?? 'Enter');
    }
    await page.mouse.click(2, 2);
    await page.waitForTimeout(3000);
    if (exceptions.length) throw new Error(`${url}: ${exceptions.join('; ')}`);
    await page.screenshot({ path: path.join(directory, capture.file) });
    console.log(`${capture.file}: loaded without JavaScript exceptions`);
    await page.close();
  }
} finally {
  await browser.close();
}
