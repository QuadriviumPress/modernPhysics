---
title: Molecular Structure
short_title: Chapter 10. Molecular Structure
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish ionic and covalent bonding in terms of the underlying electron distribution.
- Explain covalent bond formation in valence bond theory as the overlap of atomic orbitals.
- Explain the need for hybrid orbitals and identify the hybridization and molecular geometry implied by a given number of electron domains.
- Construct molecular orbitals as linear combinations of atomic orbitals and distinguish bonding from antibonding orbitals.
- Use a molecular orbital diagram to compute bond order and predict the stability and magnetic behavior of a simple diatomic molecule.
- Explain the vibrational and rotational energy levels of a diatomic molecule using the harmonic-oscillator and rigid-rotor approximations.

## Introduction

Chapters 8 and 9 explained the structure of individual atoms — how electrons occupy discrete energy levels arranged into subshells and shells, and how that arrangement produces the periodic table. This chapter asks how atoms combine to form molecules, using the same quantum-mechanical toolkit: atomic orbitals, the Pauli exclusion principle, and the variational tendency of a bound system to seek its lowest-energy configuration. Two complementary pictures are developed. **Valence bond theory** treats a bond as the overlap of atomic orbitals from two atoms, localized between them, and is the natural language for molecular geometry. **Molecular orbital theory** instead builds orbitals belonging to the molecule as a whole, and is the more powerful tool for predicting a molecule's stability, bond strength, and magnetic properties. The chapter closes by treating a bonded diatomic molecule as a single quantum system in its own right, subject to quantized vibrational and rotational energy levels — a direct application of the harmonic oscillator (Chapter 6) and angular momentum quantization (Chapter 7) to a new physical system.

## Ionic and Covalent Bonding

Chemical bonds form because a molecule can have lower total energy than its constituent separated atoms. Two limiting mechanisms produce this energy lowering. In **ionic bonding**, one atom (typically one with a low ionization energy, such as an alkali metal) transfers one or more electrons entirely to another atom (typically one with a high electron affinity, such as a halogen); the resulting oppositely charged ions are then held together by simple electrostatic (Coulomb) attraction. In **covalent bonding**, by contrast, one or more electron pairs are *shared* between two atoms, occupying a region of enhanced electron density between the two nuclei; both nuclei are then simultaneously attracted to this shared, concentrated negative charge, producing a net attractive bond. Most real bonds fall on a continuum between these two limits, described by varying degrees of bond **polarity**, depending on the difference in electronegativity between the bonded atoms; this chapter focuses on the covalent limit, whose treatment requires genuinely quantum-mechanical ideas beyond simple electrostatics.

## Valence Bond Theory and Orbital Overlap

**Valence bond theory** treats covalent bond formation as arising from the overlap of a singly occupied atomic orbital on one atom with a singly occupied atomic orbital on another, the two electrons (one from each atom, necessarily of opposite spin, per the exclusion principle applied to the resulting shared, doubly occupied region) pairing up to form the bond. The simplest example is the hydrogen molecule $\text{H}_2$: as two hydrogen atoms approach, their $1s$ orbitals begin to overlap, and if the two electrons involved have opposite spin, the resulting overlap region between the nuclei has a high joint probability of finding both electrons — an enhanced electron density that lowers the system's total energy relative to two separate atoms, up to a certain optimal internuclear separation (the **bond length**, at which attractive and repulsive contributions to the energy balance). Bonds formed by orbitals overlapping directly along the internuclear axis, giving a cylindrically symmetric electron distribution about that axis, are called **sigma ($\sigma$) bonds**; bonds formed by the sideways overlap of parallel $p$ orbitals, with electron density concentrated above and below (rather than directly along) the internuclear axis, are called **pi ($\pi$) bonds**. A single bond is one $\sigma$ bond; a double bond is one $\sigma$ plus one $\pi$ bond; a triple bond is one $\sigma$ plus two (mutually perpendicular) $\pi$ bonds.

## Hybrid Orbitals

Simple atomic $s$ and $p$ orbitals, taken directly from the hydrogen-like solutions of Chapter 8, generally point in the wrong directions (or have the wrong shapes) to account for the observed bond angles and geometries of real molecules — the observed near-$109.5°$ bond angles of methane, $\text{CH}_4$, for instance, are not reproduced by combinations of the atom's unmodified $2s$ and three $2p$ orbitals directly. The resolution is that the atomic orbitals actually used in bonding are not the pure $s$, $p$, $d$ orbitals of an isolated atom, but specific linear combinations of them, called **hybrid orbitals**, that better match the geometry demanded by minimizing electron-pair repulsion among the atom's bonding and lone electron pairs (the same qualitative principle underlying the electron-domain, or VSEPR, geometries encountered in general chemistry). Mixing one $s$ orbital with a varying number of $p$ (and, for some geometries, $d$) orbitals produces hybrid sets with characteristic, experimentally matched geometries:

| Hybridization | Orbitals mixed | Number of hybrids | Geometry | Example |
|---|---|---|---|---|
| $sp$ | one $s$, one $p$ | 2 | linear ($180°$) | $\text{BeCl}_2$ |
| $sp^2$ | one $s$, two $p$ | 3 | trigonal planar ($120°$) | $\text{BF}_3$ |
| $sp^3$ | one $s$, three $p$ | 4 | tetrahedral ($109.5°$) | $\text{CH}_4$ |
| $sp^3d$ | one $s$, three $p$, one $d$ | 5 | trigonal bipyramidal | $\text{PCl}_5$ |
| $sp^3d^2$ | one $s$, three $p$, two $d$ | 6 | octahedral | $\text{SF}_6$ |

The general rule connecting geometry to hybridization is that the number of hybrid orbitals equals the number of **electron domains** around the central atom — bonding pairs plus lone pairs — and that hybrid orbitals arrange themselves to maximize their mutual angular separation, minimizing electron-pair repulsion, exactly as in the VSEPR (valence-shell electron-pair repulsion) model of molecular geometry. Unshared (lone) electron pairs occupy hybrid orbitals just as bonding pairs do, but exert somewhat greater repulsion (being attracted to only one nucleus rather than shared between two), which is why, for example, the bond angle in water ($\text{H}_2\text{O}$, two bonding pairs and two lone pairs on an approximately $sp^3$ oxygen) is compressed to about $104.5°$ from the ideal tetrahedral $109.5°$.

## Molecular Orbital Theory

Valence bond theory, with hybridization added, accounts well for molecular geometry, but it treats bonding electrons as localized between two specific atoms and struggles to describe phenomena in which electrons are shared more broadly, or where a simple bonding picture predicts the wrong number of unpaired electrons. **Molecular orbital (MO) theory** instead constructs orbitals belonging to the molecule as a whole, built as linear combinations of the atomic orbitals (LCAO) of the constituent atoms, exactly as a molecular wave function must ultimately be some solution of the (approximate, many-electron) Schrödinger equation for the whole molecule.

For two hydrogen $1s$ orbitals, $\psi_A$ and $\psi_B$, on atoms $A$ and $B$, the two independent linear combinations are

$$
\psi_{\text{MO}}^{\pm} = \psi_A \pm \psi_B.
$$

The symmetric combination, $\psi_{\text{MO}}^{+} = \psi_A + \psi_B$, adds constructively in the region between the two nuclei, producing enhanced electron density there and a lower energy than the separate atomic orbitals — a **bonding orbital**, denoted $\sigma_{1s}$. The antisymmetric combination, $\psi_{\text{MO}}^{-} = \psi_A - \psi_B$, has a node exactly at the midpoint between the nuclei, *depleting* electron density in the internuclear region and yielding a *higher* energy than the separate atomic orbitals — an **antibonding orbital**, denoted $\sigma_{1s}^{*}$. In general, combining $N$ atomic orbitals always produces exactly $N$ molecular orbitals (never more, never fewer) — a direct consequence of treating the LCAO expansion as a change of basis for the same underlying space of trial wave functions — split symmetrically about the original atomic-orbital energy into bonding (lower) and antibonding (higher) sets.

Filling the resulting molecular orbitals with the molecule's electrons, two at a time (spin-paired, per the exclusion principle applied now to molecular rather than atomic orbitals) from lowest to highest energy, gives a **molecular orbital diagram**, from which the **bond order** is computed as

$$
\text{bond order} = \frac{(\text{number of bonding electrons}) - (\text{number of antibonding electrons})}{2}.
$$

A bond order of zero predicts an unstable molecule (no net energy lowering relative to separated atoms) that should not form; a bond order of $1, 2, 3, \ldots$ corresponds roughly to a single, double, triple, $\ldots$ bond, with higher bond order generally correlating with a shorter, stronger bond. For $\text{H}_2$ (two electrons, both in $\sigma_{1s}$), the bond order is $(2-0)/2 = 1$, consistent with the known stable single bond; for the hypothetical $\text{He}_2$ (four electrons, two in $\sigma_{1s}$ and two forced by the exclusion principle into $\sigma_{1s}^{*}$), the bond order is $(2-2)/2 = 0$ — correctly predicting that $\text{He}_2$ does not exist as a stable molecule, a conclusion valence bond theory (which has no natural way to place electrons in an antibonding orbital) does not straightforwardly reach. MO theory additionally predicts a molecule's magnetic behavior directly from its orbital diagram: any unpaired electrons (occurring, per Hund's rule applied to degenerate molecular orbitals, when a set of same-energy orbitals is only partially filled) make the molecule **paramagnetic** (weakly attracted into a magnetic field), while a fully paired configuration makes it **diamagnetic** (weakly repelled) — famously correctly predicting that $\text{O}_2$ is paramagnetic (two unpaired electrons in degenerate antibonding $\pi^*$ orbitals), a fact simple Lewis-structure/valence-bond reasoning does not anticipate.

## Vibrational and Rotational Energy Levels

Once bonded, a diatomic molecule is itself a quantum system with its own internal energy levels, in addition to the electronic energy levels associated with its bonding orbitals. Near the equilibrium bond length $r_0$ (where the molecular potential energy curve, as a function of internuclear separation, has its minimum), the potential is well approximated by a parabola, so small-amplitude **vibration** of the two nuclei about $r_0$ is, to good approximation, the quantum harmonic oscillator of Chapter 6, with quantized energies

$$
E_v = \left(v + \tfrac12\right)\hbar\omega, \qquad v = 0, 1, 2, \ldots,
$$

where $\omega = \sqrt{k/\mu}$, $k$ is the effective "spring constant" of the bond (obtained from the curvature of the potential at its minimum), and $\mu = m_1m_2/(m_1+m_2)$ is the **reduced mass** of the two-nucleus system (the appropriate effective mass for relative motion of a two-body system, reducing the two-body vibration problem to an equivalent single-particle problem).

Independently, the molecule can **rotate** about its center of mass; treating the two nuclei as point masses at fixed separation $r_0$ (the **rigid rotor** approximation, reasonable when rotational energies are small compared to vibrational spacing) makes this exactly the angular-momentum problem of Chapter 7, with quantized rotational energy

$$
E_J = \frac{\hbar^2}{2I}J(J+1), \qquad J = 0, 1, 2, \ldots,
$$

where $I = \mu r_0^2$ is the molecule's moment of inertia and $J$ plays the role of the orbital angular momentum quantum number $\ell$. Because $I$ for a typical molecule is large (bond lengths of order $10^{-10}\ \text{m}$, but heavy nuclear masses) compared to the effective "moment of inertia" scale set by an electron, rotational energy spacings are much smaller than vibrational spacings, which are in turn much smaller than electronic transition energies — a hierarchy ($E_{\text{elec}} \gg E_{\text{vib}} \gg E_{\text{rot}}$) that is directly reflected in molecular spectra: electronic transitions lie in the visible/ultraviolet, vibrational transitions in the infrared, and pure rotational transitions in the microwave region, each region probing a different aspect of molecular structure.

## Summary

- Chemical bonds lower a molecule's total energy relative to separated atoms; **ionic bonding** (electron transfer, electrostatic attraction) and **covalent bonding** (shared electron pairs, enhanced internuclear electron density) are limiting cases of a continuum set by electronegativity difference.
- **Valence bond theory** builds bonds from overlapping atomic orbitals ($\sigma$ for direct, $\pi$ for sideways overlap); **hybrid orbitals** ($sp$, $sp^2$, $sp^3$, etc.), one set per number of electron domains, reproduce observed molecular geometries via minimization of electron-pair repulsion.
- **Molecular orbital theory** builds orbitals belonging to the whole molecule as linear combinations of atomic orbitals, splitting into lower-energy **bonding** and higher-energy **antibonding** orbitals; filling these with the molecule's electrons gives the **bond order**, which predicts stability, bond strength, and (via unpaired electrons) paramagnetism — correctly predicting, e.g., $\text{O}_2$'s paramagnetism and $\text{He}_2$'s nonexistence.
- A bonded diatomic molecule has quantized **vibrational** levels, $E_v=(v+\tfrac12)\hbar\omega$ (harmonic oscillator in the reduced mass $\mu$), and **rotational** levels, $E_J = \hbar^2J(J+1)/2I$ (rigid rotor), with $E_{\text{elec}}\gg E_{\text{vib}}\gg E_{\text{rot}}$, placing electronic, vibrational, and rotational spectra in the UV/visible, infrared, and microwave regions respectively.

## Problems

1. Determine the hybridization of the central atom and predict the molecular geometry for (a) $\text{NH}_3$ (three bonding pairs, one lone pair on N), (b) $\text{CO}_2$ (two double bonds, no lone pairs on C), (c) $\text{SF}_6$.

2. Construct the molecular orbital diagram for the nitrogen molecule $\text{N}_2$ (14 electrons total; consider only the valence $2s$ and $2p$ electrons, 10 of the 14, filling $\sigma_{2s}, \sigma_{2s}^*, \pi_{2p}$ (×2), $\sigma_{2p}$ in the order relevant for $\text{N}_2$). Determine the bond order and compare it to the triple bond expected from the Lewis structure $:\text{N}\!\equiv\!\text{N}:$.

3. Using the same style of reasoning applied to $\text{H}_2$ and $\text{He}_2$ in the text, determine the bond order predicted by MO theory for the hypothetical ion $\text{He}_2^+$ (three electrons: two in $\sigma_{1s}$, one in $\sigma_{1s}^*$), and state whether this ion is predicted to be (marginally) stable.

4. The HCl molecule has an effective vibrational frequency $f = \omega/2\pi = 8.66\times10^{13}\ \text{Hz}$. Using $m_{\text{H}} = 1.008\ \text{u}$ and $m_{\text{Cl}} = 35.45\ \text{u}$ ($1\ \text{u} = 1.66\times10^{-27}\ \text{kg}$), compute (a) the reduced mass $\mu$, and (b) the zero-point vibrational energy $E_0 = \tfrac12\hbar\omega$ in eV.

5. The CO molecule has bond length $r_0 = 0.113\ \text{nm}$ and reduced mass $\mu = 6.86\ \text{u}$. Compute (a) its moment of inertia $I = \mu r_0^2$, and (b) the energy (in units of $10^{-4}\ \text{eV}$) of the $J=0\to J=1$ rotational transition.

6. Explain, using the concept of bond order, why $\text{O}_2^-$ (superoxide, one more electron than $\text{O}_2$) has a weaker, longer bond than neutral $\text{O}_2$, while $\text{O}_2^+$ (dioxygenyl, one fewer electron) has a stronger, shorter bond — referring to which type of orbital (bonding or antibonding) the added or removed electron occupies.
