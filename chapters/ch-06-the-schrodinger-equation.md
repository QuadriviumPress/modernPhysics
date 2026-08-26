---
title: The Schrödinger Equation
short_title: Chapter 6. The Schrödinger Equation
---

## Learning Objectives

By the end of this chapter, you should be able to:

- State the time-dependent and time-independent Schrödinger equations and explain the role of each.
- Interpret the wave function $\Psi(x,t)$ statistically (the Born interpretation) and apply normalization.
- State and apply the boundary and continuity conditions on acceptable wave functions.
- Solve the time-independent Schrödinger equation for a particle in an infinite square well and interpret the resulting quantized energies and stationary states.
- Solve (qualitatively and, for simple cases, quantitatively) the finite square well and explain barrier penetration and quantum tunneling.
- Solve the quantum harmonic oscillator and compare its energy spectrum and ground-state behavior to the classical oscillator.

## Introduction

Chapter 5 established that a wave packet, not a point trajectory, is the appropriate description of a quantum particle, and that this wave nature is directly responsible for the Heisenberg uncertainty principle. This chapter introduces the equation that governs how such a wave evolves: the **Schrödinger equation**, proposed by Erwin Schrödinger in 1926. It plays the role in quantum mechanics that Newton's second law plays in classical mechanics — given a system's wave function at one instant and the forces (via a potential energy function) acting on it, the Schrödinger equation determines the wave function at all later times. Solving it for a sequence of increasingly realistic potentials — a particle confined to a box, a particle in a finite well, a particle in a parabolic potential — reveals features with no classical counterpart: quantized energy levels, a nonzero minimum energy, and the ability of a particle to be found where classical mechanics says it cannot.

## The Wave Function and Its Interpretation

Quantum mechanics represents a particle's state by a complex-valued function of position and time, $\Psi(x,t)$ (in one dimension), called the **wave function**. Max Born proposed the interpretation now universally adopted: $|\Psi(x,t)|^2\,dx$ is the **probability** of finding the particle between $x$ and $x+dx$ at time $t$, if a position measurement is performed. Because the particle must be found *somewhere*, an acceptable wave function must be **normalized**:

$$
\int_{-\infty}^{\infty} |\Psi(x,t)|^2\, dx = 1.
$$

For $\Psi$ to yield a sensible probability density, it (and, where the potential is finite, its first derivative) must be single-valued, finite, and continuous; discontinuities or divergences in $\Psi$ would correspond to ill-defined or infinite probability densities.

## The Time-Dependent Schrödinger Equation

For a particle of mass $m$ moving in one dimension under a potential energy $V(x,t)$, the wave function obeys the **time-dependent Schrödinger equation**:

$$
i\hbar \frac{\partial \Psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi(x,t)}{\partial x^2} + V(x,t)\,\Psi(x,t).
$$

This equation is postulated, not derived from more elementary principles — its justification, as with Newton's laws, is that its predictions match experiment. It can, however, be motivated heuristically: substituting a free-particle plane wave $\Psi \propto e^{i(kx - \omega t)}$ (a wave of definite momentum $p = \hbar k$, per de Broglie, and definite energy $E = \hbar\omega$, per Planck–Einstein) and comparing to the classical nonrelativistic energy relation $E = p^2/2m + V$ reproduces exactly the operator correspondences $E \to i\hbar\,\partial/\partial t$ and $p \to -i\hbar\,\partial/\partial x$ built into the equation.

## Stationary States and the Time-Independent Equation

When the potential $V(x)$ does not depend on time, the Schrödinger equation admits **separable** solutions of the form $\Psi(x,t) = \psi(x)e^{-iEt/\hbar}$, where $\psi(x)$ satisfies the **time-independent Schrödinger equation**:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\,\psi(x) = E\psi(x).
$$

Such solutions are called **stationary states**: although $\Psi(x,t)$ itself oscillates in time through the phase factor $e^{-iEt/\hbar}$, the probability density $|\Psi(x,t)|^2 = |\psi(x)|^2$ is time-independent, and $E$ is the definite, sharply-valued energy of the state. Because the time-independent equation is a linear, second-order differential equation with boundary conditions imposed by the requirement that $\psi$ be normalizable, it typically admits solutions — and hence allowed values of $E$ — only for a discrete set of energies when the particle is confined (bound) by the potential. This is the origin of **energy quantization** in quantum mechanics: not an assumption added by hand, as in the Bohr model, but a direct mathematical consequence of solving a boundary-value problem for a confined wave.

## The Infinite Square Well

The simplest confining potential is the **infinite square well**: $V(x) = 0$ for $0 < x < L$, and $V(x) = \infty$ elsewhere, representing a particle strictly confined to a box of width $L$ (an idealization of, e.g., an electron trapped between strong barriers). Since $\psi$ must vanish wherever $V = \infty$ (an infinite potential permits zero probability of the particle being found there), the boundary conditions are $\psi(0) = \psi(L) = 0$.

Inside the well, the time-independent equation reduces to $\psi'' = -(2mE/\hbar^2)\psi$, with general solution $\psi(x) = A\sin(kx) + B\cos(kx)$, $k \equiv \sqrt{2mE}/\hbar$. The condition $\psi(0)=0$ forces $B=0$; the condition $\psi(L) = 0$ then forces $\sin(kL) = 0$, i.e. $kL = n\pi$ for a positive integer $n = 1, 2, 3, \ldots$ ($n=0$ is excluded, since it gives $\psi \equiv 0$ everywhere — no particle at all). Solving for the allowed energies,

$$
E_n = \frac{n^2\pi^2\hbar^2}{2mL^2} = \frac{n^2h^2}{8mL^2}, \qquad n = 1, 2, 3, \ldots
$$

Normalizing $\psi_n(x) = A\sin(n\pi x/L)$ over $[0,L]$ gives $A = \sqrt{2/L}$. Several features have no classical analog:

- **Energy is quantized**, in discrete levels $E_n \propto n^2$, rather than continuous as for a classical particle bouncing in a box.
- **The ground state ($n=1$) has $E_1 = \pi^2\hbar^2/2mL^2 > 0$**, not zero. A particle strictly confined to a box, unlike a classical particle, can never be perfectly at rest — a direct consequence of the uncertainty principle: confining $\Delta x \sim L$ forces $\Delta p \gtrsim \hbar/L$, hence a minimum kinetic energy $\sim \hbar^2/mL^2$, of the same order as $E_1$.
- **The probability density $|\psi_n(x)|^2$ has $n-1$ interior nodes** (points where the particle has zero probability of being found) — for $n>1$, positions strictly inside the box that the particle can never occupy, again with no classical counterpart.

## The Finite Square Well and Quantum Tunneling

A more physically realistic model replaces the infinitely high walls with walls of finite height $V_0$: $V(x) = 0$ for $0<x<L$ and $V(x) = V_0$ outside. For a bound state with $E < V_0$, the time-independent equation outside the well becomes $\psi'' = +\kappa^2\psi$ with $\kappa \equiv \sqrt{2m(V_0-E)}/\hbar$ real, whose normalizable solutions are decaying exponentials, $\psi(x) \propto e^{-\kappa|x|}$ moving away from the well, rather than the oscillatory sines and cosines found inside.

This is the central qualitative difference from the infinite well: **the wave function does not vanish at the walls, but decays exponentially into the classically forbidden region** where $E < V(x)$ — a region a classical particle could never enter, since it would require negative kinetic energy there. Quantum mechanically, there is a small but nonzero probability of finding the particle just outside the well. Matching $\psi$ and $\psi'$ continuously at each wall (rather than forcing $\psi=0$ as in the infinite well) yields a transcendental equation for the allowed energies, which must generally be solved numerically or graphically; qualitatively, the finite well has *fewer* bound states than the infinite well of the same width (possibly none, if $V_0$ is small enough), and each allowed energy is slightly lower than the corresponding infinite-well value, because the wave function's penetration into the forbidden region effectively widens the well.

This same exponential penetration underlies **quantum tunneling**: if a particle of energy $E$ encounters a finite-width barrier of height $V_0 > E$ (rather than an infinite wall), the wave function decays but does not necessarily reach zero before the barrier ends, re-emerging on the far side as a (reduced-amplitude, but nonzero) oscillatory wave. There is then a nonzero probability — the **transmission coefficient** $T$ — that the particle is found on the far side of the barrier, despite lacking, classically, enough energy to pass over it. For a barrier of width $L$ and height $V_0 > E$, in the regime where the barrier strongly suppresses transmission ($\kappa L \gg 1$),

$$
T \approx e^{-2\kappa L}, \qquad \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar},
$$

showing that tunneling probability falls off exponentially with both the barrier's width and the square root of $m(V_0-E)$ — which is why tunneling is significant for light particles (electrons) through thin barriers but utterly negligible for macroscopic objects. Tunneling is not a mathematical curiosity; it is the mechanism behind alpha decay (Chapter 11), the scanning tunneling microscope, and (approximately) the operation of tunnel diodes.

## The Quantum Harmonic Oscillator

A particle in a potential $V(x) = \tfrac12 kx^2$ (with $k$ here the spring constant, not a wave number) is the quantum analog of the classical simple harmonic oscillator, and it is important beyond this specific system because *any* smooth potential, expanded in a Taylor series about a point of stable equilibrium, is approximately parabolic near that minimum — the harmonic oscillator is the generic first approximation for small oscillations about equilibrium in essentially any bound system, including the vibrations of a diatomic molecule (Chapter 10).

Solving the time-independent Schrödinger equation with this potential (the details require either a power-series method or an elegant operator technique, developed in more advanced treatments) yields an evenly spaced energy spectrum,

$$
E_n = \left(n + \tfrac12\right)\hbar\omega, \qquad n = 0, 1, 2, \ldots, \qquad \omega \equiv \sqrt{k/m},
$$

with $\omega$ the classical angular frequency of the corresponding classical oscillator. Two features stand out. First, unlike the square well, the spacing between adjacent levels, $\hbar\omega$, is the *same* for every $n$ — a distinctive signature of the parabolic potential. Second, the ground state ($n=0$) has energy $E_0 = \tfrac12\hbar\omega \ne 0$, called the **zero-point energy**: even in its lowest possible energy state, a quantum oscillator retains irreducible energy and motion, again a manifestation of the uncertainty principle (a particle at rest, at the exact bottom of the well, would have $\Delta x = \Delta p = 0$, forbidden by $\Delta x\,\Delta p \geq \hbar/2$). The ground-state wave function, $\psi_0(x) \propto e^{-m\omega x^2/2\hbar}$, is a Gaussian, peaked (unlike the classical oscillator, which spends most of its time near the turning points, where it moves slowest) at the center $x=0$ — another qualitative divergence from classical intuition that only disappears, via the correspondence principle, for large $n$, where the quantum probability distribution begins to average out to resemble the classical one.

## Summary

- The wave function $\Psi(x,t)$ evolves according to the **time-dependent Schrödinger equation**; $|\Psi(x,t)|^2$ gives the probability density for finding the particle, per the Born interpretation, and $\Psi$ must be normalized, single-valued, finite, and continuous.
- For time-independent potentials, separable **stationary-state** solutions $\Psi = \psi(x)e^{-iEt/\hbar}$ satisfy the **time-independent Schrödinger equation**; requiring $\psi$ to be normalizable in a confining potential generically forces $E$ to take only discrete, quantized values.
- The **infinite square well** gives $E_n = n^2h^2/8mL^2$, a nonzero ground-state energy, and wave functions with $n-1$ interior nodes — all with no classical counterpart.
- The **finite square well** allows the wave function to penetrate into the classically forbidden region outside the well; the same mechanism, applied to a finite-width barrier, produces **quantum tunneling**, with transmission probability falling off exponentially with barrier width and $\sqrt{m(V_0-E)}$.
- The **quantum harmonic oscillator** has evenly spaced levels $E_n = (n+\tfrac12)\hbar\omega$ and a nonzero **zero-point energy** $E_0 = \tfrac12\hbar\omega$; it is the generic small-oscillation approximation to any smooth potential near a stable minimum.

## Problems

1. An electron is confined to an infinite square well of width $L = 0.20\ \text{nm}$ (roughly an atomic diameter). Find (a) the ground-state energy $E_1$ in eV, and (b) the energy of the photon emitted in a transition from $n=2$ to $n=1$.

2. Show, by direct substitution into the time-independent Schrödinger equation, that $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ with $E_n = n^2\pi^2\hbar^2/2mL^2$ is indeed a solution for the infinite square well on $0<x<L$.

3. A proton with $5.0\ \text{MeV}$ of kinetic energy strikes a rectangular potential barrier of height $10.0\ \text{MeV}$ and width $2.0\times10^{-15}\ \text{m}$ (roughly a nuclear dimension). (a) Compute $\kappa = \sqrt{2m(V_0-E)}/\hbar$ for the proton in the barrier. (b) Estimate the tunneling transmission probability $T \approx e^{-2\kappa L}$. (c) Repeat for an alpha particle (mass four times the proton mass) under the same conditions and compare, explaining qualitatively why the heavier particle tunnels less readily.

4. Verify that the ground-state wave function of the harmonic oscillator, $\psi_0(x) = A\,e^{-m\omega x^2/2\hbar}$, satisfies the time-independent Schrödinger equation for $V(x) = \tfrac12 m\omega^2 x^2$ with energy $E_0 = \tfrac12\hbar\omega$, by direct substitution (you need not determine the normalization constant $A$).

5. A diatomic molecule vibrates approximately as a harmonic oscillator with classical frequency $f = \omega/2\pi = 8.7\times10^{13}\ \text{Hz}$. Find (a) the zero-point energy in eV, and (b) the energy of a photon emitted in a transition between adjacent vibrational levels ($\Delta n = 1$), and (c) identify the region of the electromagnetic spectrum (see Chapter 4) in which this photon lies.

6. Explain, using the uncertainty principle rather than solving the Schrödinger equation directly, why both the infinite square well and the harmonic oscillator must have a ground-state energy strictly greater than the classical minimum ($E=0$ in both cases), and why this argument would not apply to a classical (macroscopic) oscillator or box.
