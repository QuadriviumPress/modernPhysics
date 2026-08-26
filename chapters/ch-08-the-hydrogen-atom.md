---
title: The Hydrogen Atom
short_title: Chapter 8. The Hydrogen Atom
---

## Learning Objectives

By the end of this chapter, you should be able to:

- State the radial equation for the hydrogen atom and the resulting energy quantization, and compare it to the Bohr model's prediction.
- Describe the hydrogen wave functions qualitatively, including radial probability distributions and angular nodal structure.
- Enumerate the allowed quantum states for a given $n$ and explain the origin of degeneracy in hydrogen.
- Explain electron spin and the Stern–Gerlach experiment that revealed it.
- Combine orbital and spin angular momentum via the orbital and spin magnetic quantum numbers, and compute orbital and spin magnetic moments.
- Apply selection rules to determine which transitions between hydrogen energy levels are allowed.

## Introduction

Chapter 7 developed the general machinery for any central potential: separation into radial and angular parts, and the universal quantization of orbital angular momentum. This chapter specializes that machinery to the single most important central potential in atomic physics — the Coulomb attraction between an electron and a proton — and solves it for the hydrogen atom, the only atom for which the Schrödinger equation can be solved exactly in closed form. The result reproduces (and explains, rather than assumes) the energy levels first found empirically in atomic spectra and postulated ad hoc in the 1913 Bohr model, while revealing a far richer structure — angular momentum, spatial probability distributions, and a fourth quantum number, electron spin, with no classical counterpart at all.

## The Radial Equation and Energy Quantization

For the hydrogen atom, the central potential is the Coulomb attraction between the electron (charge $-e$) and the proton (charge $+e$),

$$
V(r) = -\frac{e^2}{4\pi\epsilon_0\, r}.
$$

Substituting this $V(r)$ into the radial equation obtained from the separation $\psi = R(r)Y(\theta,\phi)$ (Chapter 7), and requiring $R(r)$ to be normalizable (i.e., to decay rather than blow up as $r\to\infty$, and to remain finite at $r=0$), restricts the allowed energies to exactly the same discrete set found by Bohr in 1913 from an ad hoc semiclassical model:

$$
E_n = -\frac{m_ee^4}{8\epsilon_0^2h^2}\,\frac{1}{n^2} = -\frac{13.6\ \text{eV}}{n^2}, \qquad n = 1, 2, 3,\ldots.
$$

This agreement is a triumph for the Schrödinger equation — it reproduces a result that matched atomic spectroscopy to remarkable precision — but the derivation and interpretation are entirely different from Bohr's. Bohr postulated that the electron moves on definite circular orbits, with angular momentum quantized as $L = n\hbar$ by assumption. The Schrödinger treatment makes no such assumption about orbits at all; instead, $n$ emerges purely as an index counting the normalizable solutions of the radial equation, the electron has no well-defined trajectory, and — as shown below — the ground state ($n=1$) actually has **zero** orbital angular momentum, in direct contradiction to Bohr's $L=n\hbar$. The numerical agreement in $E_n$ is, in this sense, a coincidence specific to the particular form of the $1/r$ Coulomb potential, not a sign that the Bohr picture was substantially correct.

## Quantum Numbers and Degeneracy in Hydrogen

Solving the full three-dimensional problem gives states labeled by the same three quantum numbers introduced in Chapter 7 — $n$, $\ell$, $m_\ell$ — but with a further restriction, specific to the $1/r$ Coulomb potential, tying $\ell$ to $n$:

$$
n = 1, 2, 3, \ldots, \qquad \ell = 0, 1, \ldots, n-1, \qquad m_\ell = -\ell, \ldots, \ell.
$$

Because the energy $E_n$ depends *only* on $n$ — not on $\ell$ or $m_\ell$ — every state sharing a given $n$ is degenerate (equal in energy), regardless of its orbital angular momentum. Counting the total number of $(\ell, m_\ell)$ combinations for a given $n$ gives $n^2$ degenerate states (before accounting for electron spin, discussed below): for example, $n=2$ admits $\ell=0$ (one state, $m_\ell=0$) and $\ell=1$ (three states, $m_\ell=-1,0,1$), for $1+3=4=2^2$ states total. This $\ell$-independence of the energy is itself notable — it does *not* hold for multi-electron atoms (Chapter 9), where the energy depends on $\ell$ as well as $n$, and is a special feature of the pure $1/r$ Coulomb potential (technically, a signature of a hidden extra symmetry, beyond ordinary rotational symmetry, unique to the $1/r$ potential).

## Wave Functions and Probability Distributions

The full wave functions, $\psi_{n\ell m_\ell}(r,\theta,\phi) = R_{n\ell}(r)\,Y_{\ell m_\ell}(\theta,\phi)$, have structure worth examining qualitatively even without their explicit algebraic form. The ground state, $\psi_{100}$, is spherically symmetric ($\ell=0$, so $Y_{00}$ is constant) and decays exponentially, $R_{10}(r) \propto e^{-r/a_0}$, where

$$
a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_ee^2} = 0.0529\ \text{nm}
$$

is the **Bohr radius** — reappearing here not as the radius of a Bohr orbit but as the natural length scale over which the ground-state probability density falls off. The **radial probability distribution**, $P(r) = r^2|R_{n\ell}(r)|^2$ (the probability per unit $r$ of finding the electron at distance $r$ from the nucleus, obtained by integrating $|\psi|^2$ over all angles at fixed $r$), peaks at $r = a_0$ for the ground state — the most probable electron-nucleus distance in hydrogen's ground state is exactly the Bohr radius, even though the electron has zero orbital angular momentum and hence, unlike in the Bohr picture, is not "orbiting" in any classical sense.

More generally, $R_{n\ell}(r)$ has $n-\ell-1$ radial nodes (points, other than $r=0$ and $r=\infty$, where the probability density vanishes), and the angular functions $Y_{\ell m_\ell}(\theta,\phi)$ have angular nodes (nodal planes or cones) whose count and shape depend on $\ell$ and $m_\ell$ — giving rise to the familiar $s$ (spherical), $p$ (dumbbell-shaped, with a single nodal plane through the origin), and $d$-orbital shapes used throughout chemistry (Chapter 10) to describe electron distributions in atoms and molecules.

## Electron Spin

By the mid-1920s, several pieces of spectroscopic evidence — most directly, the splitting of atomic beams passing through an inhomogeneous magnetic field — showed that the three quantum numbers $(n,\ell,m_\ell)$ do not fully specify an electron's state. In the **Stern–Gerlach experiment** (1922), a beam of (electrically neutral) silver atoms was passed through a strongly inhomogeneous magnetic field and allowed to strike a detector screen. A classical magnetic dipole, oriented randomly, should be deflected by an amount depending continuously on its orientation, producing a single smeared-out band on the screen. Instead, the beam split into exactly **two** discrete spots, symmetric about the undeflected position — direct evidence of **space quantization** (Chapter 7) applied to a new, previously unsuspected degree of freedom, since the outermost electron in a silver atom happens to be in an $s$-state ($\ell=0$, hence zero orbital angular momentum and no orbital magnetic moment to produce any deflection at all), so the observed splitting could not be due to orbital angular momentum.

The resolution, proposed by Samuel Goudsmit and George Uhlenbeck (1925), is that the electron possesses an intrinsic angular momentum, **spin**, $\vec S$, with no classical counterpart (it is not literally the electron spinning on its axis — such a picture leads to internal-consistency and speed-of-rotation contradictions and should be regarded purely as a suggestive name), quantized exactly as orbital angular momentum is, but with a spin quantum number restricted to the single value $s=\tfrac12$:

$$
S = \sqrt{s(s+1)}\,\hbar = \frac{\sqrt3}{2}\hbar, \qquad S_z = m_s\hbar, \qquad m_s = -\tfrac12, +\tfrac12.
$$

The two allowed values of $m_s$ — "spin up" and "spin down" — account exactly for the two Stern–Gerlach spots. A complete specification of an electron's state in hydrogen therefore requires **four** quantum numbers, $(n,\ell,m_\ell,m_s)$, and the count of degenerate states for a given $n$ becomes $2n^2$ rather than $n^2$, the factor of 2 from the two spin orientations — a result central to the structure of the periodic table in Chapter 9.

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

## Selection Rules

Not every pair of hydrogen energy levels is connected by an observable spectral line. An electron making a transition between stationary states typically does so by emitting or absorbing a single photon, and conservation of the photon's own angular momentum (it carries one unit, $\hbar$, of angular momentum along its propagation direction) restricts which transitions can occur via this single-photon (electric dipole) process to those satisfying the **selection rule**

$$
\Delta \ell = \pm 1,
$$

(with no similarly strict restriction on $\Delta n$). Transitions violating this rule (e.g., $2s \to 1s$, both $\ell=0$) are called **forbidden transitions** — not absolutely impossible, but strongly suppressed, occurring (if at all) only through much slower, higher-order processes. The selection rule is why, for instance, the observed hydrogen spectral series (Lyman, Balmer, Paschen, etc., corresponding to transitions ending on $n_f = 1, 2, 3,\ldots$) show specific line patterns rather than a line for every conceivable pair of levels.

## Summary

- The radial Schrödinger equation for hydrogen's $1/r$ Coulomb potential reproduces the Bohr energy levels $E_n = -13.6\ \text{eV}/n^2$, but from normalizability of $R(r)$ rather than a postulated orbit, and with the ground state having zero orbital angular momentum, unlike Bohr's model.
- Hydrogen states are labeled by $n$, $\ell = 0,\ldots,n-1$, $m_\ell = -\ell,\ldots,\ell$; because $E_n$ depends only on $n$, there are $n^2$ degenerate spatial states per $n$ — a special feature of the pure Coulomb potential.
- Radial probability distributions $P(r) = r^2|R_{n\ell}|^2$ and angular nodal structure give rise to the characteristic $s$, $p$, $d$ orbital shapes; the Bohr radius $a_0$ reappears as the most probable electron-nucleus separation in the ground state.
- The **Stern–Gerlach experiment** revealed **electron spin**, an intrinsic angular momentum with quantum number $s=\tfrac12$ and $m_s = \pm\tfrac12$, doubling the degenerate state count to $2n^2$ and requiring four quantum numbers $(n,\ell,m_\ell,m_s)$ to fully specify a state.
- Orbital and spin angular momentum each produce a magnetic moment, in units of the Bohr magneton $\mu_B$; the spin moment carries an extra $g$-factor $\approx 2$.
- Single-photon transitions obey the selection rule $\Delta\ell = \pm1$, explaining the observed pattern of hydrogen spectral lines.

## Problems

1. Compute the wavelength of the photon emitted in the hydrogen transition $n=3 \to n=2$ (the first line of the Balmer series), and identify whether it lies in the visible spectrum.

2. List all allowed $(\ell, m_\ell)$ combinations for $n=3$, count the total number of spatial states, and verify this equals $n^2=9$. Including spin, how many total quantum states share this energy?

3. Using the selection rule $\Delta\ell=\pm1$, determine which of the following single-photon transitions are allowed and which are forbidden: (a) $3d \to 2p$, (b) $3s \to 2s$, (c) $3p \to 1s$, (d) $2p \to 1s$.

4. An electron in a hydrogen atom is in a $3d$ state ($\ell=2$). (a) Compute the magnitude of its orbital angular momentum in units of $\hbar$. (b) Compute the maximum possible $z$-component of its orbital magnetic moment, in units of the Bohr magneton.

5. In the Stern–Gerlach experiment, explain why silver atoms (rather than, say, helium atoms) were a good choice for demonstrating space quantization due to electron spin, referring to the electron configuration of the outermost electron (you may look ahead to Chapter 9's discussion of electron configurations, or simply reason from the fact that silver's single outer electron is in an $s$-state).

6. Show that the ground-state radial probability distribution of hydrogen, $P(r) = r^2|R_{10}(r)|^2 \propto r^2 e^{-2r/a_0}$, is maximized at $r=a_0$ by differentiating $P(r)$ with respect to $r$ and setting the result to zero.
