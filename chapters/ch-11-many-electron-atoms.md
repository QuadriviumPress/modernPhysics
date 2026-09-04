---
title: Many-Electron Atoms
short_title: Chapter 11. Many-Electron Atoms
label: ch-many-electron-atoms
numbering:
  enumerator: "11.%s"
  heading_2: true
---

### Learning Objectives

By the end of this chapter, you should be able to:

- State the Pauli exclusion principle and explain its role in determining atomic structure.
- Explain why the energy of a state in a multi-electron atom depends on both $n$ and $\ell$, unlike in hydrogen, using the concept of electron screening.
- Write the ground-state electron configuration of a given element using the subshell-filling order and Hund's rule.
- Relate the structure of the periodic table (periods, groups, blocks) to electron configurations.
- Explain the origin of characteristic X-ray spectra and apply Moseley's law.
- Describe the physical basis of the laser: stimulated emission, population inversion, and metastable states.

### Introduction

[Chapter 10](#ch-the-hydrogen-atom) solved the hydrogen atom exactly, obtaining energies that depend on a single quantum number $n$ and states that can be filled with electrons two at a time (spin up, spin down) up to a degeneracy of $2n^2$. This chapter asks what happens for atoms with more than one electron, where the Schrödinger equation cannot be solved exactly, because each electron interacts not only with the nucleus but with every other electron. Two ideas make the many-electron problem tractable and explain the entire structure of the periodic table: an *independent-particle approximation*, in which each electron is imagined to move in an effective, average potential created by the nucleus and all the other electrons, and the *Pauli exclusion principle*, a rule with no classical analog that limits how many electrons can occupy any single quantum state. Together they explain why elements have the chemical and spectroscopic properties they do — and, in doing so, resolve one of the oldest puzzles in physics that quantum mechanics was built to explain: the periodic table itself.

## The Exclusion Principle and Screening

### The Pauli Exclusion Principle

Wolfgang Pauli proposed in 1925 (before the discovery of the Schrödinger equation) a rule required to explain observed atomic spectra and, later, understood as a consequence of the fundamentally indistinguishable and antisymmetric nature of electron wave functions: **no two electrons in an atom can occupy the same complete set of quantum numbers** $(n,\ell,m_\ell,m_s)$. Equivalently, each distinct spatial-and-spin quantum state $(n,\ell,m_\ell,m_s)$ can hold **at most one electron**. This is not a subtle statistical tendency but an absolute prohibition, and it applies generally to electrons (and more broadly to the class of particles called fermions, which includes protons and neutrons) — without it, every electron in a multi-electron atom could simply fall into the lowest-energy $1s$ state, and all atoms would have similar, small sizes and similar chemistry, in sharp contradiction to the observed diversity of the periodic table. The exclusion principle is the single most important input, beyond the Schrödinger equation itself, needed to explain atomic structure.

:::{note} Pauli's Nobel Prize — and the Deeper Theorem Behind the Rule
Pauli received the 1945 Nobel Prize in Physics "for the discovery of the Exclusion Principle," on a nomination by Albert Einstein — two decades after the 1925 postulate itself, and a reminder of how long it can take for a rule with no classical mechanism behind it to be fully vindicated. Pauli did not stop at the empirical rule: in 1940 he proved the **spin-statistics theorem**, showing that any relativistic quantum field theory *requires* half-integer-spin particles (fermions, including electrons) to obey antisymmetric statistics and integer-spin particles (bosons, including photons) to obey symmetric statistics. The exclusion principle, in other words, is not a free-standing postulate about electrons specifically — it is a necessary consequence of relativity and quantum field theory applied to any spin-$\tfrac12$ particle.
:::

#### Historical Context: Pauli's Reasoning and Hund's Empirical Rule

Pauli arrived at the exclusion principle in late 1924 by a route that had nothing to do with wave mechanics, which did not yet exist — Schrödinger's equation was still two years away. Working instead from the older Bohr–Sommerfeld quantum theory, Pauli was trying to explain two stubborn regularities that orbital quantum numbers alone could not account for: the precise electron counts (2, 8, 8, 18, $\ldots$) at which successive shells close to give a noble gas, and the "anomalous" Zeeman splitting of certain spectral lines into a number of components inconsistent with any known combination of $n$ and $\ell$. Pauli proposed that the electron carries an additional, two-valued property — which he described, before its physical meaning as spin was proposed by Goudsmit and Uhlenbeck the following year, only as a "classically non-describable two-valuedness" — and that no two electrons in an atom may share an identical set of all their quantum numbers, orbital and this new one included. Both puzzles fell into place at once: the shell-closing numbers became simple counting exercises, and the anomalous splittings became ordinary Zeeman splittings of a spin degree of freedom nobody had previously included.

Hund's rule has a similarly empirical origin. Friedrich Hund formulated it around 1925 not from any first-principles calculation but by systematically cataloging the term symbols (the quantum numbers characterizing the total orbital and spin angular momentum) that best fit the observed ground-state spectra of many atoms, and noticing that the ground state was consistently the one with maximum total spin. Only later, once the Schrödinger equation and the antisymmetry of many-electron wave functions were understood, did it become clear *why*: electrons with parallel spins are already kept apart by the exclusion principle itself (their spatial wave function must be antisymmetric, vanishing whenever two such electrons approach the same point), which lowers their mutual Coulomb repulsion energy compared to electrons of opposite spin occupying the same orbital. This spin-correlated reduction in repulsion is called the **exchange energy**, and it reappears below as the reason certain elements (chromium and copper among them) deviate from the naive Aufbau filling order.

:::{margin}
A **term symbol**, written $^{2S+1}L_J$, packages an atomic state's total spin $S$, total orbital angular momentum $L$ (coded $S,P,D,F,\ldots$ for $L=0,1,2,3,\ldots$), and total angular momentum $J$ into one label; Hund caught the *ground-state* pattern of maximum $S$ among these labels well before anyone could compute them from first principles.
:::

:::{dropdown} The Real Content of the Exclusion Principle: Antisymmetric Wave Functions
Stated as "no two electrons can share the same quantum numbers," the exclusion principle can look like an arbitrary bookkeeping rule bolted onto quantum mechanics. Its actual origin is a deeper and more general statement about *identical particles*: because electrons are fundamentally indistinguishable, swapping the labels of any two electrons in a multi-electron wave function must leave every measurable prediction unchanged, which requires the total wave function to be either symmetric or antisymmetric under that exchange. Experiment (and the spin-statistics theorem) fixes electrons, as spin-$\tfrac12$ fermions, to the antisymmetric choice.

For two electrons in single-particle states $\psi_a$ and $\psi_b$, the properly antisymmetrized two-electron wave function is

$$
\Psi(1,2) = \frac{1}{\sqrt2}\Big[\psi_a(1)\psi_b(2) - \psi_a(2)\psi_b(1)\Big].
$$

Swapping the labels $1 \leftrightarrow 2$ multiplies $\Psi$ by $-1$, as required of a fermion wave function. Now suppose the two states are the same, $a=b$: the expression becomes $\tfrac{1}{\sqrt2}[\psi_a(1)\psi_a(2)-\psi_a(2)\psi_a(1)] = 0$ identically. The wave function for two electrons in the same quantum state does not merely describe an unlikely configuration — it vanishes outright, for every possible position and spin of both electrons. "No two electrons occupy the same state" is not a separate postulate; it is this algebraic fact, stated in words. The same antisymmetry, applied to two electrons in *different* orbitals with parallel spin, is also what produces the exchange energy discussed above: the antisymmetric spatial wave function is forced toward zero whenever the two electrons approach the same point, keeping same-spin electrons farther apart on average and lowering their mutual Coulomb repulsion.
:::

### Screening and Subshell Energies

In hydrogen, the energy of a state depends only on $n$ ([Chapter 10](#ch-the-hydrogen-atom)), because the electron feels the bare $1/r$ potential of a single proton. In a multi-electron atom, an electron in an outer shell is partially **screened** from the full nuclear charge $Ze$ by the electrons in shells closer to the nucleus: it feels an *effective* nuclear charge $Z_{\text{eff}}e < Ze$, reduced from the true charge by the (partial) shielding effect of the intervening electron cloud.

:::{margin}
A **shell** groups states by principal quantum number $n$ alone; a **subshell** further groups by $\ell$ within a shell (e.g., $n=3$ is a shell; $3s$, $3p$, $3d$ are its three subshells). Screening is what makes subshell, not just shell, energy physically meaningful.
:::

Screening depends on $\ell$ as well as $n$, because electrons of lower $\ell$ (at fixed $n$) have wave functions with a greater probability of being found close to the nucleus (their radial probability distributions extend closer to $r=0$, as can be seen in the general shape of the hydrogen radial functions of [Chapter 10](#ch-the-hydrogen-atom)) — such electrons penetrate the inner electron cloud more effectively, feel less screening, and are therefore more tightly bound. The result is that, unlike in hydrogen, **energy in a multi-electron atom depends on both $n$ and $\ell$**, with energy generally increasing with $\ell$ at fixed $n$: within a given $n$, an $s$ state ($\ell=0$) lies lower in energy than a $p$ state ($\ell=1$), which lies lower than a $d$ state ($\ell=2$), and so on. This $\ell$-dependence is what breaks hydrogen's accidental degeneracy and is responsible for the specific subshell-filling order used below.

#### The Self-Consistent Field: How Screening Is Actually Computed

The qualitative picture above — "an electron feels a reduced effective charge $Z_{\text{eff}}e$" — can be made into an actual calculation, and doing so is instructive even though the resulting numbers are only ever approximate. Douglas Hartree, in 1928, proposed treating each electron as moving independently in an *effective, spherically averaged* potential built from the nucleus plus the smeared-out charge distribution of every other electron: $V_{\text{eff}}(r) = -\dfrac{Ze^2}{4\pi\epsilon_0 r} + V_{\text{other electrons}}(r)$. The trouble is circular — computing $V_{\text{other electrons}}(r)$ requires already knowing the wave functions of all the other electrons, which is exactly what one is trying to find. Hartree's resolution, the **self-consistent field (SCF) method**, is an iterative procedure: start with a reasonable guess for every electron's wave function (hydrogen-like orbitals, say); use those guesses to compute an averaged charge density and hence an effective potential $V_{\text{eff}}(r)$ for each electron; solve the resulting one-electron Schrödinger equation for each electron in that potential, obtaining *improved* wave functions; recompute the charge density and the effective potential from these improved wave functions; and repeat. The cycle is stopped once the potential fed in and the potential computed out agree to the desired precision — the field is then "self-consistent," and the resulting energies and wave functions are the Hartree approximation's best estimate for the atom's structure. (A refinement due to Vladimir Fock in 1930, Hartree–Fock theory, additionally enforces the antisymmetry required by the exclusion principle itself, which plain Hartree theory omits, and is the starting point for essentially all modern atomic-structure and quantum-chemistry calculations.)

This procedure makes the $r$-dependence of screening explicit rather than assumed: an electron that penetrates *inside* the charge cloud of the other electrons (small $r$) sees a potential close to the full, unscreened nuclear charge $Z$, while an electron that stays *outside* essentially all the other electrons (large $r$) sees a much-reduced net charge — roughly $Z$ minus the number of electrons enclosed within its orbit. A full SCF calculation is impractical by hand, which is why **Slater's rules** (1930) exist: an empirical, hand-computable recipe, calibrated against Hartree-type results, for estimating a single number $Z_{\text{eff}}$ for a given electron without running the iteration at all.

#### Worked Example: Effective Nuclear Charge via Slater's Rules

Slater's rules group orbitals as $(1s)$, $(2s,2p)$, $(3s,3p)$, $(3d)$, $(4s,4p)$, $\ldots$ and estimate the total screening $S$ felt by an electron in an $ns$ or $np$ orbital as a sum of contributions: $0.35$ for each *other* electron in the same group ($0.30$ if the group is $1s$), $0.85$ for each electron one shell lower ($n-1$), and $1.00$ (full screening) for each electron two or more shells lower. Then $Z_{\text{eff}} = Z - S$.

For the single valence electron of **sodium** ($Z=11$, configuration $1s^22s^22p^63s^1$), the electron of interest is the lone $3s$ electron. There are no other electrons in its $(3s,3p)$ group; the $n=2$ shell contributes $8$ electrons ($2s^22p^6$) at $0.85$ each; the $n=1$ shell contributes $2$ electrons at $1.00$ each:

$$
S = 8(0.85) + 2(1.00) = 6.80 + 2.00 = 8.80, \qquad Z_{\text{eff}} = 11 - 8.80 = 2.20.
$$

For a $3p$ electron of **chlorine** ($Z=17$, configuration $1s^22s^22p^63s^23p^5$), the same-group electrons are the remaining $6$ electrons of $3s^23p^5$ (excluding the one of interest), the $n=2$ shell again contributes $8$ electrons at $0.85$, and the $n=1$ shell contributes $2$ at $1.00$:

$$
S = 6(0.35) + 8(0.85) + 2(1.00) = 2.10 + 6.80 + 2.00 = 10.90, \qquad Z_{\text{eff}} = 17 - 10.90 = 6.10.
$$

Moving across period 3 from sodium to chlorine, the true nuclear charge grows by $6$ protons, but the added electrons (all in the *same* shell) screen each other only weakly ($0.35$ each rather than $0.85$ or $1.00$), so $Z_{\text{eff}}$ very nearly *keeps pace* with $Z$, rising from $2.20$ to $6.10$ — nearly a threefold increase. This is the quantitative content behind the qualitative statement that effective nuclear charge rises sharply across a period, and it is the mechanism explored further below in connection with ionization energy and atomic size.

## Electron Configurations and the Periodic Table

Combining the exclusion principle with the $n$,$\ell$-dependent ordering of subshell energies, the ground-state **electron configuration** of an atom is built by filling the lowest-energy available subshells first, two electrons (spin up and spin down) per orbital, up to $2(2\ell+1)$ electrons per subshell — this is the **Aufbau ("building-up") principle**. Because screening shifts subshell energies, the filling order does not simply follow increasing $n$; the empirical (and largely first-principles-derivable) order is approximately

$$
1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p,\ 6s,\ 4f,\ 5d,\ 6p,\ \ldots
$$

— note, for example, that $4s$ fills before $3d$, since the extra penetration of the $4s$ orbital lowers its energy below that of $3d$ despite its larger $n$. When a subshell contains more than one electron and is only partially filled, **Hund's rule** states that the ground-state configuration maximizes the total spin (electrons singly occupy separate orbitals within a subshell, with parallel spins, before any orbital is doubly occupied) — a consequence of electron-electron repulsion, which is minimized when electrons, to the extent the exclusion principle allows, avoid occupying the same spatial orbital.

:::{margin}
**Core** electrons occupy completely filled inner shells and are chemically inert bystanders; **valence** electrons occupy the outermost, generally unfilled shell and are the ones actually involved in bonding and reactivity.
:::

This filling scheme directly generates the structure of the **periodic table**. Each **period** (row) corresponds to filling a new principal shell $n$; each period ends when a subshell configuration reaches a particularly stable, filled-shell arrangement (a noble gas). Elements in the same **group** (column) share the same outer-shell (**valence**) configuration and, correspondingly, similar chemical properties, since chemical bonding ([Chapter 12](#ch-molecular-structure)) is governed primarily by the valence electrons. The table's division into $s$-block, $p$-block, $d$-block (transition metals), and $f$-block (lanthanides/actinides) regions directly reflects which subshell is being filled across that block. The chemical inertness of the noble gases, the strong reactivity of the alkali metals (a single, loosely bound $s$-electron outside a filled shell) and the halogens (one electron short of a filled shell), and the broad periodicity of atomic size and ionization energy all follow from this shell structure, without further assumptions.

:::{seealso} Pauli Exclusion Beyond Atoms: The Nuclear Shell Model
The exclusion principle is not a special rule about electrons in atoms — it applies to any collection of identical fermions. Protons and neutrons are themselves spin-$\tfrac12$ fermions, and each species independently fills its own sequence of energy levels inside the nucleus subject to the same exclusion principle, producing a shell structure with its own closed-shell "magic numbers" that is strikingly analogous to the noble-gas shell closures described here. See [](#ch-nuclear-physics) for the nuclear shell model built on exactly this idea.
:::

The Aufbau procedure is quicker to learn by doing it than by reading the rules, and {numref}`Figure %s <fig:ch11-build-atom-sim>` is the exercise: add protons, neutrons, and electrons one at a time and watch the element name, the net charge, the mass number, and the shell occupancy update together. Two habits of thought are worth breaking there. Adding a proton changes the element; adding a neutron does not, and only moves the atom along a row of isotopes ([Chapter 13](#ch-nuclear-physics)). And the electrons go into shells that fill in a fixed order, so that the chemistry of the atom is decided by the last few added rather than by the total.

```{phet} build-an-atom
:label: fig:ch11-build-atom-sim

Atoms assembled particle by particle, with element, charge, mass number, and electron shell filling all displayed as they are built. Build up to neon or argon and the outer shell closes exactly as the electron count reaches a noble gas — the closure being a fact about the electrons, and nothing to do with the nucleus underneath them.
```

#### The Aufbau Order in Practice: Configurations Across the Periodic Table

The filling order $1s,2s,2p,3s,3p,4s,3d,4p,\ldots$ is best seen applied across a representative spread of the periodic table, rather than for one or two elements in isolation. {numref}`Table %s <tab:ch11-configurations>` builds ground-state configurations by strict Aufbau filling for most entries, but flags two elements — **chromium** and **copper** — where the real, spectroscopically measured ground state disagrees with the naive prediction, and includes **lanthanum**, the first element for which the $4f$ subshell becomes energetically relevant, as a further illustration of just how close some subshell energies run to one another.

```{table} Ground-state electron configurations across the periodic table, by strict Aufbau filling order.
:label: tab:ch11-configurations

| Element | $Z$ | Naive Aufbau prediction | Actual ground state |
|---|---|---|---|
| Helium | 2 | $1s^2$ | $1s^2$ |
| Neon | 10 | $1s^22s^22p^6$ | $1s^22s^22p^6$ |
| Argon | 18 | $[\text{Ne}]\,3s^23p^6$ | $[\text{Ne}]\,3s^23p^6$ |
| Potassium | 19 | $[\text{Ar}]\,4s^1$ | $[\text{Ar}]\,4s^1$ |
| Calcium | 20 | $[\text{Ar}]\,4s^2$ | $[\text{Ar}]\,4s^2$ |
| Scandium | 21 | $[\text{Ar}]\,3d^14s^2$ | $[\text{Ar}]\,3d^14s^2$ |
| Chromium | 24 | $[\text{Ar}]\,3d^44s^2$ | $[\text{Ar}]\,3d^54s^1$ (exception) |
| Iron | 26 | $[\text{Ar}]\,3d^64s^2$ | $[\text{Ar}]\,3d^64s^2$ |
| Copper | 29 | $[\text{Ar}]\,3d^94s^2$ | $[\text{Ar}]\,3d^{10}4s^1$ (exception) |
| Krypton | 36 | $[\text{Ar}]\,3d^{10}4s^24p^6$ | $[\text{Ar}]\,3d^{10}4s^24p^6$ |
| Lanthanum | 57 | $[\text{Xe}]\,4f^16s^2$ | $[\text{Xe}]\,5d^16s^2$ (exception) |
```

Two features stand out. First, every noble gas ($\text{He}$, $\text{Ne}$, $\text{Ar}$, $\text{Kr}$) ends a row with every subshell up to that point completely filled — the defining structural feature of a noble gas, and the reason the next electron (starting a new period) must go into a new, much less tightly bound shell, exactly the drop in binding responsible for the alkali metals' low ionization energy discussed below. Second, three of the eleven entries in the table are Aufbau *exceptions*, which is a useful reminder that the filling order given earlier in this chapter is a good approximation, not an exact law — the true ordering is whatever a full self-consistent-field calculation (or, in practice, the measured spectrum) says it is, and the mnemonic order is simply the pattern that calculation follows *most* of the time.

:::{tip} Spotting Aufbau Exceptions Before You Look Them Up
The naive Aufbau order gets the ground-state configuration right for the overwhelming majority of elements, so it is worth trusting by default — but it is worth pausing to check whenever straightforward filling would leave a $d$ or $f$ subshell *one electron short* of exactly half-filled ($d^4$, $f^6$) or exactly one electron short of completely filled ($d^9$, $f^{13}$). Those are precisely the configurations where promoting one electron from the outer $s$ subshell buys extra exchange-energy stabilization by reaching $d^5$, $d^{10}$, $f^7$, or $f^{14}$. If your predicted configuration lands one electron short of one of those special counts, it is worth double-checking against a reference table before reporting it as the ground state.
:::

#### Worked Example: Why Chromium's Ground State Breaks the Naive Aufbau Order

The Aufbau order predicts chromium ($Z=24$) should have configuration $[\text{Ar}]\,3d^44s^2$: fill $4s$ completely (it is lower in energy than $3d$, as established above), then place the remaining four electrons in $3d$. The measured ground state is instead $[\text{Ar}]\,3d^54s^1$ — one electron has been promoted from $4s$ down into $3d$, apparently *uphill* in single-particle energy.

The resolution is that single-particle subshell energies are not the whole story; the *total* energy of the atom also includes the electron-electron interaction energy, and that interaction is lower, for a fixed set of occupied orbitals, when as many electrons as possible have parallel spin (the exchange energy discussed in the Historical Context box above). The configuration $3d^54s^1$ places one electron in *each* of the five $3d$ orbitals ($m_\ell = -2,-1,0,1,2$) with parallel spin, plus one further electron in $4s$, aligned with the same spin — six electrons total with parallel spin, versus at most four in the naive $3d^44s^2$ configuration (only four $3d$ orbitals singly occupied, with the fifth $3d$ orbital empty and the $4s$ orbital doubly, oppositely occupied). Six parallel spins generate more pairwise exchange-energy lowering than four, and for chromium specifically that extra lowering outweighs the modest single-particle energy cost of moving one electron from $4s$ up into $3d$. Copper ($Z=29$) is analogous: $[\text{Ar}]\,3d^{10}4s^1$ trades a doubly occupied $4s$ for a completely filled, maximally stable $3d^{10}$ shell (all orbitals doubly occupied — no further exchange gain from that shell alone, but a filled subshell carries its own extra stability, being spherically symmetric and having zero net orbital angular momentum) rather than the naive $3d^94s^2$. Both exceptions occur specifically at *half-filled* ($d^5$) and *completely filled* ($d^{10}$) subshells precisely because those are the two configurations where the parallel-spin/symmetry bookkeeping most favors the promotion.

:::{warning} Exchange Energy Is Not a Classical Force
It is tempting to picture the exchange-energy stabilization behind Hund's rule and the chromium/copper exceptions as electrons with parallel spin somehow "repelling less" because of some spin-dependent force between them, the way two bar magnets attract or repel depending on orientation. That picture is wrong: the electron-electron interaction here is the ordinary electrostatic Coulomb repulsion, and there is no additional spin-based force anywhere in the Hamiltonian. The energy difference is a purely statistical consequence of antisymmetry — the antisymmetric *spatial* wave function required for two parallel-spin electrons is forced toward zero as the two electrons approach each other, so they simply spend less time close together, and therefore have lower average Coulomb repulsion, than two opposite-spin electrons whose (symmetric) spatial wave function carries no such restriction. Same-spin electrons are not pushed apart by a force; they are correlated apart by the requirement of exchange antisymmetry.
:::

#### Ionization Energy and Atomic Radius Across the Periodic Table

The Slater's-rule calculation above — $Z_{\text{eff}}$ rising from $2.20$ (sodium) to $6.10$ (chlorine) across period 3 — is the quantitative content behind two of the most familiar patterns in chemistry. **Atomic radius** decreases across a period: each added electron goes into the *same* shell (same $n$, hence similar average distance from the nucleus, all else equal), while $Z_{\text{eff}}$ pulling on that shell steadily increases, drawing the whole electron cloud inward. **First ionization energy** — the energy required to remove the least tightly bound electron — correspondingly *increases* across a period, since a more tightly bound (higher $Z_{\text{eff}}$, smaller-radius) electron is harder to remove; sodium's outermost electron ($I_1 = 5.14\ \text{eV}$) is far easier to strip away than chlorine's ($I_1 = 12.97\ \text{eV}$), consistent with the roughly threefold increase in $Z_{\text{eff}}$ found above. Both trends reverse on descending a group: each new period adds a shell of larger $n$, and although $Z_{\text{eff}}$ for the outermost electron changes only mildly down a group (the added inner shells screen the added protons quite effectively, shell for shell), the larger $n$ dominates, so atomic radius grows and ionization energy falls — lithium, sodium, and potassium have successively *lower* first ionization energies ($5.39$, $5.14$, $4.34\ \text{eV}$) even though $Z$ more than sextuples between them.

{numref}`Figure %s <fig:ch11-ionization-energy>` shows the resulting pattern for every element from hydrogen through krypton: not a smooth trend but a sharp periodic sawtooth, rising across each period and collapsing at the start of the next, with a noble gas at every peak and an alkali metal at every trough — the periodic table's defining periodicity made directly visible in a single measurable quantity.

```{figure} ../images/ch11-ionization-energy.svg
:label: fig:ch11-ionization-energy
:alt: Plot of first ionization energy in electron volts versus atomic number Z from 1 to 36, showing a sawtooth pattern peaking at the noble gases helium, neon, argon, and krypton, and dipping at the alkali metals lithium, sodium, and potassium.

First ionization energy versus atomic number, $Z=1$–$36$. Each period rises from an alkali-metal trough to a noble-gas peak as $Z_{\text{eff}}$ grows across the period, then collapses as a new, more distant shell begins. Computed from NIST Atomic Spectra Database ionization-energy values.
```

Two smaller features in that figure repay a closer look. Within period 2, beryllium's ionization energy ($9.32\ \text{eV}$) is *higher* than boron's ($8.30\ \text{eV}$), even though boron has one more proton — a small step backward against the overall rising trend, and the same pattern recurs for nitrogen ($14.53\ \text{eV}$) against oxygen ($13.62\ \text{eV}$), and again in period 3 for phosphorus ($10.49\ \text{eV}$) against sulfur ($10.36\ \text{eV}$). These dips are not noise; they are the same subshell-stability physics responsible for the chromium and copper exceptions above, showing up in ionization energy instead of in the filling order.

#### Worked Example: The Ionization-Energy Dips at Boron and Oxygen

Beryllium's configuration is $1s^22s^2$: a completely filled $2s$ subshell. Removing an electron from boron ($1s^22s^22p^1$), by contrast, means removing the *single* $2p$ electron — a higher-energy, more weakly bound (less penetrating, more screened) subshell than $2s$ — which is easier despite boron's larger nuclear charge, since the electron being removed is not even in the same subshell as beryllium's. This is a filled-subshell effect: beryllium's two $2s$ electrons are unusually well bound because $2s$ is complete, and there is no exchange-energy assistance available to make boron's lone $2p$ electron comparably well bound.

Nitrogen's configuration is $1s^22s^22p^3$: a *half-filled* $2p$ subshell, with all three $2p$ electrons in separate orbitals with parallel spin, by Hund's rule. Oxygen ($1s^22s^22p^4$) must place its fourth $2p$ electron into an orbital that already holds one — pairing two electrons in the same spatial orbital, with opposite spins, for the first time in the $2p$ subshell. That pairing does two things at once: it loses one unit of exchange-energy stabilization (going from three mutually parallel spins to only three still parallel, minus the correlation lost to the new pair) and it adds direct Coulomb repulsion between the two electrons now sharing an orbital. Both effects make oxygen's *paired* electron easier to remove than any of nitrogen's three unpaired ones, despite oxygen's larger nuclear charge — exactly the same underlying mechanism (exchange-energy stabilization of half-filled subshells) that pins chromium at $3d^54s^1$ rather than $3d^44s^2$.

## Atomic Spectra, X-Rays, and Lasers

### Atomic Spectra and X-Rays

Optical spectra of multi-electron atoms arise, as in hydrogen, from transitions of a single (typically outer, valence) electron between energy levels, now shifted by screening as described above and further split by the interaction between an electron's orbital and spin magnetic moments (**spin-orbit coupling**), producing the closely spaced doublets and multiplets seen in high-resolution atomic spectra.

A distinct and higher-energy class of spectral lines, **characteristic X-rays**, arises from transitions of *inner-shell* electrons. If an atom is bombarded with sufficiently energetic electrons (as in an X-ray tube) or photons, an inner-shell electron (e.g., from the $n=1$, or $K$, shell) can be ejected entirely, leaving a vacancy. An electron from a higher shell then drops down to fill the vacancy, emitting a photon whose energy — since inner-shell electrons in heavier atoms feel nearly the full, largely unscreened nuclear charge $Z$ — is far larger than typical optical-transition energies, and falls in the X-ray part of the spectrum. X-ray spectroscopists label shells by letter rather than by $n$: $n=1$ is the $K$ shell, $n=2$ the $L$ shell, $n=3$ the $M$ shell, $n=4$ the $N$ shell, and so on — a historical notation, predating the Bohr model, that has simply stuck. Lines from transitions ending on the $K$ shell are called the **K series** (with $K_\alpha$ for the $n=2\to n=1$, i.e. $L\to K$, transition, $K_\beta$ for $n=3\to n=1$, i.e. $M \to K$, etc.); an atom with a vacancy in the $L$ shell instead produces the analogous, lower-energy $L$ series ($L_\alpha$ for $M\to L$, and so on).

:::{margin}
The Greek-letter subscript counts how many shells the initial electron dropped: $\alpha$ for a jump from the adjacent shell ($\Delta n=1$, e.g. $L\to K$), $\beta$ for a jump from two shells up ($\Delta n=2$, e.g. $M\to K$), and so on — the same convention used for the Lyman/Balmer-series labels of [Chapter 10](#ch-the-hydrogen-atom).
:::

Henry Moseley (1913) measured the characteristic X-ray frequencies of many elements and found that the frequency of the $K_\alpha$ line follows a strikingly simple pattern, **Moseley's law**:

$$
\sqrt{f} = a(Z - b),
$$

where $a$ and $b$ are constants (with $b\approx 1$ for the $K_\alpha$ line, reflecting screening of the nuclear charge by the one remaining $K$-shell electron) essentially independent of the element. This relation follows directly from a hydrogen-like treatment of the transition, with the true nuclear charge $Z$ replaced by an effective charge $Z_{\text{eff}} = Z - b$ to account for screening by the other $K$-shell electron, applied to the Bohr/Schrödinger hydrogen energy formula. Moseley's law provided, for the first time, a direct physical (rather than merely chemical) way to determine an element's atomic number $Z$, and was used to correctly order elements in the periodic table, resolve several ambiguities in the ordering by atomic mass, and confirm the existence of predicted-but-then-unobserved elements by their expected X-ray frequency, cementing $Z$ (nuclear charge) rather than atomic mass as the correct organizing quantity for the periodic table.

#### The Moseley Plot

Moseley's own presentation of his data was graphical rather than tabular, and remains the clearest way to see the law's content: plotting $\sqrt{f}$ (the square root of the measured $K_\alpha$ frequency) against $Z$ for every element measured produces, to remarkable precision, a single **straight line**. That linearity is the entire empirical claim — a hydrogen-like $1/n^2$ energy spectrum predicts $f \propto (Z-b)^2$, i.e., $\sqrt{f} \propto (Z-b)$, so a plot linear in $Z$ is direct evidence that inner-shell transition energies really do scale as a screened hydrogen atom's, even in atoms far too complicated to solve exactly. The same linear relationship holds separately for the $L$ series and other series, each with its own slope $a$ and intercept $b$ (the $L$-series screening constant $b$ is larger than the $K$-series value of about $1$, since an $L$-shell vacancy is screened by more surrounding electrons than a $K$-shell vacancy is) — a family of parallel diagnostic lines, one per series, any one of which pins down $Z$ from a measured frequency alone.

#### Worked Example: Moseley's Law — Predicting Nickel's $K_\alpha$ Line from Copper's

A single measured $K_\alpha$ frequency, together with the known screening constant $b\approx1$, is enough to predict the $K_\alpha$ frequency of a neighboring element. Copper ($Z=29$) has a measured $K_\alpha$ frequency $f_{\text{Cu}} = 1.94\times10^{18}\ \text{Hz}$ (corresponding to a photon energy $hf_{\text{Cu}} \approx 8.02\ \text{keV}$, close to the accepted value of $8.048\ \text{keV}$ for the Cu $K_{\alpha1}$ line). Writing Moseley's law as $\sqrt f = A(Z-1)$ and solving for $A$ using copper's data,

$$
A = \frac{\sqrt{f_{\text{Cu}}}}{29-1} = \frac{\sqrt{1.94\times10^{18}\ \text{Hz}}}{28} = \frac{1.393\times10^{9}\ \sqrt{\text{Hz}}}{28} = 4.974\times10^{7}\ \sqrt{\text{Hz}}.
$$

Applying the same $A$ to nickel ($Z=28$, one proton lighter),

$$
\sqrt{f_{\text{Ni}}} = A(28-1) = (4.974\times10^7\ \sqrt{\text{Hz}})(27) = 1.343\times10^9\ \sqrt{\text{Hz}}, \qquad f_{\text{Ni}} \approx 1.80\times10^{18}\ \text{Hz},
$$

corresponding to a predicted photon energy $hf_{\text{Ni}} \approx 7.46\ \text{keV}$. The accepted experimental value for the Ni $K_\alpha$ doublet is $7.461$–$7.478\ \text{keV}$ — agreement to better than half a percent, from a calculation using only a single measured data point and one universal constant, exactly the kind of predictive power that let Moseley assign atomic numbers to elements from X-ray measurements alone.

The surviving photograph in {numref}`Figure %s <fig:ch11-historical-moseley>` shows the physicist himself, not long before the work described above.

```{figure} ../images/historical-moseley.jpg
:label: fig:ch11-historical-moseley
:alt: Historical photograph portrait of Henry Moseley.

Henry Gwyn Jeffreys Moseley, circa 1914. Photograph via the AIP Emilio Segrè Visual Archives, W. F. Meggers Gallery of Nobel Laureates; public domain via Wikimedia Commons.
```

#### Historical Context: Henry Moseley and the 1913–1914 X-Ray Survey

Henry Moseley was 26 years old, working at Ernest Rutherford's laboratory in Manchester and then at Oxford, when he built an X-ray spectrometer and, over roughly a year, measured the characteristic $K$- and $L$-series frequencies of nearly 40 elements — an extraordinarily fast and thorough experimental survey by the standards of the day. The result was immediately and directly useful to chemistry: several elements were known, from their chemical properties, to sit in a different order than their measured atomic *masses* would suggest (tellurium and iodine are the classic example — tellurium is heavier but chemically belongs *before* iodine in the periodic table), and Moseley's X-ray frequencies confirmed that atomic *number*, not mass, was the correct ordering quantity in every such case. His data also revealed gaps: no element then known produced the $K_\alpha$ frequency predicted for $Z=43$, $61$, or $75$, and Moseley correctly concluded that these elements simply had not yet been discovered (they are now known as technetium, promethium, and rhenium, the first two of which are so unstable that terrestrial samples are exceedingly rare — technetium, in fact, was not found until 1937, isolated from a cyclotron target and never located naturally). A vacancy at $Z=72$ was, for a decade, the subject of a bitter chemical priority dispute — a French chemist had already claimed the element among the rare earths and named it "celtium" — until 1922, when X-ray measurements at Bohr's institute in Copenhagen showed conclusively that the true element 72 (hafnium) is chemically a heavier relative of zirconium, not a rare earth at all, and had simply been misidentified.

Moseley enlisted in the Royal Engineers at the outbreak of the First World War and was killed at Gallipoli on 10 August 1915, at 27, shot through the head while relaying a message during the landing. His death is often cited (including by later Nobel laureates who worked to change the practice) as a direct argument for the British and other governments' subsequent policy of not sending scientifically valuable personnel to serve at the front line — a policy adopted too late to save Moseley himself, whose X-ray survey had already, in barely two years, put the periodic table's underlying organizing principle beyond doubt.

At the optical end of the same physics, {numref}`Figure %s <fig:ch11-discharge-sim>` runs the experiment a neon sign runs: electrons accelerated through a low-pressure gas, colliding with atoms, and the light that comes out. The collisions are the point. Below a threshold electron energy the atoms are elastic scatterers and the tube stays dark; raise the accelerating voltage past the first excitation energy and the atoms begin to absorb *exactly* that much, no more, and re-emit it as a photon of fixed wavelength. That threshold behavior is the Franck–Hertz experiment, and it is direct evidence of discrete atomic levels that owes nothing to spectroscopy. Multi-level atoms can be selected to see cascades through intermediate states, which is the same level structure the next section exploits.

```{phet-legacy} discharge-lamps
:sim-name: Neon Lights & Other Discharge Lamps
:label: fig:ch11-discharge-sim

A gas discharge tube with the accelerating voltage, the gas, and the atomic energy-level scheme under control. Excitation happens only at discrete electron energies, and the emitted spectrum is the level diagram read out in light.
```

### Lasers

A further application of atomic energy levels involves the interaction between atoms and light more actively than simple absorption/emission spectroscopy. An atom in an excited state can lose energy in two distinct ways: **spontaneous emission**, in which it decays at a random time with a photon emitted in a random direction (governing ordinary fluorescence and, statistically, the exponential decay laws seen throughout atomic and nuclear physics), and **stimulated emission**, in which a passing photon of exactly the transition energy triggers the atom to emit a second, additional photon that is an exact copy of the first — same energy, direction, phase, and polarization. Einstein first predicted stimulated emission in 1917, well before it could be technologically exploited.

Ordinarily, stimulated emission is masked by the competing process of absorption, since a typical collection of atoms in thermal equilibrium has more atoms in lower-energy states than higher ones. A **laser** (light amplification by stimulated emission of radiation) requires engineering a **population inversion** — an atomic sample with more atoms in a higher-energy state than a lower one, typically achieved by "pumping" atoms into a higher state and relying on an intermediate **metastable state** (one with an anomalously long lifetime against spontaneous decay, because its decay to lower states is forbidden or strongly suppressed by selection rules such as the $\Delta\ell=\pm1$ rule of [Chapter 10](#ch-the-hydrogen-atom)) to accumulate a population large enough to exceed that of the lower lasing level. Once inverted, a single spontaneously emitted photon can trigger a cascade of stimulated emission as it passes back and forth through the gain medium (typically between two mirrors forming an optical cavity), producing an intense, coherent, highly directional, single-wavelength beam — a direct, large-scale, technological manifestation of discrete atomic energy levels and the quantum-mechanical description of light-matter interaction developed across this and the preceding chapters.

#### Two Concrete Laser Systems: Helium–Neon and Ruby

The **helium–neon (He-Ne) laser**, one of the first lasers built (1961) and still common in classrooms and barcode scanners, illustrates a **four-level scheme**. An electrical discharge through a low-pressure He-Ne gas mixture excites helium atoms into a long-lived metastable state at $20.61\ \text{eV}$ above the helium ground state — too high to decay by any allowed single-photon transition, so helium atoms accumulate there in large numbers, exactly the metastable-state bottleneck described above. That energy happens to very nearly match a neon excited state near $20.66\ \text{eV}$, so an excited helium atom colliding with a ground-state neon atom can transfer its energy directly, exciting the neon (and leaving the helium atom free to be re-excited by the discharge) — helium serves purely as an energy-transfer intermediary, never itself the lasing species. The excited neon atom then undergoes stimulated emission down to a lower excited state, emitting the familiar $632.8\ \text{nm}$ red beam; because that lower level is itself well above the neon ground state and decays away rapidly through further (non-lasing) transitions, it never accumulates a large population, so the population inversion between the upper and lower laser levels is easy to sustain — the defining advantage of a four-level design over a three-level one.

The **ruby laser**, built by Theodore Maiman in 1960 (the first laser of any kind to operate), is a **three-level system** and correspondingly harder to pump. Ruby is aluminum oxide doped with a small fraction of chromium ions ($\text{Cr}^{3+}$), whose electronic transitions (not those of the aluminum oxide host) do the lasing. An intense flash lamp pumps chromium ions from the ground state into two broad, short-lived absorption bands (centered in the blue and green, which is why ruby appears red — it absorbs the complementary colors); those ions decay almost immediately, without emitting a photon, to a metastable level about $1.79\ \text{eV}$ above the ground state, with a comparatively long lifetime of several milliseconds. Because the *lower* laser level in this scheme is the atomic ground state itself, which starts out fully populated, achieving a population inversion requires pumping *more than half* of all the chromium ions into the metastable state simultaneously — a substantially harder threshold to cross than in a four-level scheme, where the lower laser level is nearly empty to begin with. Once inverted, stimulated emission from the metastable level back to the ground state produces ruby's characteristic $694.3\ \text{nm}$ deep-red beam, historically in short, intense pulses rather than the continuous output a He-Ne laser can sustain.

Every ingredient of that description is separately adjustable in {numref}`Figure %s <fig:ch11-laser-sim>`, which is the best way to see that a laser is a threshold device rather than a bright lamp. Pump a two-level medium as hard as you like and it will not lase: absorption and stimulated emission from a two-level system saturate at equal populations, so no inversion is possible. Switch to three levels, so that atoms accumulate in a metastable state, and the inversion appears; add the cavity mirrors and, above a pump rate that the simulation makes it easy to bracket from below, the output collapses from a random scatter of spontaneous photons into a single coherent beam.

```{phet-legacy} lasers
:label: fig:ch11-laser-sim

A laser assembled from its parts: a pump, a two- or three-level gain medium, and an optical cavity. Population inversion is displayed directly, so the threshold for lasing can be found by experiment rather than asserted.
```

#### Worked Example: Population Inversion Requires Active Pumping

It is worth confirming, numerically, why a population inversion never arises on its own from thermal equilibrium and must be engineered by pumping. In thermal equilibrium at temperature $T$, the ratio of the number of atoms in an upper state (energy $E_2$) to a lower state (energy $E_1$) is set by the Boltzmann factor,

$$
\frac{N_2}{N_1} = \exp\!\left(-\frac{E_2-E_1}{k_BT}\right).
$$

For the ruby laser transition, $E_2 - E_1 \approx 1.79\ \text{eV}$ (found from $hc/\lambda$ with $\lambda = 694.3\ \text{nm}$, using $hc=1240\ \text{eV}\cdot\text{nm}$). At room temperature, $T\approx300\ \text{K}$, $k_BT \approx 0.02585\ \text{eV}$, so

$$
\frac{N_2}{N_1} = \exp\!\left(-\frac{1.79\ \text{eV}}{0.02585\ \text{eV}}\right) = \exp(-69.2) \approx 8\times10^{-31}.
$$

Out of every $10^{30}$ or so chromium ions in thermal equilibrium, essentially none sit in the upper laser level — an inversion ($N_2 > N_1$) is not just unlikely but is astronomically, hopelessly far from anything thermal equilibrium could ever produce at ordinary temperature. This is precisely why a laser requires an external pump (an intense flash lamp, an electrical discharge, or another laser) to force the population far out of thermal equilibrium, and why, once the pump is switched off, the inverted population decays and lasing stops — a laser is fundamentally a *driven*, non-equilibrium device, not a system that has simply been heated.

#### Applications: Lasers in Technology and Medicine

The properties that make a laser beam distinctive — a single, precisely defined wavelength; a high degree of spatial coherence, allowing the beam to be focused to a tiny spot or to travel long distances with little spreading; and a high degree of temporal coherence, permitting long coherence lengths ([Chapter 4](#ch-interference-of-light)) — underlie applications far removed from the gas-discharge tubes and ruby rods described above. **Fiber-optic communication**, the physical backbone of the modern internet, encodes digital data as pulses from semiconductor **diode lasers** (a solid-state laser design, distinct from both examples above, in which the population inversion is created electrically across a semiconductor junction rather than by an optical pump) sent down thin glass fibers by total internal reflection; the laser's narrow wavelength spread keeps different colors of light traveling through the same fiber from smearing into one another over long distances, allowing enormous data rates over transoceanic distances. **Laser cooling**, by contrast, exploits the momentum $p=h/\lambda$ carried by individual photons ([Chapter 6](#ch-particle-properties-of-waves)): a beam tuned just below an atom's resonant absorption frequency preferentially scatters off atoms moving *toward* the beam (Doppler-shifted into resonance), each absorption event imparting a momentum kick that opposes the atom's motion, and repeated scattering from beams in multiple directions can cool a dilute atomic gas to temperatures of a microkelvin or below — a technique essential to modern atomic clocks and to the experimental study of quantum gases. In medicine, lasers are used both destructively, where a tightly focused, high-intensity beam cuts or cauterizes tissue with a precision unavailable to a mechanical scalpel (as in some ophthalmic and dermatological surgery), and diagnostically, where the coherence and narrow linewidth of laser light are exploited in optical coherence tomography to image tissue structure with micrometer resolution — different laser properties from the list above put to work in each case.

## Summary

- The **Pauli exclusion principle** forbids two electrons from sharing the same full set of quantum numbers $(n,\ell,m_\ell,m_s)$, limiting each orbital to two electrons (opposite spin) and is essential to explaining atomic structure.
- **Screening** of the nuclear charge by inner electrons makes subshell energy depend on both $n$ and $\ell$ in multi-electron atoms, unlike hydrogen; lower-$\ell$ orbitals penetrate closer to the nucleus and lie lower in energy at fixed $n$. The **self-consistent field (Hartree) method** computes screening explicitly, by iterating each electron's wave function in the averaged potential of all the others until the potential stops changing; **Slater's rules** give a fast hand-calculable estimate of the resulting effective nuclear charge $Z_{\text{eff}}$.
- The **Aufbau principle** (fill lowest-energy subshells first, respecting exclusion) and **Hund's rule** (maximize total spin within a partially filled subshell) determine ground-state electron configurations, which in turn generate the row/column/block structure of the periodic table and the periodicity of chemical properties. **Exchange energy** favors half-filled and completely filled subshells, producing Aufbau exceptions (chromium, copper) and small dips in ionization energy (boron, oxygen) that the naive filling order alone does not predict.
- **First ionization energy** and **atomic radius** are periodic in $Z$, tracking $Z_{\text{eff}}$: both rise/fall sharply across a period as $Z_{\text{eff}}$ grows with little added screening, and reverse down a group as increasing $n$ dominates a nearly constant $Z_{\text{eff}}$.
- **Characteristic X-rays** arise from inner-shell vacancies, labeled by shell letter ($K$: $n=1$, $L$: $n=2$, $M$: $n=3$, $\ldots$); **Moseley's law**, $\sqrt f = a(Z-b)$ — a straight line when $\sqrt{f}$ is plotted against $Z$ — let X-ray spectra be used to determine atomic number directly, correctly ordering the periodic table by $Z$ and revealing the undiscovered elements $Z=43$, $61$, and $75$.
- **Lasers** exploit stimulated emission and a **population inversion**, sustained via a **metastable state**, to produce coherent light; three-level (ruby) and four-level (helium–neon) schemes differ in how hard the lower laser level is to keep empty. Lasers underlie fiber-optic communication, laser cooling, and a range of medical applications.

## Problems

:::{exercise}
:label: ex-many-electron-atoms-1

Write the ground-state electron configuration (using $n\ell^{\,x}$ notation, e.g. $1s^2\,2s^2\ldots$) for (a) carbon ($Z=6$), (b) sodium ($Z=11$), (c) iron ($Z=26$), using the filling order given in the text.
:::

:::{solution} ex-many-electron-atoms-1
:label: sol-many-electron-atoms-1
:class: dropdown

Filling orbitals in the stated energy order gives carbon: $1s^2\,2s^2\,2p^2$; sodium: $1s^2\,2s^2\,2p^6\,3s^1$; and iron: $1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^6$.  Therefore, these are the respective ground-state electron configurations for $Z=6$, $11$, and $26$.
:::

:::{exercise}
:label: ex-many-electron-atoms-2

Using Hund's rule, sketch the orbital-filling diagram (boxes for each $m_\ell$ orbital, arrows for spin) for the $2p$ subshell of nitrogen ($Z=7$, configuration $1s^22s^22p^3$), and state the resulting total spin.
:::

:::{solution} ex-many-electron-atoms-2
:label: sol-many-electron-atoms-2
:class: dropdown

Nitrogen has $2p^3$.  Hund's rule puts one parallel-spin electron into each of the three $p$ orbitals before any pairing: $[\uparrow]\,[\uparrow]\,[\uparrow]$.  The three spins each have $m_s=+\tfrac12$, so $S=3(\tfrac12)\hbar=\tfrac32\hbar$.

```{figure} ../images/ch11-sol-hunds-rule-nitrogen.svg
:label: fig:ch11-sol-hunds-rule-nitrogen
:alt: Three separate orbital boxes for nitrogen's 2p subshell, each containing a single upward-pointing spin arrow, with no orbital doubly occupied.

Hund's rule in action: all three $2p$ orbitals get one electron, spins aligned, before any orbital is filled with a second, opposite-spin electron.
```

Therefore, nitrogen's $2p$ subshell has three unpaired parallel electrons and total spin $S=\tfrac32\hbar$.
:::

:::{exercise}
:label: ex-many-electron-atoms-3

Explain why, in a multi-electron atom, a $4s$ electron can have lower energy than a $3d$ electron despite having a larger principal quantum number, using the concept of orbital penetration and screening.
:::

:::{solution} ex-many-electron-atoms-3
:label: sol-many-electron-atoms-3
:class: dropdown

A $4s$ electron penetrates toward the nucleus more effectively than a $3d$ electron, so it spends more time inside the shielding cloud of inner electrons.  It consequently feels a larger effective nuclear charge and can have a lower energy despite its larger principal quantum number.  Therefore, orbital energy in a many-electron atom depends on penetration and screening, not on $n$ alone.
:::

:::{exercise}
:label: ex-many-electron-atoms-4

The measured $K_\alpha$ X-ray frequency of copper ($Z=29$) is $f = 1.94\times10^{18}\ \text{Hz}$. Using Moseley's law in the form $\sqrt{f} = A(Z-1)$ (i.e., $b=1$) with a single data point to determine $A$, predict the $K_\alpha$ frequency of nickel ($Z=28$), and compare qualitatively to what you would expect (higher or lower than copper's).
:::

:::{solution} ex-many-electron-atoms-4
:label: sol-many-electron-atoms-4
:class: dropdown

Moseley's relation with $b=1$ gives $f\propto(Z-1)^2$.  Hence

$$f_{\rm Ni}=f_{\rm Cu}\left(\frac{28-1}{29-1}\right)^2=(1.94\times10^{18}\ \text{Hz})\left(\frac{27}{28}\right)^2=1.80\times10^{18}\ \text{Hz}.$$

```{figure} ../images/ch11-sol-moseley-plot.svg
:label: fig:ch11-sol-moseley-plot
:alt: Square root of the K-alpha frequency plotted against atomic number, with a dashed line assuming b equals 1 through the copper point predicting nickel, and a solid line fit through copper and molybdenum predicting silver, in Problem 9.

This problem's single-point, $b=1$ extrapolation (dashed) and [Problem 9](#ex-many-electron-atoms-9)'s two-point fit (solid) nearly coincide over this range — both are straight lines in $\sqrt f$ vs. $Z$, just anchored differently.
```

Therefore, nickel's predicted $K_\alpha$ frequency is $1.80\times10^{18}\ \text{Hz}$, lower than copper's because nickel has one fewer proton.
:::

:::{exercise}
:label: ex-many-electron-atoms-5

Explain, in terms of the exclusion principle, why the ground-state electron configuration of helium ($1s^2$) is chemically inert, while lithium ($1s^22s^1$) is highly reactive, referring to the energy required to remove the outermost electron in each case.
:::

:::{solution} ex-many-electron-atoms-5
:label: sol-many-electron-atoms-5
:class: dropdown

Helium's $1s$ orbital is full: the exclusion principle prevents a third electron from entering the same lowest-energy state, so removing or rearranging an electron requires a large energy.  Lithium has the closed $1s^2$ core plus one weakly bound $2s$ electron, which can be removed or shared at much lower energy.  Therefore, helium is chemically inert while lithium is reactive because lithium has an accessible unpaired outer electron.
:::

:::{exercise}
:label: ex-many-electron-atoms-6

Explain why a three-level or four-level laser scheme requires a metastable intermediate state to sustain a population inversion, rather than pumping directly into the lower lasing level's excited partner state, using the relative decay rates implied by allowed versus forbidden transitions ([Chapter 10](#ch-the-hydrogen-atom)'s selection rule).
:::

:::{solution} ex-many-electron-atoms-6
:label: sol-many-electron-atoms-6
:class: dropdown

Pumping directly to a short-lived allowed-transition level does not build an inversion because that level decays rapidly.  A metastable state has a transition to the lower state that is forbidden or strongly suppressed, so its lifetime is long enough for pumped atoms to accumulate above the lasing transition.  Therefore, metastability is what permits a sustained population inversion in three- and four-level lasers.
:::

:::{exercise}
:label: ex-many-electron-atoms-7

Using Slater's rules (the grouping $(1s)(2s,2p)(3s,3p)\ldots$ and the shielding constants $0.35$/same group, $0.85$/one shell lower, $1.00$/two or more shells lower), compute the effective nuclear charge $Z_{\text{eff}}$ felt by a $3s$ electron in magnesium ($Z=12$, configuration $1s^22s^22p^63s^2$). Compare your result to the text's values of $Z_{\text{eff}} = 2.20$ for sodium's $3s$ electron and $Z_{\text{eff}}=6.10$ for chlorine's $3p$ electron, and state whether magnesium's value is consistent with its position between them in the periodic table.
:::

:::{solution} ex-many-electron-atoms-7
:label: sol-many-electron-atoms-7
:class: dropdown

For one magnesium $3s$ electron, the other $3s$ electron shields $0.35$; the eight $n=2$ electrons shield $8(0.85)=6.80$; and the two $1s$ electrons shield $2(1.00)=2.00$.  Thus

$$S=0.35+6.80+2.00=9.15,\qquad Z_{\rm eff}=Z-S=12-9.15=2.85.$$

```{figure} ../images/ch11-sol-zeff-comparison.svg
:label: fig:ch11-sol-zeff-comparison
:alt: Bar chart of effective nuclear charge for the outer electron of sodium, magnesium, and chlorine, increasing from sodium through magnesium to chlorine.

Slater's-rules $Z_{\rm eff}$ increases steadily across the period as protons are added faster than shielding can compensate; magnesium's $2.85$ falls exactly between sodium's and chlorine's.
```

Therefore, magnesium's $3s$ electron feels $Z_{\rm eff}=2.85$, appropriately between sodium's $2.20$ and chlorine's $6.10$.
:::

:::{exercise}
:label: ex-many-electron-atoms-8

Sulfur's first ionization energy ($10.36\ \text{eV}$) is slightly *lower* than phosphorus's ($10.49\ \text{eV}$), even though sulfur has one more proton. Using phosphorus's and sulfur's electron configurations ($[\text{Ne}]\,3s^23p^3$ and $[\text{Ne}]\,3s^23p^4$, respectively) and the exchange-energy argument given in the text for the analogous nitrogen/oxygen dip, explain this reversal.
:::

:::{solution} ex-many-electron-atoms-8
:label: sol-many-electron-atoms-8
:class: dropdown

Phosphorus has $3p^3$, with three parallel electrons in separate orbitals, gaining the stabilization associated with a half-filled subshell.  Sulfur is $3p^4$, so one $p$ orbital contains a pair; the added electron introduces pairing repulsion and reduces that special exchange stabilization.

```{figure} ../images/ch11-sol-phosphorus-sulfur.svg
:label: fig:ch11-sol-phosphorus-sulfur
:alt: Orbital box diagrams comparing phosphorus 3p cubed, with three singly occupied orbitals, and sulfur 3p to the fourth, with one doubly occupied orbital and two singly occupied, alongside their first ionization energies.

Phosphorus keeps every $3p$ electron unpaired and enjoys the full half-filled-subshell exchange bonus; sulfur's fourth electron must double up, and the resulting pairing repulsion slightly outweighs its extra proton.
```

Therefore, sulfur's first ionization energy is slightly lower than phosphorus's despite sulfur's larger nuclear charge.
:::

:::{exercise}
:label: ex-many-electron-atoms-9

Copper's $K_\alpha$ frequency is $f_{\text{Cu}} = 1.94\times10^{18}\ \text{Hz}$ ($Z=29$); molybdenum's measured $K_\alpha$ photon energy is $17.478\ \text{keV}$ ($Z=42$). (a) Using both data points in Moseley's law $\sqrt{f} = a(Z-b)$ (two equations, two unknowns $a$ and $b$), solve for $a$ and $b$, and compare $b$ to the approximate value $b\approx1$ quoted in the text for the $K_\alpha$ line. (b) Use your fitted $a$ and $b$ to predict the $K_\alpha$ photon energy of silver ($Z=47$).
:::

:::{solution} ex-many-electron-atoms-9
:label: sol-many-electron-atoms-9
:class: dropdown

For molybdenum, $f_{\rm Mo}=E/h=(17.478\times10^3\ \text{eV})/(4.1357\times10^{-15}\ \text{eV s})=4.226\times10^{18}\ \text{Hz}$.  Subtracting $\sqrt{f}=a(Z-b)$ for Cu and Mo gives

$$a=\frac{\sqrt{4.226\times10^{18}}-\sqrt{1.94\times10^{18}}}{42-29}=5.10\times10^7\ \text{Hz}^{1/2},$$

$$b=29-\frac{\sqrt{1.94\times10^{18}}}{a}=1.68.$$

For silver, $\sqrt f=a(47-b)=2.31\times10^9\ \text{Hz}^{1/2}$, so $f=5.34\times10^{18}\ \text{Hz}$ and $E=hf=22.1\ \text{keV}$, the point extrapolated in {numref}`Figure %s <fig:ch11-sol-moseley-plot>`.  Therefore, $b\approx1.68$ is of order unity and the fitted law predicts a $22.1\ \text{keV}$ silver $K_\alpha$ photon.
:::

:::{exercise}
:label: ex-many-electron-atoms-10

A helium–neon laser emits a continuous beam at $\lambda = 632.8\ \text{nm}$ with an output power of $5.00\ \text{mW}$. (a) Find the energy of a single photon at this wavelength, in eV and in joules. (b) Find the number of photons emitted per second. (c) Explain briefly why this beam, despite its low power compared to an ordinary light bulb, can still be hazardous to the retina, referring to the spatial coherence discussed in the text.
:::

:::{solution} ex-many-electron-atoms-10
:label: sol-many-electron-atoms-10
:class: dropdown

The photon energy is

$$E=\frac{1240\ \text{eV nm}}{632.8\ \text{nm}}=1.96\ \text{eV}=3.14\times10^{-19}\ \text{J}.$$

The photon rate is $P/E=(5.00\times10^{-3}\ \text{J/s})/(3.14\times10^{-19}\ \text{J})=1.59\times10^{16}\ \text{s}^{-1}$.  Therefore, the laser emits $1.96\ \text{eV}$ photons at $1.59\times10^{16}$ photons/s; its spatial coherence can focus this modest power into a very small retinal spot, making it hazardous.
:::

:::{exercise}
:label: ex-many-electron-atoms-11

In your own words, explain why the Hartree self-consistent field method is "circular" — that is, why the effective potential $V_{\text{eff}}(r)$ needed to solve for an electron's wave function cannot simply be written down in advance — and describe the iterative procedure used to resolve that circularity, including what "self-consistent" means as a stopping criterion.
:::

:::{solution} ex-many-electron-atoms-11
:label: sol-many-electron-atoms-11
:class: dropdown

The electron density determines the screening part of $V_{\rm eff}$, but that density is obtained only after solving for the electron wave functions in $V_{\rm eff}$ itself.  Hartree's method begins with a trial density, solves the one-electron equations, constructs a new density and potential, and repeats.  Therefore, the method is called self-consistent when an iteration returns the same density and effective potential with no material further change.
:::

:::{exercise}
:label: ex-many-electron-atoms-12

Argon ($Z=18$, configuration $[\text{Ne}]\,3s^23p^6$) has a *smaller* atomic radius than the very next element, potassium ($Z=19$, configuration $[\text{Ar}]\,4s^1$), even though potassium has one more proton and one more electron. Using the concepts of principal quantum number $n$ and effective nuclear charge $Z_{\text{eff}}$ developed in this chapter, explain why adding a proton and an electron can *increase* atomic radius in this specific case, when it decreases atomic radius everywhere else within period 3.
:::

:::{solution} ex-many-electron-atoms-12
:label: sol-many-electron-atoms-12
:class: dropdown

Across period 3, added protons raise $Z_{\rm eff}$ while electrons stay in the $n=3$ shell, so radii generally decrease.  Potassium starts a new $n=4$ shell: its $4s$ electron is farther out and strongly shielded by the filled argon core.

```{figure} ../images/ch11-sol-atomic-radius-anomaly.svg
:label: fig:ch11-sol-atomic-radius-anomaly
:alt: Bar chart of atomic radius across period 3 from sodium to argon, steadily decreasing, followed by a sharp jump up at potassium.

Radius falls steadily as $Z_{\rm eff}$ grows across a period, then jumps back up the instant a new principal shell opens at potassium.
```

Therefore, potassium's new principal shell outweighs its extra proton, giving it a larger radius than argon.
:::
