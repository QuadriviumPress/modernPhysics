# Figure generation

Figures for Chapters 1--14 are generated with matplotlib and written
as SVG into [`../../images/`](../../images/). The rendered SVGs are
**committed**, because the GitHub Pages workflow runs `myst build --html`
only — there is no Python available at build time.

## Regenerating

```bash
python3 -m pip install -r requirements-figures.txt
python3 scripts/figures/ch01_solutions.py    # figures embedded in ch. 1 worked solutions
python3 scripts/figures/ch02_solutions.py    # figures embedded in ch. 2 worked solutions
python3 scripts/figures/ch03_solutions.py    # figures embedded in ch. 3 worked solutions
python3 scripts/figures/ch04_figures.py      # computed curves for ch. 4
python3 scripts/figures/ch04_schematics.py   # diagrams for ch. 4
python3 scripts/figures/ch04_solutions.py    # figures embedded in ch. 4 worked solutions
python3 scripts/figures/ch05_figures.py      # computed curves for ch. 5
python3 scripts/figures/ch05_schematics.py   # diagrams for ch. 5
python3 scripts/figures/ch05_solutions.py    # figures embedded in ch. 5 worked solutions
python3 scripts/figures/ch06_solutions.py    # figures embedded in ch. 6 worked solutions
python3 scripts/figures/ch07_solutions.py    # figures embedded in ch. 7 worked solutions
python3 scripts/figures/ch08_solutions.py    # figures embedded in ch. 8 worked solutions
python3 scripts/figures/ch09_solutions.py    # figures embedded in ch. 9 worked solutions
python3 scripts/figures/ch10_figures.py      # radial probability / energy levels for ch. 10
python3 scripts/figures/ch10_solutions.py    # figures embedded in ch. 10 worked solutions
python3 scripts/figures/ch11_figures.py      # ionization-energy curve for ch. 11
python3 scripts/figures/ch11_solutions.py    # figures embedded in ch. 11 worked solutions
python3 scripts/figures/ch12_figures.py      # MO diagram / rovibrational spectrum for ch. 12
python3 scripts/figures/ch12_solutions.py    # figures embedded in ch. 12 worked solutions
python3 scripts/figures/ch13_figures.py      # binding-energy curve for ch. 13
python3 scripts/figures/ch13_solutions.py    # figures embedded in ch. 13 worked solutions
python3 scripts/figures/ch14_figures.py      # Feynman diagrams / Standard Model chart for ch. 14
python3 scripts/figures/ch14_solutions.py    # figures embedded in ch. 14 worked solutions
python3 scripts/figures/simulation_placeholder.py   # fallback card for {simulation}
python3 scripts/figures/brand_assets.py             # social card, favicon, header logos
```

Each script prints the files it writes. Commit the regenerated SVGs along with
any change to the scripts, so the site and the source stay in step.

## Layout

| File | Contents |
|---|---|
| `figstyle.py` | Shared rcParams, color palette, `save()`, and the `fringe_strip()` helper that renders an intensity profile as the bright/dark bands seen on a screen |
| `ch01_solutions.py` | Solution-only figures: river-crossing/Michelson-arm analogy and ether-signal scale comparison |
| `ch02_solutions.py` | Solution-only figures: Earth-vs-muon-frame atmospheric crossing, worldline angles, twin-trip worldlines |
| `ch03_solutions.py` | Solution-only figures: back-to-back two-body products and fixed-target-vs-collider threshold comparison |
| `ch04_figures.py` | Two-slit and $N$-slit intensity, coherence wave trains, soap-film color vs. thickness |
| `ch04_schematics.py` | Huygens wavelets, double-slit geometry, phasor addition, thin-film rays, Michelson interferometer |
| `ch04_solutions.py` | Solution-only figures: six-slit principal maxima/zeros/secondary maxima, simulated Newton's-rings pattern, two-wavelength fringe-coincidence overlay, Case A/B thin-film ray diagrams |
| `ch05_figures.py` | Single-slit $\mathrm{sinc}^2$, slit-width scaling, double-slit envelope with missing orders, grating resolving power, Airy pattern and the Rayleigh criterion |
| `ch05_schematics.py` | Single-slit pairwise cancellation, the circular phasor arc, Bragg reflection |
| `ch05_solutions.py` | Solution-only figures: grating order-overlap map, Bragg order-existence limit, EHT single-dish-vs-array resolution comparison, CD/DVD order comparison |
| `ch06_solutions.py` | Solution-only figures (ch. 6 has no body figures at all): tungsten blackbody spectrum vs. visible band, two-point photoelectric $h$/$\phi$ fit, Compton shift vs. angle with visible/X-ray fractional-shift comparison, pair-production energy budget, idealized Compton-edge/photopeak spectrum |
| `ch07_solutions.py` | Solution-only figures (ch. 7 has no body figures at all): de Broglie wavelength scale comparison, $n=1$ Bohr standing-wave (wrapped and unrolled), Lorentzian natural linewidth, relativistic phase-vs-group velocity, wavepacket spreading-time scale comparison |
| `ch08_solutions.py` | Solution-only figures (ch. 8 has no body figures at all): infinite-well energy ladder with photon transition, step-reflection $R$ vs. $V_0/E$, tunneling-barrier amplitude envelope (proton vs. alpha), oscillator level ladder + H$_2$ zero-point spread, $\Delta n=\pm1$ selection-rule ladder, correspondence-principle $n=0$ vs. $n=20$ probability density, finite-well graphical bound-state count |
| `ch09_solutions.py` | Solution-only figures (ch. 9 has no body figures at all): $\ell=2$/$\ell=3$ angular-momentum vector cones, centrifugal-barrier term vs. $r$, isotropic-oscillator shell filling vs. nuclear magic numbers, $s$ vs. $p_z$ angular probability density, orbital Zeeman splitting |
| `ch10_figures.py` | Hydrogen radial probability distributions $P(r)=r^2\lvert R_{n\ell}\rvert^2$ for $1s,2s,2p,3s,3p,3d$ (closed-form $R_{n\ell}$), with node markers; energy-level diagram for $n=1$–$5$ with Lyman/Balmer/Paschen transition arrows |
| `ch10_solutions.py` | Solution-only figures: $\Delta\ell=\pm1$ selection-rule transition map, H vs. Li$^{2+}$ radial-probability $Z$-scaling, Stern–Gerlach beam-splitting schematic, Zeeman spectral-line triplet |
| `ch11_figures.py` | First ionization energy vs. atomic number ($Z=1$–$36$, NIST Atomic Spectra Database values), showing the periodic sawtooth with noble-gas peaks and alkali-metal troughs annotated |
| `ch11_solutions.py` | Solution-only figures: Hund's-rule orbital-box diagram for N $2p^3$, Moseley single- vs. two-point fit comparison, Slater's-rules $Z_{\rm eff}$ bar comparison, P vs. S orbital-box exchange-energy comparison, period-3-to-K atomic-radius anomaly |
| `ch12_figures.py` | Side-by-side N₂/O₂ molecular-orbital energy-level diagrams (atomic 2s/2p levels outside, filled MOs in the middle, showing the $\sigma_{2p}$/$\pi_{2p}$ order swap); rovibrational (vibration–rotation) stick spectrum with P-branch/R-branch lines spaced by $2B$ and the missing-Q-branch gap at the band origin |
| `ch12_solutions.py` | Solution-only figures: VSEPR shape sketches (NH$_3$/CO$_2$/SF$_6$), He$_2^+$ MO diagram, F$_2$/F$_2^+$ MO-diagram comparison, SF$_4$/XeF$_4$ lone-pair-placement comparison |
| `ch13_figures.py` | Binding energy per nucleon vs. mass number, computed from standard atomic mass data for a representative set of nuclides (deuterium through uranium-238), with the iron/nickel peak and fusion/fission arrows annotated directly on the plot |
| `ch13_solutions.py` | Solution-only figures: I-131/C-14 decay-curve pair with read-off points, Ra-226/Rn-222 secular-equilibrium buildup curve, D-T fusion energy-sharing bar |
| `ch14_figures.py` | Original Feynman-diagram schematic ($e^-e^-$ scattering via photon exchange; neutron beta decay via $W^-$ exchange, with the antiparticle arrow-reversal convention shown explicitly) and a redrawn Standard Model particle-content chart (three generations of quarks/leptons plus gauge bosons and the Higgs, in the book's own palette) |
| `ch14_solutions.py` | Solution-only figures: conservation-law pass/fail checklist (5 reactions × Q/B/L/S), $K^-$/$K^+$ antiparticle quantum-number comparison, muon-decay Feynman diagram (reuses `ch14_figures._fermion_line`/`_wavy_line`), muon decay-length vs. energy curve, electron-pair vs. proton-pair gravity/EM force-ratio comparison |
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
