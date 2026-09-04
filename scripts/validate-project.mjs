#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const config = fs.readFileSync(path.join(root, 'myst.yml'), 'utf8');
const failures = [];
const tocStart = config.indexOf('\n  toc:\n');
const siteStart = config.indexOf('\nsite:\n', tocStart);
const toc = config.slice(tocStart, siteStart);
const tocChapters = [...toc.matchAll(/^    - file: (chapters\/[^\n]+\.md)$/gm)].map(match => match[1]);
const chapterFiles = fs.readdirSync(path.join(root, 'chapters'))
  .filter(name => /^ch-\d{2}-.+\.md$/.test(name))
  .sort()
  .map(name => `chapters/${name}`);
const exportStart = config.indexOf('\n  exports:\n');
const exportConfig = config.slice(exportStart, tocStart);
const exportChapters = [...exportConfig.matchAll(/^        - file: (chapters\/[^\n]+\.md)$/gm)].map(match => match[1]);

if (JSON.stringify(tocChapters) !== JSON.stringify(chapterFiles)) {
  failures.push(`website TOC chapters differ from the chapter directory\n` +
    `  expected ${JSON.stringify(chapterFiles)}\n  found    ${JSON.stringify(tocChapters)}`);
}
if (JSON.stringify(exportChapters) !== JSON.stringify(chapterFiles)) {
  failures.push(`print export chapters differ from the chapter directory\n` +
    `  expected ${JSON.stringify(chapterFiles)}\n  found    ${JSON.stringify(exportChapters)}`);
}

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
console.log(`Project metadata valid: ${chapterFiles.length} chapters, ${labels.size} directive labels.`);
