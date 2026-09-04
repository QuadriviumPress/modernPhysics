# Modern Physics

An original MyST Markdown textbook covering special relativity, quantum
theory, atomic and molecular structure, and nuclear and particle physics —
written for a first course in modern physics following an introductory
calculus-based physics sequence.

This is an original work in progress, not a conversion of an existing
published book.

## Structure

- [`myst.yml`](myst.yml) — project metadata and table of contents
- [`index.md`](index.md) — book landing page
- [`chapters/`](chapters/) — chapter content
- [`images/`](images/) — figures and diagrams
- [`plugins/`](plugins/) — the MyST plugins that embed interactive simulations and that make the book survive a static export
- [`templates/book/`](templates/book/) — the LaTeX template for the printed editions
- [`scripts/figures/`](scripts/figures/) — matplotlib sources for the computed figures
- [`scripts/build-exports.sh`](scripts/build-exports.sh) — builds every PDF and the Word edition

The book is organized into five parts (printed as `\part` dividers in the
PDF; listed here for orientation). The website sidebar is a flat chapter
list — no part groupings — with each chapter’s numbered sections in the
page outline:

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
the material takes shape.

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

Figures are committed as SVG in [`images/`](images/). The ones for Chapters 4
and 5 are generated with matplotlib rather than drawn by hand; their source is
in [`scripts/figures/`](scripts/figures/), which also documents the palette and
styling conventions. The SVGs are committed because the Pages build runs
`myst build --html` only and has no Python. To regenerate after editing a
script:

```bash
pip install matplotlib numpy scipy
python3 scripts/figures/ch04_figures.py
python3 scripts/figures/ch04_schematics.py
python3 scripts/figures/ch05_figures.py
python3 scripts/figures/ch05_schematics.py
```

## Build

```bash
npm install
npm run start          # preview
npm run build          # static site in _build/html/
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
| `modern-physics.pdf` | The whole book, worked solutions included |
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
nothing else, and 89 of the book's 97 figures are SVG; without it every one of
them is missing from the PDF. `pandoc` and `poppler-utils` are needed only for
the Word edition.

### How it works

- [`plugins/export.mjs`](plugins/export.mjs) rewrites the handful of node types
  that no export renderer handles — exercises, solutions, margin notes,
  dropdowns — into ones that every renderer does. It is inert unless
  `MYST_PRINT` is set, so `myst start` and the website build are untouched.
- [`templates/book/`](templates/book/) is a local jtex template: the whole book
  as a `book`, or one chapter as an offprint via its `chapter` option.
- The Word edition goes through pandoc rather than `myst build --docx`, because
  MyST's own DOCX renderer writes each equation as a raw LaTeX *string* inside a
  Word equation field. Pandoc converts the same math to OMML, which Word renders
  and edits natively — 7,561 real equations rather than 7,561 lines of
  `\frac{...}{...}`. See [`scripts/tex-to-docx.py`](scripts/tex-to-docx.py).

Exports are built by
[`.github/workflows/exports.yml`](.github/workflows/exports.yml), which runs on
`v*` tags and on demand — not on every push, since the TeX Live install and the
XeLaTeX passes cost several minutes.
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) downloads that
workflow's most recent successful artifacts before building the site, so every
page carries a download menu. The consequence is that the published downloads
track the last tag rather than the tip of `main`: push a `v*` tag, or run
Exports from the Actions tab, when they need to catch up. Artifacts expire after
90 days, so a repository that has gone that long without either will deploy with
an empty download menu until the next run.

## Content sources

This book uses the chapter scaffold of a copyrighted textbook as a structural
reference only; all prose, derivations, examples, and problems are adapted
from openly licensed (OER) sources. See [`SOURCES.md`](SOURCES.md) for the
per-chapter source mapping and attribution ledger.

## License

© 2026 Martin Veillette. Licensed under
[CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
