# Figure generation

Figures for Chapters 4 and 5 are generated with matplotlib and written as SVG
into [`../../images/`](../../images/). The rendered SVGs are **committed**,
because the GitHub Pages workflow runs `myst build --html` only — there is no
Python available at build time.

## Regenerating

```bash
pip install matplotlib numpy scipy
python3 scripts/figures/ch04_figures.py      # computed curves for ch. 4
python3 scripts/figures/ch04_schematics.py   # diagrams for ch. 4
python3 scripts/figures/ch05_figures.py      # computed curves for ch. 5
python3 scripts/figures/ch05_schematics.py   # diagrams for ch. 5
python3 scripts/figures/simulation_placeholder.py   # fallback card for {simulation}
python3 scripts/figures/brand_assets.py             # social card, favicon, header logos
```

Each script prints the files it writes. Commit the regenerated SVGs along with
any change to the scripts, so the site and the source stay in step.

## Layout

| File | Contents |
|---|---|
| `figstyle.py` | Shared rcParams, color palette, `save()`, and the `fringe_strip()` helper that renders an intensity profile as the bright/dark bands seen on a screen |
| `ch04_figures.py` | Two-slit and $N$-slit intensity, coherence wave trains, soap-film color vs. thickness |
| `ch04_schematics.py` | Huygens wavelets, double-slit geometry, phasor addition, thin-film rays, Michelson interferometer |
| `ch05_figures.py` | Single-slit $\mathrm{sinc}^2$, slit-width scaling, double-slit envelope with missing orders, grating resolving power, Airy pattern and the Rayleigh criterion |
| `ch05_schematics.py` | Single-slit pairwise cancellation, the circular phasor arc, Bragg reflection |
| `simulation_placeholder.py` | The generic fallback card shown in PDF, DOCX, and print for a `{simulation}` with no screenshot |
| `brand_assets.py` | Site identity: the 1200×630 social card, the multi-size `favicon.ico`, and the light/dark header logos |

## Conventions

- **SVG everywhere except two files.** `simulation_placeholder.py` writes PNG,
  because LaTeX accepts only `.pdf .png .jpg .jpeg` and DOCX only
  `.png .jpg .jpeg`; an SVG placeholder would need Inkscape or ImageMagick on
  the build machine to survive an export. `brand_assets.py` writes PNG and ICO
  for the same class of reason — some social platforms will not render an SVG
  `og:image`, and MyST copies `site.options.favicon` to `/favicon.ico`
  byte-for-byte, so that file has to really be an ICO.
- **Palette** matches the hand-authored SVG schematics in `images/` (blue `#1769aa`,
  red `#b33a3a`, green `#2e7d5b`, purple `#6a4c93`, orange `#d97706`).
- **White background**, set explicitly, so figures read the same in either site theme.
- **`svg.fonttype: "path"`** so text renders identically without depending on the
  viewer's fonts. This makes files larger; `path.simplify` keeps them manageable.
  Avoid `fill_between` on dense curves — it is not path-simplified and inflates
  the SVG several-fold.
- **Multi-panel figures** use `ax.set_anchor("N")` so that equal-aspect panels of
  differing shape still line their titles up.
- **`fringe_strip(..., gamma=...)`** brightens faint bands so they survive
  reproduction; whenever `gamma < 1` is used, the figure caption says so, since
  the strip is then no longer linear in intensity.
