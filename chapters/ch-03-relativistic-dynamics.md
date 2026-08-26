---
title: Relativistic Dynamics
short_title: Chapter 3. Relativistic Dynamics
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain why the Newtonian definition of momentum, $p = mu$, is not conserved in all inertial frames once the Lorentz transformation replaces the Galilean transformation, and state the corrected, relativistic definition.
- Apply the relativistic expressions for momentum, kinetic energy, and total energy.
- Use the mass–energy relation $E = mc^2$ and the energy–momentum invariant $E^2 = (pc)^2 + (mc^2)^2$.
- Distinguish rest mass, relativistic momentum, kinetic energy, and total energy, and apply these to problems involving massive particles and photons.
- Recognize the low-speed (Newtonian) and high-speed (ultrarelativistic) limits of the relativistic energy and momentum expressions.

## Introduction

Chapter 2 replaced the Galilean transformation with the Lorentz transformation, because only the latter is consistent with the invariance of the speed of light. But momentum and energy in Newtonian mechanics are defined and conserved using Galilean kinematics: $p = mu$, conserved because Newton's third law and Galilean-invariant forces guarantee it in every Galilean frame. Once the underlying kinematics changes, the old definitions of momentum and energy no longer transform consistently between inertial frames, and a collision that conserves Newtonian momentum in one frame will not, in general, conserve it in another frame related by a Lorentz transformation. This chapter derives the corrected definitions — relativistic momentum and relativistic energy — that *are* conserved in every inertial frame, and works out their most important consequence: mass and energy are, up to a conversion factor $c^2$, the same quantity.

## Relativistic Momentum

Demanding that momentum be conserved in every inertial frame, consistent with the Lorentz transformation, forces a modification of the Newtonian definition. The result (which can be derived by analyzing an elastic collision as seen in two different inertial frames) is

$$
\vec p = \gamma m \vec u = \frac{m\vec u}{\sqrt{1 - u^2/c^2}},
$$

where $m$ is the particle's **rest mass** — an intrinsic, frame-independent property of the particle, equal to the mass measured by an observer at rest relative to it — and $u$ is the particle's speed in the frame in question. For $u \ll c$, $\gamma \to 1$ and this reduces to the Newtonian $\vec p = m\vec u$. As $u \to c$, however, $\gamma \to \infty$, so $p \to \infty$ as well: **an infinite momentum, and correspondingly an infinite force applied for a finite time, would be needed to accelerate a massive particle to the speed of light.** This is the precise dynamical reason no massive object can reach or exceed $c$, complementing the kinematic argument of Chapter 2 (relativistic velocity addition never produces $u \ge c$ from sub-light inputs).

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

Then $K = E - E_0$: kinetic energy is the energy *above and beyond* the energy $mc^2$ a particle possesses simply by virtue of having rest mass $m$, even at rest ($u=0$, $\gamma=1$). This is the celebrated **mass–energy equivalence**: rest mass is a form of energy, convertible (in principle and, in nuclear and particle processes, routinely in practice) into other forms of energy, and vice versa. The conversion factor $c^2 \approx 9\times 10^{16}\ \text{m}^2/\text{s}^2$ is enormous, which is why converting even a small amount of rest mass releases a very large amount of energy — the physical basis of the energy released in nuclear fission and fusion, examined in Chapter 11.

## The Energy–Momentum Relation

Momentum and energy are not independent; eliminating $u$ and $\gamma$ between $\vec p = \gamma m\vec u$ and $E = \gamma mc^2$ gives the **energy–momentum invariant**,

$$
E^2 = (pc)^2 + (mc^2)^2,
$$

a relation that holds for every particle, in every inertial frame (the combination $E^2 - (pc)^2$ is itself a Lorentz invariant, equal to $(mc^2)^2$ in all frames, in exact analogy to the invariant spacetime interval of Chapter 2). Two limits of this relation are worth committing to memory:

- **Massive particle at rest** ($p = 0$): $E = mc^2$, the rest energy alone.
- **Massless particle** ($m = 0$), such as a photon: $E = pc$. Massless particles carry momentum and energy but no rest energy, and — consistent with the momentum argument above, which forbids a *massive* particle from reaching $u=c$ — they travel at exactly $c$ in every inertial frame.

The energy–momentum relation is often more convenient than working with $u$ and $\gamma$ directly, particularly for high-energy particles and for photons, where speed is fixed at $c$ and carries no information about energy.

## Worked Example: An Electron Accelerated Through a Potential Difference

An electron (rest energy $m c^2 = 0.511\ \text{MeV}$) is accelerated from rest through a potential difference of $2.00\ \text{MV}$, gaining kinetic energy $K = qV = 2.00\ \text{MeV}$.

**Total energy:** $E = K + mc^2 = 2.00 + 0.511 = 2.511\ \text{MeV}$.

**Momentum:** from $E^2 = (pc)^2 + (mc^2)^2$,

$$
pc = \sqrt{E^2 - (mc^2)^2} = \sqrt{(2.511)^2 - (0.511)^2}\ \text{MeV} = 2.459\ \text{MeV},
$$

so $p = 2.459\ \text{MeV}/c$.

**Speed:** from $E = \gamma mc^2$, $\gamma = E/mc^2 = 2.511/0.511 = 4.914$, and $u = c\sqrt{1 - 1/\gamma^2} = 0.979c$.

Note that a Newtonian calculation of the speed from $K = \tfrac12 mu^2$ would give $u = c\sqrt{2K/mc^2} = c\sqrt{2(2.00)/0.511} \approx 2.8c$ — an unphysical result exceeding $c$, and a sharp reminder that the Newtonian kinetic-energy formula must not be used once $K$ is comparable to or larger than $mc^2$.

## Summary

- Because momentum must be conserved in every inertial frame under the Lorentz transformation, the correct definition is $\vec p = \gamma m\vec u$, not the Newtonian $m\vec u$; as $u \to c$, $p \to \infty$, which is why no massive particle can reach the speed of light.
- Relativistic kinetic energy is $K = (\gamma - 1)mc^2$, which reduces to $\tfrac12 mu^2$ for $u \ll c$.
- **Total energy** $E = \gamma mc^2$ and **rest energy** $E_0 = mc^2$ satisfy $K = E - E_0$: mass is a form of energy (mass–energy equivalence), convertible to and from other forms of energy.
- The **energy–momentum invariant** $E^2 = (pc)^2 + (mc^2)^2$ holds for all particles in all frames; it reduces to $E = mc^2$ for a particle at rest and to $E = pc$ for a massless particle such as a photon, which necessarily travels at $c$.
- Newtonian expressions for momentum and kinetic energy are the $u \ll c$ (equivalently $K \ll mc^2$) limit of the relativistic expressions and must not be used when this condition fails.

## Problems

1. A proton (rest energy $938\ \text{MeV}$) moves at $u = 0.900c$. Find (a) $\gamma$, (b) its total energy $E$, (c) its kinetic energy $K$, and (d) its momentum $p$ (in $\text{MeV}/c$).

2. Find the speed at which a particle's relativistic kinetic energy differs from the Newtonian prediction $\tfrac12 mu^2$ by 10%. (Hint: compute $K_{\text{rel}}/K_{\text{Newt}}$ as a function of $u/c$ and solve numerically or by successive approximation.)

3. In electron–positron annihilation, an electron and a positron (each of rest energy $0.511\ \text{MeV}$), both essentially at rest, annihilate into two photons. (a) Use conservation of energy to find the energy of each photon, assuming they emerge with equal energies. (b) Use conservation of momentum to explain why the two photons must travel in exactly opposite directions.

4. A pion at rest (rest energy $139.6\ \text{MeV}$) decays into a muon (rest energy $105.7\ \text{MeV}$) and a muon neutrino (treat as massless). Using conservation of energy and momentum together with $E^2 = (pc)^2+(mc^2)^2$, find the kinetic energy of the muon produced.

5. Show algebraically that $E^2 = (pc)^2 + (mc^2)^2$ follows from $\vec p = \gamma m \vec u$ and $E = \gamma mc^2$ by eliminating $u$ (use $\gamma^2(1 - u^2/c^2) = 1$).

6. The Sun radiates energy at a rate of about $3.8\times10^{26}\ \text{W}$. Use mass–energy equivalence to estimate the rate, in kg/s, at which the Sun is losing mass. Compare this rate, sustained for $4.6$ billion years, to the Sun's mass of about $2.0\times10^{30}\ \text{kg}$, and comment on whether this loss is significant over the Sun's lifetime so far.
