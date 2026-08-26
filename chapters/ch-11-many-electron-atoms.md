---
title: Many-Electron Atoms
short_title: Chapter 11. Many-Electron Atoms
label: ch-many-electron-atoms
---

## Learning Objectives

By the end of this chapter, you should be able to:

- State the Pauli exclusion principle and explain its role in determining atomic structure.
- Explain why the energy of a state in a multi-electron atom depends on both $n$ and $\ell$, unlike in hydrogen, using the concept of electron screening.
- Write the ground-state electron configuration of a given element using the subshell-filling order and Hund's rule.
- Relate the structure of the periodic table (periods, groups, blocks) to electron configurations.
- Explain the origin of characteristic X-ray spectra and apply Moseley's law.
- Describe the physical basis of the laser: stimulated emission, population inversion, and metastable states.

## Introduction

[Chapter 10](#ch-the-hydrogen-atom) solved the hydrogen atom exactly, obtaining energies that depend on a single quantum number $n$ and states that can be filled with electrons two at a time (spin up, spin down) up to a degeneracy of $2n^2$. This chapter asks what happens for atoms with more than one electron, where the Schrödinger equation cannot be solved exactly, because each electron interacts not only with the nucleus but with every other electron. Two ideas make the many-electron problem tractable and explain the entire structure of the periodic table: an *independent-particle approximation*, in which each electron is imagined to move in an effective, average potential created by the nucleus and all the other electrons, and the *Pauli exclusion principle*, a rule with no classical analog that limits how many electrons can occupy any single quantum state. Together they explain why elements have the chemical and spectroscopic properties they do — and, in doing so, resolve one of the oldest puzzles in physics that quantum mechanics was built to explain: the periodic table itself.

## The Pauli Exclusion Principle

Wolfgang Pauli proposed in 1925 (before the discovery of the Schrödinger equation) a rule required to explain observed atomic spectra and, later, understood as a consequence of the fundamentally indistinguishable and antisymmetric nature of electron wave functions: **no two electrons in an atom can occupy the same complete set of quantum numbers** $(n,\ell,m_\ell,m_s)$. Equivalently, each distinct spatial-and-spin quantum state $(n,\ell,m_\ell,m_s)$ can hold **at most one electron**. This is not a subtle statistical tendency but an absolute prohibition, and it applies generally to electrons (and more broadly to the class of particles called fermions, which includes protons and neutrons) — without it, every electron in a multi-electron atom could simply fall into the lowest-energy $1s$ state, and all atoms would have similar, small sizes and similar chemistry, in sharp contradiction to the observed diversity of the periodic table. The exclusion principle is the single most important input, beyond the Schrödinger equation itself, needed to explain atomic structure.

## Screening and Subshell Energies

In hydrogen, the energy of a state depends only on $n$ ([Chapter 10](#ch-the-hydrogen-atom)), because the electron feels the bare $1/r$ potential of a single proton. In a multi-electron atom, an electron in an outer shell is partially **screened** from the full nuclear charge $Ze$ by the electrons in shells closer to the nucleus: it feels an *effective* nuclear charge $Z_{\text{eff}}e < Ze$, reduced from the true charge by the (partial) shielding effect of the intervening electron cloud.

Screening depends on $\ell$ as well as $n$, because electrons of lower $\ell$ (at fixed $n$) have wave functions with a greater probability of being found close to the nucleus (their radial probability distributions extend closer to $r=0$, as can be seen in the general shape of the hydrogen radial functions of [Chapter 10](#ch-the-hydrogen-atom)) — such electrons penetrate the inner electron cloud more effectively, feel less screening, and are therefore more tightly bound. The result is that, unlike in hydrogen, **energy in a multi-electron atom depends on both $n$ and $\ell$**, with energy generally increasing with $\ell$ at fixed $n$: within a given $n$, an $s$ state ($\ell=0$) lies lower in energy than a $p$ state ($\ell=1$), which lies lower than a $d$ state ($\ell=2$), and so on. This $\ell$-dependence is what breaks hydrogen's accidental degeneracy and is responsible for the specific subshell-filling order used below.

## Electron Configurations and the Periodic Table

Combining the exclusion principle with the $n$,$\ell$-dependent ordering of subshell energies, the ground-state **electron configuration** of an atom is built by filling the lowest-energy available subshells first, two electrons (spin up and spin down) per orbital, up to $2(2\ell+1)$ electrons per subshell — this is the **Aufbau ("building-up") principle**. Because screening shifts subshell energies, the filling order does not simply follow increasing $n$; the empirical (and largely first-principles-derivable) order is approximately

$$
1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p,\ 6s,\ 4f,\ 5d,\ 6p,\ \ldots
$$

— note, for example, that $4s$ fills before $3d$, since the extra penetration of the $4s$ orbital lowers its energy below that of $3d$ despite its larger $n$. When a subshell contains more than one electron and is only partially filled, **Hund's rule** states that the ground-state configuration maximizes the total spin (electrons singly occupy separate orbitals within a subshell, with parallel spins, before any orbital is doubly occupied) — a consequence of electron-electron repulsion, which is minimized when electrons, to the extent the exclusion principle allows, avoid occupying the same spatial orbital.

This filling scheme directly generates the structure of the **periodic table**. Each **period** (row) corresponds to filling a new principal shell $n$; each period ends when a subshell configuration reaches a particularly stable, filled-shell arrangement (a noble gas). Elements in the same **group** (column) share the same outer-shell (**valence**) configuration and, correspondingly, similar chemical properties, since chemical bonding ([Chapter 12](#ch-molecular-structure)) is governed primarily by the valence electrons. The table's division into $s$-block, $p$-block, $d$-block (transition metals), and $f$-block (lanthanides/actinides) regions directly reflects which subshell is being filled across that block. The chemical inertness of the noble gases, the strong reactivity of the alkali metals (a single, loosely bound $s$-electron outside a filled shell) and the halogens (one electron short of a filled shell), and the broad periodicity of atomic size and ionization energy all follow from this shell structure, without further assumptions.

## Atomic Spectra and X-Rays

Optical spectra of multi-electron atoms arise, as in hydrogen, from transitions of a single (typically outer, valence) electron between energy levels, now shifted by screening as described above and further split by the interaction between an electron's orbital and spin magnetic moments (**spin-orbit coupling**), producing the closely spaced doublets and multiplets seen in high-resolution atomic spectra.

A distinct and higher-energy class of spectral lines, **characteristic X-rays**, arises from transitions of *inner-shell* electrons. If an atom is bombarded with sufficiently energetic electrons (as in an X-ray tube) or photons, an inner-shell electron (e.g., from the $n=1$, or $K$, shell) can be ejected entirely, leaving a vacancy. An electron from a higher shell then drops down to fill the vacancy, emitting a photon whose energy — since inner-shell electrons in heavier atoms feel nearly the full, largely unscreened nuclear charge $Z$ — is far larger than typical optical-transition energies, and falls in the X-ray part of the spectrum. Lines from transitions ending on the $K$ shell ($n=1$) are called the **K series** (with $K_\alpha$ for the $n=2\to n=1$ transition, $K_\beta$ for $n=3\to n=1$, etc.).

Henry Moseley (1913) measured the characteristic X-ray frequencies of many elements and found that the frequency of the $K_\alpha$ line follows a strikingly simple pattern, **Moseley's law**:

$$
\sqrt{f} = a(Z - b),
$$

where $a$ and $b$ are constants (with $b\approx 1$ for the $K_\alpha$ line, reflecting screening of the nuclear charge by the one remaining $K$-shell electron) essentially independent of the element. This relation follows directly from a hydrogen-like treatment of the transition, with the true nuclear charge $Z$ replaced by an effective charge $Z_{\text{eff}} = Z - b$ to account for screening by the other $K$-shell electron, applied to the Bohr/Schrödinger hydrogen energy formula. Moseley's law provided, for the first time, a direct physical (rather than merely chemical) way to determine an element's atomic number $Z$, and was used to correctly order elements in the periodic table, resolve several ambiguities in the ordering by atomic mass, and confirm the existence of predicted-but-then-unobserved elements by their expected X-ray frequency, cementing $Z$ (nuclear charge) rather than atomic mass as the correct organizing quantity for the periodic table.

## Lasers

A further application of atomic energy levels involves the interaction between atoms and light more actively than simple absorption/emission spectroscopy. An atom in an excited state can lose energy in two distinct ways: **spontaneous emission**, in which it decays at a random time with a photon emitted in a random direction (governing ordinary fluorescence and, statistically, the exponential decay laws seen throughout atomic and nuclear physics), and **stimulated emission**, in which a passing photon of exactly the transition energy triggers the atom to emit a second, additional photon that is an exact copy of the first — same energy, direction, phase, and polarization. Einstein first predicted stimulated emission in 1917, well before it could be technologically exploited.

Ordinarily, stimulated emission is masked by the competing process of absorption, since a typical collection of atoms in thermal equilibrium has more atoms in lower-energy states than higher ones. A **laser** (light amplification by stimulated emission of radiation) requires engineering a **population inversion** — an atomic sample with more atoms in a higher-energy state than a lower one, typically achieved by "pumping" atoms into a higher state and relying on an intermediate **metastable state** (one with an anomalously long lifetime against spontaneous decay, because its decay to lower states is forbidden or strongly suppressed by selection rules such as the $\Delta\ell=\pm1$ rule of [Chapter 10](#ch-the-hydrogen-atom)) to accumulate a population large enough to exceed that of the lower lasing level. Once inverted, a single spontaneously emitted photon can trigger a cascade of stimulated emission as it passes back and forth through the gain medium (typically between two mirrors forming an optical cavity), producing an intense, coherent, highly directional, single-wavelength beam — a direct, large-scale, technological manifestation of discrete atomic energy levels and the quantum-mechanical description of light-matter interaction developed across this and the preceding chapters.

## Summary

- The **Pauli exclusion principle** forbids two electrons from sharing the same full set of quantum numbers $(n,\ell,m_\ell,m_s)$, limiting each orbital to two electrons (opposite spin) and is essential to explaining atomic structure.
- **Screening** of the nuclear charge by inner electrons makes subshell energy depend on both $n$ and $\ell$ in multi-electron atoms, unlike hydrogen; lower-$\ell$ orbitals penetrate closer to the nucleus and lie lower in energy at fixed $n$.
- The **Aufbau principle** (fill lowest-energy subshells first, respecting exclusion) and **Hund's rule** (maximize total spin within a partially filled subshell) determine ground-state electron configurations, which in turn generate the row/column/block structure of the periodic table and the periodicity of chemical properties.
- **Characteristic X-rays** arise from inner-shell vacancies; **Moseley's law**, $\sqrt f = a(Z-b)$, let X-ray spectra be used to determine atomic number directly, correctly ordering the periodic table by $Z$.
- **Lasers** exploit stimulated emission and a **population inversion**, sustained via a **metastable state**, to produce coherent light — a macroscopic application of discrete atomic energy levels and selection rules.

## Problems

1. Write the ground-state electron configuration (using $n\ell^{\,x}$ notation, e.g. $1s^2\,2s^2\ldots$) for (a) carbon ($Z=6$), (b) sodium ($Z=11$), (c) iron ($Z=26$), using the filling order given in the text.

2. Using Hund's rule, sketch the orbital-filling diagram (boxes for each $m_\ell$ orbital, arrows for spin) for the $2p$ subshell of nitrogen ($Z=7$, configuration $1s^22s^22p^3$), and state the resulting total spin.

3. Explain why, in a multi-electron atom, a $4s$ electron can have lower energy than a $3d$ electron despite having a larger principal quantum number, using the concept of orbital penetration and screening.

4. The measured $K_\alpha$ X-ray frequency of copper ($Z=29$) is $f = 1.94\times10^{18}\ \text{Hz}$. Using Moseley's law in the form $\sqrt{f} = A(Z-1)$ (i.e., $b=1$) with a single data point to determine $A$, predict the $K_\alpha$ frequency of nickel ($Z=28$), and compare qualitatively to what you would expect (higher or lower than copper's).

5. Explain, in terms of the exclusion principle, why the ground-state electron configuration of helium ($1s^2$) is chemically inert, while lithium ($1s^22s^1$) is highly reactive, referring to the energy required to remove the outermost electron in each case.

6. Explain why a three-level or four-level laser scheme requires a metastable intermediate state to sustain a population inversion, rather than pumping directly into the lower lasing level's excited partner state, using the relative decay rates implied by allowed versus forbidden transitions ([Chapter 10](#ch-the-hydrogen-atom)'s selection rule).
