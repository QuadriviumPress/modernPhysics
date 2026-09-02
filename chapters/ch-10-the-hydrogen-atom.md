---
title: The Hydrogen Atom
short_title: Chapter 10. The Hydrogen Atom
label: ch-the-hydrogen-atom
numbering:
  enumerator: "10.%s"
---

## Learning Objectives

By the end of this chapter, you should be able to:

- State the radial equation for the hydrogen atom and the resulting energy quantization, and compare it to the Bohr model's prediction.
- Explain, from the normalizability of the radial equation's solutions, why the principal quantum number $n$ is discrete and why $\ell$ is restricted to $0,\ldots,n-1$.
- Write down the explicit hydrogen radial wave functions $R_{10}$, $R_{20}$, $R_{21}$, describe the resulting radial probability distributions, and use the effective (centrifugal) potential to explain why low-$\ell$ states penetrate closer to the nucleus.
- Extend the hydrogen solution to hydrogenic ions (e.g., $\text{He}^+$, $\text{Li}^{2+}$) and compute the $Z^2$ scaling of energy and $1/Z$ scaling of orbital size.
- Read an energy-level diagram for hydrogen and compute the wavelengths of lines in the Lyman, Balmer, and Paschen series.
- Enumerate the allowed quantum states for a given $n$ and explain the origin of degeneracy in hydrogen.
- Explain electron spin and the Stern–Gerlach experiment that revealed it, and compute the force and deflection produced by a Stern–Gerlach magnet.
- Combine orbital and spin angular momentum via the orbital and spin magnetic quantum numbers, and compute orbital and spin magnetic moments.
- Compute the frequency and wavelength shift produced by the (normal) Zeeman effect, and estimate the order of magnitude of fine-structure splitting in terms of the fine-structure constant $\alpha$.
- Apply selection rules to determine which transitions between hydrogen energy levels are allowed.

## Introduction

[Chapter 9](#ch-quantum-mechanics-in-three-dimensions) developed the general machinery for any central potential: separation into radial and angular parts, and the universal quantization of orbital angular momentum. This chapter specializes that machinery to the single most important central potential in atomic physics — the Coulomb attraction between an electron and a proton — and solves it for the hydrogen atom, the only atom for which the Schrödinger equation can be solved exactly in closed form. The result reproduces (and explains, rather than assumes) the energy levels first found empirically in atomic spectra and postulated ad hoc in the 1913 Bohr model, while revealing a far richer structure — angular momentum, spatial probability distributions, and a fourth quantum number, electron spin, with no classical counterpart at all.

## The Radial Equation and Energy Quantization

For the hydrogen atom, the central potential is the Coulomb attraction between the electron (charge $-e$) and the proton (charge $+e$),

$$
V(r) = -\frac{e^2}{4\pi\epsilon_0\, r}.
$$

Substituting this $V(r)$ into the radial equation obtained from the separation $\psi = R(r)Y(\theta,\phi)$ ([Chapter 9](#ch-quantum-mechanics-in-three-dimensions)), and requiring $R(r)$ to be normalizable (i.e., to decay rather than blow up as $r\to\infty$, and to remain finite at $r=0$), restricts the allowed energies to exactly the same discrete set found by Bohr in 1913 from an ad hoc semiclassical model:

$$
E_n = -\frac{m_ee^4}{8\epsilon_0^2h^2}\,\frac{1}{n^2} = -\frac{13.6\ \text{eV}}{n^2}, \qquad n = 1, 2, 3,\ldots.
$$

:::{margin}
**Reduced mass.** $E_n$ above technically uses the electron mass $m_e$ alone, an approximation that treats the proton as infinitely heavy and fixed. The exact two-body treatment replaces $m_e$ everywhere with the **reduced mass** $\mu = m_em_p/(m_e+m_p) \approx 0.9995\,m_e$, shifting every hydrogen level by about $0.05\%$ — small, but (see below) not unmeasurable.
:::

This agreement is a triumph for the Schrödinger equation — it reproduces a result that matched atomic spectroscopy to remarkable precision — but the derivation and interpretation are entirely different from Bohr's. Bohr postulated that the electron moves on definite circular orbits, with angular momentum quantized as $L = n\hbar$ by assumption. The Schrödinger treatment makes no such assumption about orbits at all; instead, $n$ emerges purely as an index counting the normalizable solutions of the radial equation, the electron has no well-defined trajectory, and — as shown below — the ground state ($n=1$) actually has **zero** orbital angular momentum, in direct contradiction to Bohr's $L=n\hbar$. The numerical agreement in $E_n$ is, in this sense, a coincidence specific to the particular form of the $1/r$ Coulomb potential, not a sign that the Bohr picture was substantially correct.

:::{note}
The reduced-mass correction is not just bookkeeping. In 1931–32, Harold Urey searched for a heavier isotope of hydrogen by looking for a faint companion line shifted slightly to the blue of each ordinary hydrogen line — exactly the shift predicted because a heavier nucleus pulls $\mu$ closer to $m_e$ and makes $|E_n|$ very slightly larger. Finding that predicted companion in a distilled hydrogen sample was the discovery of **deuterium**, and earned Urey the 1934 Nobel Prize in Chemistry — a case of a correction easy to dismiss as negligible turning out to carry real, measurable physics.
:::

The mechanism behind the discreteness is worth making explicit, since the same pattern recurs throughout quantum mechanics. Solving the radial equation for a trial (negative) energy $E$ produces a function that falls off as $e^{-\kappa r}$ at large $r$, with $\kappa = \sqrt{-2m_eE}/\hbar$, multiplied by an infinite series in powers of $r$; for almost any choice of $E$, that series itself grows fast enough that the full product still diverges as $r\to\infty$, exactly the unnormalizable blow-up that ruled out most trial energies in the finite square well of [Chapter 8](#ch-the-schrodinger-equation). Demanding a normalizable wave function forces the series to *terminate* after a finite number of terms — collapsing it from an infinite series into a finite polynomial — and this termination happens only when $1/\kappa a_0$ lands exactly on a positive integer, which is precisely the principal quantum number $n$. The same termination condition also caps the orbital quantum number: the polynomial's degree fixes a nonnegative integer $n_r = 0, 1, 2,\ldots$ (the number of interior radial nodes, discussed further below) related to $n$ and $\ell$ by $n = n_r + \ell + 1$, so that $n_r\ge0$ immediately forces $\ell \le n-1$ — and, for the ground state $n=1$, forces $n_r=\ell=0$ exactly, which is the direct algebraic reason the ground state must have zero orbital angular momentum, not merely an empirical fact to be taken on faith.

The distance between Bohr's picture and Schrödinger's is easiest to see by
running them side by side, as in {numref}`Figure %s <fig:ch10-hydrogen-models-sim>`. Both reproduce
the same $E_n$ and therefore the same emission lines, but only one of them
places the electron on an orbit.

```{phet} models-of-the-hydrogen-atom
:label: fig:ch10-hydrogen-models-sim

Successive models of the hydrogen atom — Bohr, de Broglie, Schrödinger, and
their predecessors — each firing photons at an atom and producing a spectrum.
The models that agree on $E_n$ disagree entirely about where the electron is.
```

### Historical Context: Bohr's 1913 Model and Its Limits

It is worth pausing on why a model built on postulates that turned out to be simply wrong — definite orbits, angular momentum quantized as $L=n\hbar$ — nonetheless earned Niels Bohr the 1922 Nobel Prize and remains the picture most people first encounter. In 1913, fourteen years before Schrödinger's equation existed, Bohr combined classical circular-orbit mechanics with a single ad hoc quantization rule and reproduced the empirical Rydberg formula for hydrogen's spectral lines essentially exactly, including its dependence on nuclear charge for hydrogenic ions (below) — a stunning success for a model with no derivation behind its central assumption. The de Broglie standing-wave argument of [Chapter 7](#ch-wave-properties-of-particles) later supplied a retroactive justification for $L=n\hbar$, which is part of why the Bohr model survived as long as it did before being fully superseded.

:::{seealso}
The de Broglie justification for $L=n\hbar$ works out concretely: demanding that an integer number of de Broglie wavelengths, $\lambda=h/p$ ([Chapter 7](#ch-wave-properties-of-particles)), fit exactly around a circular orbit of circumference $2\pi r$ gives $2\pi r = n\lambda = nh/p$, i.e. $L=rp=n\hbar$ — Bohr's quantization rule, recovered after the fact from wave interference rather than assumed outright.
:::

The model's failures, however, were just as instructive as its success. Extending Bohr's orbit-quantization scheme to **helium** — even with the refinements (elliptical orbits, relativistic orbit precession) added by Arnold Sommerfeld through the 1910s — never produced a correct ionization energy or a stable ground-state configuration for a two-electron atom; the semiclassical machinery simply had no consistent way to handle two mutually interacting orbiting electrons. The model also could not predict *which* transitions between levels actually occur (the selection rules developed later in this chapter), could not account for the relative brightness of spectral lines, and — as already emphasized above — gets the ground state's angular momentum flatly wrong: Bohr's $n=1$ orbit carries $L=\hbar$, while the true ground state has $L=0$ and no orbit, well-defined trajectory, or definite radius at all, only the probability cloud shown in {numref}`Figure %s <fig:ch10-hydrogen-models-sim>`. These failures, especially the inability to extend the model consistently beyond hydrogen, were a central motivation for the fully quantum-mechanical treatment developed in Chapters [8](#ch-the-schrodinger-equation)–[9](#ch-quantum-mechanics-in-three-dimensions) and specialized to hydrogen in this chapter — a treatment that, unlike Bohr's, generalizes cleanly to helium and every other atom in [Chapter 11](#ch-many-electron-atoms).

## Hydrogenic Ions: Scaling with Nuclear Charge

Everything derived above specializes the general central-potential machinery of [Chapter 9](#ch-quantum-mechanics-in-three-dimensions) to a nuclear charge of exactly $+e$. The same radial equation applies unchanged, with only $e^2 \to Ze^2$ in the Coulomb potential, to any **hydrogenic (hydrogen-like) ion**: a single electron bound to a nucleus of charge $+Ze$, such as singly ionized helium $\text{He}^+$ ($Z=2$) or doubly ionized lithium $\text{Li}^{2+}$ ($Z=3$). Repeating the normalizability argument above with the rescaled potential gives

$$
E_n(Z) = -Z^2\,\frac{13.6\ \text{eV}}{n^2}, \qquad a_n(Z) = \frac{n^2}{Z}\,a_0,
$$

where $a_n(Z)$ is the length scale (generalizing the Bohr radius) over which the radial probability distribution of the $n$-th shell peaks. Both dependences make direct physical sense: a larger nuclear charge attracts the electron more strongly, pulling its orbit *inward* (radius shrinks as $1/Z$) while binding it *more tightly* — and because the potential energy itself scales as $Z$ while the resulting spatial compression compounds that scaling once more, the binding energy grows as $Z^2$, not simply $Z$. This $Z^2$ scaling reappears with direct experimental consequence in [Chapter 11](#ch-many-electron-atoms), where it underlies Moseley's law for the energies of characteristic X-ray transitions in multi-electron atoms.

### Worked Example: The Ionization Energy and Orbital Size of He⁺

Find the ground-state ionization energy and the most probable electron–nucleus separation for $\text{He}^+$ ($Z=2$), a one-electron ion, and compare both to hydrogen's.

$$
E_1(\text{He}^+) = -Z^2(13.6\ \text{eV}) = -(2)^2(13.6\ \text{eV}) = -54.4\ \text{eV},
$$

so the ionization energy — the energy required to remove the electron entirely — is $54.4\ \text{eV}$, exactly four times hydrogen's $13.6\ \text{eV}$, matching the measured ionization energy of $\text{He}^+$. The orbital size scales the other way,

$$
a_1(\text{He}^+) = \frac{a_0}{Z} = \frac{0.0529\ \text{nm}}{2} = 0.0265\ \text{nm},
$$

half of hydrogen's Bohr radius: the electron in $\text{He}^+$ is bound four times more tightly and orbits, on average, twice as close to the nucleus as the electron in neutral hydrogen — both consequences of the same doubled nuclear charge, entering the energy quadratically and the size linearly (inversely).

## Quantum Numbers and Degeneracy in Hydrogen

Solving the full three-dimensional problem gives states labeled by the same three quantum numbers introduced in [Chapter 9](#ch-quantum-mechanics-in-three-dimensions) — $n$, $\ell$, $m_\ell$ — but with a further restriction, specific to the $1/r$ Coulomb potential, tying $\ell$ to $n$:

$$
n = 1, 2, 3, \ldots, \qquad \ell = 0, 1, \ldots, n-1, \qquad m_\ell = -\ell, \ldots, \ell.
$$

Because the energy $E_n$ depends *only* on $n$ — not on $\ell$ or $m_\ell$ — every state sharing a given $n$ is degenerate (equal in energy), regardless of its orbital angular momentum. Counting the total number of $(\ell, m_\ell)$ combinations for a given $n$ gives $n^2$ degenerate states (before accounting for electron spin, discussed below): for example, $n=2$ admits $\ell=0$ (one state, $m_\ell=0$) and $\ell=1$ (three states, $m_\ell=-1,0,1$), for $1+3=4=2^2$ states total. This $\ell$-independence of the energy is itself notable — it does *not* hold for multi-electron atoms ([Chapter 11](#ch-many-electron-atoms)), where the energy depends on $\ell$ as well as $n$, and is a special feature of the pure $1/r$ Coulomb potential (technically, a signature of a hidden extra symmetry, beyond ordinary rotational symmetry, unique to the $1/r$ potential).

:::{dropdown} The Hidden Symmetry Behind ℓ-Independent Degeneracy
Ordinary three-dimensional rotational symmetry guarantees that energy cannot depend on $m_\ell$, since no direction in space is special — but it says nothing about $\ell$. A generic central potential's energy levels *do* depend on $\ell$, and indeed they do for every atom with more than one electron ([Chapter 11](#ch-many-electron-atoms)). Hydrogen's extra, "accidental" $\ell$-independence traces back to a conserved quantity unique to the exact $1/r$ potential: the classical **Laplace–Runge–Lenz vector**,

$$
\vec A = \vec p\times\vec L - \frac{m_ee^2}{4\pi\epsilon_0}\,\hat r,
$$

which points from the focus of a classical Kepler orbit toward its perihelion and is constant in time only for a force that falls off as *exactly* $1/r^2$ — not $1/r^{2.01}$, not $1/r^{1.99}$. Quantum mechanically, $\vec A$ becomes an operator that commutes with the Hamiltonian and connects states of different $\ell$ at the same $n$, enlarging the symmetry governing hydrogen from ordinary three-dimensional rotations, $SO(3)$, to a larger four-dimensional rotation group, $SO(4)$, whose representations turn out to be exactly the $n^2$-fold degenerate multiplets observed. This is the same underlying fact about the $1/r^2$ force law that makes classical Kepler orbits close on themselves without precessing — the classical and quantum "accidents" are one and the same.
:::

## Wave Functions and Probability Distributions

The full wave functions, $\psi_{n\ell m_\ell}(r,\theta,\phi) = R_{n\ell}(r)\,Y_{\ell m_\ell}(\theta,\phi)$, have structure worth examining qualitatively even without their explicit algebraic form. The ground state, $\psi_{100}$, is spherically symmetric ($\ell=0$, so $Y_{00}$ is constant) and decays exponentially, $R_{10}(r) \propto e^{-r/a_0}$, where

$$
a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_ee^2} = 0.0529\ \text{nm}
$$

is the **Bohr radius** — reappearing here not as the radius of a Bohr orbit but as the natural length scale over which the ground-state probability density falls off. The **radial probability distribution**, $P(r) = r^2|R_{n\ell}(r)|^2$ (the probability per unit $r$ of finding the electron at distance $r$ from the nucleus, obtained by integrating $|\psi|^2$ over all angles at fixed $r$), peaks at $r = a_0$ for the ground state — the most probable electron-nucleus distance in hydrogen's ground state is exactly the Bohr radius, even though the electron has zero orbital angular momentum and hence, unlike in the Bohr picture, is not "orbiting" in any classical sense.

:::{warning}
"Most probable radius" is not the same thing as "average radius," and for hydrogen the two are not equal except by coincidence. The ground state's $P(r)$ peaks at $r=a_0$, but the curve falls off more gently on the outside of that peak than it rises on the inside, so the distribution is skewed toward larger $r$ — enough that the average $\langle r\rangle = \int_0^\infty rP(r)\,dr$ works out to $\tfrac32a_0$, fifty percent farther out than the peak. Don't assume a probability distribution is symmetric about its maximum just because it has a single, well-defined peak.
:::

Written out in full, with proper normalization, the lowest few radial wave functions are

$$
R_{10}(r) = \frac{2}{a_0^{3/2}}\,e^{-r/a_0}, \qquad
R_{20}(r) = \frac{1}{2\sqrt2\,a_0^{3/2}}\left(2-\frac{r}{a_0}\right)e^{-r/2a_0}, \qquad
R_{21}(r) = \frac{1}{2\sqrt6\,a_0^{3/2}}\,\frac{r}{a_0}\,e^{-r/2a_0},
$$

each verified against the standard hydrogen wave-function table (e.g. OpenStax Vol. 3, §8.2). The pattern generalizes: every $R_{n\ell}(r)$ is an exponential $e^{-r/na_0}$ (decay rate set only by $n$) multiplied by a polynomial in $r$ of degree $n-1$, and the number of interior zeros of that polynomial — the **radial nodes** counted below — is exactly $n_r = n-\ell-1$, the same integer introduced above via $n=n_r+\ell+1$. $R_{10}$ ($n_r=0$) is a bare exponential with no node; $R_{20}$ ($n_r=1$) has one node, at $r=2a_0$, exactly where its parenthetical factor vanishes; $R_{21}$ ($n_r=0$, since its higher $\ell$ "uses up" the node budget at fixed $n=2$) is a bare power of $r$ times an exponential, with no node at all despite sharing $n=2$ with $R_{20}$.

{numref}`Figure %s <fig:ch10-radial-probability>` plots the resulting $P(r)=r^2|R_{n\ell}(r)|^2$ for six low-lying states, making the node-counting rule directly visible rather than merely asserted: each panel's dotted vertical lines mark its nodes, and the count in every panel matches $n-\ell-1$ exactly — zero for $1s$, $2p$, and $3d$; one for $2s$ and $3p$; two for $3s$.

```{figure} ../images/ch10-radial-probability.svg
:label: fig:ch10-radial-probability
:alt: Six panels of radial probability distribution P(r) versus r over the Bohr radius, for the 1s, 2s, 2p, 3s, 3p, and 3d states of hydrogen, with dotted lines marking the radial nodes.

Radial probability distributions $P(r)=r^2|R_{n\ell}(r)|^2$ for the six lowest distinct $(n,\ell)$ combinations. Each state's node count matches $n-\ell-1$ exactly, and every curve for a given $n$ extends, on average, farther from the origin as $n$ increases — the size of the atom really does grow with $n$, just not along a sharp Bohr orbit. Computed directly from the closed-form $R_{n\ell}(r)$ formulas; see `scripts/figures/`.
```

More generally, $R_{n\ell}(r)$ has $n-\ell-1$ radial nodes (points, other than $r=0$ and $r=\infty$, where the probability density vanishes), and the angular functions $Y_{\ell m_\ell}(\theta,\phi)$ have angular nodes (nodal planes or cones) whose count and shape depend on $\ell$ and $m_\ell$ — giving rise to the familiar $s$ (spherical), $p$ (dumbbell-shaped, with a single nodal plane through the origin), and $d$-orbital shapes used throughout chemistry ([Chapter 12](#ch-molecular-structure)) to describe electron distributions in atoms and molecules.

:::{margin}
**Where the letters come from.** $s,p,d,f$ for $\ell=0,1,2,3$ are historical leftovers from nineteenth-century spectroscopy, abbreviating **s**harp, **p**rincipal, **d**iffuse, and **f**undamental — descriptions of how the corresponding spectral lines *looked*, decades before anyone knew what $\ell$ was. Past $f$, the letters simply continue alphabetically ($g,h,\ldots$).
:::

### The Effective Potential and the Centrifugal Barrier

[Chapter 9](#ch-quantum-mechanics-in-three-dimensions) showed that the radial equation for any central potential can be recast as an effective one-dimensional Schrödinger equation for $u(r)=rR(r)$, governed by an **effective potential**

$$
V_{\text{eff}}(r) = V(r) + \frac{\hbar^2\,\ell(\ell+1)}{2m_er^2} = -\frac{e^2}{4\pi\epsilon_0 r} + \frac{\hbar^2\,\ell(\ell+1)}{2m_er^2},
$$

the attractive Coulomb term plus the repulsive **centrifugal barrier** introduced there. For $\ell=0$ ($s$-states), $V_{\text{eff}}(r)=V(r)$: nothing but the bare attractive well, all the way in to $r=0$, which is exactly why only $\ell=0$ states have nonzero probability density at the nucleus — the $1s$, $2s$, and $3s$ curves in {numref}`Figure %s <fig:ch10-radial-probability>` all rise from zero right at the origin with no barrier in the way. For $\ell>0$, the centrifugal term ($\propto 1/r^2$) dominates the attractive term ($\propto 1/r$) at small $r$ and produces a genuine barrier that pushes the wave function away from the nucleus; the larger $\ell$ is, the taller that barrier and the farther out the first significant probability appears, exactly as seen in the figure, where $2p$, $3p$, and $3d$ all start at zero and rise more gradually than their same-$n$ $s$-state counterparts, and where $3d$ — the largest $\ell$ at $n=3$ — peaks farthest from the origin of the three $n=3$ curves. This $\ell$-dependent "penetration" toward the nucleus is purely qualitative for hydrogen's single electron, but it becomes quantitatively essential in [Chapter 11](#ch-many-electron-atoms), where it explains why an $s$-electron in a multi-electron atom is attracted more strongly by (and screens other electrons from) the nuclear charge than a $p$- or $d$-electron of the same $n$ — the mechanism that breaks hydrogen's accidental $\ell$-independent degeneracy once more than one electron is present.

## Spectral Series and the Energy-Level Diagram

Every property established so far — discrete $E_n$, the selection rule developed below — can be assembled into a single picture: the ladder of allowed energies together with the transitions between them that are actually observed. {numref}`Figure %s <fig:ch10-energy-levels>` draws that ladder for $n=1$ through $5$, together with the three most commonly tabulated spectral series, each named for whoever first catalogued it and each defined by a common *lower* level: the **Lyman series** ($n_f=1$, entirely in the ultraviolet), the **Balmer series** ($n_f=2$, spanning the visible), and the **Paschen series** ($n_f=3$, infrared). Because the spacing between successive $E_n$ shrinks rapidly as $n$ grows (it falls off as roughly $1/n^3$ near the top of the ladder), the levels bunch up as they approach $E=0$, and each series converges to a **series limit**: the shortest wavelength (highest photon energy) the series can produce, corresponding to a transition from $n_i\to\infty$ down to the series' fixed $n_f$, and equal to the energy $13.6\ \text{eV}/n_f^2$ needed to ionize the atom starting from level $n_f$. Beyond that limit the spectrum stops being a set of discrete lines at all, since a photoionized electron ($E>0$) is no longer confined to a discrete spectrum and can carry away any leftover energy continuously.

```{figure} ../images/ch10-energy-levels.svg
:label: fig:ch10-energy-levels
:alt: Hydrogen energy levels for n equals 1 through 5 on a compressed vertical scale, with clusters of arrows showing the Lyman series converging on n=1, the Balmer series converging on n=2, and the Paschen series converging on n=3.

Hydrogen energy levels $n=1$–$5$ (vertical position compressed for legibility; labels give the real $E_n=-13.6\ \text{eV}/n^2$), with the Lyman, Balmer, and Paschen series drawn as clusters of downward transitions converging on $n_f=1$, $2$, and $3$ respectively. Each series' shortest-wavelength member is its series limit, reached only as $n_i\to\infty$. Computed directly from $E_n$; see `scripts/figures/`.
```

### Worked Example: The Balmer Series and the Visible Spectrum

The **Rydberg formula** is simply $E_n=-13.6\ \text{eV}/n^2$ rewritten as a wavelength via $hc/\lambda = |E_{n_i}-E_{n_f}|$:

$$
\frac{1}{\lambda} = R\left(\frac{1}{n_f^2}-\frac{1}{n_i^2}\right), \qquad R = 1.097\times10^7\ \text{m}^{-1}.
$$

:::{margin}
**Two different $R$'s.** The Rydberg constant $R$ used here is unrelated to the radial wave function $R_{n\ell}(r)$ used earlier in this chapter — an unfortunate but standard notational collision. A bare $R$ in a wavelength formula and an $R$ carrying two subscripts and an $r$-dependence are always distinguishable from context.
:::

Find (a) the wavelength of $\text{H}_\alpha$, the first (longest-wavelength) line of the Balmer series ($n_i=3\to n_f=2$), and (b) the Balmer series limit.

**(a)**

$$
\frac{1}{\lambda} = (1.097\times10^7\ \text{m}^{-1})\left(\frac14-\frac19\right) = 1.524\times10^6\ \text{m}^{-1} \quad\Longrightarrow\quad \lambda = 656.3\ \text{nm},
$$

a deep red line — the $\text{H}_\alpha$ line used to image glowing hydrogen gas in nebulae and to trace the rotation of spiral galaxies.

**(b)** As $n_i\to\infty$, $1/n_i^2\to0$, so

$$
\frac{1}{\lambda_{\text{limit}}} = \frac{R}{4} = 2.743\times10^6\ \text{m}^{-1} \quad\Longrightarrow\quad \lambda_{\text{limit}} = 364.6\ \text{nm},
$$

just past the violet edge of the visible spectrum, in the near ultraviolet. Every Balmer line falls between these two wavelengths, $364.6\ \text{nm} < \lambda \le 656.3\ \text{nm}$ — which is why nearly the whole series, unlike the entirely ultraviolet Lyman series or the entirely infrared Paschen series, is visible to the human eye, and why Johann Balmer found the first four of these lines by curve-fitting alone in 1885, three decades before Bohr's model — or Schrödinger's equation — existed to explain them.

## Electron Spin

By the mid-1920s, several pieces of spectroscopic evidence — most directly, the splitting of atomic beams passing through an inhomogeneous magnetic field — showed that the three quantum numbers $(n,\ell,m_\ell)$ do not fully specify an electron's state. In the **Stern–Gerlach experiment** (1922), a beam of (electrically neutral) silver atoms was passed through a strongly inhomogeneous magnetic field and allowed to strike a detector screen. A classical magnetic dipole, oriented randomly, should be deflected by an amount depending continuously on its orientation, producing a single smeared-out band on the screen. Instead, the beam split into exactly **two** discrete spots, symmetric about the undeflected position — direct evidence of **space quantization** ([Chapter 9](#ch-quantum-mechanics-in-three-dimensions)) applied to a new, previously unsuspected degree of freedom, since the outermost electron in a silver atom happens to be in an $s$-state ($\ell=0$, hence zero orbital angular momentum and no orbital magnetic moment to produce any deflection at all), so the observed splitting could not be due to orbital angular momentum.

The resolution, proposed by Samuel Goudsmit and George Uhlenbeck (1925), is that the electron possesses an intrinsic angular momentum, **spin**, $\vec S$, with no classical counterpart (it is not literally the electron spinning on its axis — such a picture leads to internal-consistency and speed-of-rotation contradictions and should be regarded purely as a suggestive name), quantized exactly as orbital angular momentum is, but with a spin quantum number restricted to the single value $s=\tfrac12$:

$$
S = \sqrt{s(s+1)}\,\hbar = \frac{\sqrt3}{2}\hbar, \qquad S_z = m_s\hbar, \qquad m_s = -\tfrac12, +\tfrac12.
$$

The two allowed values of $m_s$ — "spin up" and "spin down" — account exactly for the two Stern–Gerlach spots. A complete specification of an electron's state in hydrogen therefore requires **four** quantum numbers, $(n,\ell,m_\ell,m_s)$, and the count of degenerate states for a given $n$ becomes $2n^2$ rather than $n^2$, the factor of 2 from the two spin orientations — a result central to the structure of the periodic table in [Chapter 11](#ch-many-electron-atoms).

## Magnetic Moments

Both orbital and spin angular momentum give the electron a magnetic dipole moment, since a circulating (or intrinsically "spinning") charge behaves as a small current loop. The **orbital magnetic moment** is

$$
\vec\mu_L = -\frac{e}{2m_e}\vec L, \qquad \mu_{L,z} = -m_\ell\mu_B,
$$

where $\mu_B \equiv e\hbar/2m_e = 9.274\times10^{-24}\ \text{J/T}$ is the **Bohr magneton**, a natural unit of atomic magnetic moment. The **spin magnetic moment** has an analogous form but with an extra numerical factor (the electron's $g$-factor, $g_s \approx 2$, itself a prediction of relativistic quantum theory beyond the scope of the nonrelativistic Schrödinger equation used here):

$$
\mu_{S,z} = -g_s\, m_s\, \mu_B \approx -2m_s\mu_B.
$$

These magnetic moments are what couple to an external magnetic field in the Stern–Gerlach experiment (producing the observed splitting and deflection) and, coupling to each other and to nuclear magnetic moments, produce the fine and hyperfine splittings observed in high-resolution atomic spectra.

### The Stern–Gerlach Force and a Numeric Deflection

A *uniform* magnetic field exerts a torque on a magnetic dipole — producing the Larmor precession pictured in [Chapter 9](#ch-quantum-mechanics-in-three-dimensions)'s precessing-top figure — but exerts zero *net force*, because the interaction energy $-\vec\mu\cdot\vec B$ does not depend on position when $\vec B$ itself does not. Deflecting the beam at all, as Stern and Gerlach needed to do to see anything on their screen, requires a spatially varying (inhomogeneous) field, whose gradient converts the dipole's orientation into a genuine transverse force:

$$
F_z = \mu_z\,\frac{\partial B_z}{\partial z},
$$

pushing atoms with $\mu_z>0$ one way and $\mu_z<0$ the other. Because $\mu_z$ takes only the two discrete values $\mu_{S,z}=\pm\mu_B$ (from the spin-moment formula above, with $m_s=\pm\tfrac12$ and $g_s\approx2$) rather than a continuum of values, the beam splits into exactly two discrete trajectories instead of spreading into one continuous smear — the direct experimental signature of space quantization that motivated this section.

### Worked Example: Beam Splitting in a Stern–Gerlach Magnet

A beam of silver atoms ($m=1.79\times10^{-25}\ \text{kg}$) effuses from an oven at $T=1000\ \text{K}$, giving a typical beam speed $v=\sqrt{3k_BT/m}\approx 480\ \text{m/s}$. The beam passes through a magnet of length $L=0.50\ \text{m}$ producing a field gradient $\partial B_z/\partial z = 10\ \text{T/m}$, then drifts a further $D=0.50\ \text{m}$ to a detector screen. Find the separation between the two spots.

The force on each atom is

$$
F_z = \mu_z\frac{\partial B_z}{\partial z} = \pm(9.274\times10^{-24}\ \text{J/T})(10\ \text{T/m}) = \pm9.27\times10^{-23}\ \text{N},
$$

giving a transverse acceleration $a = F_z/m = \pm518\ \text{m/s}^2$. While inside the magnet, for a time $t_1=L/v=1.04\times10^{-3}\ \text{s}$, each atom acquires a transverse displacement $z_1=\tfrac12at_1^2 = 0.28\ \text{mm}$ and a transverse velocity $v_z=at_1=0.54\ \text{m/s}$; it then drifts (no further transverse force, but still moving at $v_z$) for an additional time $t_2=D/v=1.04\times10^{-3}\ \text{s}$, adding $z_2=v_zt_2=0.56\ \text{mm}$. The one-sided deflection is $z_1+z_2\approx0.84\ \text{mm}$, so the two spin states land

$$
\Delta z = 2(z_1+z_2) \approx 1.7\ \text{mm}
$$

apart on the screen — comfortably resolvable, and the same order of magnitude as the splitting Stern and Gerlach actually measured in 1922 with a weaker gradient over a shorter path, which is what made their two-spot pattern (rather than one smeared band) unambiguous.

### The Zeeman Effect

[Chapter 9](#ch-quantum-mechanics-in-three-dimensions) introduced the (normal) **Zeeman effect** qualitatively: an external field $\vec B$ along $z$ adds an energy $-\vec\mu_L\cdot\vec B = m_\ell\mu_B B$ to each otherwise-degenerate $m_\ell$ sublevel of a given $(n,\ell)$. Including the spin moment as well, the total field-induced shift of a state $(m_\ell,m_s)$ is

$$
\Delta E = (m_\ell + g_sm_s)\,\mu_B B \approx (m_\ell + 2m_s)\,\mu_B B,
$$

so that sublevels differing by $\Delta m_\ell = \pm1$ — the only orbital transitions the selection rule below permits — are split, orbitally, by exactly $\mu_BB$. Historically, it was the *observed* splitting pattern (sometimes the simple three-line "normal" Zeeman pattern predicted by $m_\ell$ alone, but more often a more complicated "anomalous" pattern explainable only once spin and its distinct $g$-factor were included) that provided some of the earliest indirect evidence for electron spin, years before Stern and Gerlach identified its direct mechanical signature.

### Worked Example: Zeeman Splitting Frequency in a 1 T Field

Estimate the frequency splitting between adjacent $m_\ell$ sublevels for a hydrogen atom in a $B=1.0\ \text{T}$ field (a typical laboratory electromagnet), and the resulting wavelength shift of the $\text{H}_\alpha$ line ($\lambda=656.3\ \text{nm}$, from the worked example above).

$$
\Delta E = \mu_BB = (9.274\times10^{-24}\ \text{J/T})(1.0\ \text{T}) = 9.27\times10^{-24}\ \text{J} = 5.79\times10^{-5}\ \text{eV},
$$

$$
\Delta f = \frac{\Delta E}{h} = \frac{9.27\times10^{-24}\ \text{J}}{6.626\times10^{-34}\ \text{J}\cdot\text{s}} = 1.40\times10^{10}\ \text{Hz} = 14.0\ \text{GHz}
$$

(the electron's Larmor precession frequency in this field). Converting to a wavelength shift via $|\Delta\lambda|\approx(\lambda^2/c)\,\Delta f$,

$$
\Delta\lambda \approx \frac{(656.3\times10^{-9}\ \text{m})^2(1.40\times10^{10}\ \text{Hz})}{3.00\times10^8\ \text{m/s}} \approx 0.020\ \text{nm},
$$

about $30{,}000$ times smaller than the line's own wavelength — invisible by eye, but well within reach of a laboratory grating with resolving power $R=\lambda/\Delta\lambda\sim3\times10^4$ ([Chapter 5](#ch-diffraction-of-light)), which is how the Zeeman effect is actually resolved in the lab.

### Fine Structure: Spin–Orbit Coupling

Even with no external field at all, the energies $E_n=-13.6\ \text{eV}/n^2$ are not quite the whole story. In the electron's own rest frame, the orbiting (positively charged) nucleus constitutes a circulating current that produces a magnetic field at the electron's location, and that internal field couples to the electron's own spin magnetic moment exactly as an external field does in the Zeeman effect above — an interaction called **spin–orbit coupling**, whose strength depends on the relative orientation of $\vec L$ and $\vec S$ (equivalently, on the total angular momentum $\vec J = \vec L+\vec S$, a full treatment of which requires relativistic corrections beyond the nonrelativistic Schrödinger equation used throughout this book). What matters here is the *size* of the resulting **fine-structure** splitting of each $(n,\ell)$ level (other than $\ell=0$, where there is no orbital field to couple to):

$$
\Delta E_{\text{fine}} \sim \alpha^2\,|E_n|, \qquad \alpha \equiv \frac{e^2}{4\pi\epsilon_0\hbar c} \approx \frac{1}{137.0} \approx 7.30\times10^{-3},
$$

where $\alpha$, the dimensionless **fine-structure constant**, measures the intrinsic strength of the electromagnetic interaction and sets the size of essentially every relativistic correction in atomic physics. Because $\alpha^2\approx5\times10^{-5}$, fine structure shifts a level by only a few parts in $10^5$ of $|E_n|$ itself — far too fine to see with a simple grating, but readily resolved with a high-resolution spectrometer, and the historical reason spectral lines that look perfectly sharp in an introductory demonstration reveal themselves, under sufficient magnification, to be closely spaced multiplets (hence the name, coined for exactly this kind of fine-toothed splitting of what earlier instruments saw as a single line).

### Worked Example: Order-of-Magnitude Fine-Structure Splitting

Estimate the fine-structure splitting of hydrogen's $n=2$ level, and compare it to the actual measured splitting of the $2p$ levels, $\Delta E_{\text{fine}}\approx4.5\times10^{-5}\ \text{eV}$ (equivalently, about $10.9\ \text{GHz}$).

$$
E_2 = -\frac{13.6\ \text{eV}}{4} = -3.40\ \text{eV} \quad\Longrightarrow\quad \Delta E_{\text{fine}} \sim \alpha^2|E_2| = (7.30\times10^{-3})^2(3.40\ \text{eV}) \approx 1.8\times10^{-4}\ \text{eV},
$$

within about a factor of four of the measured value — entirely appropriate for an order-of-magnitude estimate that drops the numerical factors ($j$-dependence and other combinatorics supplied only by a full relativistic treatment) while correctly capturing the essential physical scale: fine structure is smaller than the gross level spacing $|E_n|$ by a factor of $\alpha^2\approx5\times10^{-5}$, the same small parameter that controls, order by order, essentially every relativistic correction in atomic physics.

The same coupling, applied to the *proton's* magnetic moment rather than the electron's, is the basis of magnetic resonance imaging, and {numref}`Figure %s <fig:ch10-mri-sim>` is a working model of it. A static field along $z$ splits the two spin orientations by $\Delta E = g\mu_N B$, which for a proton in a $1\ \text{T}$ field falls in the radio band; a transverse radio-frequency field tuned to exactly that frequency drives transitions between them, and the resonance is sharp enough that a deliberate spatial *gradient* in $B$ makes the resonant frequency a map of position. Everything in the sequence — the splitting proportional to $B$, the resonance condition $hf = \Delta E$, the return to equilibrium afterwards — is this section's physics with $\mu_B$ replaced by the nuclear magneton.

:::{margin}
**Nuclear magneton.** $\mu_N \equiv e\hbar/2m_p$, built the same way as the Bohr magneton $\mu_B$ but with the much larger proton mass $m_p$ in place of $m_e$. Since $m_p\approx1836\,m_e$, $\mu_N\approx\mu_B/1836$ — nuclear magnetic effects are intrinsically about a thousand times weaker than electronic ones, which is part of why MRI needs strong fields and sensitive receivers.
:::

```{phet-legacy} mri
:sim-name: Simplified MRI
:label: fig:ch10-mri-sim

Proton spins in a magnetic field: Zeeman splitting, resonant absorption of a radio-frequency photon, and the field gradient that turns the resonance into an image.
```

## Selection Rules

Not every pair of hydrogen energy levels is connected by an observable spectral line. An electron making a transition between stationary states typically does so by emitting or absorbing a single photon, and conservation of the photon's own angular momentum (it carries one unit, $\hbar$, of angular momentum along its propagation direction) restricts which transitions can occur via this single-photon (electric dipole) process to those satisfying the **selection rule**

$$
\Delta \ell = \pm 1,
$$

(with no similarly strict restriction on $\Delta n$). Transitions violating this rule (e.g., $2s \to 1s$, both $\ell=0$) are called **forbidden transitions** — not absolutely impossible, but strongly suppressed, occurring (if at all) only through much slower, higher-order processes. The selection rule is why, for instance, the observed hydrogen spectral series (Lyman, Balmer, Paschen, etc., corresponding to transitions ending on $n_f = 1, 2, 3,\ldots$) show specific line patterns rather than a line for every conceivable pair of levels.

:::{tip}
When checking whether a transition is allowed, check $\Delta\ell$ first and don't spend time on $\Delta n$ — the selection rule places no restriction on $n$ at all, only on $\ell$. A quick way to keep this straight while scanning a level diagram grouped by orbital letter: an allowed electric-dipole transition always moves exactly one letter over ($s\leftrightarrow p$, $p\leftrightarrow d$, etc.), never staying within the same letter and never skipping one, regardless of how far it jumps between $n$ values.
:::

## Summary

- The radial Schrödinger equation for hydrogen's $1/r$ Coulomb potential reproduces the Bohr energy levels $E_n = -13.6\ \text{eV}/n^2$, but from normalizability of $R(r)$ rather than a postulated orbit, and with the ground state having zero orbital angular momentum, unlike Bohr's model. Normalizability forces the radial series to terminate into a finite polynomial, which fixes $n$ to a positive integer and, via $n=n_r+\ell+1$ ($n_r\ge0$ the radial node count), caps $\ell$ at $n-1$.
- **Bohr's 1913 model** reproduced hydrogen's spectrum numerically from an unjustified orbit postulate, but could not be extended consistently to helium or predict transition rates, and gets the ground state's angular momentum flatly wrong — failures that motivated the full Schrödinger treatment.
- **Hydrogenic ions** (e.g. $\text{He}^+$, $\text{Li}^{2+}$) follow $E_n(Z) = -Z^2(13.6\ \text{eV})/n^2$ and $a_n(Z) = n^2a_0/Z$: binding energy scales as $Z^2$, orbital size as $1/Z$.
- Hydrogen states are labeled by $n$, $\ell = 0,\ldots,n-1$, $m_\ell = -\ell,\ldots,\ell$; because $E_n$ depends only on $n$, there are $n^2$ degenerate spatial states per $n$ — a special feature of the pure Coulomb potential.
- Explicit radial wave functions $R_{10}$, $R_{20}$, $R_{21}$, and the radial probability distributions $P(r) = r^2|R_{n\ell}|^2$ they generate, show the $n-\ell-1$ node count directly; angular nodal structure gives rise to the characteristic $s$, $p$, $d$ orbital shapes. The Bohr radius $a_0$ reappears as the most probable electron-nucleus separation in the ground state.
- The **effective potential** $V_{\text{eff}}(r)=V(r)+\hbar^2\ell(\ell+1)/2m_er^2$ shows that only $\ell=0$ states have nonzero probability density at the nucleus; higher $\ell$ states are held away from the origin by the centrifugal barrier, a penetration effect central to screening in [Chapter 11](#ch-many-electron-atoms).
- The **Lyman**, **Balmer**, and **Paschen** series (transitions ending on $n_f=1,2,3$) each converge to a series limit at $n_i\to\infty$; the Rydberg formula $1/\lambda=R(1/n_f^2-1/n_i^2)$ gives their wavelengths, with the Balmer series ($364.6$–$656.3\ \text{nm}$) spanning most of the visible range.
- The **Stern–Gerlach experiment** revealed **electron spin**, an intrinsic angular momentum with quantum number $s=\tfrac12$ and $m_s = \pm\tfrac12$, doubling the degenerate state count to $2n^2$ and requiring four quantum numbers $(n,\ell,m_\ell,m_s)$ to fully specify a state. The inhomogeneous-field force $F_z=\mu_z\,\partial B_z/\partial z$ converts the two spin orientations into two discrete beam deflections.
- Orbital and spin angular momentum each produce a magnetic moment, in units of the Bohr magneton $\mu_B$; the spin moment carries an extra $g$-factor $\approx 2$. In an external field, the (normal) **Zeeman effect** shifts sublevels by $\Delta E \approx (m_\ell+2m_s)\mu_BB$; even with no external field, **spin–orbit coupling** produces **fine-structure** splitting of order $\alpha^2|E_n|$, where $\alpha\approx1/137$ is the fine-structure constant.
- Single-photon transitions obey the selection rule $\Delta\ell = \pm1$, explaining the observed pattern of hydrogen spectral lines.

## Problems

:::{exercise}
:label: ex-the-hydrogen-atom-1

Using the Rydberg formula, compute the wavelength of the first line of the Lyman series ($n=2\to n=1$) and the Lyman series limit ($n\to\infty \to n=1$). State which portion of the electromagnetic spectrum both lie in, and explain why the entire Lyman series (unlike the Balmer series) is invisible to the human eye.
:::

:::{solution} ex-the-hydrogen-atom-1
:label: sol-the-hydrogen-atom-1
:class: dropdown

For $2\to1$, the Rydberg formula gives

$$\frac1\lambda=R\left(1-\frac14\right)=\frac34(1.097\times10^7\ \text{m}^{-1}),\qquad \lambda=121.5\ \text{nm}.$$

At the series limit, $1/\lambda=R$, so $\lambda=91.2\ \text{nm}$.  Both lines are the leftmost cluster of downward arrows in {numref}`Figure %s <fig:ch10-energy-levels>`, all converging on $n_f=1$.  Therefore, the first Lyman line is $121.5\ \text{nm}$ and the limit is $91.2\ \text{nm}$; both are ultraviolet, so the entire series is invisible to the eye.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-2

List all allowed $(\ell, m_\ell)$ combinations for $n=3$, count the total number of spatial states, and verify this equals $n^2=9$. Including spin, how many total quantum states share this energy?
:::

:::{solution} ex-the-hydrogen-atom-2
:label: sol-the-hydrogen-atom-2
:class: dropdown

For $n=3$, $\ell=0,1,2$.  The allowed sets are $(0,0)$; $(1,-1),(1,0),(1,1)$; and $(2,-2),(2,-1),(2,0),(2,1),(2,2)$.  Their count is $1+3+5=9=n^2$.  Including $m_s=\pm\tfrac12$ doubles this count to $18$.  Therefore, the $n=3$ level has nine spatial states and eighteen states when spin is included.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-3

Using the selection rule $\Delta\ell=\pm1$, determine which of the following single-photon transitions are allowed and which are forbidden: (a) $3d \to 2p$, (b) $3s \to 2s$, (c) $3p \to 1s$, (d) $2p \to 1s$.
:::

:::{solution} ex-the-hydrogen-atom-3
:label: sol-the-hydrogen-atom-3
:class: dropdown

The changes in $\ell$ are: (a) $2\to1$, so $\Delta\ell=-1$ and allowed; (b) $0\to0$, so forbidden; (c) $1\to0$, so allowed; and (d) $1\to0$, so allowed.

```{figure} ../images/ch10-sol-selection-rule-transitions.svg
:label: fig:ch10-sol-selection-rule-transitions
:alt: Energy levels grouped by orbital type s, p, and d at n equals 1, 2, and 3, with solid arrows for the three allowed transitions and a dashed crossed arrow for the forbidden 3s to 2s transition.

Grouping the levels by $\ell$ makes the rule visual: an allowed arrow always moves one column over, while $3s\to2s$ tries to stay in the same column and is forbidden.
```

Therefore, only $3s\to2s$ is forbidden by the electric-dipole selection rule.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-4

An electron in a hydrogen atom is in a $3d$ state ($\ell=2$). (a) Compute the magnitude of its orbital angular momentum in units of $\hbar$. (b) Compute the maximum possible $z$-component of its orbital magnetic moment, in units of the Bohr magneton.
:::

:::{solution} ex-the-hydrogen-atom-4
:label: sol-the-hydrogen-atom-4
:class: dropdown

For $\ell=2$,

$$L=\sqrt{\ell(\ell+1)}\hbar=\sqrt6\hbar.$$

The largest $m_\ell$ is $+2$, and $\mu_{L,z}=-m_\ell\mu_B=-2\mu_B$, whose maximum magnitude is $2\mu_B$.  Therefore, the $3d$ electron has orbital angular momentum $\sqrt6\hbar$ and maximum $z$-component magnetic-moment magnitude $2\mu_B$.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-5

In the Stern–Gerlach experiment, explain why silver atoms (rather than, say, helium atoms) were a good choice for demonstrating space quantization due to electron spin, referring to the electron configuration of the outermost electron (you may look ahead to [Chapter 11](#ch-many-electron-atoms)'s discussion of electron configurations, or simply reason from the fact that silver's single outer electron is in an $s$-state).
:::

:::{solution} ex-the-hydrogen-atom-5
:label: sol-the-hydrogen-atom-5
:class: dropdown

Silver has one unpaired outer $5s$ electron.  An $s$ state has $\ell=0$, so it has no orbital magnetic moment that could obscure the result; the two-way splitting is therefore due cleanly to spin.  Helium's paired $1s^2$ electrons have canceling spin moments.  Therefore, silver was ideal because its single outer $s$ electron leaves an uncompensated spin moment, whereas helium has no net moment.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-6

Show that the ground-state radial probability distribution of hydrogen, $P(r) = r^2|R_{10}(r)|^2 \propto r^2 e^{-2r/a_0}$, is maximized at $r=a_0$ by differentiating $P(r)$ with respect to $r$ and setting the result to zero.
:::

:::{solution} ex-the-hydrogen-atom-6
:label: sol-the-hydrogen-atom-6
:class: dropdown

Ignoring the positive normalization constant, $P(r)=r^2e^{-2r/a_0}$.  Differentiation gives

$$\frac{dP}{dr}=2re^{-2r/a_0}-\frac2{a_0}r^2e^{-2r/a_0}=2re^{-2r/a_0}\left(1-\frac r{a_0}\right).$$

For $r>0$, the derivative vanishes at $r=a_0$, changing from positive to negative there — exactly the peak of the $1s$ curve in {numref}`Figure %s <fig:ch10-radial-probability>`.  Therefore, the ground-state radial probability is largest at the Bohr radius $r=a_0$.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-7

Doubly ionized lithium, $\text{Li}^{2+}$ ($Z=3$), is a one-electron hydrogenic ion. (a) Find its ground-state ionization energy. (b) Find the radius at which its ground-state radial probability distribution peaks. (c) Compare both results, as ratios, to hydrogen's, and confirm they follow the $Z^2$ and $1/Z$ scaling laws given in the text.
:::

:::{solution} ex-the-hydrogen-atom-7
:label: sol-the-hydrogen-atom-7
:class: dropdown

Hydrogenic ionization energy scales as $Z^2$ and the most-probable radius as $a_0/Z$.  Thus

$$E_I=3^2(13.6\ \text{eV})=122.4\ \text{eV},\qquad r_{\max}=\frac{0.529\ \text{\AA}}3=0.176\ \text{\AA}=0.0176\ \text{nm}.$$

```{figure} ../images/ch10-sol-hydrogenic-z-scaling.svg
:label: fig:ch10-sol-hydrogenic-z-scaling
:alt: Ground-state radial probability distributions for hydrogen and doubly ionized lithium, each normalized to its own peak, with the lithium curve peaking at one-third the radius of hydrogen's.

Both curves have the same shape, rescaled: replacing $Z=1$ with $Z=3$ compresses the peak radius by $1/Z$ while (not shown to the same vertical scale) the binding energy grows by $Z^2$.
```

Therefore, $\text{Li}^{2+}$ has a $122.4\ \text{eV}$ ionization energy and a $0.0176\ \text{nm}$ most-probable radius: nine times hydrogen's energy and one-third its radius.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-8

A different Stern–Gerlach apparatus uses a field gradient $\partial B_z/\partial z = 15\ \text{T/m}$ over a magnet of length $L=0.20\ \text{m}$, with silver atoms ($m=1.79\times10^{-25}\ \text{kg}$) moving at $v=600\ \text{m/s}$, followed by a $D=0.40\ \text{m}$ drift to the screen. Using the method of the worked example, find the separation between the two spots.
:::

:::{solution} ex-the-hydrogen-atom-8
:label: sol-the-hydrogen-atom-8
:class: dropdown

The force magnitude is $F=\mu_B(\partial B_z/\partial z)=(9.274\times10^{-24})(15)=1.39\times10^{-22}\ \text{N}$, so $a=F/m=777\ \text{m/s}^2$.  The magnet time is $t_1=L/v=3.33\times10^{-4}\ \text{s}$ and the drift time is $t_2=D/v=6.67\times10^{-4}\ \text{s}$.  One component deflects by

$$z=\tfrac12at_1^2+(at_1)t_2=2.16\times10^{-4}\ \text{m}=0.216\ \text{mm}.$$

```{figure} ../images/ch10-sol-stern-gerlach.svg
:label: fig:ch10-sol-stern-gerlach
:alt: Schematic of a beam entering an inhomogeneous magnet and splitting into two straight paths that reach the screen separated by 0.432 millimeters, one for each spin projection.

The two spin states feel opposite forces inside the magnet, coast in straight lines afterward, and arrive at the screen separated by $2z$. (The deflection is exaggerated for visibility; the real displacement is a fraction of a millimeter.)
```

Therefore, the two opposite spin components are separated by $2z=0.432\ \text{mm}$.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-9

A hydrogen discharge tube is placed in a magnetic field of $B=0.50\ \text{T}$. (a) Find the Zeeman energy splitting $\Delta E$ (in eV) between adjacent $m_\ell$ sublevels. (b) Find the corresponding frequency splitting $\Delta f$. (c) Using $\lambda=486.1\ \text{nm}$ (the $\text{H}_\beta$ line), estimate the wavelength splitting $\Delta\lambda$, and compare its order of magnitude to the $0.50\ \text{T}$ case's expected scaling relative to the $1.0\ \text{T}$ worked example in the text.
:::

:::{solution} ex-the-hydrogen-atom-9
:label: sol-the-hydrogen-atom-9
:class: dropdown

Adjacent orbital sublevels differ by $\Delta E=\mu_BB$, so

$$\Delta E=(5.79\times10^{-5}\ \text{eV/T})(0.50\ \text{T})=2.90\times10^{-5}\ \text{eV},$$

$$\Delta f=\frac{\Delta E}{h}=7.00\times10^9\ \text{Hz}.$$

Finally $\Delta\lambda\simeq\lambda^2\Delta f/c=(486.1\times10^{-9}\ \text{m})^2(7.00\times10^9\ \text{Hz})/(3.00\times10^8\ \text{m/s})=0.00551\ \text{nm}$.

```{figure} ../images/ch10-sol-zeeman-line-splitting.svg
:label: fig:ch10-sol-zeeman-line-splitting
:alt: A single spectral line at 486.1 nanometers shown splitting into three closely spaced lines separated by 0.00551 nanometers when a 0.50 tesla field is applied.

The field-free H$_\beta$ line becomes a triplet spaced by $\Delta\lambda$, one component for each $m_\ell$ sublevel the upper and lower states split into.
```

Therefore, the $0.50\ \text{T}$ splitting is $2.90\times10^{-5}\ \text{eV}$, $7.00\ \text{GHz}$, and $0.0055\ \text{nm}$, half the corresponding $1.0\ \text{T}$ scale.
:::

:::{exercise}
:label: ex-the-hydrogen-atom-10

Estimate the order-of-magnitude fine-structure splitting of hydrogen's $n=3$ level, using $\Delta E_{\text{fine}}\sim\alpha^2|E_n|$. Compare your result to the $n=2$ estimate found in the text, and explain, in terms of the $|E_n|=13.6\ \text{eV}/n^2$ scaling, why fine structure becomes progressively harder to resolve at higher $n$.
:::

:::{solution} ex-the-hydrogen-atom-10
:label: sol-the-hydrogen-atom-10
:class: dropdown

For $n=3$, $|E_3|=13.6/9=1.51\ \text{eV}$ and $\alpha^2=(1/137)^2=5.33\times10^{-5}$.  Thus

$$\Delta E_{\rm fine}\sim\alpha^2|E_3|=(5.33\times10^{-5})(1.51\ \text{eV})=8.1\times10^{-5}\ \text{eV}.$$

This is $4/9$ of the $n=2$ estimate because $|E_n|\propto1/n^2$.  Therefore, the $n=3$ fine splitting is of order $8\times10^{-5}\ \text{eV}$ and becomes harder to resolve as $n$ rises.
:::
