# Contributing

Corrections, accessibility improvements, new exercises, and build fixes are
welcome. Substantial changes to the book's scope or chapter order should be
discussed in an issue first.

## Development environment

Use Node 22 and npm 10. The versions are declared in `.nvmrc`, `.node-version`,
and `package.json`. With nvm:

```bash
nvm use
npm ci
```

Preview with `npm start`. Before submitting a change, run:

```bash
npm run check
```

This validates chapter ordering and metadata, tests the custom export
transform, builds the site, and checks links.

## Editing chapters

Follow the heading, directive, and exercise conventions in `README.md`. The
page outline is derived from the numbered `##` headings automatically. Every
figure needs useful `:alt:` text and every reusable target needs a unique label.

Keep source attribution current in `SOURCES.md`. Record the source and license
when adding adapted prose, data, photographs, or simulations.

## Figures

Figure-generating programs live in `scripts/figures/`; their SVG or raster
outputs live in `images/` and are committed. After changing a generator, run it
and commit both source and output. To regenerate and compare the entire set:

```bash
python3 -m pip install -r requirements-figures.txt
npm run check:figures
```

## Print and Word exports

The complete export toolchain is documented in `README.md`. Changes to
`plugins/`, `templates/`, `scripts/build-exports.sh`, or `scripts/tex-to-docx.py`
should be checked with at least one chapter offprint locally. The tagged-release
workflow builds all editions and publishes the three book-level downloads as
durable GitHub Release assets. A separate monthly run refreshes workflow
artifacts without rebuilding the print editions on ordinary pushes.

## Release checklist

1. Run `npm ci` and `npm run check` with Node 22.
2. Run `npm run build:exports` and inspect the complete and student PDFs.
3. Confirm that the student PDF omits solutions and that the DOCX contains math
   and figures.
4. Update the version-facing notes, then push a `v*` tag.
5. Confirm the Exports and Pages workflows and test all download links.
