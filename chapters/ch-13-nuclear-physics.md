---
title: Nuclear Physics
short_title: Chapter 13. Nuclear Physics
label: ch-nuclear-physics
numbering:
  enumerator: "13.%s"
  heading_2: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 13.1, 13.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-13-nuclear-physics.pdf
    chapter: 13
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Describe the composition of the nucleus and use standard notation for nuclides and isotopes.
- Compute nuclear radius, density, binding energy, and binding energy per nucleon, and interpret the binding-energy-per-nucleon curve.
- Explain the qualitative form of the strong nuclear force and the semi-empirical (liquid-drop) mass formula.
- Apply the exponential radioactive decay law, including half-life, mean lifetime, and activity.
- Distinguish alpha, beta, and gamma decay, explain tunneling's role in alpha decay, and apply conservation laws to each.
- Explain nuclear fission and fusion in terms of the binding-energy curve and compute energy released in representative reactions.
- Write the semi-empirical (Weizsäcker) mass formula term by term, and use it to explain the extra stability of even-even nuclei and of the "magic-number" nuclides predicted by the nuclear shell model.
- Trace a multi-step radioactive decay chain, apply the decay law to isotopic (radiocarbon) dating, and sketch the quantitative dependence of alpha-decay tunneling probability on barrier height and width.

### Introduction

Chapters [10](#ch-the-hydrogen-atom)–[12](#ch-molecular-structure) treated the nucleus as a structureless positive point charge, a fixed source of the Coulomb potential binding atomic electrons. This chapter looks inside the nucleus itself: a bound system of protons and neutrons, held together not by the electromagnetic force (which, among the mutually repelling protons, would tend to blow the nucleus apart) but by a new fundamental interaction, the strong nuclear force, with a strength and range entirely different from anything encountered so far in this book. The same quantum-mechanical ideas developed for atoms — quantized energy levels, tunneling, exponential decay driven by fixed transition probabilities — reappear here on a length scale roughly $10^5$ times smaller and an energy scale roughly $10^6$ times larger, and account for radioactivity, nuclear stability, and the energy-release mechanisms (fission and fusion) that make the nucleus, unlike the atom, a practical source of usable energy.

## Nuclear Structure and Binding Energy

### Nuclear Composition and Notation

A nucleus consists of $Z$ protons and $N$ neutrons, collectively called **nucleons**, with mass number $A = Z + N$. A given nuclear species (**nuclide**) is denoted $^A_Z X$, where $X$ is the chemical symbol determined by $Z$ (since $Z$ alone fixes the number of atomic electrons in the neutral atom, and hence its chemistry). Nuclides sharing the same $Z$ but different $N$ (and hence different $A$) are **isotopes** of the same element — chemically near-identical but differing in mass and, often, nuclear stability. Protons and neutrons have nearly equal mass ($m_p c^2 = 938.3\ \text{MeV}$, $m_nc^2 = 939.6\ \text{MeV}$), and because a proton's charge is exactly opposite an electron's, the notation $^AZX$ carries the atom's full identity without needing $N$ written explicitly ($N = A - Z$).

The division of labor between $Z$ and $N$ — one fixes the chemistry, the other only the mass and the stability — is worth handling directly before the rest of the chapter leans on it. In {numref}`Figure %s <fig:ch13-isotopes-sim>`, adding a neutron to an atom leaves the element name untouched and moves along a row of isotopes, while adding a proton changes the element outright. The simulation also assembles the tabulated atomic mass of an element from its isotopes weighted by natural abundance, which is why the periodic table lists $35.45$ for chlorine although no chlorine nucleus has that mass.

```{phet} isotopes-and-atomic-mass
:label: fig:ch13-isotopes-sim

Isotopes built nucleon by nucleon, with natural abundances and the resulting average atomic mass. $Z$ names the element; $N$ decides how long the nucleus lasts.
```

### Nuclear Size, Density, and the Strong Force

Scattering experiments (extending Rutherford's original alpha-scattering method, now generally using higher-energy electron or nucleon probes to resolve the nuclear interior itself) show that nuclear radius grows with mass number as

$$
R = R_0 A^{1/3}, \qquad R_0 \approx 1.2\ \text{fm} \ (1\ \text{fm} = 10^{-15}\ \text{m}),
$$

so nuclear *volume* is proportional to $A$ — each nucleon occupies, on average, the same volume regardless of the size of the nucleus it belongs to, exactly as one would expect for an (nearly) incompressible fluid of tightly packed, closely spaced constituents. This is the empirical basis of the **liquid-drop model** of the nucleus, in which the nucleus is treated, for many purposes, as a droplet of incompressible nuclear fluid.

Nuclear stability is not explained by electromagnetism — the Coulomb force between two protons at nuclear separations, $\sim 1\ \text{fm}$, is enormously repulsive and would fly the nucleus apart if the electromagnetic force between nucleons were the whole story. Nuclei are held together by the **strong nuclear force**, an attractive interaction between nucleons (proton-proton, proton-neutron, and neutron-neutron alike, largely independent of charge) that is far stronger than the Coulomb repulsion at nuclear distances, but has an extremely short range (roughly $1$–$2\ \text{fm}$), falling off essentially to zero beyond a few fermis. This short range explains why nuclear binding, unlike Coulomb binding, saturates: a given nucleon interacts strongly only with its immediate neighbors, not with every other nucleon in the nucleus (unlike the long-range Coulomb repulsion, which every proton feels from every other proton, growing roughly as $Z^2$) — a key qualitative fact used below to explain both the shape of the binding-energy curve and, ultimately, nuclear fission and fusion.

:::{margin}
For scale, $1\ \text{fm}=10^{-15}\ \text{m}$ is about $10^5$ times smaller than a typical atomic radius ($\sim1\ \text{Å}=10^{-10}\ \text{m}$) — the same factor of $10^5$ flagged in the chapter introduction as the length scale separating nuclear from atomic physics.
:::

The measurement that started all of this is reconstructed in {numref}`Figure %s <fig:ch13-rutherford-sim>`. Alpha particles are fired at a nucleus of adjustable $Z$, and almost all of them pass through with a barely perceptible deflection — but a few come back. Rutherford's inference from that rare, large-angle scattering was that the positive charge is concentrated in a volume tiny compared with the atom, and the simulation makes the inference reproducible: shrink the nuclear charge and the sharp back-scattering disappears, while the plum-pudding screen shows what a diffuse charge distribution would have produced instead — no large deflections at all, at any impact parameter.

```{phet} rutherford-scattering
:label: fig:ch13-rutherford-sim

Alpha particles scattering from a nucleus of adjustable charge, with a diffuse-charge atom available for comparison. The trajectories are pure Coulomb hyperbolas; the strong force never enters, which is exactly why the experiment measures charge and size rather than nuclear structure.
```

### Binding Energy

The mass of a bound nucleus is always *less* than the sum of the masses of its separated constituent protons and neutrons — a direct manifestation of mass–energy equivalence ([Chapter 3](#ch-relativistic-dynamics)): energy must be supplied to pull the nucleus apart into free nucleons, so the bound system, having lower total energy, has correspondingly lower total mass. The **binding energy** is defined as

$$
E_B = \left[Zm_p + Nm_n - M(^A_ZX)\right]c^2,
$$

where $M(^A_ZX)$ is the measured nuclear mass (in practice, atomic masses, which include electrons, are tabulated and used consistently on both sides of this equation, since the electron masses and atomic binding energies very nearly cancel). It is generally more informative to consider the **binding energy per nucleon**, $E_B/A$, since this measures how tightly, on average, an individual nucleon is bound, independent of the nucleus's overall size.

:::{margin}
The **atomic mass unit** is defined as exactly $1/12$ the mass of a neutral $^{12}_6\text{C}$ atom, $1\ \text{u}=1.660539\times10^{-27}\ \text{kg}$, converting to energy as $1\ \text{u}\,c^2=931.494\ \text{MeV}$ — the conversion factor used throughout this chapter's worked examples.
:::

Plotting $E_B/A$ against $A$ for all known nuclides gives one of the most important curves in nuclear physics: $E_B/A$ rises sharply from very light nuclei, peaks at around $E_B/A \approx 8.7\ \text{MeV}$ near $A \approx 56$ (iron and its neighbors), and then decreases slowly for heavier nuclei. This shape is easiest to absorb by looking at it directly, plotted from real nuclear data, in {numref}`Figure %s <fig:ch13-binding-curve>`.

:::{margin}
The single most tightly bound nuclide per nucleon is actually $^{62}_{28}\text{Ni}$, not $^{56}_{26}\text{Fe}$, though the two are close enough ($8.7946$ vs. $8.7903\ \text{MeV/nucleon}$) that "the iron peak" remains the standard shorthand for this region of the curve.
:::

```{figure} ../images/ch13-binding-energy-curve.svg
:label: fig:ch13-binding-curve
:alt: Binding energy per nucleon plotted against mass number, rising steeply for the lightest nuclides, peaking near iron-56 and nickel-62, and declining slowly toward uranium, with a fusion arrow climbing the left flank and a fission arrow descending the right flank toward the peak.

Binding energy per nucleon vs. mass number, computed from standard atomic mass data for a representative set of nuclides from deuterium to uranium-238. The peak, at $A\approx56$–$62$ (iron and nickel), is the single most consequential feature of the curve: fusion climbs the steep left flank toward it, and fission descends the shallow right flank toward it, both releasing energy in the process, as developed below. Original figure by the author, computed with matplotlib from standard nuclear mass data.
```

Two competing effects, both traceable to the short range of the strong force versus the long range of the Coulomb force, explain this shape: for light nuclei, a growing fraction of nucleons sit at or near the nuclear surface, with fewer strong-force neighbors than an interior nucleon has (a **surface term**, reducing $E_B/A$ for small $A$, since surface-to-volume ratio falls as $A$ grows), while for heavy nuclei, the number of proton pairs, and hence the total Coulomb repulsion energy, grows roughly as $Z^2$ — much faster than the (short-range, saturating) strong-force binding, which grows only as $A$ — progressively weakening binding per nucleon as $A$ increases (a **Coulomb term**). Together with a bulk (volume) term that would alone give constant $E_B/A$, and additional smaller terms accounting for the extra stability of nuclei with $N=Z$ (a symmetry term) and of nuclei with even numbers of protons and neutrons (a pairing term), these considerations make up the **semi-empirical mass formula** (also called the Weizsäcker or liquid-drop mass formula), which reproduces the observed binding energy of essentially every known nuclide to good accuracy using only five fitted terms with a clear physical origin apiece.

The location of the peak at $A\approx56$ has an immediate and far-reaching consequence, developed further below: **energy can be released either by combining light nuclei into heavier ones (fusion) or by splitting heavy nuclei into lighter ones (fission)**, in each case moving the participating nucleons toward the peak of the curve, where they are more tightly bound (lower mass) than before — with the energy released equal to the resulting decrease in total rest mass, via $E = \Delta m\, c^2$.

#### The Semi-Empirical Mass Formula

Written out in full, with the volume, surface, Coulomb, symmetry, and pairing terms named above each given an explicit form, the semi-empirical (or Weizsäcker) mass formula predicts the binding energy of a nuclide with $Z$ protons and mass number $A$ ($N=A-Z$ neutrons) as

$$
E_B(Z,A) = \underbrace{a_V A}_{\text{volume}} - \underbrace{a_S A^{2/3}}_{\text{surface}} - \underbrace{a_C\dfrac{Z(Z-1)}{A^{1/3}}}_{\text{Coulomb}} - \underbrace{a_A\dfrac{(A-2Z)^2}{A}}_{\text{symmetry}} + \underbrace{\delta(A,Z)}_{\text{pairing}},
$$

with, in one standard fit to measured masses (due to Krane),

$$
a_V = 15.5\ \text{MeV}, \quad a_S = 16.8\ \text{MeV}, \quad a_C = 0.72\ \text{MeV}, \quad a_A = 23\ \text{MeV},
$$

$$
\delta(A,Z) = \begin{cases} +a_P A^{-3/4}, & Z \text{ and } N \text{ both even (even–even)} \\ 0, & A \text{ odd} \\ -a_P A^{-3/4}, & Z \text{ and } N \text{ both odd (odd–odd)} \end{cases}, \qquad a_P \approx 34\ \text{MeV}.
$$

(Different published fits to the mass table give somewhat different coefficients — a reminder that this is a phenomenological model fit to data, not derived from first principles — but all agree on the same five terms and roughly the same magnitudes.) Each term has already been motivated qualitatively above: the **volume term** $a_VA$ reflects the short-range, saturating strong force acting equally on every nucleon, as if each contributed a fixed amount of binding independent of $A$; the **surface term** $-a_SA^{2/3}$ subtracts binding from the nucleons at the nuclear surface (proportional to surface area, $\propto R^2 \propto A^{2/3}$), which have fewer strong-force neighbors than an interior nucleon; the **Coulomb term** $-a_C Z(Z-1)/A^{1/3}$ is the electrostatic self-energy of $Z$ mutually repelling protons packed into a sphere of radius $R\propto A^{1/3}$, reducing binding as the number of proton pairs, $\sim Z^2$, grows.

The **symmetry term** $-a_A(A-2Z)^2/A$ is new here: it penalizes any departure from $N=Z$, and follows from the Pauli exclusion principle rather than from either the strong or Coulomb force directly — protons and neutrons fill separate sets of momentum states (each a distinct kind of fermion, [Chapter 11](#ch-many-electron-atoms)), so for fixed $A$, forcing $N$ and $Z$ apart pushes some nucleons into higher-energy states than a balanced $N=Z$ filling would require, exactly as forcing electrons into higher shells costs energy in a many-electron atom. Minimizing $E_B$ with respect to $Z$ at fixed $A$ (differentiating the Coulomb and symmetry terms, the only two that depend on how a fixed $A$ is divided between $Z$ and $N$, and setting the result to zero) gives, for large $A$,

$$
Z_{\min}(A) \approx \frac{2a_A A}{4a_A + a_C A^{2/3}},
$$

the proton number that maximizes binding energy for that $A$. For $A=238$, this predicts $Z_{\min}\approx91.5$ — strikingly close to uranium's actual $Z=92$ — and, more generally, shows why the ratio $Z_{\min}/A$ decreases steadily below $1/2$ as $A$ grows: the Coulomb term's $Z^2$ growth increasingly outweighs the symmetry term's preference for $N=Z$, pushing the most stable nucleus for each $A$ toward greater neutron excess, exactly the neutron-rich bending of the stable band away from $N=Z$ seen in {numref}`Figure %s <fig:ch13-nucleus-sim>` below.

:::{dropdown} Deriving the Line of Stability: Minimizing $E_B$ at Fixed $A$
Only the Coulomb and symmetry terms depend on how a fixed $A$ is divided between $Z$ and $N$; the volume, surface, and (for this smooth, continuous-$Z$ treatment) pairing terms are dropped. Writing $E_B$ as a function of $Z$ alone at fixed $A$ and differentiating,

$$
\frac{\partial E_B}{\partial Z} = -a_C\frac{2Z-1}{A^{1/3}} + \frac{4a_A(A-2Z)}{A},
$$

using $\partial[Z(Z-1)]/\partial Z = 2Z-1$ and $\partial[(A-2Z)^2]/\partial Z = -4(A-2Z)$. Setting this to zero and approximating $2Z-1\approx2Z$ (an excellent approximation once $Z$ is more than a few units) gives

$$
\frac{2a_CZ}{A^{1/3}} = \frac{4a_A(A-2Z)}{A}.
$$

Multiplying both sides by $A$ and collecting every term proportional to $Z$ on the left,

$$
2a_CZA^{2/3} + 8a_AZ = 4a_AA \quad\Longrightarrow\quad Z\left(4a_A + a_CA^{2/3}\right) = 2a_AA,
$$

which rearranges directly into the formula quoted in the text,

$$
Z_{\min}(A) = \frac{2a_AA}{4a_A + a_CA^{2/3}}.
$$

Because this comes from setting a first derivative to zero, it locates a maximum of $E_B$ (equivalently, a minimum of the nuclear mass) at fixed $A$ — exactly the most stable nuclide for that mass number, which is what "the line of stability" means.
:::

The **pairing term** $\delta(A,Z)$ captures a purely quantum effect with no analog in the volume, surface, or Coulomb terms: nucleons of the same type couple preferentially in spin-paired twos (much as the two electrons of a filled atomic orbital pair their spins, [Chapter 11](#ch-many-electron-atoms)), each pair contributing extra binding beyond what the smooth terms above predict. An **even–even** nuclide (even $Z$, even $N$) has every nucleon paired and gains the full pairing bonus; an **odd–odd** nuclide has one unpaired proton and one unpaired neutron and loses it; an odd-$A$ nuclide (one odd, one even) is intermediate and conventionally assigned $\delta=0$. The consequence is stark and directly observable in the chart of the nuclides: of the roughly 260 stable nuclides, about 150 are even–even, roughly 100 are odd-$A$, and only four are odd–odd ($^2_1\text{H}$, $^6_3\text{Li}$, $^{10}_5\text{B}$, and $^{14}_7\text{N}$, all among the very lightest nuclei, where the symmetry term's cost of an odd-odd configuration is smallest) — essentially every heavier odd-odd combination is unstable, decaying by beta emission toward an even-even or odd-$A$ neighbor of lower mass.

#### Worked Example: Binding Energy from the Semi-Empirical Mass Formula

Apply the semi-empirical mass formula to $^{56}_{26}\text{Fe}$ ($A=56$, $Z=26$, $N=30$, even–even) and compare to the measured value. Term by term,

$$
a_VA = 15.5(56) = 868.0\ \text{MeV}, \qquad a_SA^{2/3} = 16.8(56)^{2/3} = 245.9\ \text{MeV},
$$

$$
a_C\frac{Z(Z-1)}{A^{1/3}} = 0.72\,\frac{26(25)}{56^{1/3}} = 122.3\ \text{MeV}, \qquad a_A\frac{(A-2Z)^2}{A} = 23\,\frac{4^2}{56} = 6.6\ \text{MeV},
$$

and, since $^{56}\text{Fe}$ is even–even, the pairing bonus $\delta=+a_PA^{-3/4}$,

$$
\delta = 34(56)^{-3/4} \approx 1.7\ \text{MeV}.
$$

Summing with the signs shown in the formula above,

$$
E_B \approx 868.0 - 245.9 - 122.3 - 6.6 + 1.7 = 494.9\ \text{MeV}, \qquad E_B/A \approx 8.84\ \text{MeV/nucleon}.
$$

The measured value, computed from $^{56}_{26}\text{Fe}$'s tabulated atomic mass $M=55.934936\ \text{u}$ using $E_B = \left[Z\,m(^1\text{H}) + Nm_n - M\right]c^2$ (with $m(^1\text{H})=1.007825\ \text{u}$, the *atomic* hydrogen mass, so that the electron masses on both sides of the equation cancel exactly rather than merely approximately), is $E_B = 492.3\ \text{MeV}$, or $8.79\ \text{MeV/nucleon}$. The five-term fit reproduces the measured binding energy to about half a percent — remarkable accuracy from a formula built on the bulk liquid-drop picture of the nucleus plus one quantum correction, and a large part of why the semi-empirical mass formula remains a standard first tool for estimating the mass of a nuclide not yet directly measured.

#### The Nuclear Shell Model and Magic Numbers

The semi-empirical mass formula treats the nucleus as a featureless liquid drop and, term by term, does remarkably well — but it is not the whole story. Certain nuclides, with $Z$ or $N$ equal to one of the **magic numbers** $2, 8, 20, 28, 50, 82, 126$, are measurably more tightly bound, more abundant, and more resistant to further reaction (larger energy gap to the first excited state, smaller neutron-capture cross section) than the smooth semi-empirical formula predicts — $^4_2\text{He}$, $^{16}_8\text{O}$, $^{40}_{20}\text{Ca}$, and $^{208}_{82}\text{Pb}$ (with $N=126$) all sit at pronounced local peaks of the true binding-energy surface, and "doubly magic" nuclides such as $^{208}_{82}\text{Pb}$ (magic in both $Z$ and $N$) are exceptionally stable for their mass. $Z=50$ (tin) is a magic proton number too: tin has ten stable isotopes, more than any other element, a record set jointly by its magic-number proton-shell closure and (since $Z=50$ is even) the full pairing bonus of an even-$Z$ nuclide — in sharp contrast to its odd-$Z$ neighbor antimony ($Z=51$), which has only two. This is the nuclear analog of the noble-gas closed-shell stability seen in atomic electron structure ([Chapter 11](#ch-many-electron-atoms)): just as an atom with a filled electron shell ($Z=2,10,18,\ldots$) is unusually inert, a nucleus with a filled proton or neutron shell is unusually well bound, for the same underlying reason — a large energy gap separates the top of a filled shell from the next available single-particle state, so removing or adding one more nucleon costs (or gains) far more energy than for a nucleus with a partially filled shell.

The **nuclear shell model** treats each nucleon, to a first approximation, as moving independently in an average central potential produced by all the other nucleons combined — conceptually similar to the mean-field treatment used for atomic electrons ([Chapter 11](#ch-many-electron-atoms)), though for a very different potential shape. As previewed in [Chapter 9](#ch-quantum-mechanics-in-three-dimensions), the isotropic three-dimensional harmonic oscillator is a convenient starting point for this average potential (its energy levels and degeneracies are exactly solvable), but the oscillator's own degeneracies alone reproduce only the lightest magic numbers ($2, 8, 20$); reproducing the full sequence up to $126$ requires an additional **spin-orbit coupling** term (splitting each oscillator level by the nucleon's intrinsic spin coupled to its orbital motion, an effect far stronger, relative to the level spacing, than the analogous fine-structure splitting in atoms), first added by Maria Goeppert Mayer and, independently, J. Hans D. Jensen in 1949 — work for which they shared the 1963 Nobel Prize in Physics. With the spin-orbit term included, the shell model correctly reorders the single-particle levels so that the cumulative count of states filled at each major shell closure lands exactly on the observed magic numbers, explaining not only the extra binding at magic $Z$ or $N$ but also finer details such as the nuclear spins and magnetic moments of odd-$A$ nuclides (set, in the simplest version of the model, entirely by the single unpaired nucleon outside an otherwise paired, spherically symmetric core).

## Radioactive Decay

An unstable nuclide decays into a different nuclide (or a lower energy state of the same nuclide) at a rate governed, as with any quantum system undergoing a transition, by a fixed, per-nucleus **decay constant** $\lambda$ (units of inverse time), independent of the nucleus's history or environment (with rare, small exceptions for certain electron-capture processes sensitive to chemical environment). If $N(t)$ is the number of undecayed nuclei present at time $t$, the rate of decay is proportional to the number remaining, $dN/dt = -\lambda N$, giving the **exponential decay law**:

$$
N(t) = N_0\, e^{-\lambda t}.
$$

The **half-life** $T_{1/2}$, the time for half of an initial sample to decay, and the **mean lifetime** $\tau$, the average lifetime of an individual nucleus, are related to $\lambda$ by

$$
T_{1/2} = \frac{\ln 2}{\lambda}, \qquad \tau = \frac{1}{\lambda} = \frac{T_{1/2}}{\ln 2}.
$$

:::{warning} A Half-Life Is Not a Countdown Timer
It is tempting to picture a radioactive nucleus as "aging" toward its half-life, becoming more likely to decay the longer it has already survived — as if $T_{1/2}$ were a fuse burning down. It is not: the decay constant $\lambda$ is fixed and history-independent, so a nucleus that has already survived ten half-lives is exactly as likely to decay in the next second as one created a moment ago. A related error is treating $T_{1/2}$ and the mean lifetime $\tau$ as interchangeable — they are not. $\tau=T_{1/2}/\ln2\approx1.44\,T_{1/2}$ is *longer* than the half-life, because the relatively rare nuclei that survive far longer than typical pull the average up, even though the *median* survival time is exactly $T_{1/2}$.
:::

The **activity**, $\mathcal{A} \equiv -dN/dt = \lambda N(t) = \mathcal{A}_0 e^{-\lambda t}$, is the physically measured decay rate (in decays per second, or the traditional unit the curie), and decays with the same exponential form and the same $T_{1/2}$ as $N(t)$ itself, since $\mathcal A$ is simply proportional to $N$ at every instant.

:::{margin}
$1\ \text{curie (Ci)} \equiv 3.7\times10^{10}$ decays/s, originally defined to match the activity of exactly $1\ \text{g}$ of $^{226}\text{Ra}$ (verified explicitly in the worked example below). The SI unit is the **becquerel** (Bq), $1\ \text{Bq}\equiv1$ decay/s.
:::

The exponential law describes a population, not a nucleus, and the difference between those two statements is where intuition usually fails. {numref}`Figure %s <fig:ch13-decay-sim>` shows both at once: individual nuclei decaying at unpredictable moments with no memory of how long they have already waited, and the count of survivors nevertheless tracing a clean exponential once the sample is large enough. The same simulation puts the law to work in reverse — measuring the residual $^{14}\text{C}$ or $^{238}\text{U}$ fraction in a sample of unknown age and reading off the elapsed time — which is the argument by which the age of a bone, a lava flow, or the Earth itself is established.

```{phet-legacy} nuclear-physics/radioactive-dating-game
:label: fig:ch13-decay-sim

Radioactive decay watched nucleus by nucleus and in bulk, then applied to dating. The decay constant is a probability per unit time and nothing else: nuclei do not age.
```

#### Historical Context: Becquerel, the Curies, and the Discovery of Radioactivity

Radioactivity was discovered by accident. In early 1896, prompted by Wilhelm Röntgen's announcement of X-rays only weeks before, Henri Becquerel was investigating whether phosphorescent materials (which glow after exposure to light) might also emit penetrating, photographic-plate-fogging radiation, using uranium salts as his test material. An overcast Paris sky in late February 1896 forced him to store an unexposed sample — uranium salt sitting atop a wrapped photographic plate, with no sunlight available to trigger any phosphorescence — in a dark drawer for several days. When he developed the plate anyway on March 1, expecting at most a faint trace, he found a strong image instead: the uranium was emitting penetrating radiation entirely on its own, with no light exposure needed to trigger it. Becquerel had discovered **radioactivity**, a spontaneous nuclear process, without initially recognizing what he had found (he first suspected an unusually persistent, invisible form of phosphorescence). Becquerel himself is shown in a portrait from around the time of the discovery in {numref}`Figure %s <fig:ch13-becquerel-historical>`.

```{figure} ../images/historical-becquerel.jpg
:width: 45%
:label: fig:ch13-becquerel-historical
:alt: Historical portrait photograph of physicist Henri Becquerel.

Henri Becquerel (1852–1908). Photograph by Paul Nadar, before 1908; Smithsonian Institution Libraries (Dibner Library collection); public domain in the United States via Wikimedia Commons.
```

Marie Skłodowska Curie, joined by her husband Pierre, took up the puzzle as a doctoral research topic and pushed it decisively further. Testing pitchblende ore (the raw uranium mineral), she found it *more* radioactive than its uranium content alone could account for — direct evidence of one or more additional, still-unidentified radioactive elements hidden within it in trace quantities. Over four years of laborious chemical separation, processing tons of ore by hand in a converted shed, the Curies isolated two new elements, **polonium** (1898, named for Marie's native Poland) and **radium** (1898), and coined the term **radioactivity** itself for the phenomenon. Becquerel and the Curies shared the 1903 Nobel Prize in Physics for this work; Marie Curie went on to win a second Nobel Prize, in Chemistry, in 1911, for the isolation and characterization of radium and polonium as new chemical elements — achievements made decades before the neutron or the proton-neutron picture of the nucleus used throughout this chapter was available to explain, even in outline, what radioactivity actually *was*.

#### A Decay Chain: Uranium-238 to Lead-206

A single alpha or beta decay usually does not, by itself, produce a stable nuclide: the daughter is often itself radioactive, decaying again, and again, until a stable nuclide is finally reached. Such a sequence is a **decay chain** (or decay series). The longest and most geologically important chain starts at $^{238}_{92}\text{U}$ and ends, fourteen decays later, at stable $^{206}_{82}\text{Pb}$, alternating alpha and beta decays; its first several steps are

$$
{}^{238}_{92}\text{U} \xrightarrow{\alpha} {}^{234}_{90}\text{Th} \xrightarrow{\beta^-} {}^{234}_{91}\text{Pa} \xrightarrow{\beta^-} {}^{234}_{92}\text{U} \xrightarrow{\alpha} {}^{230}_{90}\text{Th} \xrightarrow{\alpha} {}^{226}_{88}\text{Ra} \xrightarrow{\alpha} {}^{222}_{86}\text{Rn} \xrightarrow{\alpha} \cdots \longrightarrow {}^{206}_{82}\text{Pb}.
$$

In all, the full chain from $^{238}\text{U}$ to $^{206}\text{Pb}$ involves eight alpha decays and six beta-minus decays — a bookkeeping check confirms it must: eight alpha decays remove $8\times4=32$ from the mass number ($238-32=206$, matching $^{206}\text{Pb}$ exactly) and $8\times2=16$ from the atomic number, while six beta-minus decays each raise $Z$ by one without changing $A$, for a net $\Delta Z = -16+6=-10$ ($92-10=82$, matching lead exactly). Each step has its own half-life, ranging from the parent's $4.5\times10^9\ \text{years}$ (comparable to the age of the solar system, which is why primordial $^{238}\text{U}$ is still present in Earth's crust at all) down to a fraction of a second for the shortest-lived member of the chain — a span of many orders of magnitude in half-life among nuclides connected by nothing more exotic than successive alpha and beta emissions.

Because every step in a chain like this decays at its own fixed rate while simultaneously being *replenished* by the decay of its parent, a chain that has run undisturbed for a time long compared to every half-life except the first settles into **secular equilibrium**: each intermediate's activity ($\lambda N$ for that nuclide) becomes equal to the activity of the slowly decaying parent feeding it, even though the intermediate's own $N$ (and hence $\lambda$) can be wildly different from the parent's. This is why an old, undisturbed sample of uranium ore contains measurable, steady quantities of highly radioactive but short-lived daughters such as radium and radon: they are being produced by $^{238}\text{U}$ decay just as fast as they themselves decay away.

#### Worked Example: Activity of a Radium-226 Sample

$^{226}_{88}\text{Ra}$ (half-life $T_{1/2}=1600\ \text{years}$), a step in the uranium-238 chain above, is the isotope Marie Curie isolated and the one for which the **curie** unit of activity was originally defined: $1\ \text{Ci} \equiv 3.7\times10^{10}$ decays/s, chosen to match the activity of exactly $1\ \text{g}$ of $^{226}\text{Ra}$. Verify this using the decay law. The number of nuclei in $1.00\ \text{g}$ of $^{226}\text{Ra}$ (molar mass $\approx226\ \text{g/mol}$) is

$$
N = \frac{(1.00\ \text{g})(6.022\times10^{23}\ \text{mol}^{-1})}{226\ \text{g/mol}} = 2.665\times10^{21},
$$

and the decay constant is

$$
\lambda = \frac{\ln2}{T_{1/2}} = \frac{0.6931}{(1600\ \text{yr})(3.156\times10^7\ \text{s/yr})} = 1.372\times10^{-11}\ \text{s}^{-1}.
$$

The activity is then

$$
\mathcal{A} = \lambda N = (1.372\times10^{-11}\ \text{s}^{-1})(2.665\times10^{21}) = 3.66\times10^{10}\ \text{decays/s},
$$

matching the defined curie, $3.7\times10^{10}\ \text{Bq}$, to within rounding — a reminder that the "old" activity unit is not an arbitrary round number but a direct consequence of $^{226}\text{Ra}$'s actual half-life and molar mass, fixed once those two measured quantities are fixed.

#### Worked Example: Carbon-14 Dating

Living organisms continuously exchange carbon with the atmosphere, maintaining a constant fraction of the radioactive isotope $^{14}_6\text{C}$ (half-life $T_{1/2}=5730\ \text{years}$, continuously replenished in the atmosphere by cosmic-ray-induced nuclear reactions) relative to stable $^{12}\text{C}$; once an organism dies, that exchange stops, and the $^{14}\text{C}$ fraction — and hence the sample's $^{14}\text{C}$ activity — decays exponentially with no further replenishment. A wooden artifact is found to have a $^{14}\text{C}$ activity only $68.0\%$ that of a freshly cut, otherwise identical sample of the same wood. Since activity is proportional to $N$ at every instant, $\mathcal{A}/\mathcal{A}_0 = N/N_0 = 0.680$, and the decay law gives the artifact's age directly:

$$
0.680 = e^{-\lambda t} \quad\Longrightarrow\quad t = -\frac{\ln(0.680)}{\lambda} = -\frac{\ln(0.680)}{\ln2/T_{1/2}} = -\frac{(-0.386)(5730\ \text{yr})}{0.693} \approx 3.19\times10^{3}\ \text{yr}.
$$

The artifact is roughly $3190$ years old. This is exactly the calculation, worked from a real measurement rather than an assumed elapsed time, that {numref}`Figure %s <fig:ch13-decay-sim>` above runs interactively — and it is also a direct illustration of why radiocarbon dating has a practical ceiling: after about ten half-lives ($\sim57{,}000$ years), the remaining $^{14}\text{C}$ activity has fallen by a factor of $2^{10}\approx1000$, to a level low enough that statistical counting uncertainty in a realistic sample overwhelms the signal, and other methods (using much longer-lived parents, such as $^{238}\text{U}$ in the decay chain above) must take over.

### Modes of Decay

Three principal decay modes connect unstable nuclides to more stable ones:

**Alpha decay** ($^A_ZX \to {}^{A-4}_{Z-2}Y + \alpha$, where $\alpha = {}^4_2\text{He}$) occurs predominantly among heavy nuclei, where it is energetically favorable (the parent's mass exceeds the combined daughter-plus-alpha mass) largely because of the Coulomb term discussed above. Classically, the alpha particle is confined within the nucleus by a potential well combining the short-range attractive strong force and, outside the nuclear radius, the repulsive Coulomb barrier — a barrier typically well above the alpha particle's actual kinetic energy once emitted, so classically the particle could never escape. Alpha decay is understood, quantitatively, as **quantum tunneling** ([Chapter 8](#ch-the-schrodinger-equation)) of the alpha particle through this Coulomb barrier: the measured strong sensitivity of half-life to alpha particle energy (the **Geiger–Nuttall relation**, an empirical pattern in which small changes in emitted alpha energy correspond to enormous changes in half-life, spanning many orders of magnitude across known alpha emitters) is explained quantitatively by the exponential dependence of the tunneling probability on barrier height and width worked out in [Chapter 8](#ch-the-schrodinger-equation), making alpha decay one of the most direct large-scale confirmations of quantum tunneling. Concretely, for a heavy alpha emitter the Coulomb barrier peaks at a height of order $30$–$40\ \text{MeV}$ (roughly the Coulomb repulsion of the departing alpha particle and daughter nucleus evaluated at the nuclear radius) while the emitted alpha particle typically carries away only $4$–$9\ \text{MeV}$ of kinetic energy, so the barrier the alpha particle must tunnel through is tens of MeV high and a few femtometers wide once its outer classical turning point is reached — the illustrative rectangular-barrier tunneling estimate worked out in [Chapter 8](#ch-the-schrodinger-equation) ($\Delta E \approx 20\ \text{MeV}$, $L\approx7\ \text{fm}$, giving $T\approx e^{-2\kappa L}$ with $\kappa=\sqrt{2m_\alpha\Delta E}/\hbar$) uses numbers of exactly this order. Because $T$ depends *exponentially* on both $\Delta E$ and $L$, a modest change in the alpha particle's energy routinely changes the predicted half-life by ten or more orders of magnitude — exactly the pattern captured empirically by the Geiger–Nuttall relation.

**Beta decay** occurs in three related forms — $\beta^-$ decay ($n \to p + e^- + \bar\nu_e$, converting a neutron to a proton within the nucleus), $\beta^+$ decay ($p \to n + e^+ + \nu_e$), and electron capture ($p + e^- \to n + \nu_e$) — each mediated by the weak nuclear interaction ([Chapter 14](#ch-elementary-particles-and-the-standard-model)) and each moving a nucleus toward the more stable $N/Z$ ratio for its mass number. The **neutrino** ($\nu_e$) and **antineutrino** ($\bar\nu_e$) are required, not merely as bookkeeping devices, by conservation of energy, momentum, and angular momentum: without a third emitted particle, a two-body decay ($n \to p + e^-$ alone) would force the emitted electron to have one single, fixed energy for a given parent-daughter pair, but the observed electron energy spectrum in beta decay is continuous, spread over a range up to a fixed maximum — direct evidence (first argued by Pauli in 1930, on exactly these grounds) that a third, initially unobserved particle carries away the missing energy and momentum event by event.

:::{note} From Pauli's "Desperate Remedy" to a Confirmed Particle
Pauli's 1930 neutrino proposal — floated in an open letter to a nuclear physics conference he skipped, addressed to "Dear Radioactive Ladies and Gentlemen" — was, in his own words, a "desperate remedy" to rescue conservation of energy in beta decay, and he was privately doubtful it could ever be tested: the neutrino interacts so weakly that a typical one could pass through light-years of solid lead without interacting even once. It took until 1956, twenty-six years later, for Clyde Cowan and Frederick Reines to detect (anti)neutrinos directly, using the intense flux from a nuclear reactor and a target designed to catch the rare inverse-beta-decay event $\bar\nu_e+p\to n+e^+$ — a confirmation for which Reines shared the 1995 Nobel Prize in Physics (Cowan had died in 1974, and the Prize is never awarded posthumously).
:::

:::{seealso} The Weak Interaction, at the Quark Level
This chapter treats $\beta^-$ decay at the nucleon level, $n\to p+e^-+\bar\nu_e$. [](#ch-elementary-particles-and-the-standard-model) goes one level deeper, showing the same transformation as a single down quark converting to an up quark — the only one of the four fundamental interactions that can change one flavor of quark into another — and develops the full conservation-law framework (charge, baryon number, lepton number) that the reaction above already silently obeys.
:::

**Gamma decay** ($^A_ZX^* \to {}^A_ZX + \gamma$, where the asterisk denotes an excited nuclear state) is the nuclear analog of atomic photon emission ([Chapter 10](#ch-the-hydrogen-atom)): a nucleus left in an excited state, often as the immediate product of a preceding alpha or beta decay, drops to a lower-energy (often the ground) state by emitting a photon, with energy set by the spacing between nuclear energy levels — typically keV to MeV, far larger than atomic transition energies, because the nuclear scale of confinement is so much smaller than the atomic scale (an application of the same uncertainty-principle confinement argument used in [Chapter 7](#ch-wave-properties-of-particles)).

All three modes, and the reason a given nuclide chooses one of them, are laid out in {numref}`Figure %s <fig:ch13-nucleus-sim>`. Its chart of the nuclides is the useful part: stable nuclides form a narrow band that starts along $N = Z$ and bends toward neutron excess as $Z$ grows, and the decay mode of anything off that band is predictable from which side of it the nuclide sits on. Neutron-rich nuclides convert a neutron to a proton by $\beta^-$ and step toward the band; proton-rich ones go the other way by $\beta^+$ or electron capture; and beyond $Z \approx 83$ nothing is stable at all, so the heavy corner of the chart empties itself by alpha emission.

```{phet} build-a-nucleus
:label: fig:ch13-nucleus-sim

Nuclei assembled from protons and neutrons, with the decay mode of each unstable arrangement shown, alongside the chart of the nuclides. The chart is the whole of nuclear stability in one picture: a thin band of nuclides that last, and, on either side of it, a decay mode pointing back toward it.
```

#### Worked Example: The Alpha-Decay Q-Value for Uranium-238

Extending [Problem 4](#ex-nuclear-physics-4) into a full numerical calculation: for $^{238}_{92}\text{U}\to{}^{234}_{90}\text{Th}+\alpha$, the energy released (the **Q-value**) is the rest-mass energy of the parent minus that of the products, computed directly from tabulated atomic masses — no bare-proton-mass correction is needed here, since the same $92$ electrons appear on both sides (90 bound to the thorium daughter, 2 bound to the emerging helium atom) and cancel exactly:

$$
Q = \left[M(^{238}\text{U}) - M(^{234}\text{Th}) - M(^4\text{He})\right]c^2.
$$

Using $M(^{238}\text{U})=238.050788\ \text{u}$, $M(^{234}\text{Th})=234.043601\ \text{u}$, and $M(^4\text{He})=4.002602\ \text{u}$,

$$
Q = \left[238.050788 - 234.043601 - 4.002602\right]\text{u} \times 931.494\ \text{MeV/u} = (0.004585\ \text{u})(931.494\ \text{MeV/u}) \approx 4.27\ \text{MeV},
$$

in close agreement with the measured value. Because momentum must also be conserved and the thorium daughter recoils, the alpha particle itself carries slightly less than the full $Q$: momentum conservation splits $Q$ between the two products in inverse proportion to their masses, so the much lighter alpha particle ($m_\alpha \ll M_{\text{Th}}$) carries away the large majority of it, close to the experimentally observed $4.20\ \text{MeV}$ alpha kinetic energy for this decay, with the small remainder appearing as the recoiling thorium nucleus's kinetic energy.

:::{tip} Track Electrons Before Plugging In a Mass
Binding-energy and $Q$-value calculations mix "nuclear" bookkeeping (protons and neutrons) with tabulated *atomic* masses (nucleus plus electrons), and the two must be reconciled before any numbers go into a formula. The rule that keeps this honest: compare only mass values that carry the same total number of electrons. The $^{56}\text{Fe}$ binding-energy example above uses $m(^1\text{H})$ in place of a bare $m_p$ specifically so that all $26$ atomic electrons cancel exactly rather than approximately; the $^{238}\text{U}$ alpha-decay $Q$-value works directly from atomic masses with no correction at all, because the same $92$ electrons are present on both sides, split between the daughter thorium atom ($90$) and the emerging helium atom ($2$). Whenever the electron count does not match up this neatly, the mismatch has to be added back in by hand before the result can be trusted.
:::

## Fission and Fusion

### Fission

**Nuclear fission** is the splitting of a heavy nucleus (typically after absorbing a neutron, which excites the nucleus into oscillation, distorting the initially spherical liquid drop) into two lighter, roughly comparable-mass fragments, plus several free neutrons. Because the binding-energy-per-nucleon curve rises steeply from heavy $A$ toward the $A\approx56$ peak, the fragments are individually more tightly bound (per nucleon) than the original heavy nucleus was, and the reaction releases a large amount of energy, typically around $200\ \text{MeV}$ per fission event for a nucleus such as $^{235}_{92}\text{U}$ — overwhelmingly larger than typical chemical reaction energies (electron-volts per bond, versus roughly $10^8$ times more energy per fission event), directly reflecting the vastly greater strength of the nuclear force compared to the electromagnetic forces governing chemical bonding.

Because each fission event releases, on average, more than one free neutron, and each of those neutrons can potentially induce a further fission event in a neighboring nucleus, a **chain reaction** is possible if enough fissile material is present (a **critical mass**) to sustain, on average, at least one neutron-induced fission per neutron released — the basis of both controlled fission (nuclear power reactors, where the reaction rate is regulated, e.g. via neutron-absorbing control rods) and uncontrolled fission (fission weapons). A power reactor adds one further ingredient beyond control rods: because the neutrons released promptly by fission are fast (born with roughly $1$–$2\ \text{MeV}$ of kinetic energy) while $^{235}\text{U}$ fissions far more readily on absorbing a *slow* (thermal, $\sim0.025\ \text{eV}$) neutron, most reactor designs surround the fuel with a **moderator** — a light-nuclide material such as ordinary water, heavy water, or graphite — whose job is to slow fast neutrons toward thermal energies through repeated elastic collisions (most efficient, per collision, with nuclei of mass comparable to the neutron itself, which is why light nuclei make good moderators and heavy ones make poor ones) without absorbing them outright, so that they are far more likely to induce a further fission before escaping the reactor core or being captured non-productively.

The distinction between those last two outcomes is quantitative, not qualitative, and {numref}`Figure %s <fig:ch13-fission-sim>` is where that becomes obvious. Fire a neutron at a single $^{235}\text{U}$ nucleus and watch the liquid drop distort, neck, and split; assemble a pile of nuclei instead and the multiplication factor decides everything. Below one neutron per fission surviving to cause another, the reaction dies out; above it, the population grows exponentially; and the control rods in the reactor screen do nothing more sophisticated than hold that number at exactly one by absorbing the surplus.

```{phet-legacy} nuclear-physics/nuclear-fission
:label: fig:ch13-fission-sim

A single fission event, a chain reaction in an assembly of adjustable size and enrichment, and a controlled reactor. Criticality is a statement about a ratio, and it is the same ratio in all three.
```

### Fusion

**Nuclear fusion**, the combination of two light nuclei into a single heavier one, releases energy for exactly the mirror-image reason: moving from very light $A$ toward the peak of the binding-energy curve increases $E_B/A$, so the fused product is more tightly bound (per nucleon) than the separate light nuclei were. Fusion is the energy source that powers stars, where sequences of fusion reactions (in the Sun, predominantly the **proton-proton chain**, ultimately converting four protons into a helium-4 nucleus plus positrons, neutrinos, and gamma rays) release the energy that balances gravitational collapse and produces the Sun's luminosity ([Chapter 3](#ch-relativistic-dynamics), [Problem 6](#ex-relativistic-dynamics-6)). Because fusion requires two positively charged nuclei to approach to within the range of the strong force ($\sim 1\ \text{fm}$) against their mutual Coulomb repulsion, it requires very high temperatures (tens of millions of kelvin or more, as in stellar cores) to proceed at an appreciable rate even with the assistance of quantum tunneling through the Coulomb barrier — the same tunneling mechanism responsible for alpha decay, now working in reverse to allow two light nuclei to fuse despite insufficient classical kinetic energy to overcome their mutual repulsion.

#### The Proton-Proton Chain

Written out step by step, the dominant sequence in the Sun (the **proton-proton chain**, or pp I branch) is:

$$
{}^1\text{H} + {}^1\text{H} \to {}^2\text{H} + e^+ + \nu_e \qquad (\text{one proton weak-converts to a neutron in the process}),
$$

$$
{}^2\text{H} + {}^1\text{H} \to {}^3\text{He} + \gamma,
$$

$$
{}^3\text{He} + {}^3\text{He} \to {}^4\text{He} + 2\,{}^1\text{H},
$$

with the first two steps each occurring twice to supply the two $^3\text{He}$ nuclei consumed in the third. Adding up all three steps and canceling the deuterium, helium-3, and one pair of protons that appear only as intermediates gives the net effect,

$$
4\,{}^1\text{H} \to {}^4\text{He} + 2e^+ + 2\nu_e,
$$

converting four ordinary hydrogen nuclei into one helium-4 nucleus, two positrons (which promptly annihilate with ambient electrons, releasing further gamma-ray energy), and two neutrinos (which, interacting only weakly, escape the Sun's interior directly, carrying off a small fraction of the released energy without contributing to solar heating). The full sequence releases a net $26.7\ \text{MeV}$ per helium-4 nucleus formed — about $0.7\%$ of the rest-mass energy of the four consumed protons converted directly to energy — which, multiplied by the enormous number of such reactions occurring per second in the Sun's core, accounts for the Sun's entire luminosity ([Chapter 3](#ch-relativistic-dynamics), [Problem 6](#ex-relativistic-dynamics-6)). The first step — two protons fusing directly, with one simultaneously beta-plus-converting to a neutron — is both essential (it is the chain's only entry point from pure hydrogen) and extraordinarily slow, mediated by the weak interaction ([Chapter 14](#ch-elementary-particles-and-the-standard-model)) at the same instant as the strong-force capture, giving an individual proton in the Sun's core a mean waiting time of order *billions of years* before it fuses — the single biggest reason the Sun burns for billions rather than millions of years despite its core temperature and density being otherwise sufficient for fusion to proceed immediately.

Terrestrial fusion research targets a different, much faster reaction than the Sun's own, since the proton-proton chain's bottleneck first step is far too slow to be useful outside a star: **deuterium-tritium (D-T) fusion**,

$$
{}^2_1\text{H} + {}^3_1\text{H} \to {}^4_2\text{He} + n,
$$

pursued in magnetic-confinement **tokamak** reactors such as ITER, currently under construction in France — a fundamentally different confinement strategy from the Sun's, which needs no physical confinement at all beyond its own gravity, and instead uses strong magnetic fields to hold a plasma far too hot ($\sim10^8\ \text{K}$, hotter than the Sun's core, needed to compensate for the much lower particle density achievable in a laboratory) for any physical vessel to contain directly.

#### Worked Example: Energy Released in Deuterium–Tritium Fusion

Using $m(^2\text{H})=2.014102\ \text{u}$, $m(^3\text{H})=3.016049\ \text{u}$, $m(^4\text{He})=4.002602\ \text{u}$, and $m_n=1.008665\ \text{u}$, the mass defect of the D-T reaction above is

$$
\Delta m = \left[2.014102+3.016049\right]-\left[4.002602+1.008665\right] = 5.030151-5.011267 = 0.018884\ \text{u},
$$

so the energy released is

$$
Q = \Delta m\, c^2 = (0.018884\ \text{u})(931.494\ \text{MeV/u}) \approx 17.6\ \text{MeV},
$$

in agreement with the accepted value. Conservation of momentum (the reacting nuclei have small initial momentum compared to the products' final momenta) splits this energy between the two products in inverse proportion to their masses, giving the alpha particle about $3.5\ \text{MeV}$ and the neutron about $14.1\ \text{MeV}$ of kinetic energy — a single D-T event releasing, in one step, roughly four times the energy of the U-238 alpha decay computed above, from a reaction between two of the lightest nuclei that exist rather than one of the heaviest.

## Summary

- A nucleus $^A_ZX$ contains $Z$ protons and $N=A-Z$ neutrons; nuclear radius scales as $R = R_0A^{1/3}$, consistent with a roughly incompressible liquid-drop model of tightly packed nucleons.
- The short-range, charge-independent **strong nuclear force** overcomes Coulomb repulsion to bind the nucleus; **binding energy**, $E_B = [Zm_p+Nm_n-M]c^2$, and **binding energy per nucleon**, peaking near $A\approx56$ (iron), summarize nuclear stability and are captured by the semi-empirical mass formula's volume, surface, Coulomb, symmetry, and pairing terms.
- Radioactive decay follows the exponential law $N(t)=N_0e^{-\lambda t}$, with half-life $T_{1/2}=\ln2/\lambda$ and activity $\mathcal A = \lambda N$.
- **Alpha decay** proceeds by quantum tunneling through the Coulomb barrier; **beta decay** ($\beta^-$, $\beta^+$, electron capture) proceeds via the weak interaction and requires a neutrino/antineutrino to conserve energy, momentum, and angular momentum, as shown by the continuous beta-electron energy spectrum; **gamma decay** is photon emission between nuclear energy levels.
- **Fission** (heavy nucleus splits) and **fusion** (light nuclei combine) both release energy by moving nucleons toward the binding-energy peak near $A\approx56$; fission chain reactions require a critical mass and, in a reactor, a **moderator** to slow fission-born fast neutrons, and fusion requires overcoming the Coulomb barrier, typically via high temperature and tunneling, as in stellar interiors.
- The **semi-empirical (Weizsäcker) mass formula** writes $E_B$ as volume ($a_VA$), surface ($-a_SA^{2/3}$), Coulomb ($-a_CZ(Z-1)A^{-1/3}$), symmetry ($-a_A(A-2Z)^2/A$), and pairing ($\pm a_PA^{-3/4}$, or $0$) terms; the pairing term explains why even-even nuclides dominate the stable chart (and stable odd-odd nuclides are essentially absent), and minimizing $E_B$ at fixed $A$ shows why heavy stable nuclei favor $N>Z$. The **nuclear shell model** (an average central potential plus spin-orbit coupling) explains the extra stability of nuclides at the magic numbers $2,8,20,28,50,82,126$, the nuclear analog of noble-gas electron-shell closure.
- A radioactive **decay chain** links successive unstable nuclides (e.g. $^{238}\text{U}$ through fourteen alpha and beta decays to stable $^{206}\text{Pb}$) until a stable nuclide is reached, reaching **secular equilibrium** when run undisturbed for long enough; the same exponential decay law underlies **radiocarbon dating** of once-living material.
- **Fusion** proceeds in stars via the multi-step **proton-proton chain** ($4\,{}^1\text{H}\to{}^4\text{He}+2e^++2\nu_e$, net $26.7\ \text{MeV}$) and in terrestrial reactors via the faster **deuterium-tritium reaction** ($17.6\ \text{MeV}$ per event), the latter pursued in magnetic-confinement devices such as tokamaks.

## Problems

:::{exercise}
:label: ex-nuclear-physics-1

Estimate the nuclear radius of $^{238}_{92}\text{U}$ and of $^{4}_{2}\text{He}$ using $R = R_0A^{1/3}$, and compute the ratio of their radii. Comment on whether this ratio is consistent with $A^{1/3}$ scaling given the ratio of their mass numbers.
:::

:::{solution} ex-nuclear-physics-1
:label: sol-nuclear-physics-1
:class: dropdown

Using $R=R_0A^{1/3}$ with $R_0=1.2\ \text{fm}$,

$$R_\mathrm{U}=1.2(238)^{1/3}\ \text{fm}=7.44\ \text{fm},\qquad R_\mathrm{He}=1.2(4)^{1/3}\ \text{fm}=1.90\ \text{fm}.$$

Their ratio is $7.44/1.90=3.91$, while $(238/4)^{1/3}=3.90$.  Therefore, uranium's radius is about $7.4\ \text{fm}$ and helium's is about $1.9\ \text{fm}$, fully consistent with $A^{1/3}$ scaling.
:::

:::{exercise}
:label: ex-nuclear-physics-2

Compute the binding energy and binding energy per nucleon of $^{4}_{2}\text{He}$, given $M(^4_2\text{He}) = 4.002602\ \text{u}$, $m_p = 1.007276\ \text{u}$, $m_n=1.008665\ \text{u}$, and using $1\ \text{u}\,c^2 = 931.5\ \text{MeV}$ (you may neglect the small correction from atomic electron binding energies).
:::

:::{solution} ex-nuclear-physics-2
:label: sol-nuclear-physics-2
:class: dropdown

The separated-nucleon mass is $2m_p+2m_n=2(1.007276)+2(1.008665)=4.031882\ \text{u}$.  Since $M(^4_2\text{He})$ is an *atomic* mass, it includes two orbital electrons, while $m_p$ is the bare nuclear proton mass; comparing them directly would omit two electron rest masses. Removing $2m_e=2(5.49\times10^{-4}\ \text{u})=0.001097\ \text{u}$ from the atomic mass (and neglecting the much smaller atomic electron binding energy, as instructed) gives the nuclear mass $M_\mathrm{nuc}=4.002602\ \text{u}-0.001097\ \text{u}=4.001505\ \text{u}$.  Thus

$$\Delta m=4.031882\ \text{u}-4.001505\ \text{u}=0.030377\ \text{u},$$

$$E_B=(0.030377\ \text{u})(931.5\ \text{MeV}/\text{u})=28.30\ \text{MeV},\qquad \frac{E_B}{A}=\frac{28.30\ \text{MeV}}4=7.07\ \text{MeV/nucleon}.$$

This value is one of the low-$A$ points on the rising left flank of {numref}`Figure %s <fig:ch13-binding-curve>`, well below the $A\approx56$–$62$ peak.  Therefore, helium-4 has binding energy $28.3\ \text{MeV}$, or $7.07\ \text{MeV}$ per nucleon.
:::

:::{exercise}
:label: ex-nuclear-physics-3

A radioactive sample of $^{131}_{53}\text{I}$ (half-life $8.02$ days) initially contains $N_0 = 1.00\times10^{18}$ nuclei. (a) Find the decay constant $\lambda$. (b) Find the number of nuclei remaining after $24$ days. (c) Find the initial activity, in becquerels (decays/s).
:::

:::{solution} ex-nuclear-physics-3
:label: sol-nuclear-physics-3
:class: dropdown

Convert the half-life: $T_{1/2}=8.02(86400\ \text{s})=6.929\times10^5\ \text{s}$.  Hence

$$\lambda=\frac{\ln2}{T_{1/2}}=\frac{0.693}{6.929\times10^5\ \text{s}}=1.00\times10^{-6}\ \text{s}^{-1}.$$

After $t=24.0\ \text{d}$, $N=N_0 2^{-t/T_{1/2}}=10^{18}2^{-24/8.02}=1.26\times10^{17}$.  Initially,

$$A_0=\lambda N_0=(1.00\times10^{-6}\ \text{s}^{-1})(1.00\times10^{18})=1.00\times10^{12}\ \text{Bq}.$$

```{figure} ../images/ch13-sol-decay-curves.svg
:label: fig:ch13-sol-decay-curves
:alt: Two exponential decay curves: iodine-131 fraction remaining versus time in days with the 24-day point marked, and carbon-14 fraction remaining versus time in thousands of years with the 42 percent point marked, in Problem 9.

Left: this problem's $^{131}\text{I}$ decay, with $t=24\ \text{d}$ landing at $N/N_0=0.126$. Right: [Problem 9](#ex-nuclear-physics-9)'s $^{14}\text{C}$ dating curve, read the opposite way — a measured fraction fixes the elapsed time instead.
```

Therefore, $\lambda=1.00\times10^{-6}\ \text{s}^{-1}$, $1.26\times10^{17}$ nuclei remain after $24\ \text{d}$, and the initial activity is $1.00\times10^{12}\ \text{Bq}$.
:::

:::{exercise}
:label: ex-nuclear-physics-4

$^{238}_{92}\text{U}$ undergoes alpha decay to $^{234}_{90}\text{Th}$. Write the full decay equation, and explain, using the shape of the binding-energy-per-nucleon curve, why alpha decay (rather than, say, single-proton emission) is the energetically favored decay mode for very heavy nuclei.
:::

:::{solution} ex-nuclear-physics-4
:label: sol-nuclear-physics-4
:class: dropdown

Conservation of mass number and charge gives

$$^{238}_{92}\text{U}\longrightarrow{}^{234}_{90}\text{Th}+{}^{4}_{2}\text{He}+Q.$$

An alpha particle is an exceptionally tightly bound cluster, and its emission moves a very heavy nucleus toward a region of higher binding energy per nucleon while reducing its Coulomb repulsion.  A single proton is much less tightly bound as an emitted fragment and would leave a less favorable daughter.  This is precisely the physics drawn on the right-hand flank of {numref}`Figure %s <fig:ch13-binding-curve>`: heavy nuclei sit below the peak, and shedding a tightly-bound alpha cluster moves the daughter closer to it.  Therefore, uranium-238 alpha-decays to thorium-234 plus helium-4 because this channel lowers the total mass more effectively than single-proton emission.
:::

:::{exercise}
:label: ex-nuclear-physics-5

In beta-minus decay of a free neutron, $n \to p + e^- + \bar\nu_e$, use $m_nc^2 = 939.57\ \text{MeV}$, $m_pc^2 = 938.27\ \text{MeV}$, $m_ec^2 = 0.511\ \text{MeV}$ (and treat the antineutrino as massless) to find the total kinetic energy shared among the three decay products. Explain why the electron's kinetic energy alone is not fixed at this value, but instead varies continuously up to it.
:::

:::{solution} ex-nuclear-physics-5
:label: sol-nuclear-physics-5
:class: dropdown

The available kinetic energy is the rest-energy difference:

$$Q=939.57\ \text{MeV}-938.27\ \text{MeV}-0.511\ \text{MeV}=0.789\ \text{MeV}.$$

Therefore, the proton, electron, and antineutrino share $0.789\ \text{MeV}$ of kinetic energy.  The electron does not always receive that whole amount because the antineutrino and recoiling proton can carry variable shares while conserving energy and momentum, producing a continuous electron spectrum.
:::

:::{exercise}
:label: ex-nuclear-physics-6

In the fission of $^{235}_{92}\text{U}$ (via neutron absorption to $^{236}_{92}\text{U}$, then fission), roughly $200\ \text{MeV}$ is released per event. Estimate the mass (in kg) of $^{235}\text{U}$ that would need to fission completely to release $1.0\times10^{14}\ \text{J}$ (order of magnitude of a small commercial reactor's daily output), using Avogadro's number and the molar mass of $^{235}\text{U}$.
:::

:::{solution} ex-nuclear-physics-6
:label: sol-nuclear-physics-6
:class: dropdown

One fission releases

$$E_f=200\ \text{MeV}\left(1.602\times10^{-13}\ \text{J/MeV}\right)=3.204\times10^{-11}\ \text{J}.$$

The required number is $N=(1.0\times10^{14}\ \text{J})/E_f=3.12\times10^{24}$.  Its amount is $n=N/N_A=5.18\ \text{mol}$, so

$$m=(5.18\ \text{mol})(235\ \text{g/mol})=1.22\times10^3\ \text{g}=1.22\ \text{kg}.$$

Therefore, complete fission of about $1.2\ \text{kg}$ of uranium-235 releases $1.0\times10^{14}\ \text{J}$.
:::

:::{exercise}
:label: ex-nuclear-physics-7

Using the semi-empirical mass formula coefficients given in the text, compute the predicted binding energy per nucleon of $^{120}_{50}\text{Sn}$ ($N=70$, even–even). Compare your result to the measured value, $8.51\ \text{MeV/nucleon}$, and comment on the size and likely origin of any discrepancy.
:::

:::{solution} ex-nuclear-physics-7
:label: sol-nuclear-physics-7
:class: dropdown

For $A=120$, $Z=50$, $A^{1/3}=4.932$, $A^{2/3}=24.33$, and $A-2Z=20$.  The five terms are

$$15.5(120)=1860.0,\quad16.8(24.33)=408.7,\quad0.72\frac{50(49)}{4.932}=357.5,$$

$$23\frac{20^2}{120}=76.7,\qquad \delta=34(120)^{-3/4}=0.94\ \text{MeV}.$$

Thus $E_B=1860.0-408.7-357.5-76.7+0.94=1018\ \text{MeV}$ and $E_B/A=8.48\ \text{MeV/nucleon}$.  This lands squarely on the near-peak plateau of {numref}`Figure %s <fig:ch13-binding-curve>`, close to where tin's $A=120$ actually falls.  Therefore, the formula predicts about $8.48\ \text{MeV/nucleon}$, within $0.03\ \text{MeV/nucleon}$ of $8.51\ \text{MeV/nucleon}$; the small difference reflects shell effects and fitted-coefficient limitations.
:::

:::{exercise}
:label: ex-nuclear-physics-8

In the uranium-238 decay chain, $^{226}_{88}\text{Ra}$ (half-life $1600\ \text{yr}$) alpha-decays to $^{222}_{86}\text{Rn}$ (half-life $3.8$ days). A sealed sample containing $1.00\ \text{g}$ of $^{226}\text{Ra}$ has been undisturbed for many thousands of years — far longer than radon's half-life, so the radon has reached secular equilibrium with its radium parent. Using the result of the radium worked example, find the activity, in becquerels, of the $^{222}\text{Rn}$ in the sample. (Hint: what must the daughter's activity equal, in secular equilibrium?)
:::

:::{solution} ex-nuclear-physics-8
:label: sol-nuclear-physics-8
:class: dropdown

In secular equilibrium the daughter production rate equals its decay rate, so $A_\mathrm{Rn}=A_\mathrm{Ra}$.  The worked example gives $A_\mathrm{Ra}=3.7\times10^{10}\ \text{Bq}$ for $1.00\ \text{g}$ of radium-226.

```{figure} ../images/ch13-sol-secular-equilibrium.svg
:label: fig:ch13-sol-secular-equilibrium
:alt: Activity versus time since the sample was sealed, with radium-226 activity flat and radon-222 activity rising from zero and asymptotically approaching the same level after about 20 days.

Because $^{226}\text{Ra}$'s activity barely changes on a timescale of days, $^{222}\text{Rn}$ grows in until its own activity catches up completely — secular equilibrium is this curve's flat asymptote.
```

Therefore, the radon-222 activity is $3.7\times10^{10}\ \text{Bq}$, even though its number of atoms is much smaller because its decay constant is much larger.
:::

:::{exercise}
:label: ex-nuclear-physics-9

A bone fragment has a measured $^{14}\text{C}$ activity that is $42.0\%$ of that of living bone. Using $T_{1/2}=5730\ \text{years}$ for $^{14}\text{C}$, find the fragment's age.
:::

:::{solution} ex-nuclear-physics-9
:label: sol-nuclear-physics-9
:class: dropdown

Activity is proportional to the number of undecayed nuclei, so $A/A_0=2^{-t/T_{1/2}}=0.420$.  Taking logarithms,

$$t=-T_{1/2}\frac{\ln(0.420)}{\ln2}=-(5730\ \text{yr})\frac{-0.8675}{0.6931}=7.17\times10^3\ \text{yr}.$$

This is the point marked on the $^{14}\text{C}$ curve in {numref}`Figure %s <fig:ch13-sol-decay-curves>`.  Therefore, the bone fragment is about $7.2\times10^3\ \text{years}$ old.
:::

:::{exercise}
:label: ex-nuclear-physics-10

Verify the claim in the deuterium-tritium fusion worked example that momentum conservation splits the reaction's $17.6\ \text{MeV}$ Q-value into $3.5\ \text{MeV}$ (carried by the alpha particle) and $14.1\ \text{MeV}$ (carried by the neutron): treating the initial deuteron and triton as essentially at rest, set the magnitudes of the final alpha-particle and neutron momenta equal (nonrelativistic momentum conservation) and solve for each product's share of the total kinetic energy in terms of the two product masses ($m_\alpha \approx 4.00\ \text{u}$, $m_n\approx1.01\ \text{u}$).
:::

:::{solution} ex-nuclear-physics-10
:label: sol-nuclear-physics-10
:class: dropdown

Momentum conservation gives equal momentum magnitudes $p$ for the alpha particle and neutron.  Since $K=p^2/(2m)$, $K_\alpha/K_n=m_n/m_\alpha$.  With $Q=K_\alpha+K_n$,

$$K_\alpha=Q\frac{m_n}{m_\alpha+m_n}=17.6\ \text{MeV}\frac{1.01}{4.00+1.01}=3.55\ \text{MeV},$$

$$K_n=Q\frac{m_\alpha}{m_\alpha+m_n}=17.6\ \text{MeV}\frac{4.00}{5.01}=14.1\ \text{MeV}.$$

```{figure} ../images/ch13-sol-fusion-energy-sharing.svg
:label: fig:ch13-sol-fusion-energy-sharing
:alt: A horizontal bar split into two segments proportional to the kinetic energies of the alpha particle and neutron produced in deuterium-tritium fusion, totaling 17.6 megaelectronvolts.

Equal and opposite momenta split $Q$ in inverse proportion to mass: the neutron, four times lighter, carries four times the energy.
```

Therefore, the alpha particle receives about $3.5\ \text{MeV}$ and the neutron about $14.1\ \text{MeV}$, as required by equal and opposite final momenta.
:::
