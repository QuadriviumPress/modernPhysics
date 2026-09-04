---
title: Molecular Structure
short_title: Chapter 12. Molecular Structure
label: ch-molecular-structure
numbering:
  enumerator: "12.%s"
  heading_2: true
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish ionic and covalent bonding in terms of the underlying electron distribution.
- Explain covalent bond formation in valence bond theory as the overlap of atomic orbitals.
- Explain the need for hybrid orbitals and identify the hybridization and molecular geometry implied by a given number of electron domains.
- Construct molecular orbitals as linear combinations of atomic orbitals and distinguish bonding from antibonding orbitals.
- Use a molecular orbital diagram to compute bond order and predict the stability and magnetic behavior of a simple diatomic molecule.
- Explain the vibrational and rotational energy levels of a diatomic molecule using the harmonic-oscillator and rigid-rotor approximations.

### Introduction

Chapters [10](#ch-the-hydrogen-atom) and [11](#ch-many-electron-atoms) explained the structure of individual atoms — how electrons occupy discrete energy levels arranged into subshells and shells, and how that arrangement produces the periodic table. This chapter asks how atoms combine to form molecules, using the same quantum-mechanical toolkit: atomic orbitals, the Pauli exclusion principle, and the variational tendency of a bound system to seek its lowest-energy configuration. Two complementary pictures are developed. **Valence bond theory** treats a bond as the overlap of atomic orbitals from two atoms, localized between them, and is the natural language for molecular geometry. **Molecular orbital theory** instead builds orbitals belonging to the molecule as a whole, and is the more powerful tool for predicting a molecule's stability, bond strength, and magnetic properties. The chapter closes by treating a bonded diatomic molecule as a single quantum system in its own right, subject to quantized vibrational and rotational energy levels — a direct application of the harmonic oscillator ([Chapter 8](#ch-the-schrodinger-equation)) and angular momentum quantization ([Chapter 9](#ch-quantum-mechanics-in-three-dimensions)) to a new physical system.

## Bonding and Hybrid Orbitals

### Ionic and Covalent Bonding

Chemical bonds form because a molecule can have lower total energy than its constituent separated atoms. Two limiting mechanisms produce this energy lowering. In **ionic bonding**, one atom (typically one with a low ionization energy, such as an alkali metal) transfers one or more electrons entirely to another atom (typically one with a high electron affinity, such as a halogen); the resulting oppositely charged ions are then held together by simple electrostatic (Coulomb) attraction. In **covalent bonding**, by contrast, one or more electron pairs are *shared* between two atoms, occupying a region of enhanced electron density between the two nuclei; both nuclei are then simultaneously attracted to this shared, concentrated negative charge, producing a net attractive bond. Most real bonds fall on a continuum between these two limits, described by varying degrees of bond **polarity**, depending on the difference in electronegativity between the bonded atoms; this chapter focuses on the covalent limit, whose treatment requires genuinely quantum-mechanical ideas beyond simple electrostatics.

:::{margin}
**Electronegativity**, on the dimensionless Pauling scale, runs from about $0.7$ (cesium) to $4.0$ (fluorine). A difference of roughly $1.7$ or more between two bonded atoms is the conventional (rough, not sharp) threshold above which a bond is usually described as "ionic" rather than "polar covalent."
:::

That continuum is a slider rather than a classification, and {numref}`Figure %s <fig:ch12-polarity-sim>` makes it one: set the electronegativity of each atom in a diatomic and watch the shared electron density slide from the midpoint toward the more electronegative partner, dragging a dipole moment with it. At equal electronegativity the bond is purely covalent and the dipole vanishes; at a large difference the electron is effectively transferred and what remains is a pair of ions attracting each other. Neither limit is a separate mechanism — they are the two ends of one.

```{phet} molecule-polarity
:label: fig:ch12-polarity-sim

Bond polarity as a continuous function of the electronegativity difference between two atoms, with the electron density and the resulting dipole moment displayed. Later screens add a third atom, where bond dipoles combine vectorially and a molecule of polar bonds can still be nonpolar overall.
```

### Valence Bond Theory and Orbital Overlap

**Valence bond theory** treats covalent bond formation as arising from the overlap of a singly occupied atomic orbital on one atom with a singly occupied atomic orbital on another, the two electrons (one from each atom, necessarily of opposite spin, per the exclusion principle applied to the resulting shared, doubly occupied region) pairing up to form the bond. The simplest example is the hydrogen molecule $\text{H}_2$: as two hydrogen atoms approach, their $1s$ orbitals begin to overlap, and if the two electrons involved have opposite spin, the resulting overlap region between the nuclei has a high joint probability of finding both electrons — an enhanced electron density that lowers the system's total energy relative to two separate atoms, up to a certain optimal internuclear separation (the **bond length**, at which attractive and repulsive contributions to the energy balance). Bonds formed by orbitals overlapping directly along the internuclear axis, giving a cylindrically symmetric electron distribution about that axis, are called **sigma ($\sigma$) bonds**; bonds formed by the sideways overlap of parallel $p$ orbitals, with electron density concentrated above and below (rather than directly along) the internuclear axis, are called **pi ($\pi$) bonds**. A single bond is one $\sigma$ bond; a double bond is one $\sigma$ plus one $\pi$ bond; a triple bond is one $\sigma$ plus two (mutually perpendicular) $\pi$ bonds.

:::{margin}
The labels $\sigma$ and $\pi$ describe the *symmetry* of the orbital overlap about the bond axis, not the bond's strength or order directly: a single bond is always exactly one $\sigma$ bond, however the orbitals forming it are hybridized, and every bond beyond the first in a double or triple bond is necessarily a $\pi$ bond.
:::

### Hybrid Orbitals

Simple atomic $s$ and $p$ orbitals, taken directly from the hydrogen-like solutions of [Chapter 10](#ch-the-hydrogen-atom), generally point in the wrong directions (or have the wrong shapes) to account for the observed bond angles and geometries of real molecules — the observed near-$109.5°$ bond angles of methane, $\text{CH}_4$, for instance, are not reproduced by combinations of the atom's unmodified $2s$ and three $2p$ orbitals directly. The resolution is that the atomic orbitals actually used in bonding are not the pure $s$, $p$, $d$ orbitals of an isolated atom, but specific linear combinations of them, called **hybrid orbitals**, that better match the geometry demanded by minimizing electron-pair repulsion among the atom's bonding and lone electron pairs (the same qualitative principle underlying the electron-domain, or VSEPR, geometries encountered in general chemistry). Mixing one $s$ orbital with a varying number of $p$ (and, for some geometries, $d$) orbitals produces hybrid sets with characteristic, experimentally matched geometries:

The standard geometries are collected in {numref}`Table %s <tab:ch12-hybridization>`.

```{table} Common orbital hybridizations and their molecular geometries
:label: tab:ch12-hybridization

| Hybridization | Orbitals mixed | Number of hybrids | Geometry | Example |
|---|---|---|---|---|
| $sp$ | one $s$, one $p$ | 2 | linear ($180°$) | $\text{BeCl}_2$ |
| $sp^2$ | one $s$, two $p$ | 3 | trigonal planar ($120°$) | $\text{BF}_3$ |
| $sp^3$ | one $s$, three $p$ | 4 | tetrahedral ($109.5°$) | $\text{CH}_4$ |
| $sp^3d$ | one $s$, three $p$, one $d$ | 5 | trigonal bipyramidal | $\text{PCl}_5$ |
| $sp^3d^2$ | one $s$, three $p$, two $d$ | 6 | octahedral | $\text{SF}_6$ |
```

The general rule connecting geometry to hybridization is that the number of hybrid orbitals equals the number of **electron domains** around the central atom — bonding pairs plus lone pairs — and that hybrid orbitals arrange themselves to maximize their mutual angular separation, minimizing electron-pair repulsion, exactly as in the VSEPR (valence-shell electron-pair repulsion) model of molecular geometry. Unshared (lone) electron pairs occupy hybrid orbitals just as bonding pairs do, but exert somewhat greater repulsion (being attracted to only one nucleus rather than shared between two), which is why, for example, the bond angle in water ($\text{H}_2\text{O}$, two bonding pairs and two lone pairs on an approximately $sp^3$ oxygen) is compressed to about $104.5°$ from the ideal tetrahedral $109.5°$.

The counting rule behind {numref}`Table %s <tab:ch12-hybridization>` is worth exercising on molecules other than the five listed, and {numref}`Figure %s <fig:ch12-shapes-sim>` is set up for exactly that: attach single, double, or triple bonds and lone pairs to a central atom in any combination and the geometry rearranges itself, with the bond angles reported as they change. Two predictions from the paragraph above can be checked in a few seconds there. A double bond and a single bond count the same for geometry — both are one electron domain — and replacing a bonding pair by a lone pair squeezes the remaining angles, reproducing water's $104.5°$ from tetrahedral.

```{phet} molecule-shapes
:label: fig:ch12-shapes-sim

Molecular geometry built from electron domains. Bond angles are displayed live, and the "real molecules" screen compares the idealized VSEPR prediction with measured geometries.
```

#### Worked Example: The Geometry of Xenon Tetrafluoride

Predict the hybridization and molecular geometry of $\text{XeF}_4$.

Xenon forms four Xe–F $\sigma$ bonds to the four fluorine atoms. After those four bonding pairs and the three lone pairs required on each fluorine to complete its own octet are accounted for, the count of xenon's eight valence electrons leaves **two lone pairs on xenon itself** — xenon, unlike carbon or nitrogen, has enough valence electrons to bond fully *and* retain lone pairs of its own. The central atom therefore has $4$ bonding domains $+\ 2$ lone pairs $= 6$ electron domains, calling for **$sp^3d^2$ hybridization** and an octahedral arrangement of those six domains.

The two lone pairs could sit at $90°$ (adjacent) or $180°$ (opposite) to each other on the octahedron. Because lone-pair–lone-pair repulsion is the strongest of the three repulsion types recognized by the electron-domain model (lone pair–lone pair $>$ lone pair–bonding pair $>$ bonding pair–bonding pair), the two lone pairs move as far apart as the octahedral geometry allows: directly opposite one another. That leaves the four Xe–F bonds occupying the remaining four positions, all in a single plane — a **square planar** molecular geometry, with $\text{F}$–$\text{Xe}$–$\text{F}$ bond angles of exactly $90°$ between adjacent fluorines and $180°$ across. This result is worth remembering precisely because the naive guess for "four bonded groups" — tetrahedral, as in $\text{CH}_4$ — is wrong here: the two lone pairs, invisible in a skeletal formula, are what flatten the molecule into a plane.

## Molecular Orbital Theory

Valence bond theory, with hybridization added, accounts well for molecular geometry, but it treats bonding electrons as localized between two specific atoms and struggles to describe phenomena in which electrons are shared more broadly, or where a simple bonding picture predicts the wrong number of unpaired electrons. **Molecular orbital (MO) theory** instead constructs orbitals belonging to the molecule as a whole, built as linear combinations of the atomic orbitals (LCAO) of the constituent atoms, exactly as a molecular wave function must ultimately be some solution of the (approximate, many-electron) Schrödinger equation for the whole molecule.

For two hydrogen $1s$ orbitals, $\psi_A$ and $\psi_B$, on atoms $A$ and $B$, the two independent linear combinations are

$$
\psi_{\text{MO}}^{\pm} = \psi_A \pm \psi_B.
$$

The symmetric combination, $\psi_{\text{MO}}^{+} = \psi_A + \psi_B$, adds constructively in the region between the two nuclei, producing enhanced electron density there and a lower energy than the separate atomic orbitals — a **bonding orbital**, denoted $\sigma_{1s}$. The antisymmetric combination, $\psi_{\text{MO}}^{-} = \psi_A - \psi_B$, has a node exactly at the midpoint between the nuclei, *depleting* electron density in the internuclear region and yielding a *higher* energy than the separate atomic orbitals — an **antibonding orbital**, denoted $\sigma_{1s}^{*}$. In general, combining $N$ atomic orbitals always produces exactly $N$ molecular orbitals (never more, never fewer) — a direct consequence of treating the LCAO expansion as a change of basis for the same underlying space of trial wave functions — split symmetrically about the original atomic-orbital energy into bonding (lower) and antibonding (higher) sets.

:::{dropdown} Why the Antibonding Orbital Rises More Than the Bonding Orbital Falls
The qualitative claim that $\psi_{\text{MO}}^+$ is lower in energy and $\psi_{\text{MO}}^-$ is higher can be made quantitative. Define three integrals: the **overlap integral** $S=\int\psi_A\psi_B\,d\tau$ (how much the two atomic orbitals overlap in space, $0\le S\le1$), the **Coulomb integral** $\alpha=\int\psi_A\hat H\psi_A\,d\tau=\int\psi_B\hat H\psi_B\,d\tau$ (essentially the original atomic-orbital energy, perturbed by the presence of the other nucleus), and the **resonance integral** $\beta=\int\psi_A\hat H\psi_B\,d\tau$ (negative, and nonzero only because the orbitals overlap). Normalizing $\psi_{\text{MO}}^{\pm}=(\psi_A\pm\psi_B)/\sqrt{2(1\pm S)}$ and evaluating $\langle\psi_{\text{MO}}^{\pm}|\hat H|\psi_{\text{MO}}^{\pm}\rangle$ gives

$$
E_{\pm} = \frac{\alpha \pm \beta}{1 \pm S}.
$$

Because $\beta<0$, $E_+=(\alpha+\beta)/(1+S)$ lies below $\alpha$ (bonding) and $E_-=(\alpha-\beta)/(1-S)$ lies above $\alpha$ (antibonding) — but the two shifts are **not equal in magnitude**. The $(1-S)$ in the antibonding denominator is smaller than the $(1+S)$ in the bonding denominator, so $E_-$ rises above $\alpha$ by more than $E_+$ falls below it. This asymmetry is the entire reason $\text{He}_2$ fails to bond: two electrons in $\sigma_{1s}$ and two in $\sigma_{1s}^*$ do not cancel to zero net energy change, because the antibonding pair's destabilization outweighs the bonding pair's stabilization, leaving $\text{He}_2$ at *higher* energy than two separate helium atoms — consistent with, and quantitatively explaining, the bond order of zero found by simple electron counting below.
:::

Filling the resulting molecular orbitals with the molecule's electrons, two at a time (spin-paired, per the exclusion principle applied now to molecular rather than atomic orbitals) from lowest to highest energy, gives a **molecular orbital diagram**, from which the **bond order** is computed as

$$
\text{bond order} = \frac{(\text{number of bonding electrons}) - (\text{number of antibonding electrons})}{2}.
$$

:::{margin}
Bond order need not be an integer. Whenever an odd number of electrons occupies an antibonding level, the formula returns a half-integer, such as bond order $\tfrac12$ for $\text{He}_2^+$ or $\tfrac52$ for $\text{N}_2^+$ — a genuine prediction of MO theory, not a rounding artifact.
:::

A bond order of zero predicts an unstable molecule (no net energy lowering relative to separated atoms) that should not form; a bond order of $1, 2, 3, \ldots$ corresponds roughly to a single, double, triple, $\ldots$ bond, with higher bond order generally correlating with a shorter, stronger bond. For $\text{H}_2$ (two electrons, both in $\sigma_{1s}$), the bond order is $(2-0)/2 = 1$, consistent with the known stable single bond; for the hypothetical $\text{He}_2$ (four electrons, two in $\sigma_{1s}$ and two forced by the exclusion principle into $\sigma_{1s}^{*}$), the bond order is $(2-2)/2 = 0$ — correctly predicting that $\text{He}_2$ does not exist as a stable molecule, a conclusion valence bond theory (which has no natural way to place electrons in an antibonding orbital) does not straightforwardly reach. MO theory additionally predicts a molecule's magnetic behavior directly from its orbital diagram: any unpaired electrons (occurring, per Hund's rule applied to degenerate molecular orbitals, when a set of same-energy orbitals is only partially filled) make the molecule **paramagnetic** (weakly attracted into a magnetic field), while a fully paired configuration makes it **diamagnetic** (weakly repelled) — famously correctly predicting that $\text{O}_2$ is paramagnetic (two unpaired electrons in degenerate antibonding $\pi^*$ orbitals), a fact simple Lewis-structure/valence-bond reasoning does not anticipate.

:::{warning} Antibonding Is Not the Same as Nonbonding
It is tempting to think of an antibonding orbital as simply "not contributing" to the bond, the way a lone pair sitting in an uninvolved orbital does. That is wrong: an antibonding orbital actively *raises* the energy of an electron placed in it above the energy of the separated atomic orbitals, because destructive interference at the internuclear midpoint removes electron density from between the nuclei rather than merely failing to add any. A fully occupied antibonding orbital does not leave a bond unaffected — paired with a corresponding fully occupied bonding orbital, it cancels the bond outright, exactly as for $\text{He}_2$ above. "Antibonding" means actively destabilizing, not neutral.
:::

The bonding and antibonding pair are not a chemical convention; they are what the Schrödinger equation returns for two wells brought close together, and {numref}`Figure %s <fig:ch12-double-well-sim>` solves that problem directly. Start with two widely separated square wells: each has its own ground state, and the two are degenerate. Slide them together and the degeneracy lifts into exactly two states — one symmetric, with no node between the wells and an energy *below* the isolated-atom level, and one antisymmetric, with a node at the midpoint and an energy above it. That is $\sigma_{1s}$ and $\sigma_{1s}^*$, obtained without mentioning chemistry, and the splitting between them grows as the wells approach, which is why bond strength depends on overlap.

```{phet-legacy} bound-states/covalent-bonds
:sim-name: Double Wells and Covalent Bonds
:label: fig:ch12-double-well-sim

A double square well with adjustable separation and depth, and the eigenstates it supports. The symmetric–antisymmetric splitting of a pair of formerly degenerate levels is the origin of the bonding/antibonding pair of MO theory, and — extended to $N$ wells in a row — of the energy bands of a solid.
```

#### Historical Context: From Lewis's Electron Pair to the Pauling–Mulliken Rivalry

The idea that a covalent bond is a *shared pair of electrons* predates quantum mechanics itself. In 1916 — a full decade before Schrödinger's equation — the American chemist Gilbert N. Lewis proposed exactly this picture, together with the electron-dot notation still used to sketch molecules today, purely from chemical reasoning about valence and the stability of the noble-gas electron count, with no wave mechanics available to justify it. Lewis's shared pair was a hypothesis in search of a mechanism, and quantum mechanics supplied one a decade later, in two competing forms.

**Valence bond theory**, developed by Walter Heitler and Fritz London (1927) and then extended and popularized by Linus Pauling through the early 1930s — including the hybrid-orbital concept of this chapter — kept Lewis's picture of a bond as a localized pair shared between two specific atoms, now computed from overlapping atomic wave functions rather than guessed at. **Molecular orbital theory**, developed in the same years chiefly by Friedrich Hund and Robert Mulliken, instead discarded the idea that an electron belongs to one bond at a time, building orbitals delocalized over the whole molecule from the outset. The two camps disagreed, sometimes sharply, over which picture was the physically correct starting point — Pauling's localized, chemist-friendly bonds versus Mulliken's delocalized, spectroscopically motivated orbitals — and valence bond theory, propelled by Pauling's enormously influential 1939 book *The Nature of the Chemical Bond*, remained the dominant teaching framework through the 1950s. Molecular orbital theory eventually overtook it, in no small part on the strength of results like the $\text{O}_2$ paramagnetism prediction below, which valence bond theory cannot produce without ad hoc patching. Pauling received the 1954 Nobel Prize in Chemistry "for his research into the nature of the chemical bond," and Mulliken received the 1966 Prize "for his fundamental work concerning chemical bonds and the electronic structure of molecules by the molecular orbital method" ({numref}`Figure %s <fig:ch12-pauling>`). Both theories remain in active use today, each suited to different questions — geometry and localized reactivity for valence bond theory, spectra and magnetism for molecular orbital theory — which is why this chapter, like the field itself, teaches both.

```{figure} ../images/historical-linus-pauling-1962.jpg
:label: fig:ch12-pauling
:alt: Historical photograph of Linus Pauling, 1962.

Linus Pauling, photographed in 1962, eight years after his 1954 Nobel Prize in Chemistry for work on the nature of the chemical bond — the valence-bond and hybridization framework of this chapter. Photograph by the Nobel Foundation; public domain via Wikimedia Commons.
```

#### Building the Diagram for the Second Row: N₂ and O₂

Hydrogen and helium have only $1s$ orbitals to combine, but a second-row diatomic such as $\text{N}_2$ or $\text{O}_2$ has both $2s$ and $2p$ atomic orbitals on each atom, and the resulting molecular orbital diagram, while built by exactly the same LCAO recipe used for $\text{H}_2$, has more structure worth spelling out explicitly.

Combining the two $2s$ orbitals (one per atom) gives a bonding $\sigma_{2s}$ and an antibonding $\sigma_{2s}^{*}$, exactly as for $1s$. Of the three $2p$ orbitals on each atom, the pair pointing directly *along* the internuclear axis overlaps head-on, giving a bonding $\sigma_{2p}$ and antibonding $\sigma_{2p}^{*}$; the two remaining pairs of $2p$ orbitals, oriented *perpendicular* to the axis, overlap sideways, giving a bonding $\pi_{2p}$ and antibonding $\pi_{2p}^{*}$ pair for each of the two independent perpendicular directions — so the $\pi_{2p}$ level (and, separately, the $\pi_{2p}^{*}$ level) is **doubly degenerate**, two orbitals at the same energy. In all, ten atomic orbitals (two $2s$ and three $2p$, on each of two atoms) combine into ten molecular orbitals: $\sigma_{2s}$, $\sigma_{2s}^{*}$, $\sigma_{2p}$, $\sigma_{2p}^{*}$, and the degenerate pairs $\pi_{2p}$ and $\pi_{2p}^{*}$.

The one genuine subtlety is the *relative* energy of $\sigma_{2p}$ and $\pi_{2p}$, and it is worth getting right because it is a famous trap. Head-on ($\sigma$) overlap is intrinsically stronger than sideways ($\pi$) overlap, so a naive picture would put $\sigma_{2p}$ below $\pi_{2p}$ always — and that is indeed the order for $\text{O}_2$, $\text{F}_2$, and $\text{Ne}_2$. But for the *lighter* diatomics $\text{B}_2$, $\text{C}_2$, and $\text{N}_2$, the order **inverts**: $\pi_{2p}$ sits below $\sigma_{2p}$. The mechanism is **$s$–$p$ mixing**: $\sigma_{2s}$ and $\sigma_{2p}$ share the same symmetry along the internuclear axis, and whenever the atomic $2s$ and $2p$ energies are close enough, these two molecular orbitals mix with each other quantum mechanically, pushing $\sigma_{2s}$ lower and $\sigma_{2p}$ higher than a naive non-interacting picture would predict — enough, for the lighter elements, to push $\sigma_{2p}$ above $\pi_{2p}$ entirely. Moving across the period, increasing nuclear charge pulls the $2s$ orbital down in energy faster than the $2p$ orbital (a $2s$ electron spends more time near the nucleus and so feels the increasing charge more strongly), widening the $2s$–$2p$ gap; by oxygen, that gap is wide enough that $s$–$p$ mixing is too weak to invert the order, and the naive $\sigma_{2p}$-below-$\pi_{2p}$ sequence is restored. {numref}`Figure %s <fig:ch12-mo-n2-o2>` shows both diagrams side by side, filled with electrons.

```{figure} ../images/ch12-mo-diagram-n2-o2.svg
:label: fig:ch12-mo-n2-o2
:alt: Side-by-side molecular orbital energy level diagrams for N2 and O2, showing atomic 2s and 2p levels on the outside, molecular orbitals in the middle filled with electrons from the bottom up, and the swapped sigma-2p and pi-2p order between the two molecules.

Molecular orbital diagrams for N$_2$ and O$_2$. Atomic $2s$ and $2p$ levels sit outside; molecular orbitals sit in the middle, filled from the bottom with the molecule's valence electrons. Note the swapped $\sigma_{2p}/\pi_{2p}$ order: $\pi_{2p}$ below $\sigma_{2p}$ for N$_2$ (light diatomic, strong $s$–$p$ mixing), $\sigma_{2p}$ below $\pi_{2p}$ for O$_2$ (heavier, weak $s$–$p$ mixing). Original schematic generated with matplotlib; see `scripts/figures/`.
```

For $\text{N}_2$ (10 valence electrons), filling from the bottom — $\sigma_{2s}$ (2), $\sigma_{2s}^{*}$ (2), $\pi_{2p}$ (4), $\sigma_{2p}$ (2) — uses all ten electrons with every orbital either completely filled or completely empty, giving

$$
\text{bond order}(\text{N}_2) = \frac{8-2}{2} = 3,
$$

consistent with the triple bond of the Lewis structure $:\text{N}\!\equiv\!\text{N}:$, and, with every electron paired, correctly predicting that $\text{N}_2$ is diamagnetic.

#### Worked Example: The Molecular Orbital Diagram and Paramagnetism of O₂

Construct the molecular orbital diagram for $\text{O}_2$, determine its bond order, and explain its paramagnetism.

$\text{O}_2$ has $6+6=12$ valence electrons. Using the *heavier-diatomic* ordering established above — $\sigma_{2s}$, $\sigma_{2s}^{*}$, $\sigma_{2p}$, $\pi_{2p}$ ($\times2$), $\pi_{2p}^{*}$ ($\times2$), $\sigma_{2p}^{*}$ — fill from the bottom, two electrons per orbital, respecting Hund's rule (spread electrons across a set of degenerate orbitals, one each, before pairing any of them), as in {numref}`Table %s <tab:ch12-o2-filling>`:

```{table} Filling the O2 molecular orbital diagram
:label: tab:ch12-o2-filling

| Orbital | Electrons added | Running total |
|---|---|---|
| $\sigma_{2s}$ | 2 | 2 |
| $\sigma_{2s}^{*}$ | 2 | 4 |
| $\sigma_{2p}$ | 2 | 6 |
| $\pi_{2p}$ (both orbitals) | 4 | 10 |
| $\pi_{2p}^{*}$ (both orbitals) | 2 | 12 |
```

The last two electrons enter the doubly degenerate $\pi_{2p}^{*}$ level. Hund's rule places one electron in each of the two degenerate $\pi_{2p}^{*}$ orbitals, with parallel spins, rather than pairing both into a single orbital — leaving **two unpaired electrons**. Counting bonding electrons ($\sigma_{2s}$: 2, $\sigma_{2p}$: 2, $\pi_{2p}$: 4, total 8) against antibonding electrons ($\sigma_{2s}^{*}$: 2, $\pi_{2p}^{*}$: 2, total 4),

$$
\text{bond order}(\text{O}_2) = \frac{8-4}{2} = 2,
$$

consistent with the double bond of the Lewis structure $\text{O}\!=\!\text{O}$. But that Lewis structure, with every electron paired off into bonds and lone pairs, gives no hint of the two unpaired $\pi_{2p}^{*}$ electrons found here — and it is exactly those two unpaired electrons that make liquid oxygen **paramagnetic**, visibly drawn toward the poles of a strong magnet in the standard classroom demonstration, a fact valence bond theory cannot explain without modification but that falls directly out of the molecular orbital diagram.

#### Bond Order, Bond Length, and Bond Strength: A Worked Comparison

Bond order is a prediction about two directly measurable quantities: bond length and bond dissociation energy. Higher bond order means more shared electron density concentrated between the nuclei, which pulls the nuclei closer together (shorter bond length) and requires more energy to pull them apart (higher dissociation energy). The nitrogen–nitrogen bond, compared across three different molecules in {numref}`Table %s <tab:ch12-nn-bonds>`, shows the trend cleanly, because in each case the bond order is unambiguous from the Lewis structure:

```{table} Nitrogen–nitrogen bond order, length, and dissociation energy
:label: tab:ch12-nn-bonds

| Molecule | Bond | Bond order | Bond length | Dissociation energy |
|---|---|---|---|---|
| $\text{N}_2\text{H}_4$ (hydrazine) | N–N | 1 | $145\ \text{pm}$ | $167\ \text{kJ/mol}$ |
| $\text{N}_2\text{H}_2$ (diazene) | N=N | 2 | $125\ \text{pm}$ | $418\ \text{kJ/mol}$ |
| $\text{N}_2$ (nitrogen) | N$\equiv$N | 3 | $110\ \text{pm}$ | $942\ \text{kJ/mol}$ |
```

Tripling the bond order roughly quintuples the dissociation energy while shortening the bond by nearly a quarter — and the relationship is not linear in dissociation energy: going from a single to a double bond adds $251\ \text{kJ/mol}$, while going from a double to a triple bond adds $524\ \text{kJ/mol}$, more than double the first increment, because the additional $\pi$ bonds of a multiple bond form between orbitals already held close together by the existing $\sigma$ bond and so overlap unusually well. This is also why $\text{N}_2$, held together by one of the strongest common bonds in chemistry, is so notoriously unreactive that converting it into a chemically usable form of nitrogen (the industrial Haber–Bosch process) is one of the most energy-intensive reactions carried out on Earth.

:::{tip} Read the HOMO Before You Refill the Whole Diagram
When a problem asks how ionizing (or reducing) a molecule changes its bond length or bond strength, there is rarely a need to refill an entire molecular orbital diagram from scratch. Identify only the **highest occupied molecular orbital (HOMO)** — the orbital the added or removed electron actually occupies — and ask whether it is bonding or antibonding. Removing an electron from a bonding HOMO weakens the bond (as for $\text{N}_2\to\text{N}_2^+$ below); removing one from an antibonding HOMO strengthens it (as for $\text{O}_2\to\text{O}_2^+$ in [Problem 6](#ex-molecular-structure-6)). That one fact settles the direction of the change before a bond order is ever computed.
:::

#### Worked Example: Ionizing Nitrogen — N₂ versus N₂⁺

Removing an electron from $\text{N}_2$ to form the molecular ion $\text{N}_2^{+}$ (as happens, for example, when a fast electron or solar-wind particle strikes an atmospheric nitrogen molecule during an aurora) removes it from the highest-occupied orbital identified above — for $\text{N}_2$, the bonding $\sigma_{2p}$. That leaves $9$ valence electrons: $\sigma_{2s}$ (2), $\sigma_{2s}^{*}$ (2), $\pi_{2p}$ (4), $\sigma_{2p}$ (1), so

$$
\text{bond order}(\text{N}_2^{+}) = \frac{7-2}{2} = 2.5,
$$

down from $3$ for neutral $\text{N}_2$. Removing an electron from a *bonding* orbital weakens the bond, predicting a longer, weaker bond in the ion than in the neutral molecule — and indeed $\text{N}_2^{+}$'s measured bond length, about $112\ \text{pm}$, is longer than $\text{N}_2$'s $110\ \text{pm}$, consistent with its lower bond order. The single unpaired electron left in $\sigma_{2p}$ also makes $\text{N}_2^{+}$ paramagnetic, in contrast to diamagnetic neutral $\text{N}_2$; the characteristic blue emission of the aurora's nitrogen-ion band is, in fact, this very ion relaxing from an excited electronic state.

Compare this with the $\text{O}_2$ family of [Problem 6](#ex-molecular-structure-6): there, removing an electron instead comes from the *antibonding* $\pi_{2p}^{*}$ orbital, which *strengthens* the bond rather than weakening it, because $\text{O}_2$'s highest-occupied orbital is antibonding while $\text{N}_2$'s is bonding. The same operation — ionization, removing one electron — can strengthen or weaken a bond depending entirely on the character of the specific orbital the electron is removed from, information only the molecular orbital diagram supplies and that a Lewis structure alone cannot.

## Intermolecular Forces and Molecular Spectra

### Intermolecular Forces

Everything so far in this chapter describes **intramolecular** forces — the bonds that hold the atoms of a single molecule together, whether ionic, covalent, or described by a molecular orbital diagram. Bulk matter — liquids and solids made of many molecules — depends just as much on much weaker **intermolecular forces**, the attractions *between* separate, already-bonded molecules. These forces are typically one to two orders of magnitude weaker than a covalent bond (tens of $\text{kJ/mol}$, rather than hundreds), but they are exactly what must be overcome to melt a solid or boil a liquid, and their strength — not the strength of the covalent bonds within each molecule, which survive melting and boiling completely intact — is what actually sets a substance's melting and boiling points.

**London dispersion forces** act between *every* pair of molecules, regardless of polarity. A molecule's electron cloud fluctuates from instant to instant, producing a fleeting, temporary dipole moment even in a molecule with no permanent dipole at all; that instantaneous dipole induces a matching temporary dipole in a neighboring molecule, and the two weakly attract. Dispersion forces strengthen with a molecule's **polarizability** — how easily its electron cloud is distorted — which in turn grows with the number of electrons and the physical size of the molecule, which is why boiling points climb steadily up a family of increasingly large nonpolar molecules (the noble gases, or the halogens) even though none of them has a permanent dipole moment at all.

**Dipole–dipole forces** act between molecules that already carry a *permanent* dipole moment (recall {numref}`Figure %s <fig:ch12-polarity-sim>`, above): the positive end of one polar molecule is attracted to the negative end of its neighbor. Because this attraction does not have to wait on a random fluctuation, it is generally stronger, molecule for molecule, than a dispersion-only attraction between molecules of comparable size.

**Hydrogen bonding** is an unusually strong special case of dipole–dipole attraction, occurring specifically when a hydrogen atom is bonded directly to a small, highly electronegative atom — nitrogen, oxygen, or fluorine — leaving that hydrogen with a large, concentrated partial positive charge (it has essentially no core electrons of its own to shield its bare proton) that is then strongly attracted to a lone pair on an N, O, or F atom of a neighboring molecule. Hydrogen bonds are typically five to ten times stronger than an ordinary dipole–dipole attraction, though still far weaker than a covalent bond, and are responsible for water's unusually high boiling point, the double-helix structure of DNA (hydrogen bonds between complementary base pairs), and the open crystal structure that makes ice less dense than the liquid water it floats on.

#### Worked Example: Dispersion versus Dipole–Dipole — Butane and Acetone

Butane ($\text{C}_4\text{H}_{10}$, nonpolar, molar mass $58.1\ \text{g/mol}$) and acetone ($\text{C}_3\text{H}_6\text{O}$, polar, molar mass $58.1\ \text{g/mol}$) have essentially identical molar mass — and therefore comparable numbers of electrons, comparable polarizability, and hence comparable London dispersion forces — yet butane boils at $-1°\text{C}$ while acetone boils at $56°\text{C}$, a difference of $57$ Celsius degrees. Since dispersion forces are approximately equal for the two molecules, the entire difference must come from an attraction dispersion forces alone cannot supply: acetone's carbonyl group ($\text{C=O}$) carries a substantial permanent dipole moment (about $2.9\ \text{D}$), giving it dipole–dipole attractions that butane, with no permanent dipole at all, simply lacks. Holding molecular size (and hence dispersion strength) roughly fixed isolates dipole–dipole attraction as the deciding factor.

The same logic, pushed one step further, isolates hydrogen bonding specifically. Water ($\text{H}_2\text{O}$, molar mass $18\ \text{g/mol}$) boils at $100°\text{C}$, while hydrogen sulfide ($\text{H}_2\text{S}$, molar mass $34\ \text{g/mol}$, the next member down the same column of the periodic table) boils at $-60°\text{C}$ — even though the *heavier*, more polarizable $\text{H}_2\text{S}$ should, by dispersion forces alone, boil *higher* than water, not lower. Water's anomalously high boiling point is the signature of hydrogen bonding: each water molecule can form up to four hydrogen bonds (two through its own hydrogens, two through its oxygen's lone pairs), building an extended three-dimensional network that an ordinary dipole–dipole liquid like $\text{H}_2\text{S}$ — whose S–H bond is too weakly polar for effective hydrogen bonding — never forms.

### Vibrational and Rotational Energy Levels

:::{note} Why Electrons and Nuclei Can Be Treated Separately: The Born–Oppenheimer Approximation
Every molecular orbital diagram and hybridization argument earlier in this chapter implicitly treats the nuclei as fixed in place while the electrons rearrange around them, and the analysis that follows now treats the nuclei as vibrating and rotating about a bond length $r_0$ taken as already known, with no further reference to the electrons at all. This split is justified by the **Born–Oppenheimer approximation**, proposed by Max Born and J. Robert Oppenheimer in 1927: because a nucleus is thousands of times more massive than an electron (a lone proton alone outweighs an electron by a factor of about $1836$), the electrons respond to any change in nuclear position essentially instantaneously on the timescale of nuclear motion. The electronic structure problem can therefore be solved first, at each fixed internuclear separation, to obtain an effective potential energy curve for the nuclei — precisely the curve plotted in {numref}`Figure %s <fig:ch12-interatomic-sim>` below — after which the vibration and rotation of the nuclei on that curve become a separate, subsequent problem. Without this approximation, the full molecular Schrödinger equation, coupling every electron's motion to every nucleus's motion at once, would be intractable for all but the smallest molecules.
:::

Once bonded, a diatomic molecule is itself a quantum system with its own internal energy levels, in addition to the electronic energy levels associated with its bonding orbitals. Near the equilibrium bond length $r_0$ (where the molecular potential energy curve, as a function of internuclear separation, has its minimum), the potential is well approximated by a parabola, so small-amplitude **vibration** of the two nuclei about $r_0$ is, to good approximation, the quantum harmonic oscillator of [Chapter 8](#ch-the-schrodinger-equation), with quantized energies

$$
E_v = \left(v + \tfrac12\right)\hbar\omega, \qquad v = 0, 1, 2, \ldots,
$$

where $\omega = \sqrt{k/\mu}$, $k$ is the effective "spring constant" of the bond (obtained from the curvature of the potential at its minimum), and $\mu = m_1m_2/(m_1+m_2)$ is the **reduced mass** of the two-nucleus system (the appropriate effective mass for relative motion of a two-body system, reducing the two-body vibration problem to an equivalent single-particle problem).

The parabola is an approximation, and it is useful to see what it approximates. {numref}`Figure %s <fig:ch12-interatomic-sim>` plots the interatomic potential energy of a diatomic pair as a function of separation: strongly repulsive at short range, attractive at long range, with a minimum at $r_0$ whose depth is the bond energy and whose curvature is the $k$ in $\omega = \sqrt{k/\mu}$. Pull the atoms far from $r_0$ and the curve is visibly not a parabola — it flattens out toward dissociation on one side and rises much faster than quadratically on the other — which is why real molecular vibrational levels crowd together at high $v$ instead of staying evenly spaced at $\hbar\omega$.

```{phet} atomic-interactions
:label: fig:ch12-interatomic-sim

The potential energy curve between two atoms, with the atom types adjustable. The equilibrium separation, the well depth, and the curvature at the minimum are the bond length, the bond energy, and the vibrational spring constant respectively.
```

Independently, the molecule can **rotate** about its center of mass; treating the two nuclei as point masses at fixed separation $r_0$ (the **rigid rotor** approximation, reasonable when rotational energies are small compared to vibrational spacing) makes this exactly the angular-momentum problem of [Chapter 9](#ch-quantum-mechanics-in-three-dimensions), with quantized rotational energy

$$
E_J = \frac{\hbar^2}{2I}J(J+1), \qquad J = 0, 1, 2, \ldots,
$$

where $I = \mu r_0^2$ is the molecule's moment of inertia and $J$ plays the role of the orbital angular momentum quantum number $\ell$. Because $I$ for a typical molecule is large (bond lengths of order $10^{-10}\ \text{m}$, but heavy nuclear masses) compared to the effective "moment of inertia" scale set by an electron, rotational energy spacings are much smaller than vibrational spacings, which are in turn much smaller than electronic transition energies — a hierarchy ($E_{\text{elec}} \gg E_{\text{vib}} \gg E_{\text{rot}}$) that is directly reflected in molecular spectra: electronic transitions lie in the visible/ultraviolet, vibrational transitions in the infrared, and pure rotational transitions in the microwave region, each region probing a different aspect of molecular structure.

This hierarchy is not merely a table of numbers; it is why a molecule responds to one part of the spectrum and ignores another, and {numref}`Figure %s <fig:ch12-molecules-light-sim>` lets it be tested one photon at a time. Aim microwaves at a molecule and it rotates. Switch to infrared and it starts to vibrate — but only if the vibration changes the molecule's dipole moment, which is why $\text{N}_2$ and $\text{O}_2$ are transparent in the infrared while $\text{CO}_2$ and $\text{H}_2\text{O}$ are not, and hence why the two minor constituents of the atmosphere, not the two major ones, set the temperature of the planet. Go to the ultraviolet and the molecule breaks apart, the electronic energy scale having been reached at last.

```{phet} molecules-and-light
:label: fig:ch12-molecules-light-sim

Single photons of a chosen wavelength directed at a chosen molecule. Microwave, infrared, visible, and ultraviolet photons each produce a different response — rotation, vibration, electronic excitation, or dissociation — in the order of the $E_{\text{elec}} \gg E_{\text{vib}} \gg E_{\text{rot}}$ hierarchy.
```

#### The Rovibrational Spectrum: Vibration and Rotation Together

A real infrared absorption spectrum does not show the vibrational transition as a single line at $\hbar\omega$. Because a molecule is simultaneously vibrating *and* rotating, a photon absorbed in a vibrational transition ($\Delta v = +1$) is generally accompanied by a simultaneous change in rotational state, subject to the selection rule

$$
\Delta J = \pm 1
$$

(for a diatomic molecule, whose single vibrational mode necessarily oscillates the dipole moment along the bond axis itself, quantum-mechanical selection rules for this type of vibration forbid $\Delta J = 0$ — the analog of a missing $Q$ branch — leaving only $\Delta J = \pm 1$ available; some polyatomic vibrations that shift the dipole moment perpendicular to a molecular symmetry axis do permit a weak $Q$ branch, but a diatomic never has that option). Writing the combined vibration–rotation energy as $E_{v,J} = \left(v+\tfrac12\right)\hbar\omega + BJ(J+1)$, with the **rotational constant** $B \equiv \hbar^2/2I$ (an energy, in the convention used throughout this chapter), the photon energy absorbed in a transition from $(v=0,J)$ to $(v=1,J')$ is

$$
h\nu = \hbar\omega + B\big[J'(J'+1) - J(J+1)\big].
$$

Two families of lines result, sketched in {numref}`Figure %s <fig:ch12-rovibrational>`. The **R branch** ($\Delta J = +1$, $J'=J+1$) works out to $h\nu = \hbar\omega + 2B(J+1)$ for $J=0,1,2,\ldots$, giving lines above $\hbar\omega$ spaced by $2B$. The **P branch** ($\Delta J = -1$, $J'=J-1$) works out to $h\nu = \hbar\omega - 2BJ$ for $J=1,2,3,\ldots$, giving lines below $\hbar\omega$, also spaced by $2B$. No line appears at $h\nu = \hbar\omega$ itself — that would be the forbidden $\Delta J=0$ **Q branch** — leaving a characteristic gap of about $4B$ at the center of the band, a gap that is itself a direct, measurable signature of the selection rule.

```{figure} ../images/ch12-rovibrational-spectrum.svg
:label: fig:ch12-rovibrational
:alt: Stick spectrum of a rovibrational absorption band, showing a P branch of lines below the band origin and an R branch above it, each spaced by 2B, with a gap at the band origin where the forbidden Q branch would fall.

A rovibrational absorption band. The $R$ branch ($\Delta J=+1$) and $P$ branch ($\Delta J=-1$) each consist of lines spaced by $2B$; the missing $Q$ branch ($\Delta J=0$, forbidden for a diatomic) leaves a gap of about $4B$ at the band origin. Line intensities (schematic here) track the thermal population of each rotational level before absorption.
```

Because $B$ depends only on the molecule's moment of inertia, measuring the line spacing in a single rovibrational (infrared) spectrum determines $I$ — and hence the bond length $r_0$ — directly, without needing a separate microwave (pure-rotation) measurement at all.

:::{margin}
A **wavenumber**, $\tilde\nu \equiv E/hc$, reports energy in units of $\text{cm}^{-1}$ — the number of wave cycles per centimeter for a photon of that energy. It is the conventional unit throughout infrared and microwave spectroscopy, chosen because a spectrometer directly measures wavelength or frequency, not joules.
:::

#### Worked Example: Line Spacing in the CO Rovibrational Spectrum

Using the same carbon monoxide data as [Problem 5](#ex-molecular-structure-5) ($r_0 = 0.113\ \text{nm}$, $\mu = 6.86\ \text{u}$), find the rotational constant $B$ and the resulting rovibrational line spacing.

The moment of inertia is

$$
I = \mu r_0^2 = (6.86)(1.66\times10^{-27}\ \text{kg})(0.113\times10^{-9}\ \text{m})^2 = 1.45\times10^{-46}\ \text{kg}\cdot\text{m}^2,
$$

so

$$
B = \frac{\hbar^2}{2I} = \frac{(1.055\times10^{-34}\ \text{J}\cdot\text{s})^2}{2(1.45\times10^{-46}\ \text{kg}\cdot\text{m}^2)} = 3.82\times10^{-23}\ \text{J} = 2.39\times10^{-4}\ \text{eV}.
$$

Both branches are spaced by $2B = 4.77\times10^{-4}\ \text{eV}$ — the same energy as the $J=0\to J=1$ pure rotational transition of [Problem 5](#ex-molecular-structure-5), as it must be, since both quantities are just $2B$ measured two different ways. Converting to the wavenumber units ($\tilde\nu \equiv E/hc$) conventional in infrared spectroscopy,

$$
\tilde{B} = \frac{B}{hc} = \frac{3.82\times10^{-23}\ \text{J}}{(6.626\times10^{-34}\ \text{J}\cdot\text{s})(2.998\times10^{10}\ \text{cm/s})} = 1.93\ \text{cm}^{-1},
$$

so the predicted line spacing is $2\tilde{B} = 3.85\ \text{cm}^{-1}$ — in excellent agreement with the spacing of about $3.86\ \text{cm}^{-1}$ actually observed in the CO fundamental infrared band. A bond length and a reduced mass, fed into a formula derived from nothing more than the rigid-rotor approximation, correctly predict the fine structure of a real molecular spectrum.

#### Anharmonicity Revisited

{numref}`Figure %s <fig:ch12-interatomic-sim>`, above, already showed that the true interatomic potential is not a perfect parabola: it rises more steeply than quadratic at short range (the repulsive wall) and flattens out well below quadratic at long range, approaching the dissociation energy asymptotically rather than climbing forever. A more realistic potential — the **Morse potential** is the standard choice for modeling this curve quantitatively — gives vibrational energy levels that are no longer *exactly* evenly spaced:

$$
E_v \approx \left(v+\tfrac12\right)\hbar\omega - \left(v+\tfrac12\right)^2 x_e\hbar\omega, \qquad v = 0, 1, 2, \ldots,
$$

where the small, positive **anharmonicity constant** $x_e$ (typically a few percent, for real molecules) quantifies the departure from a perfect harmonic oscillator. The negative correction term grows with $v$, so **the levels crowd closer together at higher $v$** — an effect invisible near the bottom of the well, where the potential is well approximated by the parabola of the harmonic-oscillator treatment above, but increasingly important as $v$ climbs toward the dissociation limit, where the level spacing shrinks to zero exactly at the molecule's bond dissociation energy. Anharmonicity also relaxes the strict $\Delta v = \pm 1$ selection rule of the ideal harmonic oscillator, permitting weak **overtone** transitions with $\Delta v = \pm2, \pm3, \ldots$ — additional, much fainter absorption lines at roughly (but not exactly) integer multiples of the fundamental frequency. This is why a real vibrational spectrum shows one strong fundamental band accompanied by a series of progressively weaker overtones, rather than the single, perfectly sharp line the ideal harmonic oscillator of [Chapter 8](#ch-the-schrodinger-equation) would predict.

:::{seealso} A Bound System Weighs Less Than Its Parts, Again
A bond's dissociation energy — the energy needed to pull two bonded atoms apart to infinite separation — is the molecular-scale instance of a pattern that reappears, at a vastly different energy and length scale, when the same nuclei are pulled apart from *within*. See [](#ch-nuclear-physics) for the nuclear binding energy, where the same logic (a bound system has lower total energy, and hence lower total mass, than its separated constituents) explains why nuclei resist being split or fused apart, on a scale of $\text{MeV}$ rather than $\text{kJ/mol}$.
:::

## Summary

- Chemical bonds lower a molecule's total energy relative to separated atoms; **ionic bonding** (electron transfer, electrostatic attraction) and **covalent bonding** (shared electron pairs, enhanced internuclear electron density) are limiting cases of a continuum set by electronegativity difference.
- **Valence bond theory** builds bonds from overlapping atomic orbitals ($\sigma$ for direct, $\pi$ for sideways overlap); **hybrid orbitals** ($sp$, $sp^2$, $sp^3$, etc.), one set per number of electron domains, reproduce observed molecular geometries via minimization of electron-pair repulsion.
- **Molecular orbital theory** builds orbitals belonging to the whole molecule as linear combinations of atomic orbitals, splitting into lower-energy **bonding** and higher-energy **antibonding** orbitals; filling these with the molecule's electrons gives the **bond order**, which predicts stability, bond strength, and (via unpaired electrons) paramagnetism — correctly predicting, e.g., $\text{O}_2$'s paramagnetism and $\text{He}_2$'s nonexistence.
- A bonded diatomic molecule has quantized **vibrational** levels, $E_v=(v+\tfrac12)\hbar\omega$ (harmonic oscillator in the reduced mass $\mu$), and **rotational** levels, $E_J = \hbar^2J(J+1)/2I$ (rigid rotor), with $E_{\text{elec}}\gg E_{\text{vib}}\gg E_{\text{rot}}$, placing electronic, vibrational, and rotational spectra in the UV/visible, infrared, and microwave regions respectively.
- The **$\sigma_{2p}/\pi_{2p}$ ordering inverts** between light second-row diatomics ($\text{B}_2$–$\text{N}_2$, $\pi_{2p}$ lower via strong $s$–$p$ mixing) and heavier ones ($\text{O}_2$–$\text{Ne}_2$, $\sigma_{2p}$ lower); higher bond order predicts a shorter, stronger bond, confirmed across N–N single/double/triple bonds and by ionizing $\text{N}_2$, $\text{O}_2$, and $\text{F}_2$.
- **Intermolecular forces** — London dispersion (universal, grows with polarizability), dipole–dipole (permanent dipoles), and **hydrogen bonding** (an unusually strong dipole–dipole interaction specific to H bonded to N, O, or F) — act *between* already-bonded molecules and set melting and boiling points; comparing molecules of similar size isolates each contribution.
- A **rovibrational spectrum** combines a vibrational transition with a simultaneous rotational one, producing $R$-branch ($\Delta J=+1$) and $P$-branch ($\Delta J=-1$) lines spaced by $2B=\hbar^2/I$, with a missing central $Q$ branch ($\Delta J=0$, forbidden for a diatomic); **anharmonicity** of the real interatomic potential crowds vibrational levels together at high $v$ and permits weak overtone transitions.

## Problems

:::{exercise}
:label: ex-molecular-structure-1

Determine the hybridization of the central atom and predict the molecular geometry for (a) $\text{NH}_3$ (three bonding pairs, one lone pair on N), (b) $\text{CO}_2$ (two double bonds, no lone pairs on C), (c) $\text{SF}_6$.
:::

:::{solution} ex-molecular-structure-1
:label: sol-molecular-structure-1
:class: dropdown

VSEPR counts electron domains.  Ammonia has four domains, so nitrogen is $sp^3$ hybridized; one lone pair makes its molecular geometry trigonal pyramidal.  Carbon dioxide has two domains, so carbon is $sp$ hybridized and the molecule is linear.  Sulfur hexafluoride has six domains, so sulfur is $sp^3d^2$ hybridized with octahedral geometry.

```{figure} ../images/ch12-sol-vsepr-shapes.svg
:label: fig:ch12-sol-vsepr-shapes
:alt: Three ball-and-stick sketches: ammonia as a trigonal pyramid with a lone pair, carbon dioxide as a straight line, and sulfur hexafluoride as an octahedron with six bonds around the central atom.

Electron-domain count alone fixes the shape: four domains (one a lone pair) bends $\text{NH}_3$ into a pyramid, two domains keep $\text{CO}_2$ straight, and six domains spread $\text{SF}_6$'s bonds into an octahedron.
```

Therefore, the predicted geometries are trigonal pyramidal for $\text{NH}_3$, linear for $\text{CO}_2$, and octahedral for $\text{SF}_6$.
:::

:::{exercise}
:label: ex-molecular-structure-2

Construct the molecular orbital diagram for the nitrogen molecule $\text{N}_2$ (14 electrons total; consider only the valence $2s$ and $2p$ electrons, 10 of the 14, filling $\sigma_{2s}, \sigma_{2s}^*, \pi_{2p}$ (×2), $\sigma_{2p}$ in the order relevant for $\text{N}_2$). Determine the bond order and compare it to the triple bond expected from the Lewis structure $:\text{N}\!\equiv\!\text{N}:$.
:::

:::{solution} ex-molecular-structure-2
:label: sol-molecular-structure-2
:class: dropdown

The ten valence electrons fill

$$\sigma_{2s}^2\,\sigma_{2s}^{*2}\,(\pi_{2p})^4\,\sigma_{2p}^2.$$

There are $8$ bonding and $2$ antibonding electrons, so

$$\text{bond order}=\frac{8-2}{2}=3.$$

This is exactly the filled diagram drawn in {numref}`Figure %s <fig:ch12-mo-n2-o2>`.  Therefore, MO theory predicts bond order $3$ for $\text{N}_2$, agreeing with the triple bond in the Lewis structure.
:::

:::{exercise}
:label: ex-molecular-structure-3

Using the same style of reasoning applied to $\text{H}_2$ and $\text{He}_2$ in the text, determine the bond order predicted by MO theory for the hypothetical ion $\text{He}_2^+$ (three electrons: two in $\sigma_{1s}$, one in $\sigma_{1s}^*$), and state whether this ion is predicted to be (marginally) stable.
:::

:::{solution} ex-molecular-structure-3
:label: sol-molecular-structure-3
:class: dropdown

For $\text{He}_2^+$, two electrons occupy bonding $\sigma_{1s}$ and one occupies antibonding $\sigma_{1s}^*$.  Thus

$$\text{bond order}=\frac{N_b-N_a}{2}=\frac{2-1}{2}=\frac12.$$

```{figure} ../images/ch12-sol-he2-plus-mo.svg
:label: fig:ch12-sol-he2-plus-mo
:alt: Molecular orbital diagram for helium-2-plus, with two electrons filling the bonding sigma-1s orbital and one electron in the antibonding sigma-1s-star orbital.

Two bonding electrons and one antibonding electron leave a net half a bond — weaker than $\text{H}_2$'s full bond, but not zero like neutral $\text{He}_2$.
```

Therefore, $\text{He}_2^+$ is predicted to have a weak, marginally stable half-order bond.
:::

:::{exercise}
:label: ex-molecular-structure-4

The HCl molecule has an effective vibrational frequency $f = \omega/2\pi = 8.66\times10^{13}\ \text{Hz}$. Using $m_{\text{H}} = 1.008\ \text{u}$ and $m_{\text{Cl}} = 35.45\ \text{u}$ ($1\ \text{u} = 1.66\times10^{-27}\ \text{kg}$), compute (a) the reduced mass $\mu$, and (b) the zero-point vibrational energy $E_0 = \tfrac12\hbar\omega$ in eV.
:::

:::{solution} ex-molecular-structure-4
:label: sol-molecular-structure-4
:class: dropdown

The reduced mass is

$$\mu=\frac{m_{\rm H}m_{\rm Cl}}{m_{\rm H}+m_{\rm Cl}}=\frac{(1.008)(35.45)}{1.008+35.45}\ \text{u}=0.980\ \text{u}=1.63\times10^{-27}\ \text{kg}.$$

With $\omega=2\pi f=2\pi(8.66\times10^{13}\ \text{s}^{-1})$,

$$E_0=\frac12\hbar\omega=\frac12(1.055\times10^{-34}\ \text{J s})(5.44\times10^{14}\ \text{s}^{-1})=2.87\times10^{-20}\ \text{J}=0.179\ \text{eV}.$$

Therefore, HCl has reduced mass $1.63\times10^{-27}\ \text{kg}$ and zero-point vibrational energy $0.179\ \text{eV}$.
:::

:::{exercise}
:label: ex-molecular-structure-5

The CO molecule has bond length $r_0 = 0.113\ \text{nm}$ and reduced mass $\mu = 6.86\ \text{u}$. Compute (a) its moment of inertia $I = \mu r_0^2$, and (b) the energy (in units of $10^{-4}\ \text{eV}$) of the $J=0\to J=1$ rotational transition.
:::

:::{solution} ex-molecular-structure-5
:label: sol-molecular-structure-5
:class: dropdown

First convert $\mu=6.86\ \text{u}=1.139\times10^{-26}\ \text{kg}$ and $r_0=0.113\ \text{nm}=1.13\times10^{-10}\ \text{m}$.  Then

$$I=\mu r_0^2=(1.139\times10^{-26})(1.13\times10^{-10})^2=1.45\times10^{-46}\ \text{kg m}^2.$$

For $J=0\to1$, $\Delta E=\hbar^2/I$:

$$\Delta E=\frac{(1.055\times10^{-34}\ \text{J s})^2}{1.45\times10^{-46}\ \text{kg m}^2}=7.68\times10^{-23}\ \text{J}=4.79\times10^{-4}\ \text{eV}.$$

Therefore, CO has $I=1.45\times10^{-46}\ \text{kg m}^2$ and its first rotational transition has energy $4.79\times10^{-4}\ \text{eV}$, or $4.79$ in units of $10^{-4}\ \text{eV}$.
:::

:::{exercise}
:label: ex-molecular-structure-6

Explain, using the concept of bond order, why $\text{O}_2^-$ (superoxide, one more electron than $\text{O}_2$) has a weaker, longer bond than neutral $\text{O}_2$, while $\text{O}_2^+$ (dioxygenyl, one fewer electron) has a stronger, shorter bond — referring to which type of orbital (bonding or antibonding) the added or removed electron occupies.
:::

:::{solution} ex-molecular-structure-6
:label: sol-molecular-structure-6
:class: dropdown

The highest occupied orbitals of $\text{O}_2$ are antibonding $\pi_{2p}^*$ orbitals.  Adding an electron to make $\text{O}_2^-$ raises the antibonding count and lowers bond order by $\tfrac12$; removing one to make $\text{O}_2^+$ lowers the antibonding count and raises bond order by $\tfrac12$ — the same $\pi_{2p}^*$ level marked in {numref}`Figure %s <fig:ch12-mo-n2-o2>`'s $\text{O}_2$ diagram is where both changes happen.  Therefore, superoxide has a weaker, longer bond, whereas dioxygenyl has a stronger, shorter bond.
:::

:::{exercise}
:label: ex-molecular-structure-7

Determine the hybridization of the central atom and predict the molecular geometry of $\text{SF}_4$ (four bonding pairs and one lone pair on S). Sketch, in words, where the lone pair sits relative to the five electron domains of the underlying trigonal-bipyramidal arrangement, and state the resulting molecular geometry. Compare your reasoning to the $\text{XeF}_4$ worked example above: why does one lone pair produce a very different-looking molecule than two lone pairs do?
:::

:::{solution} ex-molecular-structure-7
:label: sol-molecular-structure-7
:class: dropdown

$\text{SF}_4$ has five electron domains, so sulfur uses $sp^3d$ hybridization and has trigonal-bipyramidal electron-domain geometry.  A lone pair preferentially occupies an equatorial site, where it has only two $90^\circ$ interactions rather than three.  The four atoms then form a seesaw geometry.

```{figure} ../images/ch12-sol-sf4-xef4.svg
:label: fig:ch12-sol-sf4-xef4
:alt: Side-by-side sketches of SF4 as a seesaw shape with one equatorial lone pair, and XeF4 as a square planar shape with two lone pairs perpendicular to the plane of the four fluorine atoms.

One equatorial lone pair pushes $\text{SF}_4$'s four bonds into a lopsided seesaw; a second lone pair, forced to the opposite axial position, symmetrizes the remaining four bonds into a flat square.
```

Therefore, one equatorial lone pair gives $\text{SF}_4$ a seesaw shape, whereas two lone pairs in $\text{XeF}_4$ occupy both axial-equivalent arrangements that leave a square planar molecular shape.
:::

:::{exercise}
:label: ex-molecular-structure-8

Using the same reasoning applied to $\text{N}_2$/$\text{N}_2^+$ in the text and to $\text{O}_2$/$\text{O}_2^{\pm}$ in [Problem 6](#ex-molecular-structure-6), construct the molecular orbital diagram for neutral $\text{F}_2$ (14 valence electrons, heavier-diatomic ordering: $\sigma_{2s}, \sigma_{2s}^*, \sigma_{2p}, \pi_{2p}\,(\times2), \pi_{2p}^*\,(\times2), \sigma_{2p}^*$), and determine its bond order. Then remove one electron to form $\text{F}_2^+$, identify which orbital it comes from, and state whether the ion's bond is predicted to be stronger or weaker (and shorter or longer) than neutral $\text{F}_2$'s, and whether the ion is paramagnetic or diamagnetic.
:::

:::{solution} ex-molecular-structure-8
:label: sol-molecular-structure-8
:class: dropdown

The fourteen valence electrons fill

$$\sigma_{2s}^2\sigma_{2s}^{*2}\sigma_{2p}^2(\pi_{2p})^4(\pi_{2p}^*)^4.$$

Thus $N_b=8$ and $N_a=6$, giving bond order $(8-6)/2=1$.  Ionization removes an electron from the highest, antibonding $\pi_{2p}^*$ level, so $\text{F}_2^+$ has bond order $1.5$.  One unpaired electron remains in $\pi_{2p}^*$.

```{figure} ../images/ch12-sol-f2-mo-diagram.svg
:label: fig:ch12-sol-f2-mo-diagram
:alt: Side-by-side molecular orbital diagrams for F2 and F2-plus, with F2 having all orbitals through pi-2p-star fully paired and F2-plus missing one electron from the antibonding pi-2p-star level, leaving it unpaired.

Removing one electron from an antibonding level does double duty: it raises the bond order from $1$ to $1.5$ and leaves one $\pi_{2p}^*$ electron unpaired, making $\text{F}_2^+$ paramagnetic where neutral $\text{F}_2$ is not.
```

Therefore, neutral $\text{F}_2$ has a single bond, while $\text{F}_2^+$ is paramagnetic and has a stronger, shorter bond.
:::

:::{exercise}
:label: ex-molecular-structure-9

Using the reduced mass $\mu$ found in [Problem 4](#ex-molecular-structure-4)(a) for HCl and a bond length $r_0 = 127.5\ \text{pm}$, find (a) the moment of inertia $I$, (b) the rotational constant $B$ in eV, (c) the rovibrational line spacing $2B$ in $\text{cm}^{-1}$, and (d) the size of the gap (in $\text{cm}^{-1}$) at the band origin left by the missing $Q$ branch.
:::

:::{solution} ex-molecular-structure-9
:label: sol-molecular-structure-9
:class: dropdown

Using $\mu=1.63\times10^{-27}\ \text{kg}$ from Problem 4 and $r_0=127.5\ \text{pm}=1.275\times10^{-10}\ \text{m}$,

$$I=\mu r_0^2=2.65\times10^{-47}\ \text{kg m}^2,$$

$$B=\frac{\hbar^2}{2I}=2.10\times10^{-22}\ \text{J}=1.31\times10^{-3}\ \text{eV}.$$

The wavenumber $B/(hc)=10.6\ \text{cm}^{-1}$, so adjacent rovibrational lines are $2B/(hc)=21.2\ \text{cm}^{-1}$ apart.  The missing $Q$ branch leaves a central gap of $2(2B/hc)=42.4\ \text{cm}^{-1}$ between the nearest $P$ and $R$ lines — the same structure {numref}`Figure %s <fig:ch12-rovibrational>` draws in general, with HCl's own numbers filled in.  Therefore, HCl has the stated moment of inertia, $B=1.31\times10^{-3}\ \text{eV}$, $21.2\ \text{cm}^{-1}$ line spacing, and a $42.4\ \text{cm}^{-1}$ central gap.
:::

:::{exercise}
:label: ex-molecular-structure-10

The boiling points of the halogens rise steadily down the group: $\text{F}_2$, $-188°\text{C}$; $\text{Cl}_2$, $-34°\text{C}$; $\text{Br}_2$, $59°\text{C}$; $\text{I}_2$, $184°\text{C}$. All four are nonpolar diatomic molecules with zero permanent dipole moment. Explain this trend using London dispersion forces, and state what physical property of the molecule is chiefly responsible for it.
:::

:::{solution} ex-molecular-structure-10
:label: sol-molecular-structure-10
:class: dropdown

All four halogens are nonpolar, so their rising boiling points are not caused by permanent dipoles.  Down the group, the electron cloud contains more electrons and is larger and more easily distorted; its polarizability increases.  Stronger instantaneous induced dipoles then give stronger London dispersion forces and require more thermal energy to separate molecules.  Therefore, the rising boiling points are caused chiefly by increasing molecular polarizability (and associated electron-cloud size).
:::
