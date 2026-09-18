import assert from 'node:assert/strict';
import test from 'node:test';
import { chapterLists, endMatterIssues, figuresWithoutAlt } from '../scripts/validate-project.mjs';

test('chapter lists accept quoted paths, reordered keys, and nested navigation', () => {
  const result = chapterLists(`project:
    exports:
      - articles: [{file: "chapters/ch-01-test.md", level: 0}]
        id: book
    toc:
      - title: Part one
        children:
          - file: 'chapters/ch-01-test.md' # chapter
`);
  assert.deepEqual(result, { toc: ['chapters/ch-01-test.md'], exports: ['chapters/ch-01-test.md'] });
});

test('figure alt checks support all fences and nested directives', () => {
  for (const fence of ['```', '````', '~~~', '::::']) {
    assert.deepEqual(figuresWithoutAlt(`${fence}{figure} image.png\n:alt: A plot\n${fence}`), []);
    assert.deepEqual(figuresWithoutAlt(`${fence}{figure} image.png\n${fence}`), ['image.png']);
  }
  assert.deepEqual(figuresWithoutAlt('::::{solution}\n:::{figure} nested.png\n:::\n::::'), ['nested.png']);
  assert.deepEqual(figuresWithoutAlt('````markdown\n```{figure} example.png\n```\n````'), []);
  assert.deepEqual(figuresWithoutAlt('````\n```{figure} example.png\n```\n````'), []);
});

test('end matter requires review, conceptual questions, ordered problems, and difficulty tags', () => {
  const valid = `## Check Your Understanding

1. Question?

## Conceptual Questions

1. Why?

## Problems

:::{exercise}
:label: ex-one

*(Moderate)*

Solve it.
:::
`;
  assert.deepEqual(endMatterIssues(valid), []);
  assert.match(endMatterIssues(valid.replace('*(Moderate)*\n\n', '')).join('\n'), /difficulty tags cover 0 of 1/);
  assert.match(endMatterIssues(valid.replace('## Conceptual Questions', '## Discussion')).join('\n'), /Conceptual Questions/);
});
