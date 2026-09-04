---
title: Elementary Particles and the Standard Model
short_title: Chapter 14. Elementary Particles and the Standard Model
label: ch-elementary-particles-and-the-standard-model
numbering:
  enumerator: "14.%s"
  heading_2: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 14.1, 14.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-14-elementary-particles-and-the-standard-model.pdf
    chapter: 14
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Classify particles as fermions or bosons and explain the physical distinction.
- Distinguish the four fundamental interactions by their relative strength, range, and mediating boson.
- Distinguish leptons and quarks as the two families of fundamental fermions, and state the generation structure of each.
- Explain quark confinement and construct the quark content of simple baryons and mesons.
- Apply conservation laws (charge, baryon number, lepton number, and strangeness) to determine whether a proposed particle reaction is allowed, and identify which interaction (strong, electromagnetic, or weak) a given reaction must proceed through.
- Describe the role of the Higgs field in giving mass to fundamental particles.
- Read and interpret a simple Feynman diagram, including the convention that an antiparticle's arrow points backward in time along a line that itself still runs forward.
- Describe, in outline, how particle accelerators and detectors produce and identify new particles, and explain why colliders are favored over fixed-target machines for reaching the highest energies.
- Recount the historical "particle zoo" of the 1930s–1960s and explain how the eightfold way and the quark model resolved it.
- Estimate, quantitatively, why gravitational effects between individual particles are negligible compared with the other fundamental interactions.
- Identify several of the major open questions at the current frontier of particle physics and cosmology.

### Introduction

Nuclear physics ([Chapter 13](#ch-nuclear-physics)) treated protons and neutrons as elementary building blocks, bound by the strong force into nuclei. This chapter goes one level deeper, to the particles and forces from which protons, neutrons, and indeed all matter are built. Over the course of the twentieth century, a rapidly growing zoo of "elementary" particles, discovered first in cosmic rays and then in purpose-built particle accelerators, was gradually organized into a coherent theoretical framework, the **Standard Model of particle physics**, which identifies a genuinely small set of truly fundamental particles and the forces (themselves mediated by particle exchange) that govern their interactions. This chapter surveys that framework: the classification of particles by spin and by the forces they feel, the substructure of protons and neutrons in terms of quarks, the conservation laws that govern which particle reactions can occur, and the mechanism by which most fundamental particles acquire mass at all. It also traces how this framework was actually established — the historical progression from a bewildering "particle zoo" of cosmic-ray discoveries to the ordered quark model, and the particle accelerators and detectors that turned particle physics into a precision experimental science — and closes, as befits the final chapter of this book, with several of the major questions the Standard Model leaves unanswered.

## Particles, Forces, and Feynman Diagrams

### Classifying Particles: Fermions and Bosons

Every known particle carries an intrinsic spin angular momentum, quantized exactly as orbital angular momentum is ([Chapter 9](#ch-quantum-mechanics-in-three-dimensions)), $S = \sqrt{s(s+1)}\hbar$, but with $s$ either a half-integer ($\tfrac12, \tfrac32, \ldots$) or an integer ($0, 1, 2, \ldots$). This distinction is far more than bookkeeping: particles with half-integer spin, called **fermions**, obey the Pauli exclusion principle ([Chapter 11](#ch-many-electron-atoms)) and cannot occupy the same quantum state as an identical partner; particles with integer spin, called **bosons**, obey no such restriction and can occupy the same state in unlimited numbers (the basis, for photons, of the stimulated-emission cascade in a laser, [Chapter 11](#ch-many-electron-atoms)). Matter, in the Standard Model, is built from fermions (spin $\tfrac12$); the forces between them are mediated by the exchange of bosons.

:::{margin}
The names honor statistics, not the particles themselves: **fermions** obey Fermi–Dirac statistics, after Enrico Fermi, while **bosons** obey Bose–Einstein statistics, after Satyendra Nath Bose, whose 1924 analysis of photon statistics (soon extended by Einstein to massive particles) first showed that indistinguishable integer-spin particles behave nothing like classical particles, or like half-integer-spin fermions.
:::

### The Four Fundamental Interactions

All observed particle interactions are, to the precision of current experiments, accounted for by exactly four fundamental forces, each mediated by the exchange of a characteristic boson (a **gauge boson**, in the language of the quantum field theories underlying the Standard Model) and each with a distinct characteristic strength and range:

The interactions are compared directly in {numref}`Table %s <tab:ch14-fundamental-interactions>`.

```{table} The four fundamental interactions
:label: tab:ch14-fundamental-interactions

| Interaction | Relative strength | Range | Mediating boson(s) | Governs |
|---|---|---|---|---|
| Strong | $1$ | $\sim 1\ \text{fm}$ | gluon | quark binding; nuclear force (residual) |
| Electromagnetic | $\sim 10^{-2}$ | infinite | photon | charged-particle interactions |
| Weak | $\sim 10^{-6}$ | $\sim 10^{-3}\ \text{fm}$ | $W^\pm$, $Z^0$ | beta decay; some particle decays |
| Gravitational | $\sim 10^{-38}$ | infinite | graviton (hypothesized, not yet observed) | negligible for individual particles; dominant only for macroscopic masses |
```

The strong and weak interactions, both confined to nuclear-scale distances, are the reason their effects were unknown until nuclear and particle physics probed those scales directly; the electromagnetic and gravitational interactions, both infinite in range because their mediating boson is massless, dominate everyday, macroscopic experience. The relative strengths quoted are approximate and depend on the energy/distance scale at which the comparison is made, but the ordering — strong $\gg$ electromagnetic $\gg$ weak $\gg$ gravitational, at typical particle-physics scales — is robust. The strong force between nucleons discussed in [Chapter 13](#ch-nuclear-physics) is, in the Standard Model's deeper description, a residual effect of the strong force acting between the quarks confined inside each nucleon (analogous to the way the residual electromagnetic force between neutral atoms, the van der Waals force, is a residual effect of the more fundamental electromagnetic force between the charged constituents of each atom).

#### Worked Example: Gravity Versus Electromagnetism for Two Protons

{numref}`Table %s <tab:ch14-fundamental-interactions>` states that gravity is weaker than the strong interaction by a factor of order $10^{-38}$; it is worth seeing this concretely for the simplest possible case — two protons separated by some distance $r$ — where both the gravitational attraction and the electric (Coulomb) repulsion are exactly known, textbook formulas requiring no particle-physics machinery at all:

$$
\frac{F_{\text{grav}}}{F_{\text{EM}}} = \frac{Gm_p^2/r^2}{ke^2/r^2} = \frac{Gm_p^2}{ke^2},
$$

independent of $r$, since both forces obey the same inverse-square law and the separation cancels out of the ratio. Substituting $G = 6.674\times10^{-11}\ \text{N}\cdot\text{m}^2/\text{kg}^2$, $m_p = 1.673\times10^{-27}\ \text{kg}$, $k = 8.988\times10^{9}\ \text{N}\cdot\text{m}^2/\text{C}^2$, and $e = 1.602\times10^{-19}\ \text{C}$,

$$
\frac{F_{\text{grav}}}{F_{\text{EM}}} = \frac{(6.674\times10^{-11})(1.673\times10^{-27})^2}{(8.988\times10^{9})(1.602\times10^{-19})^2} \approx 8\times10^{-37},
$$

consistent, to within the precision either figure is normally quoted, with the ratio of the two relative-strength entries in {numref}`Table %s <tab:ch14-fundamental-interactions>` ($10^{-38}/10^{-2} = 10^{-36}$). Gravity between two individual protons is roughly $36$ orders of magnitude weaker than their mutual electric repulsion — so extreme that no experiment has ever measured the gravitational force between two elementary particles directly; it is simply swamped by every other force present. Gravity dominates only on macroscopic and astronomical scales because mass is exclusively attractive and accumulates without limit (every proton in a star adds to the same gravitational pull), whereas electric charge comes in both signs and ordinary bulk matter is almost perfectly charge-neutral, so the electromagnetic forces of its enormous number of individual charges cancel to a degree gravity's never does. This is also, precisely, why the graviton remains hypothetical in {numref}`Table %s <tab:ch14-fundamental-interactions>`: a force this feeble, acting between single particles, is far beyond the reach of any conceivable particle-physics detector, and quantum gravity remains an unsolved theoretical problem rather than an experimentally accessible one, as the Open Questions section at the end of this chapter discusses further.

Of the four, the weak interaction is the one with no everyday signature to point at — it is too short-ranged to hold anything together and too feeble to push anything around — and its importance is easy to underrate as a result. Its distinction is that it is the only interaction that changes one kind of quark into another, and {numref}`Figure %s <fig:ch14-beta-decay-sim>` is that transformation at work: a neutron ($udd$) becomes a proton ($uud$) by turning a down quark into an up quark, with an electron and an antineutrino carrying off the charge and lepton-number balance. None of the other interactions in {numref}`Table %s <tab:ch14-fundamental-interactions>` can do this. Without it, the proton-proton chain could never take its first step, no hydrogen would ever become helium, and stars would not shine.

```{phet-legacy} nuclear-physics/beta-decay
:label: fig:ch14-beta-decay-sim

Beta decay of a single nucleus and of a sample, with the emitted electron and antineutrino shown. The conservation laws catalogued later in this chapter can be read directly off the products: charge, baryon number, and electron lepton number each balance, event by event.
```

### Reading Feynman Diagrams

Every interaction catalogued in {numref}`Table %s <tab:ch14-fundamental-interactions>` — one particle scattering off another, one particle decaying into several — can be drawn as a **Feynman diagram**, a bookkeeping and visualization tool introduced by Richard Feynman in the late 1940s as part of the machinery that made precise calculations in quantum electrodynamics tractable (work for which Feynman shared the 1965 Nobel Prize with Julian Schwinger and Sin-Itiro Tomonaga). A Feynman diagram is not a literal picture of particle trajectories in space, the way a cloud-chamber photograph is; it is closer to a schematic circuit diagram, read according to a small set of fixed conventions:

- The vertical axis is **time**, increasing upward (some texts instead run time left to right; the convention adopted here matches the light-cone diagrams of [Chapter 2](#ch-special-relativity)). The horizontal axis is space, drawn schematically and not to scale.
- A straight line represents a **fermion** (a matter particle), with an arrow indicating the direction of particle flow. A particle's arrow points forward in time, in the direction the line is actually traversed; an **antiparticle** is drawn as its particle's line traversed backward — the arrow points backward in time even though, like everything else in the diagram, the antiparticle itself only ever moves forward in time.
- A wavy or dashed internal line represents the **exchanged boson** that mediates the interaction — a photon, gluon, or $W^\pm$/$Z^0$, depending on which force is at work.
- A **vertex**, where lines meet, represents a single interaction. Every exactly-conserved quantity introduced in this chapter — electric charge above all — must balance at *each individual vertex*, not merely for the diagram as a whole, since a vertex is the fundamental, irreducible unit of interaction the Standard Model actually specifies.

The internal boson line is called **virtual**: unlike an external line (an actual incoming or outgoing particle, which must satisfy the energy–momentum relation $E^2=(pc)^2+(mc^2)^2$ of [Chapter 3](#ch-relativistic-dynamics) for its own rest mass), a virtual particle is permitted to briefly violate that relation, borrowing the energy it needs from the energy–time form of the uncertainty principle ([Chapter 7](#ch-wave-properties-of-particles)) for a time short enough, and hence a distance short enough, that the "loan" is never actually observable. This is, in fact, precisely what sets the range entries in {numref}`Table %s <tab:ch14-fundamental-interactions>`: a virtual particle of mass $m$ can travel no farther than roughly $\hbar/(mc)$ before it must be reabsorbed, so a massless exchanged boson (the photon, or, in the residual sense of [Chapter 13](#ch-nuclear-physics), the gluon-mediated force between nucleons) gives a force of unlimited range, while the massive $W^\pm$ and $Z^0$ ($m_Wc^2 \approx 80.4\ \text{GeV}$) confine the weak interaction to a range of only $\hbar c/(m_Wc^2) \approx (197\ \text{MeV}\cdot\text{fm})/(8.04\times10^4\ \text{MeV}) \approx 2\times10^{-3}\ \text{fm}$ — matching the table's entry to within the precision it is normally quoted.

{numref}`Figure %s <fig:ch14-feynman-diagrams>` shows two of the simplest possible diagrams, one for each of two very different interactions.

```{figure} ../images/ch14-feynman-diagrams.svg
:label: fig:ch14-feynman-diagrams
:alt: Two Feynman diagrams, one for electron-electron scattering via photon exchange and one for neutron beta decay via W-boson exchange, with time running upward.

Left: two electrons scatter by exchanging a virtual photon — the same photon whose particle nature was established in [Chapter 6](#ch-particle-properties-of-waves), here playing the role of the electromagnetic force carrier at the vertex level. Right: a neutron decays to a proton by emitting a virtual $W^-$, which itself decays to an electron and an electron antineutrino; the antineutrino's arrow points backward in time, marking it as an antiparticle. Original schematic by the author.
```

The left-hand diagram is the quantum-field-theoretic picture underlying ordinary Coulomb repulsion: two electrons never touch, but exchange a virtual photon at a single vertex on each of their two lines, each vertex conserving charge trivially (an electron's charge is unchanged by absorbing or emitting an uncharged photon). The right-hand diagram redraws the beta-decay process already introduced above, but at the level of an individual quark rather than the nucleon as a whole: it is really the neutron's down quark that emits the virtual $W^-$ and converts directly to an up quark, turning $udd$ into $uud$, while the neutron's other two quarks look on as unaffected spectators. This is also the precise reason the weak interaction, uniquely among the four, can change a quark's flavor at all. At a photon or gluon vertex, the boson emitted or absorbed carries zero electric charge, so charge conservation alone forces the quark's charge — and hence its flavor family — to be exactly the same before and after; a $d$ quark ($-\tfrac13e$) simply cannot become a $u$ quark ($+\tfrac23e$) at such a vertex without violating charge conservation right there at the vertex. The $W^\pm$ boson is the only carrier with nonzero electric charge ($\pm e$), and $\pm e$ is exactly the charge difference between an up-type and a down-type quark in the same generation ($Q(u)-Q(d) = \tfrac23e - (-\tfrac13e) = e$), so only a $W^\pm$ vertex has the right charge budget to convert one into the other.

:::{margin}
The generic term for a quark or lepton type — up, down, strange, charm, top, bottom for quarks; electron, muon, tau (and their neutrinos) for leptons — is **flavor**. Flavor is independent of the color charge introduced later in this chapter: two quarks of the same flavor, two up quarks say, can still carry different colors.
:::

#### Worked Example: Reading a Feynman Diagram

Verify, vertex by vertex, that the beta-decay diagram in {numref}`Figure %s <fig:ch14-feynman-diagrams>` conserves charge, baryon number, and lepton number at *each* vertex individually, not merely for the overall reaction $n \to p + e^- + \bar\nu_e$ already checked earlier in this chapter.

**First vertex** ($n \to p + W^-$): charge before is $0$ (the neutron); charge after is $Q(p) + Q(W^-) = (+e) + (-e) = 0$. Balanced. Baryon number before is $+1$ ($n$); after, $B(p) = +1$ and $B(W^-)=0$ (the $W$ is a boson, carrying no baryon number), so $B_{\text{after}} = +1$. Balanced.

**Second vertex** ($W^- \to e^- + \bar\nu_e$): charge before is $-e$ (the $W^-$); charge after is $Q(e^-)+Q(\bar\nu_e) = (-e) + 0 = -e$. Balanced. Lepton number ($L_e$) before is $0$ (the $W$ carries none); after, $L_e(e^-) = +1$ and $L_e(\bar\nu_e) = -1$, summing to $0$. Balanced.

Every conservation law holds separately at each vertex, which is both a check on the diagram and the deeper reason the *overall* reaction conserves these quantities in the first place: a multi-vertex process can only conserve a quantity globally if every individual vertex conserves it, since nothing is allowed to leak in or out of an internal line that connects two vertices back to back.

## Accelerators, Leptons, and Quarks

### Particle Accelerators and Detectors

None of the particle content, forces, or conservation laws catalogued in this chapter were read directly off nature; they were inferred, often at great technical and financial cost, from what came out of high-energy collisions. A **particle accelerator** uses electric fields to increase a charged particle's kinetic energy, typically bending its path into a circle with magnetic fields (a **synchrotron**, of exactly the type used at the Bevatron introduced in [Chapter 3](#ch-relativistic-dynamics)) so that the same beam can be accelerated repeatedly on each pass rather than only once, as in a straight-line (linear) accelerator. That beam is then steered into a collision — either against a stationary target (**fixed-target**) or head-on against a second, oppositely circulating beam (a **collider**) — and the CM-frame threshold-energy analysis of [Chapter 3](#ch-relativistic-dynamics) governs, in either case, exactly how much beam energy is needed to produce a given final state.

What comes out of the collision is reconstructed by a **detector**, typically built in concentric layers immediately surrounding the collision point: an inner **tracking** layer, threaded by a magnetic field, records the curved paths of charged particles, whose momentum is read off from the radius of curvature via $p=qBr$ — the same relation used to test $p=\gamma m u$ directly in [Chapter 3](#ch-relativistic-dynamics); beyond that, a **calorimeter** stops most particles outright and measures their energy from the size of the resulting shower of secondary particles; and an outermost layer specifically identifies **muons**, since a muon, carrying no strong-interaction charge and losing energy only slowly, is typically the only charged particle able to punch all the way through the calorimeter's absorbing material. Combining the tracking, calorimetry, and timing information from every layer, for millions of collisions per second, is how a modern detector reconstructs which particles were actually produced in each individual event — the only way any of the particles, decay modes, and conservation laws in this chapter were ever actually established.

The largest such machine ever built is the Large Hadron Collider (**LHC**), operated by CERN outside Geneva: a 27-kilometer circular tunnel in which two counter-circulating proton beams are accelerated to several $\text{TeV}$ each ($1\ \text{TeV} = 10^3\ \text{GeV} = 10^6\ \text{MeV}$) before colliding head-on at four points around the ring, each instrumented with a detector of exactly the layered design just described. Two of those detectors, ATLAS and CMS, are shown mid-construction in {numref}`Figure %s <fig:ch14-atlas-historical>`; it was data from detectors of this kind, sifted from many billions of recorded collisions, that produced the statistically decisive evidence for the Higgs boson announced in 2012 and discussed further below.

:::{margin}
Particle physicists routinely quote a particle's rest mass directly in energy units via $E=mc^2$, dropping the "$/c^2$" as understood: "the $W$ boson's mass is $80.4\ \text{GeV}$" and "$m_Wc^2=80.4\ \text{GeV}$," used earlier in this chapter, mean exactly the same thing. Taken to its logical conclusion, this is the field's **natural-unit** convention $c=\hbar=1$, in which mass, momentum, and energy all share a single unit.
:::

```{figure} ../images/historical-atlas-detector.jpg
:width: 45%
:label: fig:ch14-atlas-historical
:alt: Historical photograph looking down into the ATLAS detector cavern at CERN during its construction, showing the detector's large wheel-shaped toroid magnet structures.

The ATLAS detector at CERN, photographed during construction in February 2007; the detector's wheel-shaped toroid magnets, used to bend and measure the momentum of outgoing muons, are visible at either side. Photograph by Sindre Skrede, 2007; released into the public domain via Wikimedia Commons.
```

Not every particle produced in a collision leaves a signal a detector can see. A neutrino — carrying no electric charge and feeling only the weak interaction — passes through even a large, modern detector's tracking, calorimetry, and muon layers essentially undisturbed, exactly as it passes through the Earth itself; no detector built or conceivably buildable stops enough neutrinos to identify one directly, event by event, in this setting. Its presence is instead inferred exactly as Pauli originally inferred it from the continuous beta-decay energy spectrum ([Chapter 13](#ch-nuclear-physics)), but applied now to *momentum* rather than energy: because the two colliding beams carry zero net momentum transverse to the beam direction, any transverse momentum imbalance among everything the detector *does* see must have been carried away by whatever escaped unseen.

#### Worked Example: Inferring a Missing Neutrino from Momentum Conservation

Suppose a collision event at a detector produces several visible particles (tracked and measured by the calorimeter) whose momentum components transverse to the beam sum to $p_x = 12.4\ \text{GeV}/c$ and $p_y = -5.1\ \text{GeV}/c$. Since the incoming beams carry zero net transverse momentum by construction, conservation of momentum requires the missing transverse momentum, carried by one or more undetected particles (a neutrino, most often), to be exactly the negative of the visible sum:

$$
p_x^{\text{miss}} = -12.4\ \text{GeV}/c, \qquad p_y^{\text{miss}} = +5.1\ \text{GeV}/c,
$$

with magnitude $|\vec p^{\,\text{miss}}| = \sqrt{(12.4)^2+(5.1)^2}\ \text{GeV}/c \approx 13.4\ \text{GeV}/c$. A sizable "missing transverse momentum" of exactly this kind, event after event, was part of the experimental signature used to identify $W$-boson production and decay ($W \to e^-+\bar\nu_e$ or $\mu^-+\bar\nu_\mu$) in the collider experiments of the 1980s, and remains a routine tool today for tagging any collision producing a neutrino (or, in searches for physics beyond the Standard Model, any other weakly-interacting particle that would likewise escape undetected — including, potentially, a dark-matter particle of the kind discussed in Open Questions below).

#### Worked Example: Threshold Energy for Pion Production

The fixed-target threshold method of [Chapter 3](#ch-relativistic-dynamics)'s worked example on antiproton production applies to any particle-creation reaction, not only that one. Consider a proton beam striking a stationary proton target and producing a neutral pion, $p+p \to p+p+\pi^0$, with $m_{\pi^0}c^2 = 135.0\ \text{MeV}$. Following exactly the same method, with $M = 2m_p + m_{\pi^0}$ in place of the antiproton reaction's $4m_p$:

$$
(2m_p+m_{\pi^0})^2c^4 = (E_1+m_pc^2)^2 - (p_1c)^2 = 2m_p^2c^4 + 2E_1m_pc^2.
$$

Expanding the left side and solving for the beam proton's total energy $E_1$,

$$
E_1 = m_pc^2 + 2m_{\pi^0}c^2 + \frac{(m_{\pi^0}c^2)^2}{2m_pc^2},
$$

so the threshold *kinetic* energy is

$$
K_1 = E_1 - m_pc^2 = 2m_{\pi^0}c^2 + \frac{(m_{\pi^0}c^2)^2}{2m_pc^2} = 2(135.0\ \text{MeV}) + \frac{(135.0\ \text{MeV})^2}{2(938.3\ \text{MeV})} \approx 270.0\ \text{MeV} + 9.7\ \text{MeV} = 280\ \text{MeV}.
$$

This is dramatically less demanding than the $6m_pc^2 \approx 5.6\ \text{GeV}$ threshold found for antiproton production in [Chapter 3](#ch-relativistic-dynamics), consistent with pion physics having been accessible to the very first generation of proton accelerators in the late 1940s and early 1950s, well before the antiproton search motivated the Bevatron. Reaching successively higher thresholds like these — hundreds of $\text{MeV}$ for pions, several $\text{GeV}$ for antiprotons and strange particles, hundreds of $\text{GeV}$ for the Higgs boson, and $\text{TeV}$-scale collision energies for direct searches beyond the Standard Model — is the entire history of why particle accelerators have grown, generation after generation, from tabletop devices to the 27-kilometer LHC.

### Leptons and Quarks

The Standard Model's fundamental matter fermions fall into two families, **leptons** and **quarks**, each organized into three repeating **generations** of increasing mass, with (as far as current experiments show) identical properties within a generation apart from mass:

:::{margin}
The names are Greek in origin and describe relative mass, not any structural property: **lepton** comes from *leptos* ("small, thin"), fitting how light the electron and its relatives are, while **hadron** (introduced below) comes from *hadros* ("stout, bulky"), coined only in 1962 once cosmic-ray and accelerator experiments had revealed a menagerie of strongly-interacting particles considerably heavier than any lepton.
:::

**Leptons** are fermions that do not feel the strong interaction. Each generation contains a charged lepton and a corresponding (essentially massless, electrically neutral) neutrino: the electron $e^-$ and electron neutrino $\nu_e$ (generation 1, the only stable charged lepton and the only leptons found in ordinary matter); the muon $\mu^-$ and muon neutrino $\nu_\mu$ (generation 2); and the tau $\tau^-$ and tau neutrino $\nu_\tau$ (generation 3). The muon and tau are, in essentially every respect apart from mass and consequent instability, heavier copies of the electron — the muon, for instance, decays via the weak interaction ($\mu^- \to e^- + \bar\nu_e + \nu_\mu$) with a mean lifetime of about $2.2\ \mu\text{s}$, far too short-lived to be found as a stable constituent of ordinary matter.

#### Worked Example: Muon Decay Length in a Particle Beam

A beam of muons is produced at a particle accelerator with kinetic energy $K = 300\ \text{MeV}$, well above the muon's rest energy $m_\mu c^2 = 105.7\ \text{MeV}$, so the relativistic machinery of [Chapter 3](#ch-relativistic-dynamics) is required rather than a Newtonian estimate. The total energy is $E = K + m_\mu c^2 = 405.7\ \text{MeV}$, so

$$
\gamma = \frac{E}{m_\mu c^2} = \frac{405.7\ \text{MeV}}{105.7\ \text{MeV}} = 3.84, \qquad \beta = \sqrt{1-\frac{1}{\gamma^2}} = 0.966,
$$

giving a lab-frame speed $v = 0.966c$. Time dilation ([Chapter 2](#ch-special-relativity)) stretches the muon's proper mean lifetime $\tau_0 = 2.20\ \mu\text{s}$ to a lab-frame mean lifetime $\tau = \gamma\tau_0 = (3.84)(2.20\ \mu\text{s}) = 8.44\ \mu\text{s}$, so the mean distance the beam travels before decaying away is

$$
L = v\tau = (0.966)(3.00\times10^8\ \text{m/s})(8.44\times10^{-6}\ \text{s}) \approx 2.4\times10^3\ \text{m} = 2.4\ \text{km}.
$$

Even with time dilation stretching the muon's lifetime nearly fourfold, the beam is reduced to a small fraction of its original intensity within a couple of kilometers — a distance that accelerator and neutrino-beam facilities (which create intense neutrino beams by steering a pion beam down a long "decay pipe" and collecting the neutrinos from the resulting pion, and then muon, decays) must design around explicitly, and exactly the same time-dilation effect responsible for cosmic-ray muons reaching Earth's surface at all, applied here to a laboratory beam instead of the atmosphere.

**Quarks** are fermions that do feel the strong interaction, and — unlike leptons — are never observed as free, isolated particles (a phenomenon called **confinement**, discussed further below). The three generations are: up ($u$) and down ($d$) (generation 1, the constituents of ordinary protons and neutrons); charm ($c$) and strange ($s$) (generation 2); and top ($t$) and bottom ($b$) (generation 3). Quarks carry fractional electric charge, $+\tfrac23 e$ ($u$, $c$, $t$) or $-\tfrac13 e$ ($d$, $s$, $b$), the only known particles to do so, and additionally carry a strong-interaction charge called **color** (in three varieties, whimsically named red, green, and blue, with no relation to visible color), which plays a role for the strong force directly analogous to the role electric charge plays for the electromagnetic force.

For every lepton and quark there exists a corresponding **antiparticle**, with identical mass and spin but opposite electric charge (and, for quarks, opposite color) — the electron's antiparticle, the positron, was introduced already in [Chapter 6](#ch-particle-properties-of-waves)'s discussion of pair production, and the same particle-antiparticle structure is universal across all Standard Model fermions.

{numref}`Figure %s <fig:ch14-standard-model-chart>` collects everything catalogued so far — three generations apiece of quarks and leptons, plus the gauge bosons of {numref}`Table %s <tab:ch14-fundamental-interactions>` and the Higgs boson introduced later in this chapter — into a single chart of the Standard Model's complete particle content.

```{figure} ../images/ch14-standard-model-chart.svg
:label: fig:ch14-standard-model-chart
:alt: Grid chart of the Standard Model's fundamental particles: three generations each of up-type quarks, down-type quarks, charged leptons, and neutrinos, plus the photon, gluon, W and Z bosons, and the Higgs boson.

The Standard Model's fundamental particles: three repeating generations of matter fermions (quarks and leptons), plus the force-carrying gauge bosons and the Higgs boson, neither of which come in generations. Original schematic by the author, redrawn independently of the familiar CERN/Wikipedia layout.
```

## Hadrons, Conservation Laws, and Open Questions

### Hadrons and Confinement

Quarks are never seen individually; they are always found bound into composite particles called **hadrons**, a consequence of quark confinement: unlike the Coulomb or nuclear forces encountered so far, which weaken with distance, the strong force between two quarks does *not* weaken as they are pulled apart — instead, the energy stored in the strong-force field between them grows without bound, so that attempting to separate two quarks (e.g., in a high-energy collision) eventually supplies enough energy, via mass–energy equivalence, to spontaneously create a new quark-antiquark pair from the field energy itself, snapping the field into two shorter, separately confined pieces rather than yielding a single free quark. Hadrons are observed in exactly two configurations, both of which happen to have net integer electric charge and (color-)neutral total color charge, consistent with confinement always producing color-neutral bound states:

- **Baryons**: three quarks bound together (or three antiquarks, for antibaryons). The proton ($uud$) and neutron ($udd$) are the lightest, most familiar baryons; baryons are fermions (three half-integer spins combine to a net half-integer spin) and obey a conservation law, **baryon number** (discussed below).
- **Mesons**: a quark-antiquark pair. Mesons, such as the pion ($\pi^+ = u\bar d$, among others), are bosons (a half-integer spin combined with a half-integer spin gives an integer net spin) and carry baryon number zero.

:::{dropdown} The Confinement Potential: A Toy Model
The qualitative story above — that the strong-force field between two quarks stores energy without bound as they separate — can be made quantitative with a simple model that captures the essential physics. Unlike the Coulomb potential $V(r)\propto -1/r$, which weakens with distance because electric field lines spread out to fill three-dimensional space, the gluon field between a quark and an antiquark is observed, both experimentally and in lattice-QCD calculations, to collapse into a narrow, roughly constant-cross-section **flux tube**, so that separating the two ends by a distance $r$ requires an energy that grows *linearly*,

$$
V(r) \approx \sigma r,
$$

where $\sigma$, the **string tension**, is measured to be about $1\ \text{GeV/fm}$. Once the stored energy $\sigma r$ climbs to a few hundred $\text{MeV}$ — comparable to the energy needed to create a light quark-antiquark pair from the vacuum via $E=mc^2$ — it becomes energetically cheaper for the field to supply that pair than to keep stretching, so the flux tube snaps into two shorter, separately confined pieces rather than yielding an isolated quark. This typically happens after the tube has stretched only about $1\ \text{fm}$, comparable to a hadron's own size, which is exactly why no accelerator, however powerful, can pull a free quark out of a hadron: pushing $r$ larger simply manufactures more hadrons, never a lone one.
:::

#### Worked Example: Quark Content of the $K^+$ Meson

The $K^+$ meson (a **kaon**), like the pion above, is a quark-antiquark pair, but built from a different combination: $K^+ = u\bar s$, an up quark bound to a strange *antiquark*. Every antiquark carries the exact opposite electric charge of its corresponding quark, so $\bar s$ (the antiparticle of the $-\tfrac13e$ strange quark) carries $+\tfrac13e$, and

$$
Q(K^+) = Q(u) + Q(\bar s) = +\frac23e + \frac13e = +e,
$$

matching the kaon's experimentally known charge of $+e$ exactly. Like the pion, the $K^+$ is a boson with baryon number zero — but unlike the pion, it carries a nonzero **strangeness**: the strange antiquark $\bar s$ carries strangeness $+1$ (opposite the strange quark's $S=-1$, by the sign convention introduced below), while the up quark carries $S=0$, giving $S(K^+) = +1$. This one extra bookkeeping number, absent from the pion, is exactly what made kaons behave so differently from pions when both were first encountered in cosmic-ray data — the subject of the next section.

#### Historical Context: The Particle Zoo

The tidy classification of hadrons into baryons and mesons, each built from a handful of quark flavors, is a retrospective simplification of what was, for roughly three decades, one of the most disorienting periods in the history of physics. Cosmic rays — high-energy particles arriving from space and colliding with nuclei in the upper atmosphere — were, before particle accelerators reached comparable energies, the only available source of exotic new particles, and they did not disappoint. In 1936–1937, Carl Anderson and Seth Neddermeyer, studying cosmic-ray tracks in a cloud chamber, identified a new particle with a mass about $200$ times the electron's — initially mistaken for the meson Hideki Yukawa had predicted the previous year as the carrier of the nuclear force, but eventually recognized (it interacted far too weakly, and penetrated far too much matter, to be Yukawa's particle) as an entirely new, heavier cousin of the electron: the **muon**, already met above. Yukawa's actual meson turned up a decade later, in 1947, when Cecil Powell, Giuseppe Occhialini, and César Lattes, examining photographic emulsions exposed at high-altitude observatories, identified the **pion**, caught in the act of decaying into exactly the muon Anderson and Neddermeyer had already found — untangling, at a stroke, two distinct particles that had been conflated for a decade. That same year, George Rochester and Clifford Butler, also working from cosmic-ray cloud-chamber photographs, found still stranger tracks: V-shaped pairs of particle trails, produced abundantly yet decaying only slowly — the signature of what came to be called, aptly, **strange particles**: the kaons of the worked example above, and the lightest hyperons (baryons heavier than the proton and neutron, such as the $\Lambda^0$ introduced earlier in this chapter).

By the 1950s, particle accelerators had overtaken cosmic rays as the primary discovery tool, and the pace of discovery, if anything, accelerated: dozens of "elementary" hadrons were catalogued through that decade and into the next, with no organizing principle in sight — derisively called the **particle zoo** by physicists who had expected nature's fundamental building blocks to be few in number, not a sprawling menagerie. Order emerged in 1961, when Murray Gell-Mann and, independently, Yuval Ne'eman noticed that plotting hadrons by electric charge against strangeness placed each family into strikingly regular geometric patterns — hexagons and triangles of eight or ten particles apiece — a scheme Gell-Mann named the **eightfold way**. The scheme's predictive power was demonstrated dramatically in 1964, when a particle it predicted but which had not yet been observed, the $\Omega^-$ baryon, was found at Brookhaven National Laboratory with essentially the predicted mass, charge, and strangeness. That same year, Gell-Mann and, independently, George Zweig proposed the deeper explanation for why the pattern worked at all: every hadron in the eightfold way's patterns is simply a bound state of a small number of still more fundamental constituents, which Gell-Mann named **quarks** — the up, down, and strange quarks already introduced in this chapter, with the heavier charm, bottom, and top quarks discovered only later, between 1974 and 1995, as accelerators reached the correspondingly higher energies needed to produce them. What had looked, in the 1950s, like a hopeless proliferation of unrelated "elementary" particles turned out to be nothing more than the many possible ways of combining a mere handful of truly fundamental building blocks — precisely the kind of underlying simplicity the Standard Model was built to express.

:::{seealso} Predicting the Unknown from a Pattern
The eightfold way's success in predicting the $\Omega^-$ before it was ever observed is not a one-off in the history of physics. [Chapter 11](#ch-many-electron-atoms) recounts how Moseley's law, another purely empirical pattern relating a measured quantity ($\sqrt f$, there; charge and strangeness, here) to an integer index, correctly predicted the existence of three then-undiscovered elements ($Z=43$, $61$, $75$) from gaps in an otherwise orderly sequence. In both cases, an organizing pattern was trusted well before anyone understood *why* it held — the "why" (electron shell structure in one case, quark substructure in the other) came only afterward.
:::

:::{note} Where the Name "Quark" Came From
Gell-Mann's name for the new constituents was borrowed, by his own account, from a nonsense line in James Joyce's *Finnegans Wake* — "Three quarks for Muster Mark!" — which happened to fit neatly with the three quark flavors ($u$, $d$, $s$) known at the time. Zweig, who proposed the same constituents independently and simultaneously, called them "aces" instead; Gell-Mann's name, and his convention of fractional-$e$ electric charges, is the one the entire field still uses today.
:::

### Conservation Laws

Not every combination of particles satisfying energy-momentum conservation is actually observed to occur; particle reactions additionally obey several conservation laws, some familiar from earlier chapters and some new to particle physics:

- **Electric charge** is conserved in every known interaction, without exception.
- **Baryon number** $B$ (defined as $+1$ for each baryon, $-1$ for each antibaryon, $0$ for all other particles, including mesons and leptons) is conserved in every observed reaction — this is why, for instance, the proton, the lightest baryon, is observed to be stable (or at least extremely long-lived: no proton decay has ever been observed, despite dedicated searches, placing its lifetime, if it decays at all, above $10^{34}$ years), since there is no lighter baryon for it to decay into consistent with $B$ conservation.
- **Lepton number**, separately for each generation ($L_e$, $L_\mu$, $L_\tau$, each $+1$ for the corresponding particle, $-1$ for its antiparticle, $0$ otherwise), is conserved to good approximation in essentially all observed reactions (this is why, for example, muon decay $\mu^- \to e^- + \bar\nu_e + \nu_\mu$ produces *both* an electron antineutrino and a muon neutrino, rather than either alone, to separately conserve $L_e$ and $L_\mu$: the initial state has $L_\mu = +1, L_e = 0$, and only the combination $\bar\nu_e + \nu_\mu$ on the right-hand side reproduces $L_e=0$, $L_\mu=+1$ on the left).

These conservation laws function exactly as energy, momentum, and angular momentum conservation do in earlier chapters: a proposed reaction consistent with all other physics can nonetheless be immediately ruled out if it violates one of these rules, and they provide a fast, purely bookkeeping-based check on whether an observed or hypothesized particle process is allowed.

#### Strangeness: An (Almost) Conserved Quantum Number

The particle-zoo puzzle described above is also where **strangeness** $S$ enters as a genuine, book-keepable quantum number, alongside charge, baryon number, and lepton number. Strangeness is assigned by quark content: $S=-1$ for each strange quark $s$ a particle contains, $S=+1$ for each strange antiquark $\bar s$, and $S=0$ for every other quark flavor (a sign convention fixed historically, before quarks themselves were proposed, when strangeness was assigned directly to particles from their production and decay patterns rather than derived from a quark that had not yet been identified). The defining, and at first deeply puzzling, experimental fact about strangeness is that it is treated differently by different interactions:

- The **strong** and **electromagnetic** interactions conserve strangeness exactly, in every observed reaction.
- The **weak** interaction does not: a single weak vertex can change strangeness by exactly $\pm 1$, consistent with a $W^\pm$ vertex converting an $s$ quark to a $u$ quark, or vice versa, one unit of strangeness at a time (the same charge-budget argument given above for why only the weak interaction changes quark flavor at all).

This single fact resolves Rochester and Butler's original puzzle: strange particles were produced copiously but decayed reluctantly because **associated production**, the strong-interaction process that actually creates strange particles in accelerator and cosmic-ray collisions (worked through below), always creates strangeness in matched pairs summing to the initial strangeness of zero — consistent with strong-interaction conservation, and proceeding on the characteristically fast strong-interaction timescale of order $10^{-23}\ \text{s}$. But once created, an isolated strange particle such as the $\Lambda^0$ has no strangeness-*conserving* decay available to it: there is no lighter, non-strange combination of ordinary particles it can fall apart into without changing $S$. It can only decay via the strangeness-violating weak interaction, on the correspondingly slow weak-interaction timescale — typically $10^{-10}\ \text{s}$, some thirteen orders of magnitude longer than a typical strong-interaction process, though still far too brief to see with the naked eye. Produced fast, decaying slow: hence "strange."

:::{tip} A Fast Checklist for Particle Reactions
When checking whether a proposed reaction is allowed, work through the conservation laws in order of how absolute they are, not in the order this chapter introduced them. Charge and baryon number are conserved without exception in every observed process, so check those first — a violation there kills the reaction outright, with no further work needed. Lepton number, checked separately per generation, is next, similarly exception-free in every confirmed observation. Only then check strangeness, and check it last precisely because it is *allowed* to change: a reaction with $\Delta S=0$ can proceed strongly or electromagnetically, $\Delta S=\pm1$ can only proceed weakly, and $\Delta S=\pm2$ or more is forbidden outright, since no single vertex changes strangeness by more than one unit. The size of $\Delta S$, in other words, is itself a fast diagnostic for *which* interaction a reaction must proceed through.
:::

#### Worked Example: Strangeness Conservation in Associated Production and Decay

Consider two reactions involving the $\Lambda^0$ ($uds$) introduced earlier in this chapter and the $K^0$ meson ($d\bar s$):

$$
\pi^- + p \to K^0 + \Lambda^0 \qquad \text{(associated production)}, \qquad \Lambda^0 \to p + \pi^- \qquad \text{(the $\Lambda^0$'s actual decay)}.
$$

Neither the pion nor the proton on the left of the first reaction contains a strange quark ($\pi^- = \bar u d$, $p = uud$), so the total initial strangeness is $S_i = 0$. On the right, $K^0 = d\bar s$ carries $S=+1$ (from its $\bar s$) and $\Lambda^0=uds$ carries $S=-1$ (from its $s$), for a total final strangeness $S_f = (+1)+(-1) = 0$. Strangeness is conserved — consistent with this reaction proceeding via the strong interaction, exactly the associated-production mechanism described above, with the $K^0$ and $\Lambda^0$ created together, their strangeness values canceling. (Charge and baryon number are conserved as well: $Q$: $-e+e=0=0+0$; $B$: $1+0=0+1$.)

The second reaction, the $\Lambda^0$'s actual decay, is different: $S_i = S(\Lambda^0) = -1$, while $S_f = S(p) + S(\pi^-) = 0+0=0$, a change of $\Delta S = +1$ — forbidden for the strong or electromagnetic interaction, but allowed, one unit at a time, for the weak interaction. This is consistent with the $\Lambda^0$'s measured mean lifetime of about $2.6\times10^{-10}\ \text{s}$, squarely in the weak-interaction range, roughly $10^{13}$ times longer than the strong-interaction timescale on which the very same particle was created in the first reaction.

### The Higgs Mechanism

A long-standing puzzle in the Standard Model was that the mathematical framework describing the weak and electromagnetic interactions in a unified way most naturally predicts that all fundamental particles, including the electron and quarks, should be massless — directly contradicted by experiment. The resolution, proposed independently by several theorists in 1964 (and associated most closely with the name of Peter Higgs), is that space is permeated by a nonzero background field, the **Higgs field**, and that fundamental particles acquire mass through their interaction with this field: a particle that couples strongly to the Higgs field behaves as though it has large inertia (large mass) as it moves through the field, while a particle that does not couple to it (the photon, for instance) remains exactly massless. Associated with the Higgs field, exactly as the electromagnetic field has an associated particle (the photon) representing its quantized excitations, is the **Higgs boson**, whose discovery at the Large Hadron Collider in 2012 — decades after it was first predicted, and requiring a purpose-built accelerator capable of reaching the multi-hundred-GeV collision energies needed to produce it directly — provided direct experimental confirmation of the mechanism and completed the last missing piece of the Standard Model's particle content.

The strength of a given particle's coupling to the Higgs field is not itself predicted by the mechanism — it is a separate, measured number for every fermion and for the $W^\pm$/$Z^0$ bosons — but the *pattern* it produces is a striking, directly testable success: the more strongly a particle couples, the larger its mass, and the Standard Model's heaviest fermion, the top quark ($m_tc^2 \approx 173\ \text{GeV}$, almost the mass of an entire gold nucleus packed into one point particle), couples to the Higgs field roughly as strongly as the coupling can go, while the electron, some $300{,}000$ times lighter, couples correspondingly more weakly. The photon's exact masslessness is, in this same language, simply the statement that the photon does not couple to the Higgs field at all — a consequence of the specific way electroweak symmetry breaking mixes the underlying gauge bosons of the unified electroweak theory into the photon and the $W^\pm$/$Z^0$ observed today, with only the latter three acquiring mass from the mechanism.

:::{warning} The Higgs Field Explains Mass — But Not Most of Your Mass
It is tempting to read the Higgs mechanism as a complete explanation of why matter has mass, but for ordinary matter it accounts for only a small fraction of it. The Higgs mechanism generates the *fundamental* masses cataloged in {numref}`Figure %s <fig:ch14-standard-model-chart>` — the bare rest mass of an individual quark or electron, on its own, with nothing else around it. A proton's mass is not simply the sum of its three quarks' Higgs-generated masses: two up quarks and a down quark contribute barely $1\%$ of the proton's $938.3\ \text{MeV}$. The remaining $99\%$ is confinement energy — the strong-force flux-tube energy introduced above, plus the quarks' own relativistic kinetic energy, converted to rest mass via $E=mc^2$ exactly as in the nuclear mass defect of [Chapter 13](#ch-nuclear-physics). The Higgs field is why quarks and electrons have mass at all; confinement, not the Higgs field, accounts for almost all of the mass of everyday matter.
:::

### Open Questions

As the final chapter of this book, it is worth being explicit that the Standard Model, for all its precision and predictive success — every particle it predicts has now been found, and its predictions for their properties typically agree with experiment to several decimal places — is not a complete "theory of everything." Several major open questions define the current frontier of particle physics and cosmology, worth naming even though, unlike everything else in this book, none has yet been resolved:

- **Dark matter.** Galaxies and clusters of galaxies rotate and move as though they contain roughly five times more gravitating mass than is visible in stars, gas, and dust combined — a discrepancy first noted from galaxy rotation curves and since confirmed by multiple independent lines of evidence (gravitational lensing, the large-scale structure of the universe, the cosmic microwave background). No known Standard Model particle has the right properties — electrically neutral, stable or extremely long-lived, interacting only very weakly with ordinary matter — to account for it, and despite decades of dedicated direct-detection experiments, no dark-matter particle has yet been observed in the laboratory.
- **Matter–antimatter asymmetry.** [Chapter 6](#ch-particle-properties-of-waves) and this chapter both treat particles and antiparticles as, in most respects, perfectly symmetric, yet the observable universe is made overwhelmingly of matter, with no evidence anywhere of large antimatter regions — even though the Big Bang, run forward through known physics, should have produced matter and antimatter in almost exactly equal amounts, which would then have mutually annihilated into pure radiation and left nothing behind to form galaxies, stars, or the reader of this sentence. Explaining the tiny observed excess of matter over antimatter (**baryogenesis**) requires physics that violates matter–antimatter symmetry more thoroughly than the Standard Model's confirmed interactions currently account for.
- **Neutrino mass.** The Standard Model outlined in this chapter, in its original form, predicted neutrinos to be exactly massless, like the photon. Neutrino oscillation experiments — a neutrino produced in one flavor (say $\nu_\mu$) measured, some distance later, with a nonzero probability of being detected as a different flavor ($\nu_e$ or $\nu_\tau$) — demonstrated conclusively, beginning in the late 1990s, that neutrinos have a small but nonzero mass: a firmly established experimental fact with no settled place in the version of the Standard Model presented in this chapter, and one of the clearest concrete signs that the model, though successful, is not the final word.
- **Unification.** The electromagnetic and weak interactions are already understood as two facets of a single underlying "electroweak" interaction, unified at sufficiently high energy — a success this chapter's Higgs mechanism is part of. Many physicists suspect the strong interaction unifies with the electroweak interaction at a still higher energy (**grand unification**), and that gravity itself — entirely absent from the Standard Model, and still described only by Einstein's classical general relativity — must eventually be brought into a single quantum-mechanical framework together with the other three forces. Such a "theory of everything" remains, despite decades of effort (string theory and loop quantum gravity among the leading proposals), unconfirmed by any experiment.

These are not signs of failure so much as an honest map of where the frontier currently sits: the Standard Model surveyed in this chapter is, by a wide margin, the most thoroughly tested theory in the history of physics, and every one of these open questions is being actively pursued — at facilities from the LHC to underground dark-matter detectors to neutrino observatories — by the direct descendants of the same experimental methods, particle accelerators, colliders, and increasingly sophisticated layered detectors, introduced earlier in this chapter.

## Summary

- Particles are classified by spin as **fermions** (half-integer spin, obey the exclusion principle; matter is built from these) or **bosons** (integer spin, no exclusion restriction; forces are mediated by these).
- Four fundamental interactions — **strong**, **electromagnetic**, **weak**, and **gravitational** — are distinguished by relative strength, range, and mediating gauge boson (gluon, photon, $W^\pm/Z^0$, and the hypothesized graviton, respectively).
- Matter fermions are **leptons** (no strong interaction; electron, muon, tau and their neutrinos, across three generations) and **quarks** (feel the strong interaction, carry fractional charge and color, never observed free due to **confinement**).
- Quarks bind into color-neutral **hadrons**: **baryons** (three quarks, e.g. proton $uud$, neutron $udd$) and **mesons** (quark-antiquark pairs).
- **Conservation laws** — electric charge, baryon number, and (approximately, per generation) lepton number — determine which proposed particle reactions are physically allowed. **Strangeness** is a further, only-approximately-conserved quantity: exactly conserved by the strong and electromagnetic interactions, but changeable by $\pm 1$ per vertex under the weak interaction, which is why strange particles are produced quickly (via the strong interaction) but decay slowly (via the weak).
- The **Higgs field**, and its associated **Higgs boson** (discovered 2012), is the mechanism by which most fundamental Standard Model particles acquire mass.
- A **Feynman diagram** depicts a particle interaction as fermion lines (particle arrows forward in time, antiparticle arrows reversed) meeting at **vertices**, connected by internal, virtual boson lines; every exactly-conserved quantity must balance at each individual vertex, and only the charged $W^\pm$ boson can change a quark's flavor, since it alone carries enough charge to balance an up-type/down-type quark transition.
- **Particle accelerators** (linear or, more commonly, synchrotron-based) collide beams either against a fixed target or head-on in a **collider**, and layered **detectors** — tracking, calorimetry, and muon identification — reconstruct what each collision produced; the Large Hadron Collider at CERN is the largest such machine yet built.
- The **particle zoo** of hadrons discovered via cosmic rays and early accelerators (muon, 1936; pion and strange particles, 1947) was organized by the **eightfold way** (Gell-Mann and Ne'eman, 1961) and explained by the **quark model** (Gell-Mann and Zweig, 1964).
- Gravity is negligible for individual particles: the ratio of the gravitational to the electromagnetic force between two protons is only $\sim 10^{-36}$, because mass (unlike charge) is always attractive and accumulates without limit, while ordinary bulk matter is nearly charge-neutral.
- The Standard Model remains incomplete: **dark matter**, the **matter–antimatter asymmetry**, nonzero **neutrino mass**, and the search for a **unified** theory including gravity are among the major open questions at the current frontier of particle physics.

## Problems

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-1

Classify each of the following as a fermion or boson, based on its spin: photon ($s=1$), electron ($s=\tfrac12$), pion ($s=0$), proton ($s=\tfrac12$).
:::

:::{solution} ex-elementary-particles-and-the-standard-model-1
:label: sol-elementary-particles-and-the-standard-model-1
:class: dropdown

Particles with integer spin are bosons, while particles with half-integer spin are fermions.  Thus the photon ($s=1$) and pion ($s=0$) are bosons, whereas the electron ($s=\tfrac12$) and proton ($s=\tfrac12$) are fermions.  Therefore, photons and pions obey Bose statistics, while electrons and protons obey Fermi--Dirac statistics.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-2

Determine the electric charge of a baryon composed of $uds$ (this particle is the $\Lambda^0$) using the quark charges $+\tfrac23 e$ for $u$, $-\tfrac13 e$ for $d$ and $s$, and check your result against the known charge of the $\Lambda^0$ (zero).
:::

:::{solution} ex-elementary-particles-and-the-standard-model-2
:label: sol-elementary-particles-and-the-standard-model-2
:class: dropdown

Adding the constituent-quark charges gives

$$Q_{uds}=\left(+\frac23e\right)+\left(-\frac13e\right)+\left(-\frac13e\right)=0.$$

Therefore, the $uds$ baryon has charge $0$, in agreement with the neutral charge of the $\Lambda^0$.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-3

Determine whether each proposed reaction conserves charge, baryon number, and lepton number as required, and state which conservation law (if any) forbids the ones that are not allowed: (a) $p \to e^+ + \gamma$, (b) $n \to p + e^- + \bar\nu_e$, (c) $\mu^- \to e^- + \gamma$, (d) $p + p \to p + p + \pi^0$.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-3
:label: sol-elementary-particles-and-the-standard-model-3
:class: dropdown

For (a), the initial proton has $(Q,B,L)=(+1,+1,0)$, while $e^++\gamma$ has $(+1,0,-1)$; baryon number and lepton number fail, so it is forbidden.  For (b), both sides have $(Q,B,L)=(0,1,0)$, because $e^-$ has $L=+1$ and $\bar\nu_e$ has $L=-1$; it is allowed.  For (c), charge is conserved, but the initial state has $L_\mu=+1$ and the final state has $L_\mu=0$, so it is forbidden.  For (d), both sides have $Q=+2$, $B=2$, and $L=0$, so it is allowed if sufficient kinetic energy is supplied.

```{figure} ../images/ch14-sol-conservation-checklist.svg
:label: fig:ch14-sol-conservation-checklist
:alt: Table of four proposed reactions against charge, baryon number, and lepton number, marked pass or fail, plus a fifth row for the K minus plus p reaction from Problem 8 checked against charge, baryon number, and strangeness.

Reading conservation laws as a pass/fail table: (a) fails on two counts, (c) fails on lepton number alone, and (b), (d), and [Problem 8](#ex-elementary-particles-and-the-standard-model-8)'s reaction pass everything asked of them.
```

Therefore, (b) and (d) conserve all listed quantum numbers, whereas (a) violates $B$ and $L$ and (c) violates muon lepton number.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-4

Using the known quark content of the proton ($uud$) and neutron ($udd$), and the quark charges given in [Problem 2](#ex-elementary-particles-and-the-standard-model-2), verify that the proton has charge $+e$ and the neutron has charge $0$.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-4
:label: sol-elementary-particles-and-the-standard-model-4
:class: dropdown

For a proton, $Q_{uud}=\tfrac23e+\tfrac23e-\tfrac13e=+e$.  For a neutron,

$$Q_{udd}=\left(+\frac23-\frac13-\frac13\right)e=0.$$

Therefore, quark charges give the observed proton charge $+e$ and neutron charge $0$.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-5

The muon decays via $\mu^- \to e^- + \bar\nu_e + \nu_\mu$. Explain, using lepton-number conservation applied separately to the electron-generation number $L_e$ and muon-generation number $L_\mu$, why the decay $\mu^- \to e^- + \gamma$ alone (without the two neutrinos) is forbidden, even though it conserves charge, energy, and momentum.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-5
:label: sol-elementary-particles-and-the-standard-model-5
:class: dropdown

Initially, $\mu^-$ has $L_e=0$ and $L_\mu=+1$.  In $\mu^-\to e^-+\gamma$, the final electron has $L_e=+1$ and $L_\mu=0$, while the photon has both numbers zero.  The proposed final state therefore changes both generation numbers.  In the observed decay, $\bar\nu_e$ supplies $L_e=-1$ and $\nu_\mu$ supplies $L_\mu=+1$, so each total is restored.  Therefore, the neutrinos are required by separate electron- and muon-lepton-number conservation.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-6

Explain, in your own words, why quark confinement means that the constituent quarks of a proton can never be observed as free, isolated particles no matter how much energy is used to try to separate them, and contrast this with the behavior of the electromagnetic force between two separated electric charges, which weakens (rather than growing) with increasing separation.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-6
:label: sol-elementary-particles-and-the-standard-model-6
:class: dropdown

Separating colored quarks stores increasing energy in the strong-force field between them.  Before an isolated quark can emerge, the stored energy is sufficient to create a quark--antiquark pair, which forms new color-neutral hadrons instead.  By contrast, the electromagnetic force between charges decreases approximately as $1/r^2$, so separating charges requires progressively less additional force.  Therefore, quark confinement produces only color-neutral particles, whereas electric charges can be isolated.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-7

The $K^-$ meson has quark content $K^- = \bar u s$. (a) Using the quark charges given in [Problem 2](#ex-elementary-particles-and-the-standard-model-2) and the rule that an antiquark carries the opposite charge of its quark, find the electric charge of $K^-$. (b) Find its strangeness. (c) Explain why your results show that $K^-$ is the antiparticle of the $K^+$ found in the worked example on kaon quark content, and state the general rule (in terms of charge and strangeness) that a particle and its antiparticle must always satisfy.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-7
:label: sol-elementary-particles-and-the-standard-model-7
:class: dropdown

An anti-up quark has charge $-\tfrac23e$, and an $s$ quark has charge $-\tfrac13e$, so

$$Q_{\bar us}=-\frac23e-\frac13e=-e.$$

The $s$ quark has strangeness $S=-1$, so $K^-$ has $S=-1$.  The antiparticle $K^+$ has the opposite values, $Q=+e$ and $S=+1$.

```{figure} ../images/ch14-sol-kaon-antiparticle.svg
:label: fig:ch14-sol-kaon-antiparticle
:alt: K minus and K plus shown side by side with their quark content, charge, and strangeness, connected by a double arrow labeled antiparticles: opposite Q, opposite S.

Every additive quantum number a particle carries — not just charge — reverses sign for its antiparticle; $K^-$ and $K^+$ show this for both $Q$ and $S$ at once.
```

Therefore, $K^-$ is the antiparticle of $K^+$ because antiparticles have opposite additive quantum numbers, including charge and strangeness.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-8

Determine whether the reaction $K^- + p \to \Lambda^0 + \pi^0$ conserves charge, baryon number, and strangeness, and state whether it can proceed via the strong interaction, the weak interaction, or neither.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-8
:label: sol-elementary-particles-and-the-standard-model-8
:class: dropdown

Initially $K^-+p$ has $Q=-1+1=0$, $B=0+1=1$, and $S=-1+0=-1$.  Finally $\Lambda^0+\pi^0$ has $Q=0+0=0$, $B=1+0=1$, and $S=-1+0=-1$, the bottom row of {numref}`Figure %s <fig:ch14-sol-conservation-checklist>`.  Therefore, charge, baryon number, and strangeness are all conserved, so the reaction can proceed through the strong interaction.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-9

The muon decays via $\mu^- \to e^- + \bar\nu_e + \nu_\mu$ ([Chapter 2](#ch-special-relativity)), and, like neutron beta decay, this proceeds by $\mu^-$ emitting a virtual $W^-$ and converting directly into $\nu_\mu$ at one vertex, with the $W^-$ then decaying to $e^- + \bar\nu_e$ at a second vertex. Sketch this two-vertex diagram in the style of {numref}`Figure %s <fig:ch14-feynman-diagrams>`, and verify explicitly that electric charge and each generation's lepton number ($L_e$ and $L_\mu$ separately) balance at *each* vertex individually, following the method of the worked example on reading a Feynman diagram.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-9
:label: sol-elementary-particles-and-the-standard-model-9
:class: dropdown

Draw an incoming $\mu^-$ line ending at a vertex that emits an outgoing $\nu_\mu$ line and a virtual $W^-$ line; the $W^-$ ends at a second vertex in outgoing $e^-$ and $\bar\nu_e$ lines.  At the first vertex, $Q:-1=0+(-1)$ and $L_\mu:+1=+1+0$.  At the second, $Q:-1=-1+0$ and $L_e:0=+1+(-1)$.  All unmentioned generation numbers are zero on both sides.

```{figure} ../images/ch14-sol-muon-decay-feynman.svg
:label: fig:ch14-sol-muon-decay-feynman
:alt: Feynman diagram for muon decay with time running upward, an incoming mu minus turning into an outgoing nu mu at the first vertex, emitting a virtual W minus that decays at a second vertex into an outgoing electron and an outgoing antineutrino.

Drawn in the same style as {numref}`Figure %s <fig:ch14-feynman-diagrams>`: the $\mu^-$ converts to $\nu_\mu$ at vertex 1 while emitting a virtual $W^-$, which decays to $e^-+\bar\nu_e$ at vertex 2 — charge and each generation's lepton number balance separately at both vertices.
```

Therefore, each vertex separately conserves charge and the electron and muon lepton numbers.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-10

A second muon beam is produced with total energy $E = 1.20\ \text{GeV}$ (using $m_\mu c^2 = 105.7\ \text{MeV}$ and proper mean lifetime $\tau_0 = 2.20\ \mu\text{s}$, as in the worked example on muon decay length). Find (a) $\gamma$, (b) $\beta$, and (c) the mean decay length of this beam in the lab frame. Compare your answer to the $2.4\ \text{km}$ found in the worked example, and explain the direction of the difference in terms of $\gamma$.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-10
:label: sol-elementary-particles-and-the-standard-model-10
:class: dropdown

Convert the total energy to $1200\ \text{MeV}$.  Then

$$\gamma=\frac{E}{m_\mu c^2}=\frac{1200\ \text{MeV}}{105.7\ \text{MeV}}=11.35,$$

$$\beta=\sqrt{1-\gamma^{-2}}=\sqrt{1-\frac1{(11.35)^2}}=0.9961.$$

The mean lab lifetime is $\gamma\tau_0=(11.35)(2.20\ \mu\text{s})=25.0\ \mu\text{s}$, so

$$\ell=\beta c\gamma\tau_0=(0.9961)(3.00\times10^8\ \text{m/s})(25.0\times10^{-6}\ \text{s})=7.47\times10^3\ \text{m}.$$

```{figure} ../images/ch14-sol-muon-decay-length.svg
:label: fig:ch14-sol-muon-decay-length
:alt: Mean muon decay length versus total beam energy, rising smoothly, with the worked example's 2.4 kilometer point and this problem's 7.47 kilometer point both marked on the curve.

Both beams sit on the same $\beta c\gamma\tau_0$ curve; this problem's higher energy gives a larger $\gamma$ and a correspondingly longer mean decay length.
```

Therefore, this beam has $\gamma=11.35$, $\beta=0.9961$, and a mean decay length of $7.47\ \text{km}$, longer than $2.4\ \text{km}$ because its Lorentz factor is larger.
:::

:::{exercise}
:label: ex-elementary-particles-and-the-standard-model-11

Repeat the gravitational-versus-electromagnetic force-ratio calculation of the worked example in "The Four Fundamental Interactions," but for two electrons instead of two protons (using $m_e = 9.109\times10^{-31}\ \text{kg}$ in place of $m_p$, with $G$, $k$, and $e$ unchanged). Explain, in terms of the formula for the ratio, why the result is so much smaller than the two-proton ratio even though an electron and a proton carry exactly the same magnitude of electric charge.
:::

:::{solution} ex-elementary-particles-and-the-standard-model-11
:label: sol-elementary-particles-and-the-standard-model-11
:class: dropdown

For two identical particles, the force ratio is $F_G/F_E=Gm^2/(ke^2)$.  For electrons,

$$\frac{F_G}{F_E}=\frac{(6.674\times10^{-11}\ \text{N m}^2\! /\text{kg}^2)(9.109\times10^{-31}\ \text{kg})^2}{(8.988\times10^9\ \text{N m}^2\! /\text{C}^2)(1.602\times10^{-19}\ \text{C})^2}=2.4\times10^{-43}.$$

```{figure} ../images/ch14-sol-gravity-em-ratio.svg
:label: fig:ch14-sol-gravity-em-ratio
:alt: Log-scale bar chart comparing the gravity-to-electromagnetism force ratio for two protons and two electrons, with the electron ratio about six orders of magnitude smaller.

Same formula, same charge magnitude, but $m_e/m_p\approx1/1836$ enters squared: the electron ratio is smaller by roughly $(1836)^2\approx3.4\times10^6$.
```

Therefore, gravity between two electrons is only about $2.4\times10^{-43}$ of their electrical repulsion; the ratio is far smaller than for protons because it scales as $m^2$ while the charge magnitude is unchanged.
:::
