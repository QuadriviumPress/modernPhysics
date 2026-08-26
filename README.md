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
- [`plugins/`](plugins/) — the MyST plugin that embeds interactive simulations
- [`scripts/figures/`](scripts/figures/) — matplotlib sources for the computed figures

The current table of contents (see [`myst.yml`](myst.yml)) is a scaffold:

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

Each chapter file starts as a stub (Learning Objectives / Introduction /
Summary / Problems) to be filled in with real content, figures, and
worked examples. Feel free to reorder, split, merge, or rename
chapters/parts in `myst.yml` as the material takes shape.

## Writing chapters

Chapters are plain MyST Markdown. Use MyST directives for math, figures,
admonitions, and cross-references — see the
[MyST Markdown guide](https://mystmd.org/guide) for the full syntax
(`$...$` / `$$...$$` for math, `{figure}` for images, `{prf:theorem}` /
`{prf:proof}` and similar for structured content, etc.).

## Interactive simulations

Chapters can embed a running browser simulation with the `{openphysics}`,
`{phet}`, or `{simulation}` directives, supplied by
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

## Preview locally

```bash
npm install -g mystmd@1.10.1
myst start
```

## Build the static site

```bash
myst build --html
```

Generated output is written to `_build/` and is not committed.

## Deploy

The book builds and deploys to GitHub Pages via
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) on every push
to `main`, once the repository is pushed to GitHub with Pages enabled
(Settings → Pages → Source: GitHub Actions).

## Content sources

This book uses the chapter scaffold of a copyrighted textbook as a structural
reference only; all prose, derivations, examples, and problems are adapted
from openly licensed (OER) sources. See [`SOURCES.md`](SOURCES.md) for the
per-chapter source mapping and attribution ledger.

## License

© 2026 Martin Veillette. Licensed under
[CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
