# Adding Diagrams to Worked Solutions — Chapters 4–14

Goal: add a diagram to selected worked solutions in `## Problems` sections, chapters 4
through 14 (chapters 1–3 are out of scope — see `ch04-14-solution-review.md` for the
separate correctness-review pass over these same chapters). Coverage is **selective**:
only where a diagram genuinely clarifies the answer (geometric setups, energy-level/decay
schemes, spectra, potential-well sketches, computed curves specific to the problem's
numbers) — not every solution. Target is roughly 3–7 new figures per chapter, not
exhaustive coverage. Purely algebraic/plug-and-chug solutions are left as text.

Figures are generated with matplotlib via `scripts/figures/chNN_solutions.py` (new files,
one per chapter, alongside the existing `chNN_figures.py`/`chNN_schematics.py` used for the
main chapter body) and written as committed SVGs into `images/`, following the existing
house style in `scripts/figures/figstyle.py` (palette, `save()`, `fringe_strip()`, white
background, `svg.fonttype: path`). See `scripts/figures/README.md` for the regeneration
list. Editing is done directly in the chapter `.md` files: a `{figure}` directive is
inserted into the relevant `:::{solution}` block, with a `:label:` and short `:alt:` text,
placed just before the closing "Therefore, ..." sentence.

No virtualenv is provided in this repo for regenerating figures; a scratch one was created
during this task (numpy/matplotlib/scipy only — no committed `requirements.txt` change).

If this task is resumed in a new session: read the status table below and continue from
the first chapter marked `N`. Each chapter's row lists which problems got a diagram, so a
fresh session does not need to re-read the whole chapter to know what's done.

## Status

| Ch | File | # Problems | Diagrams added? | Problems illustrated |
|---|---|---|---|---|
| 4 | ch-04-interference-of-light.md | 20 | Y | 9, 11, 13, 20 |
| 5 | ch-05-diffraction-of-light.md | 20 | Y | 5\*, 8\*, 9, 10\*, 14, 19, 20 |
| 6 | ch-06-particle-properties-of-waves.md | 20 | Y | 2, 5, 9, 10\*, 12\*, 14, 17 |
| 7 | ch-07-wave-properties-of-particles.md | 20 | Y | 1, 6, 8, 15\*, 16, 19 |
| 8 | ch-08-the-schrodinger-equation.md | 20 | Y | 1, 4, 6, 9, 10\*, 12, 13, 17 |
| 9 | ch-09-quantum-mechanics-in-three-dimensions.md | 19 | Y | 3, 8, 9\*, 11, 13\*, 15, 16 |
| 10 | ch-10-the-hydrogen-atom.md | 10 | Y | 1\*, 3, 6\*, 7, 8, 9 |
| 11 | ch-11-many-electron-atoms.md | 12 | Y | 2, 4\*, 7, 8, 9, 12 |
| 12 | ch-12-molecular-structure.md | 10 | Y | 1, 2\*, 3, 6\*, 7, 8, 9\* |
| 13 | ch-13-nuclear-physics.md | 10 | Y | 2\*, 3, 4\*, 7\*, 8, 9\*, 10 |
| 14 | ch-14-elementary-particles-and-the-standard-model.md | 11 | Y | 3, 7, 8\*, 9, 10, 11 |

## Chapter details

### Chapter 4 — Interference of Light (4 diagrams added)

New script: `scripts/figures/ch04_solutions.py`.

- **Problem 9** (six equally-spaced slits, $N=6$): `ch04-sol-six-slit.svg` — full-range
  principal-maxima plot plus a zoomed panel between $m=0$ and $m=1$ showing the 5 zeros
  and 4 secondary maxima the solution counts.
- **Problem 11** (oil on water vs. oil on $n=1.60$, Case A vs. Case B): `ch04-sol-thin-film-cases.svg`
  — side-by-side ray schematics with phase-shift annotations at each interface, showing why
  the minimum-thickness formula differs by a factor of two.
- **Problem 13** (Newton's rings, $R=2.00\ \text{m}$): `ch04-sol-newton-rings.svg` — simulated
  2D reflected ring pattern (dark center, one phase reversal) with the 10th dark ring radius
  marked, illustrating both the dark center and the ring-crowding-with-$m$ argument.
- **Problem 20** (two-wavelength fringe coincidence): `ch04-sol-coincidence.svg` — the two
  bright-fringe patterns overlaid plus their product, with the first coincidence at
  $y=3.20\ \text{cm}$ marked.

Problems not illustrated (1–8, 10, 12, 14–19) are pure angle/spacing/thickness algebra where
a new diagram would not add beyond the existing body figures (e.g. Michelson and thin-film
geometry are already shown in `ch04-michelson.svg` / `ch04-thin-film-rays.svg`).

### Chapter 5 — Diffraction of Light (4 new diagrams + 3 reused-figure references)

New script: `scripts/figures/ch05_solutions.py`. Starred (\*) problems below reference an
*existing* body figure via `{numref}` rather than a new image, because the body figure
already plots that problem's exact case:

- **Problem 5\*** ($d/a=5$, missing orders, nine bright fringes): the body's
  `ch05-double-slit-envelope.svg` (`fig:ch05-double-slit`) already is this exact case.
- **Problem 8\*** (grating resolving power, first vs. second order): the body's
  `ch05-grating-resolving-power.svg` (`fig:ch05-resolving-power`) shows the same
  $R=mN$ resolving-power argument for the sodium doublet.
- **Problem 9** (grating order overlap, white light): new `ch05-sol-order-overlap.svg` —
  $\theta_m(\lambda)$ for $m=1,2,3$ with the 2nd/3rd-order overlap band shaded.
- **Problem 10\*** (Rayleigh criterion, human eye): the body's `ch05-airy-rayleigh.svg`
  (`fig:ch05-rayleigh`) shows the "just resolved" Airy-pattern case referenced here.
- **Problem 14** (Bragg order limit, $d=0.137\ \text{nm}$): new `ch05-sol-bragg-order-limit.svg`
  — bar chart of $\sin\theta_m$ for $m=1$–$5$, showing the physical ceiling at $m=3$.
- **Problem 19** (Event Horizon Telescope resolution): new `ch05-sol-eht-resolution.svg` —
  log-log $\theta_{\min}$ vs. aperture $D$, marking a large single dish, the Earth-scale
  array, and the $40\ \mu\text{arcsec}$ M87 shadow target.
- **Problem 20** (CD vs. DVD track spacing): new `ch05-sol-cd-dvd-orders.svg` — bar
  comparison of diffraction angles by order for both media, showing the DVD has no
  second order at all.

Problems not illustrated (1–4, 6, 7, 11–13, 15–18) are pure algebra, or (Problem 11, 13)
immediately follow a just-illustrated problem using the same criterion.

### Chapter 6 — Particle Properties of Waves (5 new diagrams, 7 problems touched)

Chapter 6 had **zero** figures of any kind before this pass (no body figures either). New
script: `scripts/figures/ch06_solutions.py`. Starred (\*) problems reference the new figure
built primarily for another problem rather than getting their own.

- **Problem 2** (tungsten filament, Wien + Stefan–Boltzmann): new `ch06-sol-tungsten-spectrum.svg`
  — the $T=2900\ \text{K}$ blackbody curve with the visible band shaded, showing visually why
  incandescent bulbs waste most of their output as infrared.
- **Problem 5** (two-point photoelectric determination of $h$ and $\phi$): new
  `ch06-sol-photoelectric-fit.svg` — $V_0$ vs. $f$ with the two data points, the fitted line,
  and the threshold-frequency intercept.
- **Problem 9 / 10\* / 12\*** (Compton shift at $90°$/$180°$, and why visible light hides the
  effect): new `ch06-sol-compton-angle.svg` — one figure serving all three: $\Delta\lambda(\theta)$
  with both angles marked (9, 10), plus a log-scale bar comparing $\Delta\lambda/\lambda$ for
  visible vs. X-ray light (12).
- **Problem 14** (pair-production energy sharing): new `ch06-sol-pair-production-budget.svg` —
  a stacked energy bar showing the $2.50\ \text{MeV}$ photon split into two rest masses plus
  shared kinetic energy.
- **Problem 17** (Compton edge vs. photopeak): new `ch06-sol-compton-spectrum.svg` — an
  idealized detector spectrum with both features, explicitly captioned as schematic (not the
  exact Klein–Nishina shape).

Problems not illustrated (1, 3–4, 6–8, 11, 13, 15–16, 18–20) are pure algebra/derivation or
short conceptual-explanation answers with no natural picture.

### Chapter 7 — Wave Properties of Particles (5 new diagrams, 6 problems touched)

Chapter 7 also had zero figures before this pass. New script: `scripts/figures/ch07_solutions.py`.

- **Problem 1** (de Broglie wavelengths: electron/proton/baseball): new `ch07-sol-debroglie-scale.svg`
  — log-scale comparison across 70 orders of magnitude, with atomic- and nuclear-diameter
  reference lines showing which wavelengths are large enough to diffract.
- **Problem 6** (Bohr $n=1$ standing wave): new `ch07-sol-bohr-standing-wave.svg` — the wave
  shown both wrapped around the orbit and unrolled into a line, making $\lambda=2\pi r$ literal.
- **Problem 8** (natural linewidth from finite lifetime): new `ch07-sol-linewidth.svg` — a
  Lorentzian line shape with its FWHM marked as $\Delta E$.
- **Problem 15\*** (nonrelativistic phase vs. group velocity, conceptual only): references the
  new Problem 19 figure rather than getting its own, since it makes the same qualitative point.
- **Problem 16** (wavepacket spreading time, electron vs. dust grain): new `ch07-sol-spreading-time.svg`
  — log-scale comparison with "1 second lab measurement" and "age of the universe" reference lines.
- **Problem 19** (relativistic phase velocity exceeds $c$): new `ch07-sol-phase-group-velocity.svg`
  — $v_g=u$ and $v_p=c^2/u$ plotted together, showing $v_p>c$ everywhere except at $u=c$.

Problems not illustrated (2–5, 7, 9–14, 17–18, 20) are pure algebra/derivation or short
conceptual-explanation answers with no natural picture.

### Chapter 8 — The Schrödinger Equation (7 new diagrams, 8 problems touched)

Chapter 8 also had zero figures before this pass — a natural gap given how visual this
chapter is. New script: `scripts/figures/ch08_solutions.py`.

- **Problem 1** (infinite-well $n=2\to1$ photon): new `ch08-sol-infinite-well-levels.svg` —
  the $n^2$ energy ladder with the emitted photon marked.
- **Problem 4** (step reflection $R$ at two heights): new `ch08-sol-step-reflection.svg` —
  continuous $R(V_0/E)$ curve with both computed cases marked, generalizing part (c)'s
  "comment on how $R$ changes" into an actual curve.
- **Problem 6** (proton vs. alpha tunneling): new `ch08-sol-tunneling-barrier.svg` — wavefunction
  amplitude envelope through the barrier, showing the alpha's faster exponential decay.
- **Problem 9 / 10\*** (oscillator zero-point energy and level spacing; H$_2$ zero-point
  spread vs. bond length): new `ch08-sol-oscillator-ladder-spread.svg` — one figure serving
  both: the level ladder (9) beside the position-space spread compared to the bond length (10).
- **Problem 12** ($\Delta n=\pm1$ selection rule): new `ch08-sol-selection-rule.svg` — three
  levels with the allowed $2\to1$ and forbidden $2\to0$ transitions drawn side by side.
- **Problem 13** (correspondence principle, large-$n$ oscillator): new
  `ch08-sol-correspondence-principle.svg` — computed $|\psi_n|^2$ for $n=0$ and $n=20$
  (via Hermite polynomials), the $n=20$ panel overlaid with the classical time-averaged
  density peaking at the turning points.
- **Problem 17** (finite-well bound-state count vs. depth): new
  `ch08-sol-finite-well-bound-states.svg` — graphical solution of $z\tan z=\sqrt{z_0^2-z^2}$
  for two well depths, showing the deeper well crossing more branches.

Problems not illustrated (2–3, 5, 7–8, 11, 14–16, 18–20) are pure algebra/derivation, short
proofs, or conceptual-explanation answers with no natural picture.

### Chapter 9 — Quantum Mechanics in Three Dimensions (5 new diagrams, 7 problems touched)

Chapter 9 also had zero figures before this pass. New script: `scripts/figures/ch09_solutions.py`.

- **Problem 3 / 9\*** ($\ell=2$ vector model; minimum-angle trend with $\ell$): new
  `ch09-sol-angular-momentum-cones.svg` — the five allowed $\vec L$ orientations for $\ell=2$,
  plus a side panel comparing the minimum angle at $\ell=2$ and $\ell=3$ (Problem 9).
- **Problem 8** (centrifugal barrier, $s$ vs. $p$ at $r=0$): new `ch09-sol-centrifugal-barrier.svg`
  — the term plotted vs. $r$, flat at zero for $\ell=0$ and diverging for $\ell=1$.
- **Problem 11 / 13\*** (3D oscillator shell degeneracy; nuclear magic numbers): new
  `ch09-sol-oscillator-shells.svg` — shells $N=0,1,2$ with spatial degeneracy, spin capacity,
  and running total, landing on $2,8,20$.
- **Problem 15** ($p_z$ angular shape): new `ch09-sol-p-orbital-shape.svg` — polar plots of the
  isotropic $s$-state density beside the dumbbell-shaped $p_z$ density.
- **Problem 16** (orbital Zeeman splitting): new `ch09-sol-zeeman-splitting.svg` — $\ell=1$
  splitting into three levels vs. $\ell=0$ staying single, field off vs. on.

Problems not illustrated (1–2, 4–7, 10, 12, 14, 17–19) are pure algebra/derivation, short
proofs, or conceptual-explanation answers with no natural picture.

### Chapter 10 — The Hydrogen Atom (4 new diagrams + 2 reused-figure references)

Chapter 10 already had body figures for the radial probability distributions and the energy
levels — this pass reused both. New script: `scripts/figures/ch10_solutions.py`.

- **Problem 1\*** (Lyman series wavelengths): references the body's `fig:ch10-energy-levels`,
  whose Lyman cluster already draws exactly this transition and its series limit.
- **Problem 3** ($\Delta\ell=\pm1$ selection rule on 4 transitions): new
  `ch10-sol-selection-rule-transitions.svg` — levels grouped by orbital type, with allowed
  transitions crossing one column and the forbidden $3s\to2s$ trying to stay in place.
- **Problem 6\*** (ground-state radial probability peaks at $a_0$): references the body's
  `fig:ch10-radial-probability`, whose $1s$ panel already shows this exact peak.
- **Problem 7** (Li$^{2+}$ $Z$-scaling): new `ch10-sol-hydrogenic-z-scaling.svg` — H and
  Li$^{2+}$ radial probability curves (each normalized to its own peak) showing the $1/Z$
  peak-radius shift.
- **Problem 8** (Stern–Gerlach spot separation): new `ch10-sol-stern-gerlach.svg` — beam
  splitting into two spots at the screen, deflection exaggerated for visibility and captioned
  as such.
- **Problem 9** (Zeeman wavelength splitting of H$_\beta$): new `ch10-sol-zeeman-line-splitting.svg`
  — the field-free line becoming a triplet spaced by $\Delta\lambda$.

Problems not illustrated (2, 4–5, 10) are pure algebra/counting or a short conceptual
explanation with no natural picture.

### Chapter 11 — Many-Electron Atoms (5 new diagrams, 6 problems touched)

New script: `scripts/figures/ch11_solutions.py`.

- **Problem 2** (Hund's rule, N $2p^3$): new `ch11-sol-hunds-rule-nitrogen.svg` — three
  orbital boxes each with one aligned-spin electron.
- **Problem 4\* / 9** (Moseley's law, single-point vs. two-point fit): new `ch11-sol-moseley-plot.svg`
  — both fits plotted together with their predicted points (Ni, Ag) marked; Problem 4 links to it.
- **Problem 7** (Slater's-rules $Z_{\rm eff}$ for Mg): new `ch11-sol-zeff-comparison.svg` —
  bar comparison against the text's Na and Cl values.
- **Problem 8** (P vs. S ionization-energy reversal): new `ch11-sol-phosphorus-sulfur.svg` —
  orbital-box diagrams showing P's three unpaired electrons vs. S's one pair.
- **Problem 12** (Ar vs. K atomic-radius anomaly): new `ch11-sol-atomic-radius-anomaly.svg` —
  period-3 radii decreasing, then jumping up at potassium's new shell.

Problems not illustrated (1, 3, 5–6, 10–11) are pure algebra/counting or short conceptual
explanations with no natural picture.

### Chapter 12 — Molecular Structure (4 new diagrams + 3 reused-figure references)

New script: `scripts/figures/ch12_solutions.py`. Chapter 12 already had a body MO diagram
(N$_2$/O$_2$) and rovibrational spectrum figure — both reused directly.

- **Problem 1** (VSEPR shapes for NH$_3$/CO$_2$/SF$_6$): new `ch12-sol-vsepr-shapes.svg` —
  three ball-and-stick sketches side by side.
- **Problem 2\*** (N$_2$ MO diagram, bond order 3): references the body's `fig:ch12-mo-n2-o2`,
  which already shows this exact filled diagram.
- **Problem 3** (He$_2^+$ MO diagram, bond order 1/2): new `ch12-sol-he2-plus-mo.svg`.
- **Problem 6\*** (O$_2^\pm$ bond-order shift): references the same body MO figure, pointing
  at the $\pi_{2p}^*$ level where the extra/missing electron goes.
- **Problem 7** (SF$_4$ seesaw vs. XeF$_4$ square planar): new `ch12-sol-sf4-xef4.svg` —
  lone-pair placement drawn explicitly for both.
- **Problem 8** (F$_2$/F$_2^+$ MO diagram and paramagnetism): new `ch12-sol-f2-mo-diagram.svg`
  — full filled diagrams side by side, showing the unpaired $\pi_{2p}^*$ electron in the ion.
- **Problem 9\*** (HCl rovibrational line spacing and Q-branch gap): references the body's
  `fig:ch12-rovibrational`, the same P/R-branch structure with HCl's own numbers.

Problems not illustrated (4–5, 10) are pure algebra or a short conceptual explanation with no
natural picture.

### Chapter 13 — Nuclear Physics (3 new diagrams + 3 reused-figure references)

New script: `scripts/figures/ch13_solutions.py`. The body's binding-energy-per-nucleon curve
(`fig:ch13-binding-curve`) is reused three times, since three separate problems each land a
specific numeric point on that one curve.

- **Problem 2\*** (He-4 binding energy per nucleon): references `fig:ch13-binding-curve`,
  noting the point sits on the curve's rising left flank, well below the peak.
- **Problem 3** ($^{131}$I activity decay): new `ch13-sol-decay-curves.svg` — built as a
  two-panel figure that also serves Problem 9.
- **Problem 4\*** (why alpha decay is favored for heavy nuclei): references
  `fig:ch13-binding-curve` directly, tying the argument to the curve's shape.
- **Problem 7\*** (semi-empirical mass formula for Sn-120): references `fig:ch13-binding-curve`,
  noting the predicted value's location near the peak plateau.
- **Problem 8** (secular equilibrium, Ra-226/Rn-222): new `ch13-sol-secular-equilibrium.svg` —
  daughter activity growing in to match the parent's.
- **Problem 9\*** ($^{14}$C dating): second panel of `ch13-sol-decay-curves.svg` (shared with
  Problem 3).
- **Problem 10** (D-T fusion energy sharing): new `ch13-sol-fusion-energy-sharing.svg` — an
  energy bar split in inverse proportion to mass.

Problems not illustrated (1, 5–6) are pure algebra/derivation with no natural picture.

### Chapter 14 — Elementary Particles and the Standard Model (5 new diagrams, 6 problems touched)

New script: `scripts/figures/ch14_solutions.py`. The muon-decay Feynman diagram reuses the
body script's `_fermion_line`/`_wavy_line` helpers (imported from `ch14_figures.py`) so it
matches the body's `fig:ch14-feynman-diagrams` style exactly, per the problem's own request.

- **Problem 3 / 8\*** (conservation-law checks across 5 reactions): new
  `ch14-sol-conservation-checklist.svg` — a pass/fail table covering Problem 3's four
  reactions plus Problem 8's strong-interaction check, across $Q$, $B$, $L$, $S$.
- **Problem 7** ($K^-$ as $K^+$'s antiparticle): new `ch14-sol-kaon-antiparticle.svg` — quark
  content, charge, and strangeness shown side by side with opposite signs.
- **Problem 9** (two-vertex muon-decay Feynman diagram): new `ch14-sol-muon-decay-feynman.svg`
  — drawn in the body figure's own style, referencing it directly.
- **Problem 10** (muon decay length vs. beam energy): new `ch14-sol-muon-decay-length.svg` —
  the worked example's and this problem's beams marked on one $\ell$-vs-$E$ curve.
- **Problem 11** (electron-pair gravity/EM ratio): new `ch14-sol-gravity-em-ratio.svg` — log-scale
  bar comparison against the worked example's two-proton ratio.

Problems not illustrated (1–2, 4–6) are short algebra/classification with no natural picture.

## Summary

All 11 chapters (4–14) now have diagrams supporting selected worked solutions: 51 new
solution-specific figures across 11 new `scripts/figures/chNN_solutions.py` scripts, plus 12
`{numref}` references (8 distinct figures) to existing body figures where a body figure
already showed the exact case a solution needed — 3 in ch. 5, 2 in ch. 10, 2 in ch. 12
(one used twice), 1 in ch. 13 (used three times). Chapters 6, 7, 8, and 9 had no figures of
any kind before this pass, and gained solution figures only (no body figures existed to
reference). Every new `{figure}` block was verified with a real `myst build --html` (no
errors/warnings) and the resulting image files confirmed present in `_build/site/public/`.
