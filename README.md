# Modern Physics

An original MyST Markdown textbook covering special relativity, quantum
theory, atomic and molecular structure, and nuclear and particle physics —
written for a first course in modern physics following an introductory
calculus-based physics sequence.

This is an original work in progress, not a conversion of an existing
published book.

## Structure

- [`myst.yml`](myst.yml) — project metadata and table of contents
- [`index.md`](index.md) — book landing page (website only)
- [`preface.md`](preface.md) — preface (website sidebar and print front matter)
- [`chapters/`](chapters/) — chapter content
- [`images/`](images/) — figures and diagrams
- [`plugins/`](plugins/) — the MyST plugins that embed interactive simulations and that make the book survive a static export
- [`templates/book/`](templates/book/) — the LaTeX template for the printed editions
- [`scripts/figures/`](scripts/figures/) — matplotlib sources for the computed figures
- [`scripts/build-exports.sh`](scripts/build-exports.sh) — builds every PDF and the Word edition
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — development, checks, and release checklist

The book is organized into five parts (printed as `\part` dividers in the
PDF; listed here for orientation). The website sidebar lists the preface,
then the chapters — no part groupings — with each chapter’s numbered
sections expandable underneath:

- **Part I — Relativity**: the need for relativity, special relativity,
  relativistic dynamics
- **Part II — Wave Optics**: interference of light, diffraction of light
- **Part III — Quantum Theory**: particle properties of waves, wave
  properties of particles, the Schrödinger equation, quantum mechanics in
  three dimensions
- **Part IV — Atoms and Molecules**: the hydrogen atom, many-electron
  atoms, molecular structure
- **Part V — Nuclear and Particle Physics**: nuclear physics, elementary
  particles and the Standard Model

Feel free to reorder, split, merge, or rename chapters in `myst.yml` as
the material takes shape. If you rename a `##` reading section, update
the matching sidebar entry under that chapter in `myst.yml` as well
(`npm run check:project` reports mismatches).

The printed book does not use `index.md`. It opens with the title and
copyright pages from [`templates/book/template.tex`](templates/book/template.tex),
then [`preface.md`](preface.md) while still in LaTeX `\frontmatter` (so the
preface is unnumbered). The preface ends with a raw `\mainmatter`, after
which Part I / Chapter 1 begin the numbered body.

## Writing chapters

Chapters are plain MyST Markdown. Use MyST directives for math, figures,
admonitions, and cross-references — see the
[MyST Markdown guide](https://mystmd.org/guide) for the full syntax
(`$...$` / `$$...$$` for math, `{figure}` for images, `{prf:theorem}` /
`{prf:proof}` and similar for structured content, etc.).

### Section structure

Each chapter is one file. Numbered reading sections are `##` headings
(rendered as *N.1*, *N.2*, … via `heading_1: true` in the chapter
frontmatter — MyST maps content `##` to `heading_1` when page titles
are unnumbered) and are kept roughly equal in length so a professor can
assign, for example, §§5.2–5.3. Topic headings under a section are
`###`; finer headings are `####`. Learning Objectives and Introduction
stay unnumbered (`###`). Summary, Conceptual Questions (when present),
and Problems remain `##` so they continue the section numbering.

### Admonitions, margin notes, dropdowns, and tabs

Beyond math, figures, and cross-references, chapters use a few more MyST
directives for pedagogical asides. Use them sparingly — a handful per
chapter, not per section — and only where there's a genuine fit:

- **Admonitions** — one directive per intent:
  - `` ```{note} `` — historical or contextual asides (who discovered what,
    when).
  - `` ```{tip} `` — problem-solving strategies (e.g. check units first, or
    when a relativistic correction can be dropped).
  - `` ```{warning} `` — a misconception or pitfall specific to that topic.
  - `` ```{seealso} `` — a pointer to related material elsewhere in the book,
    via `[](#label)`.
- **Margin notes** (`` ```{margin} ``) — a short aside that would be a
  distracting parenthetical inline: a unit reminder, a notation
  clarification, a quick defining fact.
- **Dropdowns** (`` ```{dropdown} Title ``) — an optional deep-dive: an
  extended or alternate derivation, a "for the curious" tangent, or a proof
  of a result asserted in the main text.
- **Tabs** (`` ```{tab-set} `` / `` ```{tab-item} ``) — side-by-side
  alternative treatments, used only where the book genuinely presents more
  than one approach (two solution methods, SI vs. natural units,
  non-relativistic vs. relativistic limits).

These are additive — they don't replace or restructure the surrounding
prose, headings, math, figures, or exercises.

## Interactive simulations

Chapters can embed a running browser simulation with the `{openphysics}`,
`{phet}`, `{phet-legacy}`, or `{simulation}` directives, supplied by
[`plugins/simulation.mjs`](plugins/simulation.mjs):

````markdown
```{openphysics} InterferometryLab
:label: fig:ch04-interferometry-sim

Move a mirror and count fringes.
```
````

On the website this is the live simulation. In a PDF, a Word document, exported
Markdown, or a printed page — none of which can run JavaScript — the same figure
becomes a screenshot with its caption and a link to the running version. Any URL
that works in an iframe can be embedded, not only simulations from
[OpenPhysics](https://github.com/OpenPhysics) and
[PhET](https://phet.colorado.edu). See
[`plugins/README.md`](plugins/README.md) for the options and for how the
fallback works.

`{phet-legacy}` reaches PhET's pre-HTML5 Java simulations, which PhET runs in
the browser through CheerpJ. Several topics here — the photoelectric effect,
quantum bound states, tunneling, lasers, gas discharge, the nuclear-physics
family — have no HTML5 equivalent, so the Java version is the only interactive
option. It is slow to start and mouse-only; prefer `{phet}` or `{openphysics}`
where either has something comparable.

Every chapter carries at least one simulation;
[`SOURCES.md`](SOURCES.md) lists which, chapter by chapter, along with the
attribution each supplier requires.

## Figures

Figures are committed in [`images/`](images/). Computed plots, schematics,
solution diagrams, simulation fallbacks, and brand assets are generated by the
programs in [`scripts/figures/`](scripts/figures/), which also document the
palette and styling conventions. Generated assets are committed because the
Pages build runs `myst build --html` only and has no Python. Regenerate the
affected script after editing it, or check the entire set with:

```bash
python3 -m pip install -r requirements-figures.txt
npm run check:figures
```

## Build

Use Node 22 (`nvm use` if you have nvm; see `.nvmrc`).

```bash
npm ci
npm run start          # preview
npm run build          # static site in _build/html/
npm run check          # metadata, plugin tests, HTML, and links
```

Generated output is written to `_build/` and is not committed. CI runs on
pull requests (`.github/workflows/ci.yml`); pushes to `main` deploy via
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

## Print and Word editions

The website is the primary edition, but the same source builds a printable book,
a set of chapter offprints, and a Word document — all into `exports/`, which is
not committed.

```bash
npm run build:exports    # everything below, about a minute
npm run build:pdf        # the two book PDFs only
npm run build:chapters   # the fourteen chapter offprints only
npm run build:docx       # the Word edition only
```

| File | What it is |
|---|---|
| `modern-physics.pdf` | The whole book (preface + chapters), worked solutions included |
| `modern-physics-student.pdf` | The whole book, exercises but no solutions |
| `modern-physics.docx` | The complete edition as a Word document |
| `ch-NN-<slug>.pdf` | One standalone offprint per chapter |

Everything stays clickable. A "see Chapter 7" jumps to Chapter 7 inside the PDF,
`{numref}` and `{eq}` references jump to the figure or equation, and every
simulation's caption links out to the running simulation on the web. In a
chapter offprint — which contains only its own chapter — the cross-chapter
references point at the website instead.

Interactive simulations cannot run on paper, so each one becomes the screenshot
and caption link that [`plugins/simulation.mjs`](plugins/simulation.mjs) already
emits beside the live iframe. Nothing in a chapter needs to change for this.

### Toolchain

Beyond Node, the print build needs:

```bash
sudo apt-get install -y --no-install-recommends \
  inkscape latexmk texlive-xetex texlive-latex-base texlive-latex-recommended \
  texlive-latex-extra texlive-fonts-recommended texlive-plain-generic \
  pandoc poppler-utils
```

**Inkscape is not optional.** MyST converts SVG to PDF with Inkscape and with
nothing else, and most of the book's figures are SVG; without it they are
missing from the PDF. `pandoc` and `poppler-utils` are needed only for
the Word edition.

### How it works

- [`plugins/export.mjs`](plugins/export.mjs) rewrites the handful of node types
  that no export renderer handles — exercises, solutions, margin notes,
  dropdowns — into ones that every renderer does. It is inert unless
  `MYST_PRINT` is set, so `myst start` and the website build are untouched.
- [`templates/book/`](templates/book/) is a local jtex template: the whole book
  as a `book` (title, copyright, TOC, and unnumbered preface in `\frontmatter`,
  then numbered parts and chapters), or one chapter as an offprint via its
  `chapter` option.
- The Word edition goes through pandoc rather than `myst build --docx`, because
  MyST's own DOCX renderer writes each equation as a raw LaTeX *string* inside a
  Word equation field. Pandoc converts the same math to OMML, which Word renders
  and edits natively. See [`scripts/tex-to-docx.py`](scripts/tex-to-docx.py).

Exports are built by
[`.github/workflows/exports.yml`](.github/workflows/exports.yml), which runs on
`v*` tags, every two months, and on demand — not on every push, since installing
TeX Live and running XeLaTeX is comparatively expensive. Tagged builds publish
the book-level files as durable GitHub Release assets; scheduled builds refresh
the workflow artifacts used by sites without a tagged release.
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) prefers the latest
release and falls back to the most recent successful export artifacts before
building the site. Thus the downloads track the last release or export run,
rather than every commit on `main`.

Development and release procedures are collected in
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Content sources

This book uses the chapter scaffold of a copyrighted textbook as a structural
reference only; all prose, derivations, examples, and problems are adapted
from openly licensed (OER) sources. See [`SOURCES.md`](SOURCES.md) for the
per-chapter source mapping and attribution ledger.

## License

© 2026 Martin Veillette. Licensed under
[CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
