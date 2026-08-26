---
title: Relativistic Dynamics
short_title: Chapter 3. Relativistic Dynamics
label: ch-relativistic-dynamics
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain why the Newtonian definition of momentum, $p = mu$, is not conserved in all inertial frames once the Lorentz transformation replaces the Galilean transformation, and derive the corrected, relativistic definition from a symmetric elastic-collision thought experiment.
- Apply the relativistic expressions for momentum, kinetic energy, and total energy.
- Use the mass–energy relation $E = mc^2$ and the energy–momentum invariant $E^2 = (pc)^2 + (mc^2)^2$.
- Distinguish rest mass, relativistic momentum, kinetic energy, and total energy, and apply these to problems involving massive particles and photons.
- Represent energy and momentum as components of a single four-vector, and use conservation of this four-vector to analyze collisions, decays, and annihilation events.
- Transform to the center-of-momentum frame of a collision and compute threshold energies for particle-production reactions.
- Recognize the low-speed (Newtonian) and high-speed (ultrarelativistic) limits of the relativistic energy and momentum expressions.
- Explain why the combination of momentum blowing up as $u \to c$ and the causality argument of [Chapter 2](#ch-special-relativity) together rule out faster-than-light material particles.

## Introduction

[Chapter 2](#ch-special-relativity) replaced the Galilean transformation with the Lorentz transformation, because only the latter is consistent with the invariance of the speed of light. But momentum and energy in Newtonian mechanics are defined and conserved using Galilean kinematics: $p = mu$, conserved because Newton's third law and Galilean-invariant forces guarantee it in every Galilean frame. Once the underlying kinematics changes, the old definitions of momentum and energy no longer transform consistently between inertial frames, and a collision that conserves Newtonian momentum in one frame will not, in general, conserve it in another frame related by a Lorentz transformation. This chapter derives the corrected definitions — relativistic momentum and relativistic energy — that *are* conserved in every inertial frame, assembles them into a single four-component object whose conservation law captures both at once, and works out their most important consequences: mass and energy are, up to a conversion factor $c^2$, the same quantity, and a whole new class of practical calculations — threshold energies for particle production — becomes possible.

## Deriving Relativistic Momentum

Rather than simply asserting the corrected formula, it is worth seeing exactly where it comes from, because the argument is a direct descendant of the light-clock argument used to derive time dilation in [Chapter 2](#ch-special-relativity), and it makes clear that the correction is forced on us by the Lorentz transformation, not chosen for convenience.

Set up two identical particles, $A$ and $B$, each of rest mass $m$, in a symmetric elastic collision designed so that ordinary Newtonian intuition about "before" and "after" still applies to the parts of the motion parallel to the particles' relative velocity, while only the *perpendicular* (transverse) motion is used to track momentum. Let frame $S'$ move at speed $v$ along the $x$-axis relative to frame $S$. Particle $B$ is permanently at rest in $S$ except for a small transverse "bounce": as measured in $S$, $B$ moves with a small speed $w_0$ in the $+y$ direction, collides elastically with $A$ at the origin, and rebounds with speed $w_0$ in the $-y$ direction — a purely transverse, symmetric bounce, as measured in $S$. Particle $A$ undergoes the mirror-image motion, but as measured in *its own* rest frame $S'$: $A$ moves with speed $w_0$ in the $-y'$ direction, bounces elastically off $B$, and rebounds at $+w_0$ in $y'$, as measured in $S'$. Since $S'$ moves at speed $v$ relative to $S$, particle $A$'s velocity as measured in frame $S$ has an $x$-component of $v$ (the frame's relative velocity) and a $y$-component obtained from the velocity-transformation rule for the direction perpendicular to the boost: because $\Delta y = \Delta y'$ while $\Delta t = \gamma(v)\left(\Delta t' + v\Delta x'/c^2\right) = \gamma(v)\Delta t'$ for a particle with $\Delta x' = 0$, the transverse speed measured in $S$ is reduced by a factor of $\gamma(v)$ compared to the transverse speed $w_0$ measured in $S'$:

$$
u_y(A) = \frac{w_0}{\gamma(v)}, \qquad \text{as measured in } S.
$$

Now demand that the total $y$-momentum, as measured in frame $S$, be conserved by this collision — indeed, by the mirror symmetry of the setup (swapping the labels $A \leftrightarrow B$ together with $y \to -y$ maps the "before" configuration onto an equivalent "before" configuration), the total transverse momentum measured in $S$ must equal exactly zero, both before and after the bounce. Writing the momentum of a particle moving at speed $u$ as $p = m(u)\,u$, for some as-yet-undetermined function $m(u)$ that reduces to the particle's ordinary mass at $u=0$, this symmetry condition reads

$$
m\big(u(A)\big)\, u_y(A) \;-\; m\big(u(B)\big)\, w_0 \;=\; 0,
$$

where $u(A)$ and $u(B)$ denote the total (not just transverse) speeds of $A$ and $B$ in frame $S$. Substituting $u_y(A) = w_0/\gamma(v)$ and cancelling the common factor of $w_0$,

$$
\frac{m\big(u(A)\big)}{\gamma(v)} = m\big(u(B)\big).
$$

Finally, take the limit $w_0 \to 0$: in this limit, $B$'s transverse motion vanishes entirely, so $u(B) \to 0$ and $m(u(B)) \to m(0) \equiv m$, the particle's ordinary rest mass. Meanwhile $A$'s transverse velocity component also vanishes, leaving $A$ moving purely along $x$ at the frame's relative velocity, so $u(A) \to v$. The boxed relation becomes

$$
\frac{m(v)}{\gamma(v)} = m \quad \Longrightarrow \quad m(v) = \gamma(v)\, m,
$$

for *arbitrary* $v$, since $v$ was the (otherwise unconstrained) relative speed of the two frames. In other words, momentum conservation across inertial frames, together with the Lorentz transformation's effect on transverse velocities, forces the "effective mass" $m(u)$ appearing in $p = m(u)u$ to be exactly $\gamma(u)m$ — not simply $m$, as Newtonian mechanics assumed. This is the relativistic momentum derived below; unlike the Newtonian formula, it is exactly the definition needed to make momentum conservation frame-independent, consistent with the Lorentz transformation of [Chapter 2](#ch-special-relativity).

## Relativistic Momentum

The result of the argument above is

$$
\vec p = \gamma m \vec u = \frac{m\vec u}{\sqrt{1 - u^2/c^2}},
$$

where $m$ is the particle's **rest mass** — an intrinsic, frame-independent property of the particle, equal to the mass measured by an observer at rest relative to it — and $u$ is the particle's speed in the frame in question. For $u \ll c$, $\gamma \to 1$ and this reduces to the Newtonian $\vec p = m\vec u$. As $u \to c$, however, $\gamma \to \infty$, so $p \to \infty$ as well: **an infinite momentum, and correspondingly an infinite force applied for a finite time, would be needed to accelerate a massive particle to the speed of light.** This is the precise dynamical reason no massive object can reach or exceed $c$, complementing the kinematic argument of [Chapter 2](#ch-special-relativity) (relativistic velocity addition never produces $u \ge c$ from sub-light inputs).

### Worked Example: Testing $p = \gamma m u$ Against Data

The formula $\vec p = \gamma m \vec u$ is not merely a theoretical nicety; it has been tested directly by measuring the momentum and speed of fast electrons and protons independently — momentum from the radius of curvature in a known magnetic field ($p = qBr$), speed from time-of-flight over a measured distance. Historical experiments of exactly this kind (Rogers et al., 1940, for electrons; Zrelov et al., 1958, for protons, among others) confirm $p/(mu) = \gamma(u)$ to high precision across a wide range of speeds, and sharply rule out the Newtonian prediction $p/(mu) = 1$ at any appreciable fraction of $c$. For a proton with $u = 0.60c$, for instance, $\gamma = 1/\sqrt{1-0.36} = 1.25$, so the measured momentum is $25\%$ larger than the Newtonian formula would predict — a discrepancy easily resolved by 1950s particle-accelerator instrumentation, and one of the most direct confirmations that $m(u) = \gamma m$, not $m$, governs a moving particle's inertia.

## Relativistic Energy

A parallel argument — demanding that the work-energy theorem, $dK = \vec F\cdot d\vec x$, hold with the relativistic force $\vec F = d\vec p/dt$ — leads to the relativistic kinetic energy

$$
K = \gamma mc^2 - mc^2 = (\gamma - 1)mc^2.
$$

It is useful to expand this for $u \ll c$ using the binomial approximation $\gamma \approx 1 + \tfrac{1}{2}u^2/c^2 + \cdots$:

$$
K \approx \left(1 + \frac{1}{2}\frac{u^2}{c^2}\right)mc^2 - mc^2 = \frac{1}{2}mu^2,
$$

recovering the familiar Newtonian kinetic energy as the low-speed limit — a necessary consistency check, since Newtonian mechanics is extremely well tested at everyday speeds.

The kinetic energy expression separates naturally into two terms: $\gamma mc^2$, and a constant $mc^2$ subtracted off. Einstein's insight was to take both terms seriously as *energy*, not just their difference. Define the **total energy**

$$
E = \gamma mc^2,
$$

and the **rest energy**

$$
E_0 = mc^2.
$$

Then $K = E - E_0$: kinetic energy is the energy *above and beyond* the energy $mc^2$ a particle possesses simply by virtue of having rest mass $m$, even at rest ($u=0$, $\gamma=1$). This is the celebrated **mass–energy equivalence**: rest mass is a form of energy, convertible (in principle and, in nuclear and particle processes, routinely in practice) into other forms of energy, and vice versa. The conversion factor $c^2 \approx 9\times 10^{16}\ \text{m}^2/\text{s}^2$ is enormous, which is why converting even a small amount of rest mass releases a very large amount of energy — the physical basis of the energy released in nuclear fission and fusion, examined in [Chapter 11](#ch-many-electron-atoms).

## The Energy–Momentum Four-Vector

Momentum and energy are not independent; eliminating $u$ and $\gamma$ between $\vec p = \gamma m\vec u$ and $E = \gamma mc^2$ gives the **energy–momentum invariant**,

$$
E^2 = (pc)^2 + (mc^2)^2,
$$ (eq:ch03-energy-momentum)

a relation that holds for every particle, in every inertial frame. This is directly analogous to the invariant spacetime interval $(\Delta s)^2 = c^2\Delta t^2 - \Delta x^2$ of [Chapter 2](#ch-special-relativity), and the analogy is not superficial: just as $(ct, x, y, z)$ can be assembled into a single spacetime-displacement four-vector that transforms under a Lorentz boost according to the Lorentz transformation, the quadruple $(E/c, p_x, p_y, p_z)$ can be assembled into a single **energy–momentum four-vector**,

$$
p^\mu = \left(\frac{E}{c},\, p_x,\, p_y,\, p_z\right),
$$

which transforms from one inertial frame to another by exactly the same Lorentz transformation rule used for $(ct,x,y,z)$ in [Chapter 2](#ch-special-relativity) (with $ct \to E/c$ and $x \to p_x$). Its invariant magnitude is

$$
\left(\frac{E}{c}\right)^2 - p_x^2 - p_y^2 - p_z^2 = (mc)^2,
$$

which is precisely the energy–momentum relation in Equation {eq}`eq:ch03-energy-momentum`, rearranged; the rest mass $m$ plays the same role for the energy–momentum four-vector that the invariant interval plays for the spacetime-displacement four-vector — a quantity every observer computes to be the same, regardless of the frame in which $E$ and $\vec p$ individually are measured. Because $E/c$ and $\vec p$ transform together, an object's energy–momentum four-vector is always parallel to its worldline on a spacetime diagram of the $(ct, x)$ plane extended to include $(E/c, p_x)$: a slower particle has a "steeper" four-vector (larger $E/c$ relative to $p_x$), and the ratio $v/c = p_xc/E$ recovers the particle's ordinary velocity.

The relation can be read geometrically as a right triangle, as shown in {numref}`Figure %s <fig:ch03-energy-momentum>`: the total-energy term is the hypotenuse, while rest energy and momentum provide the two legs.

```{figure} ../images/ch03-energy-momentum.svg
:label: fig:ch03-energy-momentum
:alt: Right-triangle diagram showing total energy E as the hypotenuse and mc squared and pc as the legs.

The energy–momentum relation as a right triangle: $E^2=(pc)^2+(mc^2)^2$. Original schematic by the author.
```

Two limits of the energy–momentum relation are worth committing to memory:

- **Massive particle at rest** ($p = 0$): $E = mc^2$, the rest energy alone.
- **Massless particle** ($m = 0$), such as a photon: $E = pc$. Massless particles carry momentum and energy but no rest energy, and — consistent with the momentum argument above, which forbids a *massive* particle from reaching $u=c$ — they travel at exactly $c$ in every inertial frame.

The energy–momentum relation is often more convenient than working with $u$ and $\gamma$ directly, particularly for high-energy particles and for photons, where speed is fixed at $c$ and carries no information about energy.

### Why the Four-Vector Formalism Earns Its Keep

The payoff of packaging $(E/c, \vec p)$ as a single object is that **the energy–momentum four-vector is exactly conserved in every collision or decay, in every inertial frame, component by component** — precisely because the underlying, separately-conserved quantities (in every frame) are energy and the three components of momentum. This means a conservation calculation can be carried out entirely by four-vector addition: add up the four-vectors of everything going into a collision, add up the four-vectors of everything coming out, and set the two sums equal, four components at a time. Because the four-vector's magnitude, $(E/c)^2 - p^2 = (mc)^2$, is invariant, this magnitude can be computed in *whichever* frame is most convenient — often a frame in which one particle is initially at rest, or the frame in which the total three-momentum is zero (the subject of the next section) — and the resulting relation between energies and masses will hold in every other frame as well.

**Electron–positron annihilation**, revisited: consider an electron and a positron (each of mass $m$), both essentially at rest, annihilating. Charge conservation alone would permit $e^- + e^+ \to \gamma$ (a single photon), but the four-vector of the initial state is $(2mc, 0,0,0)$ (both particles at rest, energies $mc^2$ each, zero total momentum), while any single photon's four-vector must satisfy $E=pc$, i.e., have equal, nonzero energy and momentum magnitude — it cannot have zero momentum unless its energy is also zero. A single outgoing photon is therefore impossible; conservation of the energy–momentum four-vector, not merely of energy or momentum separately, forces at least two photons, emitted back-to-back so that their momenta cancel, each carrying energy $mc^2$. This is the same conclusion reached by separate energy and momentum arguments in [Problem 3](#ex-relativistic-dynamics-3) below, but the four-vector language makes clear that both conservation laws are really a single, unified statement, and this is exactly the physical process (positron annihilation, producing two back-to-back $511\ \text{keV}$ gamma rays) exploited in medical positron-emission tomography (PET) scans to locate a radioactive tracer inside the body.

## Center-of-Momentum Frame and Threshold Energies

Many practical problems in nuclear and particle physics — will one particle collision produce a new particle, or not? — are most easily solved by transforming to the **center-of-momentum (CM) frame**: the unique inertial frame in which the total three-momentum of a system is zero. Because $(E/c)^2 - p^2$ is Lorentz-invariant, the *total* invariant mass of a system of particles,

$$
(Mc^2)^2 \equiv E_{\text{total}}^2 - (p_{\text{total}}c)^2,
$$

is the same number whether computed in the lab frame or in the CM frame — but in the CM frame, where $p_{\text{total}} = 0$ by definition, it simplifies to $Mc^2 = E_{\text{total,CM}}$: the total CM-frame energy alone. This invariant $M$ is exactly the quantity that determines whether a given reaction can occur at all: by conservation of the energy-momentum four-vector, a reaction that produces a set of final-state particles with total rest mass $\sum m_f$ is only possible if the *available* energy in the CM frame is at least $\left(\sum m_f\right)c^2$ — i.e., if $M \ge \sum m_f$. The **threshold** condition is $M = \sum m_f$ exactly, corresponding to all final-state particles created at rest relative to the CM frame (and hence relative to each other), with no leftover kinetic energy to spare.

The CM frame is not a relativistic invention, and it is worth recovering the non-relativistic intuition before leaning on it. {numref}`Figure %s <fig:ch03-collision-sim>` runs elastic and inelastic collisions in one and two dimensions, with the center of mass drawn on the screen and a momentum diagram beside it. Whatever the pucks do, that marker glides on at constant velocity — the collision cannot touch it, because the internal forces cancel in pairs — which is what makes its rest frame a natural place to do the bookkeeping. Choose the masses and velocities so that the marker stands still, and the momentum diagram shows what has been bought: two arrows equal and opposite before the collision, two arrows equal and opposite after it, however much kinetic energy was lost in between. The relativistic version below keeps that structure exactly, replacing $m\vec u$ by $\gamma m \vec u$ and the total mass by the invariant $M$; what changes is that $M$ is no longer the sum of the parts.

```{phet} collision-lab
:label: fig:ch03-collision-sim

Classical collisions with the center of mass and the momentum vectors displayed. The center of mass moves at a velocity no collision can change, elastic or not, which is what makes its rest frame a natural place to do the bookkeeping — and what carries over, with $\gamma m\vec u$ in place of $m\vec u$, to the relativistic threshold calculations of this section.
```

### Worked Example: The Threshold for Antiproton Production

In 1955, the Bevatron at Berkeley was built specifically to search for the antiproton, via the reaction

$$
p + p \to p + p + p + \bar p,
$$

a proton beam striking a stationary proton (in a hydrogen target), producing an additional proton–antiproton pair. (Baryon number and charge are each automatically conserved by this reaction; nothing prevents it kinematically once enough energy is available.) What is the minimum, or *threshold*, kinetic energy the beam proton must have, in the lab frame, where the target proton is at rest?

Let $m$ be the proton (and antiproton) rest mass, $m_1 = m_2 = m$ for beam and target, and let $M = 4m$ be the total rest mass of the four final-state particles, all momentarily at rest in the CM frame at threshold. The invariant $M^2c^4 = E_{\text{total}}^2 - (p_{\text{total}}c)^2$ can be computed in the lab frame, where the target is at rest ($E_2 = mc^2$, $p_2 = 0$) and the beam proton has energy $E_1$ and momentum $p_1$:

$$
(4mc^2)^2 = (E_1 + mc^2)^2 - (p_1c)^2 = E_1^2 + 2E_1mc^2 + m^2c^4 - (p_1c)^2.
$$

Using $E_1^2 - (p_1c)^2 = (mc^2)^2$ (the beam proton's own invariant), this simplifies to

$$
16m^2c^4 = m^2c^4 + 2E_1mc^2 + m^2c^4 \quad \Longrightarrow \quad E_1 = 7mc^2.
$$

The threshold *kinetic* energy is $K_1 = E_1 - mc^2 = 6mc^2$. With $mc^2 = 938\ \text{MeV}$ for the proton, this is $K_1 = 6(938\ \text{MeV}) = 5.6\ \text{GeV}$ — dramatically larger than the naive $2mc^2 = 2(938\ \text{MeV}) = 1.9\ \text{GeV}$ one might have guessed from simply counting the rest-mass energy of the new particle pair. The extra factor of three arises because, in the lab frame, the newly created particles must all share the *same* velocity as the CM frame itself (since at threshold they are at rest *in* the CM frame, which is itself moving relative to the lab), so a substantial fraction of the beam's kinetic energy is unavoidably "wasted" maintaining the overall forward motion of the collision products rather than being converted into new rest mass. The Bevatron was deliberately designed to reach a beam energy of $6.2\ \text{GeV}$, comfortably above this threshold, and the antiproton was discovered there later that same year by Owen Chamberlain, Emilio Segrè, and collaborators.

This "wasted energy" problem is exactly why modern particle physics favors **colliders**, in which two beams travel toward each other and collide head-on. If the beam and target in the reaction above were replaced by two protons of equal and opposite momentum (so that the lab frame *is* the CM frame), the threshold condition becomes simply $2E_1 = 4mc^2$, i.e., $K_1 = mc^2$ per beam — nearly six times less kinetic energy required per proton than the fixed-target case, precisely because no energy needs to be spent maintaining a net forward CM velocity.

The contrast between the two arrangements is summarized in {numref}`Figure %s <fig:ch03-collider>`.

```{figure} ../images/ch03-fixed-target-collider.svg
:label: fig:ch03-collider
:alt: Comparison of a fixed-target collision, which retains forward momentum, and a head-on collider collision, whose total momentum is zero.

Fixed-target versus collider kinematics. In a head-on collider the center-of-momentum frame can coincide with the laboratory, so more of the beam energy is available to create rest mass. Original schematic by the author.
```

The historical setting of this threshold calculation is shown in {numref}`Figure %s <fig:ch03-bevatron-historical>`: the Bevatron was built in the 1950s to reach the energies needed to discover the antiproton.

```{figure} ../images/historical-bevatron.jpg
:label: fig:ch03-bevatron-historical
:alt: Historical photograph of the interior of the Bevatron accelerator building at Lawrence Berkeley National Laboratory.

Interior of the former Bevatron building at Lawrence Berkeley National Laboratory. Photograph by Daniel Parks, 2010; CC BY 2.0 via Wikimedia Commons. The photograph shows the surviving facility structure, not the operating 1955 machine.
```

## Aside: Why There Are No Faster-Than-Light Massive Particles

[Chapter 2](#ch-special-relativity) argued, from causality alone, that no signal or influence can travel faster than $c$ without permitting effects to precede their causes in some valid inertial frame. This chapter's momentum formula, $p = \gamma m u$, gives an independent, purely dynamical reason a *massive* particle in particular can never reach or exceed $c$: as $u \to c^-$, $\gamma \to \infty$, so accelerating a massive particle arbitrarily close to $c$ requires arbitrarily large — and, at $u=c$ itself, literally infinite — momentum and energy. No finite amount of work can supply this, so $c$ is a strict, unreachable asymptote for any object with $m>0$, approached but never attained no matter how long or how powerfully it is accelerated.

It is sometimes asked whether a hypothetical particle might simply be *born* moving faster than $c$, without ever having to accelerate through $c$ — such a hypothetical particle is called a **tachyon**. Formally, applying $E^2 = (pc)^2+(mc^2)^2$ at $u>c$ requires $\gamma^2 = 1/(1-u^2/c^2)$ to be negative, so consistency would force $m^2$ itself to be negative (an "imaginary rest mass"), a mathematical possibility with no known physical instantiation. More importantly, even setting this oddity aside, a tachyon would necessarily connect spacelike-separated events ([Chapter 2](#ch-special-relativity)) — and the causality argument there shows that *some* inertial observer would measure any spacelike-connecting signal to travel backward in time, arriving before it was sent. No experiment has ever detected a particle exceeding $c$, and every attempt to build a fully self-consistent theory of tachyons that avoids these causal paradoxes has failed; the mass–energy relation of this chapter and the light-cone causality argument of [Chapter 2](#ch-special-relativity) are two independent, mutually reinforcing reasons $c$ is an absolute speed limit for anything that can carry energy or information.

## Worked Example: An Electron Accelerated Through a Potential Difference

An electron (rest energy $m c^2 = 0.511\ \text{MeV}$) is accelerated from rest through a potential difference of $2.00\ \text{MV}$, gaining kinetic energy $K = qV = 2.00\ \text{MeV}$.

**Total energy:** $E = K + mc^2 = 2.00\ \text{MeV} + 0.511\ \text{MeV} = 2.511\ \text{MeV}$.

**Momentum:** from $E^2 = (pc)^2 + (mc^2)^2$,

$$
pc = \sqrt{E^2 - (mc^2)^2} = \sqrt{(2.511\ \text{MeV})^2 - (0.511\ \text{MeV})^2} = 2.459\ \text{MeV},
$$

so $p = 2.459\ \text{MeV}/c$.

**Speed:** from $E = \gamma mc^2$, $\gamma = E/mc^2 = (2.511\ \text{MeV})/(0.511\ \text{MeV}) = 4.914$, and $u = c\sqrt{1 - 1/\gamma^2} = 0.979c$.

Note that a Newtonian calculation of the speed from $K = \tfrac12 mu^2$ would give $u = c\sqrt{2K/mc^2} = c\sqrt{2(2.00\ \text{MeV})/(0.511\ \text{MeV})} \approx 2.8c$ — an unphysical result exceeding $c$, and a sharp reminder that the Newtonian kinetic-energy formula must not be used once $K$ is comparable to or larger than $mc^2$.

## Summary

- Because momentum must be conserved in every inertial frame under the Lorentz transformation, the correct definition is $\vec p = \gamma m\vec u$, not the Newtonian $m\vec u$. This can be derived by analyzing a symmetric elastic collision in two frames related by a boost: requiring conservation of transverse momentum, together with the Lorentz-transformation rule for transverse velocities, forces a moving particle's effective inertia to scale as $\gamma(u)m$.
- As $u \to c$, $p \to \infty$, which is why no massive particle can reach the speed of light; this is confirmed directly by measurements of $p/(mu)$ for fast electrons and protons, which match $\gamma(u)$ and rule out the Newtonian prediction of $1$.
- Relativistic kinetic energy is $K = (\gamma - 1)mc^2$, which reduces to $\tfrac12 mu^2$ for $u \ll c$.
- **Total energy** $E = \gamma mc^2$ and **rest energy** $E_0 = mc^2$ satisfy $K = E - E_0$: mass is a form of energy (mass–energy equivalence), convertible to and from other forms of energy.
- The **energy–momentum invariant** $E^2 = (pc)^2 + (mc^2)^2$ holds for all particles in all frames; it reduces to $E = mc^2$ for a particle at rest and to $E = pc$ for a massless particle such as a photon, which necessarily travels at $c$.
- Energy and momentum combine into a single **energy–momentum four-vector**, $p^\mu = (E/c, p_x, p_y, p_z)$, which transforms like $(ct,x,y,z)$ under a Lorentz boost and whose invariant magnitude is the rest mass, $(E/c)^2 - p^2 = (mc)^2$. Conservation of energy and momentum together is equivalent to conservation of this single four-vector.
- The **center-of-momentum (CM) frame** is the frame in which total momentum is zero; the invariant total mass $M$ of a system, computed from $M^2c^4 = E_{\text{total}}^2 - (p_{\text{total}}c)^2$, sets the **threshold** condition, $M = \sum m_f$, for whether a reaction producing a given set of final-state particles is energetically possible, and fixed-target reactions require substantially more beam kinetic energy than head-on collider reactions to reach the same threshold.
- Combining the divergence of $p=\gamma m u$ as $u\to c$ with the causality argument of [Chapter 2](#ch-special-relativity) rules out faster-than-light massive particles (and hypothetical "tachyons") on two independent grounds.
- Newtonian expressions for momentum and kinetic energy are the $u \ll c$ (equivalently $K \ll mc^2$) limit of the relativistic expressions and must not be used when this condition fails.

## Problems

1. A proton (rest energy $938\ \text{MeV}$) moves at $u = 0.900c$. Find (a) $\gamma$, (b) its total energy $E$, (c) its kinetic energy $K$, and (d) its momentum $p$ (in $\text{MeV}/c$).

2. Find the speed at which a particle's relativistic kinetic energy differs from the Newtonian prediction $\tfrac12 mu^2$ by 10%. (Hint: compute $K_{\text{rel}}/K_{\text{Newt}}$ as a function of $u/c$ and solve numerically or by successive approximation.)

(ex-relativistic-dynamics-3)=
3. In electron–positron annihilation, an electron and a positron (each of rest energy $0.511\ \text{MeV}$), both essentially at rest, annihilate into two photons. (a) Use conservation of energy to find the energy of each photon, assuming they emerge with equal energies. (b) Use conservation of momentum to explain why the two photons must travel in exactly opposite directions.

4. A pion at rest (rest energy $139.6\ \text{MeV}$) decays into a muon (rest energy $105.7\ \text{MeV}$) and a muon neutrino (treat as massless). Using conservation of energy and momentum together with $E^2 = (pc)^2+(mc^2)^2$, find the kinetic energy of the muon produced.

5. Show algebraically that $E^2 = (pc)^2 + (mc^2)^2$ follows from $\vec p = \gamma m \vec u$ and $E = \gamma mc^2$ by eliminating $u$ (use $\gamma^2(1 - u^2/c^2) = 1$).

(ex-relativistic-dynamics-6)=
6. The Sun radiates energy at a rate of about $3.8\times10^{26}\ \text{W}$. Use mass–energy equivalence to estimate the rate, in kg/s, at which the Sun is losing mass. Compare this rate, sustained for $4.6$ billion years, to the Sun's mass of about $2.0\times10^{30}\ \text{kg}$, and comment on whether this loss is significant over the Sun's lifetime so far.

7. Fill in the missing step in the derivation of relativistic momentum: starting from the requirement $m(u(A))\,u_y(A) = m(u(B))\,w_0$ and the transverse-velocity relation $u_y(A) = w_0/\gamma(v)$, verify that taking $w_0 \to 0$ gives $u(A) \to v$ and $u(B) \to 0$, and hence that $m(v) = \gamma(v)\,m$.

8. Two identical lumps of putty, each of rest mass $m$ and speed $u = 0.60c$ (in the lab frame), collide head-on and stick together, forming a single composite lump at rest in the lab frame. (a) Using conservation of the energy–momentum four-vector, find the rest mass $M$ of the resulting composite lump, in terms of $m$. (b) Explain why $M \ne 2m$, and identify what has happened to the "missing" (or "extra") mass–energy.

9. A physicist wants to create a hypothetical new particle $X$, of rest mass $m_X = 10m_p$ (ten proton masses), via the fixed-target reaction $p + p \to p + p + X$, firing a proton beam at a stationary proton target. (a) Find the threshold beam kinetic energy, in units of $m_pc^2$, using the method of the worked example. (b) Find the threshold beam kinetic energy per proton if, instead, two beams of equal and opposite momentum collide head-on. (c) Compute the ratio of your two answers, and comment on why collider experiments are favored for producing very massive particles.

10. A photon of energy $E_\gamma$ collides head-on with a stationary electron (rest mass $m$) and is absorbed, forming a single particle of some new rest mass $M$ at rest in the lab frame after the collision (an idealized, energy-non-conserving toy problem — real photon absorption by a free electron cannot conserve energy and momentum simultaneously unless the resulting particle recoils; ignore that subtlety here and simply find $M$ from four-vector conservation, treating the collision as perfectly inelastic). Express $M$ in terms of $m$, $E_\gamma$, and $c$.

11. A tachyon is hypothesized to have real, finite energy and momentum despite traveling at $u = 1.5c$. (a) Show that the relation $E^2 = (pc)^2 + (mc^2)^2$ can only be satisfied for $u>c$ if $m^2 < 0$. (b) Explain, using the light-cone argument of [Chapter 2](#ch-special-relativity), why even setting aside the issue in (a), a signal carried by such a particle would create a causality paradox for some inertial observer.

12. Verify the claim in the worked example on antiproton production that a naive estimate of $2mc^2$ (simply the rest-energy cost of the new proton–antiproton pair) undercounts the true threshold kinetic energy of $6mc^2$. Do this by computing the speed of the center-of-momentum frame at threshold (i.e., the velocity of the frame in which the total momentum is zero) as a fraction of $c$, and explain qualitatively, in terms of this CM-frame velocity, where the "extra" energy beyond $2mc^2$ goes.
