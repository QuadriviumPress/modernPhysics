#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const config = fs.readFileSync(path.join(root, 'myst.yml'), 'utf8');
const failures = [];

function slugify(value) {
  return value.toLowerCase()
    .replace(/[’']/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

function normalizeTitle(value) {
  return value.replace(/[’']/g, "'");
}

const tocStart = config.indexOf('\n  toc:\n');
const siteStart = config.indexOf('\nsite:\n', tocStart);
const toc = `${config.slice(tocStart, siteStart)}\n    - file: __end__.md\n`;
const chapterBlocks = [...toc.matchAll(/^    - file: (chapters\/[^\n]+\.md)\n([\s\S]*?)(?=^    - file: )/gm)];

for (const match of chapterBlocks) {
  const relative = match[1];
  const source = fs.readFileSync(path.join(root, relative), 'utf8');
  const chapter = Number(/ch-(\d{2})-/.exec(relative)?.[1]);
  const headings = [...source.matchAll(/^## (.+)$/gm)].map((item, index) => ({
    title: normalizeTitle(`${chapter}.${index + 1} ${item[1]}`),
    anchor: slugify(item[1])
  }));
  const children = [...match[2].matchAll(/^        - title: "([^"]+)"\n          url: \/[^#\n]+#([^\n]+)$/gm)]
    .map(item => ({ title: normalizeTitle(item[1]), anchor: item[2] }));
  if (JSON.stringify(headings) !== JSON.stringify(children)) {
    failures.push(`${relative}: sidebar entries differ from its ## headings\n` +
      `  expected ${JSON.stringify(headings)}\n  found    ${JSON.stringify(children)}`);
  }
}

if (chapterBlocks.length !== 14) failures.push(`expected 14 chapter TOC entries; found ${chapterBlocks.length}`);

const labels = new Map();
for (const relative of fs.readdirSync(path.join(root, 'chapters')).filter(name => name.endsWith('.md'))) {
  const file = path.join('chapters', relative);
  const source = fs.readFileSync(path.join(root, file), 'utf8');
  for (const [, label] of source.matchAll(/^:(?:label|name):\s*(\S+)/gm)) {
    if (labels.has(label)) failures.push(`duplicate label ${label}: ${labels.get(label)} and ${file}`);
    labels.set(label, file);
  }
  const figures = [...source.matchAll(/^```\{figure\} ([^\n]+)\n([\s\S]*?)^```/gm)];
  for (const figure of figures) {
    if (!/^:alt:\s*\S+/m.test(figure[2])) failures.push(`${file}: figure ${figure[1]} has no :alt:`);
  }
}

if (failures.length) {
  console.error(failures.map(item => `ERROR: ${item}`).join('\n'));
  process.exit(1);
}
console.log(`Project metadata valid: ${chapterBlocks.length} chapters, ${labels.size} directive labels.`);
