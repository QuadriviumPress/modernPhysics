# AGENTS.md

## Standard

This book follows the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and the [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md).

## Commands

```bash
npm run check:toolchain
npm run h5p:check
npm run h5p:generate
npm run h5p:prepare
npm run prestart
npm run start
npm run prebuild
npm run build
npm run precheck
npm run verify
npm run check
npm run check:figures
npm run check:project
npm run test
npm run test:exports
npm run build:exports
npm run build:pdf
npm run build:chapters
npm run build:docx
```

`npm run check` is the production-equivalent verification and HTML build.

## Intentional differences

- `check:toolchain`, `h5p:generate`, `h5p:check`, and `h5p:prepare` support self-hosted H5P quizzes. `prestart` and `prebuild` run the toolchain check and H5P prepare step.
- `verify` runs the H5P check, project validator, and `npm test`.
- `check:project` and `check:figures` are extra checks. `test:exports`, `build:exports`, `build:pdf`, `build:chapters`, and `build:docx` build the print editions.
- `devDependencies` includes `fflate` for the H5P packages.
- `scripts/setup-pwa.mjs` deletes the duplicate `/build/h5p` copy MyST emits and marks H5P iframes `loading="lazy"`.

## Presentation gap

Problems already use `{exercise}` with a `{solution}` dropdown. Learning objectives are an H3 rather than a `{note}`, and some labels use hyphens (`ex-…`, `fig:ch03-…`) rather than the `ex:` / `fig:` form in the presentation skill. Callout-role alignment is deferred.
