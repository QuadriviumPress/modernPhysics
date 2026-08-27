---
title: The Schrödinger Equation
short_title: Chapter 8. The Schrödinger Equation
label: ch-the-schrodinger-equation
numbering:
  enumerator: "8.%s"
---

## Learning Objectives

By the end of this chapter, you should be able to:

- State the time-dependent and time-independent Schrödinger equations and explain the role of each.
- Interpret the wave function $\Psi(x,t)$ statistically (the Born interpretation) and apply normalization.
- State and apply the boundary and continuity conditions on acceptable wave functions.
- Compute expectation values of position and momentum from a wave function using the position and momentum operators.
- Solve the time-independent Schrödinger equation for a particle in an infinite square well and interpret the resulting quantized energies and stationary states.
- Analyze a potential step and compute reflection and transmission coefficients, and explain why quantum mechanics allows partial reflection even when $E > V_0$.
- Solve (qualitatively and, for simple cases, quantitatively) the finite square well and explain barrier penetration and quantum tunneling.
- Solve the quantum harmonic oscillator, apply its selection rule, and compare its energy spectrum and ground-state behavior to the classical oscillator.

## Introduction

[Chapter 7](#ch-wave-properties-of-particles) established that a wave packet, not a point trajectory, is the appropriate description of a quantum particle, and that this wave nature is directly responsible for the Heisenberg uncertainty principle. This chapter introduces the equation that governs how such a wave evolves: the **Schrödinger equation**, proposed by Erwin Schrödinger in 1926. It plays the role in quantum mechanics that Newton's second law plays in classical mechanics — given a system's wave function at one instant and the forces (via a potential energy function) acting on it, the Schrödinger equation determines the wave function at all later times. Solving it for a sequence of increasingly realistic potentials — a particle confined to a box, a particle encountering a step or barrier, a particle in a parabolic potential — reveals features with no classical counterpart: quantized energy levels, a nonzero minimum energy, partial reflection where classical physics predicts certain transmission, and the ability of a particle to be found where classical mechanics says it cannot.

## The Wave Function and Its Interpretation

Quantum mechanics represents a particle's state by a complex-valued function of position and time, $\Psi(x,t)$ (in one dimension), called the **wave function**. Max Born proposed the interpretation now universally adopted: $|\Psi(x,t)|^2\,dx$ is the **probability** of finding the particle between $x$ and $x+dx$ at time $t$, if a position measurement is performed. Because the particle must be found *somewhere*, an acceptable wave function must be **normalized**:

$$
\int_{-\infty}^{\infty} |\Psi(x,t)|^2\, dx = 1.
$$

For $\Psi$ to yield a sensible probability density, it (and, where the potential is finite, its first derivative) must be single-valued, finite, and continuous; discontinuities or divergences in $\Psi$ would correspond to ill-defined or infinite probability densities.

The Born rule is easy to state and easy to under-read, because probability is also what a classical physicist reaches for when describing ignorance about a definite fact. The two are not the same, and {numref}`Figure %s <fig:ch08-measurement-sim>` is built around the difference. Its first screen puts a classical coin under a cover beside a quantum one: both give heads half the time, but the classical coin already *is* heads or tails while it is hidden, and the quantum one is in a superposition of the two until it is looked at. Its later screens make the distinction operational — single photons through a polarizer arriving with probability $\cos^2\theta$, and spin-$\tfrac12$ particles through a chain of analyzers whose statistics no assignment of pre-existing values reproduces.

```{phet} quantum-measurement
:label: fig:ch08-measurement-sim

Measurement statistics for a classical coin, for single photons through a polarizer, and for spin-$\tfrac12$ particles. $|\Psi|^2$ is a probability, but not a probability about something already decided — the distinction this chapter's mathematics quietly assumes.
```

### Expectation Values and Operators

Because $|\Psi(x,t)|^2$ gives only a probability distribution, not a definite trajectory, a quantum "measurement" of position generally yields different results on identically prepared systems, with a statistical average — the **expectation value** — defined by

$$
\langle x \rangle = \int_{-\infty}^{\infty} \Psi^*(x,t)\, x\, \Psi(x,t)\, dx,
$$

the same weighted-average construction used for any probability distribution in statistics, here weighted by $|\Psi|^2$. Momentum, energy, and other physical quantities are represented in quantum mechanics by **operators** acting on $\Psi$ — most importantly the momentum operator $\hat p = -i\hbar\,\partial/\partial x$, already implicit in the correspondence used to motivate the Schrödinger equation below — and their expectation values follow the same sandwich pattern,

$$
\langle p \rangle = \int_{-\infty}^{\infty} \Psi^*(x,t)\left(-i\hbar\frac{\partial}{\partial x}\right)\Psi(x,t)\, dx.
$$

Expectation values are the quantities that connect the abstract wave function to numbers that can be compared with experiment: repeating a position (or momentum) measurement on many identically prepared copies of the same system and averaging the results reproduces $\langle x \rangle$ (or $\langle p \rangle$), while the statistical spread of those repeated measurements is exactly the $\Delta x$ (or $\Delta p$) appearing in the Heisenberg uncertainty principle of [Chapter 7](#ch-wave-properties-of-particles).

### Ehrenfest's Theorem: Recovering Newton's Second Law on Average

Although an individual quantum particle does not follow a definite classical trajectory, its *expectation values* obey equations strikingly close to the classical equations of motion. Differentiating $\langle x \rangle$ and $\langle p \rangle$ with respect to time and using the time-dependent Schrödinger equation to evaluate the results (a calculation carried out in more advanced treatments) gives **Ehrenfest's theorem**,

$$
\frac{d\langle x\rangle}{dt} = \frac{\langle p\rangle}{m}, \qquad \frac{d\langle p\rangle}{dt} = -\left\langle \frac{dV}{dx}\right\rangle = \langle F\rangle,
$$

which are exactly Newton's second law, $F=ma$, written for expectation values rather than for a sharp classical position and momentum. This is a precise, quantitative statement of the correspondence principle developed later in this chapter: quantum mechanics does not contradict Newtonian mechanics but contains it, recovered as a statement about the *average* behavior of a quantum ensemble. For a wave packet narrow enough that $\langle dV/dx\rangle \approx \left.dV/dx\right|_{x=\langle x\rangle}$ (a good approximation whenever the potential varies slowly across the packet's width, typically satisfied for macroscopic objects but not necessarily for an electron confined to atomic dimensions), Ehrenfest's theorem shows that the packet's center moves, to excellent approximation, exactly like a classical particle obeying Newton's second law — which is precisely why macroscopic objects, whose wave packets are always narrow on any macroscopically relevant length scale, appear to move along sharp classical trajectories even though their underlying description is fully quantum mechanical.

## The Time-Dependent Schrödinger Equation

For a particle of mass $m$ moving in one dimension under a potential energy $V(x,t)$, the wave function obeys the **time-dependent Schrödinger equation**:

$$
i\hbar \frac{\partial \Psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi(x,t)}{\partial x^2} + V(x,t)\,\Psi(x,t).
$$

This equation is postulated, not derived from more elementary principles — its justification, as with Newton's laws, is that its predictions match experiment. It can, however, be motivated heuristically: substituting a free-particle plane wave $\Psi \propto e^{i(kx - \omega t)}$ (a wave of definite momentum $p = \hbar k$, per de Broglie, and definite energy $E = \hbar\omega$, per Planck–Einstein) and comparing to the classical nonrelativistic energy relation $E = p^2/2m + V$ reproduces exactly the operator correspondences $E \to i\hbar\,\partial/\partial t$ and $p \to -i\hbar\,\partial/\partial x$ built into the equation.

### The Free Particle and the Need for Wave Packets

Setting $V=0$, the plane wave $\Psi(x,t) = Ae^{i(kx-\omega t)}$ used above to motivate the equation is itself an exact solution, with $\omega = \hbar k^2/2m$ (the same nonrelativistic dispersion relation used in [Chapter 7](#ch-wave-properties-of-particles) to derive the group velocity). This solution has a serious defect as a description of an actual free particle, however: $|\Psi|^2 = |A|^2$ is the same at every point $x$ and every time $t$, so it cannot be normalized ($\int|\Psi|^2dx$ diverges) and represents a particle equally likely to be found anywhere in all of space — a definite momentum but no localization whatsoever, the extreme limit of the uncertainty principle in which $\Delta p = 0$ forces $\Delta x \to \infty$. A physically realizable free particle is instead represented, exactly as in [Chapter 7](#ch-wave-properties-of-particles), by a normalizable **wave packet**: a superposition of plane-wave solutions of many different $k$, each individually a solution of the time-dependent Schrödinger equation (which is linear, so any superposition of solutions is itself a solution), combined so that the total wave function is localized. Because different $k$-components have different $\omega(k)$ and therefore different phase and group velocities, such a packet is precisely the object that spreads over time, as discussed in [Chapter 7](#ch-wave-properties-of-particles); the Schrödinger equation makes that spreading a specific, calculable prediction rather than a qualitative expectation.

## Stationary States and the Time-Independent Equation

When the potential $V(x)$ does not depend on time, the Schrödinger equation admits **separable** solutions of the form $\Psi(x,t) = \psi(x)e^{-iEt/\hbar}$, where $\psi(x)$ satisfies the **time-independent Schrödinger equation**:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\,\psi(x) = E\psi(x).
$$

Such solutions are called **stationary states**: although $\Psi(x,t)$ itself oscillates in time through the phase factor $e^{-iEt/\hbar}$, the probability density $|\Psi(x,t)|^2 = |\psi(x)|^2$ is time-independent, and $E$ is the definite, sharply-valued energy of the state. Because the time-independent equation is a linear, second-order differential equation with boundary conditions imposed by the requirement that $\psi$ be normalizable, it typically admits solutions — and hence allowed values of $E$ — only for a discrete set of energies when the particle is confined (bound) by the potential. This is the origin of **energy quantization** in quantum mechanics: not an assumption added by hand, as in the Bohr model, but a direct mathematical consequence of solving a boundary-value problem for a confined wave. When the particle is *not* confined (as in the potential step below, where the particle can escape to $x\to+\infty$), the same equation instead admits solutions for a continuous range of $E$, describing **scattering states** rather than bound states.

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

All three features are on display in {numref}`Figure %s <fig:ch08-bound-states-sim>`, which solves the time-independent equation numerically for a potential you choose and draws the resulting eigenfunctions on top of the level diagram. Start with a square well and make it deep: the levels approach the $n^2$ ladder derived above, the ground state sits visibly above the bottom of the well, and $\psi_n$ picks up one more node with each step up that ladder. The same simulation carries the finite well, the harmonic oscillator, and the one-dimensional Coulomb potential, so it is worth returning to as those appear later in this chapter and in [Chapter 10](#ch-the-hydrogen-atom); the differences between their level *spacings* — $n^2$ here, uniform for the oscillator, $-1/n^2$ for Coulomb — are the fingerprints of the three potentials.

```{phet-legacy} bound-states
:sim-name: Quantum Bound States
:label: fig:ch08-bound-states-sim

Bound states of a one-dimensional potential, with the well shape, depth, and width adjustable and the eigenfunctions drawn at their own energies. Superpositions of two eigenstates can be built and run in time, which is where the stationary states stop being stationary.
```

### Worked Example: Expectation Values in the Ground State

For the infinite-well ground state $\psi_1(x) = \sqrt{2/L}\sin(\pi x/L)$, the probability density $|\psi_1(x)|^2$ is symmetric about the well's midpoint $x=L/2$, so by symmetry alone,

$$
\langle x \rangle = \frac{L}{2},
$$

without needing to evaluate the defining integral explicitly — the particle is, on average, found at the center of the well, exactly as classical intuition would suggest, even though (unlike a classical particle) it is never actually found moving through the center with a definite velocity. By the same symmetry, $\langle p \rangle = 0$: the stationary state carries no net probability current in either direction. However, $\langle p^2 \rangle \ne 0$: since the ground-state energy is purely kinetic ($V=0$ inside the well), $E_1 = \langle p^2\rangle/2m$, so $\langle p^2 \rangle = 2mE_1 = \pi^2\hbar^2/L^2 \ne 0$. The particle has a nonzero *typical* momentum magnitude, $\sqrt{\langle p^2\rangle} = \pi\hbar/L$, even though its *average* momentum is zero — a direct, quantitative illustration of the uncertainty principle at work: a particle confined to width $\Delta x \sim L$ cannot have $p=0$ exactly, only $\langle p \rangle = 0$ with a nonzero spread $\Delta p = \sqrt{\langle p^2\rangle - \langle p\rangle^2} = \pi\hbar/L$, consistent with $\Delta x\,\Delta p \sim \hbar$.

## The Potential Step: Partial Reflection and Transmission

Before turning to bound states in a finite well, it is instructive to consider a simpler, unbound configuration: a **potential step**, $V(x) = 0$ for $x<0$ and $V(x) = V_0$ for $x>0$, with a particle of energy $E>V_0$ incident from $x=-\infty$. Classically, the particle simply slows down (its kinetic energy dropping from $E$ to $E-V_0$) as it crosses $x=0$, but continues forward with certainty — transmission probability $1$, reflection probability $0$.

Quantum mechanically, the time-independent equation in each region gives oscillatory solutions, $\psi_{\text{I}}(x) = Ae^{ik_1x} + Be^{-ik_1x}$ for $x<0$ (an incident wave of amplitude $A$ plus a reflected wave of amplitude $B$) and $\psi_{\text{II}}(x) = Ce^{ik_2x}$ for $x>0$ (a transmitted wave only, since nothing is incident from $x=+\infty$), with $k_1 = \sqrt{2mE}/\hbar$ and $k_2 = \sqrt{2m(E-V_0)}/\hbar$. Matching $\psi$ and $\psi'$ continuously at $x=0$ gives two equations in $A$, $B$, $C$, which solve to

$$
\frac{B}{A} = \frac{k_1-k_2}{k_1+k_2}, \qquad \frac{C}{A} = \frac{2k_1}{k_1+k_2}.
$$

Because $B \ne 0$ whenever $k_1 \ne k_2$ (i.e., whenever $V_0 \ne 0$), **some of the incident wave is reflected even though $E > V_0$** — a purely wave-mechanical effect (the same kind of partial reflection that occurs when light passes from one medium of different refractive index to another, [Chapter 4](#ch-interference-of-light)) with no classical particle counterpart at all. Comparing probability flux (rather than amplitude) on the two sides gives the **reflection and transmission coefficients**,

$$
R = \left(\frac{k_1-k_2}{k_1+k_2}\right)^2, \qquad T = \frac{4k_1k_2}{(k_1+k_2)^2}, \qquad R+T=1,
$$

the last equality expressing overall conservation of probability: every incident particle is eventually found either reflected or transmitted. If instead $E < V_0$, then $k_2$ becomes imaginary, the "transmitted" solution turns into a decaying exponential (no propagating wave in region II at all), and $R=1$ exactly — total reflection, as classically expected — but, just as in the wave-packet argument of [Chapter 7](#ch-wave-properties-of-particles), the wave function does not vanish abruptly at $x=0$; writing $k_2 = i\kappa$ with $\kappa = \sqrt{2m(V_0-E)}/\hbar$ real, the wave function in region II becomes $\psi_{\text{II}}(x) \propto e^{-\kappa x}$, decaying with a characteristic **penetration depth** $1/\kappa$ rather than vanishing abruptly at $x=0$. The particle therefore has a small but nonzero probability of being found some distance *into* the classically forbidden region, even though it is certain, eventually, to be reflected back the way it came — a preview of the tunneling phenomenon developed below, in which a *second* boundary, ending the forbidden region before $\psi$ has fully decayed away, allows the particle to escape entirely rather than merely penetrate and return.

Both halves of that story — partial reflection at a step the particle has the energy to cross, and exponential decay into a step it does not — can be run against a real wave packet rather than a plane wave in {numref}`Figure %s <fig:ch08-tunneling-sim>`. Send a packet at a step with $E > V_0$ and it visibly splits: part of it continues, slower and stretched, and part comes back, with the areas under the two pieces reproducing the $T$ and $R$ computed above. Lower the energy below $V_0$ and the packet is entirely reflected, but during the encounter it leaks a decaying tail into the barrier. Replacing the step by a barrier of finite thickness — the simulation's next potential — is the whole of tunneling: the tail reaches the far side before it has died away, and what emerges there is a transmitted packet.

```{phet-legacy} quantum-tunneling
:sim-name: Quantum Tunneling and Wave Packets
:label: fig:ch08-tunneling-sim

A wave packet incident on a step, a barrier, or a double barrier, with the real and imaginary parts of $\psi$ and the probability density all available. The energy relative to the barrier height is adjustable, as are the barrier's width and height — the two parameters the transmission coefficient of the next section depends on exponentially.
```

### Worked Example: Reflection at a Potential Step

An electron with kinetic energy $E = 2.00\ \text{eV}$ approaches a potential step of height $V_0 = 1.00\ \text{eV}$. Since $k \propto \sqrt{E}$ (with the same proportionality constant on both sides, as $m$ is unchanged), the ratio $k_2/k_1 = \sqrt{(E-V_0)/E} = \sqrt{(1.00\ \text{eV})/(2.00\ \text{eV})} = 0.707$. The reflection coefficient is then

$$
R = \left(\frac{1-0.707}{1+0.707}\right)^2 = \left(\frac{0.293}{1.707}\right)^2 = 0.0295,
$$

so about $3\%$ of an incident beam of such electrons is reflected by the step, and $T = 1-R \approx 0.97$ is transmitted — a small but entirely real and measurable effect, with no analog for a classical particle rolling over a downward step in a potential energy landscape.

## The Finite Square Well and Quantum Tunneling

A more physically realistic bound-state model replaces the infinitely high walls of the square well with walls of finite height $V_0$: $V(x) = 0$ for $0<x<L$ and $V(x) = V_0$ outside. For a bound state with $E < V_0$, the time-independent equation outside the well becomes $\psi'' = +\kappa^2\psi$ with $\kappa \equiv \sqrt{2m(V_0-E)}/\hbar$ real, whose normalizable solutions are decaying exponentials, $\psi(x) \propto e^{-\kappa|x|}$ moving away from the well, rather than the oscillatory sines and cosines found inside.

This is the central qualitative difference from the infinite well: **the wave function does not vanish at the walls, but decays exponentially into the classically forbidden region** where $E < V(x)$ — a region a classical particle could never enter, since it would require negative kinetic energy there. Quantum mechanically, there is a small but nonzero probability of finding the particle just outside the well. Matching $\psi$ and $\psi'$ continuously at each wall (rather than forcing $\psi=0$ as in the infinite well) yields a transcendental equation for the allowed energies, which must generally be solved numerically or graphically. Choosing the well symmetrically, $V(x)=0$ for $-L/2<x<L/2$, exploits the potential's reflection symmetry to separate the bound-state solutions into two families: **even** solutions, $\psi(x) = A\cos(kx)$ inside the well ($k \equiv \sqrt{2mE}/\hbar$), for which matching to the exterior decay $\psi\propto e^{-\kappa|x|}$ gives the condition

$$
k\tan(kL/2) = \kappa,
$$

and **odd** solutions, $\psi(x) = A\sin(kx)$ inside the well, for which the matching condition is instead

$$
-k\cot(kL/2) = \kappa.
$$

Because $\kappa = \sqrt{2m(V_0-E)}/\hbar$ and $k$ are both functions of the single unknown $E$, each of these is a single transcendental equation in $E$, most easily solved graphically by plotting both sides as functions of $k$ and reading off the intersections; each intersection is one allowed bound-state energy. The lowest bound state is always of the even type (a symmetric, node-free wave function, exactly like the infinite well's ground state); qualitatively, the finite well has *fewer* bound states than the infinite well of the same width (possibly none at all, if $V_0$ is small enough that even the even-solution curves fail to intersect), and each allowed energy is slightly lower than the corresponding infinite-well value, because the wave function's penetration into the forbidden region effectively widens the well.

This same exponential penetration underlies **quantum tunneling**: if a particle of energy $E$ encounters a finite-width barrier of height $V_0 > E$ (rather than an infinite wall), the wave function decays but does not necessarily reach zero before the barrier ends, re-emerging on the far side as a (reduced-amplitude, but nonzero) oscillatory wave. There is then a nonzero probability — the **transmission coefficient** $T$ — that the particle is found on the far side of the barrier, despite lacking, classically, enough energy to pass over it. For a barrier of width $L$ and height $V_0 > E$, in the regime where the barrier strongly suppresses transmission ($\kappa L \gg 1$),

$$
T \approx e^{-2\kappa L}, \qquad \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar},
$$

showing that tunneling probability falls off exponentially with both the barrier's width and the square root of $m(V_0-E)$ — which is why tunneling is significant for light particles (electrons) through thin barriers but utterly negligible for macroscopic objects. Tunneling is not a mathematical curiosity; it is the mechanism behind alpha decay ([Chapter 13](#ch-nuclear-physics)), the scanning tunneling microscope, and (approximately) the operation of tunnel diodes.

### Worked Example: Distance Sensitivity of a Scanning Tunneling Microscope

A scanning tunneling microscope (STM) images a conducting surface by scanning a sharp metal tip a fraction of a nanometer above it and measuring the tunneling current of electrons crossing the vacuum gap — a gap that acts as a potential barrier of height roughly equal to the metal's work function, here taken as $V_0 - E \approx 4.0\ \text{eV}$. The decay constant is

$$
\kappa = \frac{\sqrt{2m_e(V_0-E)}}{\hbar} = \frac{\sqrt{2(9.11\times10^{-31}\ \text{kg})[(4.0\ \text{eV})(1.60\times10^{-19}\ \text{J/eV})]}}{1.055\times10^{-34}\ \text{J}\cdot\text{s}} \approx 1.02\times10^{10}\ \text{m}^{-1} \approx 10.2\ \text{nm}^{-1}.
$$

Since $T \propto e^{-2\kappa L}$, increasing the tip–surface gap by just $\Delta L = 0.10\ \text{nm}$ (one angstrom) changes the transmission probability, and hence the measured tunneling current, by a factor of

$$
e^{-2\kappa\,\Delta L} = e^{-2(10.2\ \text{nm}^{-1})(0.10\ \text{nm})} = e^{-2.05} \approx \frac{1}{7.8},
$$

roughly an order of magnitude per angstrom of vertical displacement — exactly the extreme sensitivity that allows an STM to resolve individual atoms on a surface by tracking tiny changes in tunneling current as the tip scans across atomic-scale height variations.

### Worked Example: Order-of-Magnitude Estimate for Alpha Decay

Alpha decay ([Chapter 13](#ch-nuclear-physics)) is understood as an alpha particle ($m_\alpha \approx 6.64\times10^{-27}\ \text{kg}$) tunneling through the Coulomb barrier confining it inside a heavy nucleus. As a rough, illustrative model, approximate this barrier as rectangular, with the alpha particle's energy falling $\Delta E \approx V_0-E = 20\ \text{MeV}$ below the barrier height and an effective barrier width $L \approx 7\ \text{fm} = 7\times10^{-15}\ \text{m}$ (real barriers are Coulombic, not rectangular, and a proper treatment integrates $\kappa(r)$ over the barrier's actual shape — the **Gamow factor** — but the rectangular approximation captures the essential physics). Then

$$
\kappa = \frac{\sqrt{2m_\alpha \Delta E}}{\hbar} = \frac{\sqrt{2(6.64\times10^{-27}\ \text{kg})[(20\ \text{MeV})(1.602\times10^{-13}\ \text{J/MeV})]}}{1.055\times10^{-34}\ \text{J}\cdot\text{s}} \approx 1.96\times10^{15}\ \text{m}^{-1},
$$

so the tunneling probability per attempt is

$$
T \approx e^{-2\kappa L} = e^{-2(1.96\times10^{15}\ \text{m}^{-1})(7\times10^{-15}\ \text{m})} = e^{-27.4} \approx 1\times10^{-12}.
$$

This tiny number is not the final answer for a decay rate; it must be combined with an **assault frequency**, the rate at which the alpha particle, rattling back and forth inside the nucleus at a speed of order $10^7\ \text{m/s}$ across a nuclear diameter of order $10^{-14}\ \text{m}$, "attempts" to escape — roughly $f \sim 10^{21}\ \text{s}^{-1}$. The decay rate is then of order $f\,T \sim (10^{21}\ \text{s}^{-1})(10^{-12}) = 10^{9}\ \text{s}^{-1}$, corresponding to a half-life of order $10^{-9}\ \text{s}$ for *this* choice of illustrative barrier parameters. Real alpha emitters span half-lives from microseconds to billions of years, entirely because $T$ depends *exponentially* on $\Delta E$ and $L$: changing the barrier parameters by a modest amount changes $T$, and hence the half-life, by many orders of magnitude — exactly the empirical pattern captured by the **Geiger–Nuttall relation** revisited quantitatively in [Chapter 13](#ch-nuclear-physics).

## The Quantum Harmonic Oscillator

A particle in a potential $V(x) = \tfrac12 kx^2$ (with $k$ here the spring constant, not a wave number) is the quantum analog of the classical simple harmonic oscillator, and it is important beyond this specific system because *any* smooth potential, expanded in a Taylor series about a point of stable equilibrium, is approximately parabolic near that minimum — the harmonic oscillator is the generic first approximation for small oscillations about equilibrium in essentially any bound system, including the vibrations of a diatomic molecule ([Chapter 12](#ch-molecular-structure)).

Solving the time-independent Schrödinger equation with this potential (the details require either a power-series method or an elegant operator technique, developed in more advanced treatments) yields an evenly spaced energy spectrum,

$$
E_n = \left(n + \tfrac12\right)\hbar\omega, \qquad n = 0, 1, 2, \ldots, \qquad \omega \equiv \sqrt{k/m},
$$

with $\omega$ the classical angular frequency of the corresponding classical oscillator. Two features stand out. First, unlike the square well, the spacing between adjacent levels, $\hbar\omega$, is the *same* for every $n$ — a distinctive signature of the parabolic potential. Second, the ground state ($n=0$) has energy $E_0 = \tfrac12\hbar\omega \ne 0$, called the **zero-point energy**: even in its lowest possible energy state, a quantum oscillator retains irreducible energy and motion, again a manifestation of the uncertainty principle (a particle at rest, at the exact bottom of the well, would have $\Delta x = \Delta p = 0$, forbidden by $\Delta x\,\Delta p \geq \hbar/2$). The ground-state wave function, $\psi_0(x) \propto e^{-m\omega x^2/2\hbar}$, is a Gaussian, peaked (unlike the classical oscillator, which spends most of its time near the turning points, where it moves slowest) at the center $x=0$ — another qualitative divergence from classical intuition that only disappears, via the correspondence principle, for large $n$, where the quantum probability distribution begins to average out to resemble the classical one.

Excited harmonic-oscillator wave functions follow the same node-counting pattern already seen for the infinite well: $\psi_n(x)$ has exactly $n$ nodes (points, other than the boundaries at infinity, where the wave function crosses zero), so $\psi_0$ (the Gaussian ground state) has none, $\psi_1$ has one node at $x=0$, $\psi_2$ has two nodes symmetric about the origin, and so on — a general feature of one-dimensional bound-state wave functions (also true of the infinite well, where $\psi_n$ has $n-1$ *interior* nodes in addition to the two required zeros at the walls themselves) that provides a quick, qualitative check on whether a proposed solution corresponds to the ground state, first excited state, or a higher state, without needing to solve the full equation.

Transitions between harmonic-oscillator levels by absorption or emission of a photon obey the **selection rule** $\Delta n = \pm 1$: an oscillating dipole (the physical mechanism by which a vibrating charged system couples to the electromagnetic field) can only connect states whose quantum numbers differ by exactly one, so the emitted or absorbed photon energy is always $\hbar\omega$, the same fixed spacing regardless of which pair of adjacent levels is involved — a fact used directly in [Chapter 12](#ch-molecular-structure) to interpret the vibrational spectra of diatomic molecules, where (to the extent the harmonic approximation holds) all vibrational transitions cluster near a single characteristic frequency rather than spreading across many distinct energies.

### Worked Example: Zero-Point Motion, Macroscopic Versus Molecular

The characteristic spread of the ground-state Gaussian wave function is $\Delta x = \sqrt{\hbar/2m\omega}$. For a macroscopic oscillator — a $1.0\ \text{kg}$ mass on a spring with $k = 100\ \text{N/m}$, so $\omega = \sqrt{k/m} = 10\ \text{rad/s}$ — this gives

$$
\Delta x = \sqrt{\frac{1.055\times10^{-34}\ \text{J}\cdot\text{s}}{2(1.0\ \text{kg})(10\ \text{s}^{-1})}} \approx 2.3\times10^{-18}\ \text{m},
$$

many orders of magnitude smaller than even a proton's radius ($\sim10^{-15}\ \text{m}$): zero-point motion is utterly unobservable for a macroscopic object, consistent with everyday experience that a spring at rest simply looks at rest. By contrast, a carbon monoxide molecule vibrating with $\omega \approx 4.0\times10^{14}\ \text{rad/s}$ (a typical molecular vibrational frequency, corresponding to the reduced mass $\mu \approx 1.14\times10^{-26}\ \text{kg}$ and bond stiffness $k \approx 1860\ \text{N/m}$ of the C–O bond) has

$$
\Delta x = \sqrt{\frac{1.055\times10^{-34}\ \text{J}\cdot\text{s}}{2(1.14\times10^{-26}\ \text{kg})(4.0\times10^{14}\ \text{s}^{-1})}} \approx 3.4\times10^{-12}\ \text{m} = 3.4\ \text{pm},
$$

a few percent of the bond's equilibrium length ($\approx 113\ \text{pm}$) — small, but not at all negligible, and precisely why zero-point vibrational motion has measurable consequences (a nonzero zero-point vibrational energy that must be included in molecular bond-energy calculations) for real molecules even though the analogous effect is entirely unobservable for a spring on a lab bench.

## The Correspondence Principle Across Three Systems

The three systems solved in this chapter — the infinite well, the finite well with tunneling, and the harmonic oscillator — share a common thread despite their different mathematical detail: each has a nonzero, quantized ground-state energy set by the uncertainty principle, each allows the particle to be found (with vanishing but nonzero probability, in the finite-well and barrier cases) in regions forbidden to a classical particle of the same energy, and each converges toward classical predictions in an appropriate limit. For the infinite well, closely spaced levels at large $n$ (where $E_n \propto n^2$ but the *fractional* spacing $\Delta E_n/E_n \to 0$) approach a quasi-continuous classical energy spectrum; for the harmonic oscillator, the large-$n$ probability distribution $|\psi_n(x)|^2$ develops peaks near the classical turning points, where a classical oscillator spends most of its time, rather than the single central peak seen for $n=0$. This is Bohr's **correspondence principle**: quantum predictions must merge smoothly into classical ones in the limit of large quantum numbers (equivalently, macroscopic action large compared to $\hbar$), and it serves as a valuable consistency check on any quantum-mechanical solution.

The same principle explains why quantum effects are unobservable for everyday macroscopic objects even though, formally, every object obeys the Schrödinger equation. A macroscopic pendulum or block on a spring has an enormous effective quantum number $n$ (its total energy, measured in units of $\hbar\omega$, is astronomically large for ordinary masses, spring constants, and amplitudes), placing it deep in the correspondence-principle regime where quantized energy levels are spaced far too closely, relative to the total energy, to be distinguished from a continuum, and where the wave-packet spreading of [Chapter 7](#ch-wave-properties-of-particles) is negligible on any observable timescale. The three exactly solvable systems of this chapter are pedagogically valuable precisely because they are simple enough to solve exactly while still exhibiting, at small $n$, the full richness of specifically quantum behavior — behavior that becomes progressively harder to detect, though never strictly absent, as a system's size, mass, or energy grows toward the macroscopic scale.

## Summary

- The wave function $\Psi(x,t)$ evolves according to the **time-dependent Schrödinger equation**; $|\Psi(x,t)|^2$ gives the probability density for finding the particle, per the Born interpretation, and $\Psi$ must be normalized, single-valued, finite, and continuous. **Expectation values** of position and momentum are computed by sandwiching the position operator ($x$) or momentum operator ($-i\hbar\,\partial/\partial x$) between $\Psi^*$ and $\Psi$ and integrating; **Ehrenfest's theorem** shows these expectation values obey Newton's second law, recovering classical mechanics as the average behavior of a narrow wave packet.
- For time-independent potentials, separable **stationary-state** solutions $\Psi = \psi(x)e^{-iEt/\hbar}$ satisfy the **time-independent Schrödinger equation**; requiring $\psi$ to be normalizable in a confining potential generically forces $E$ to take only discrete, quantized values, while an unconfined particle has a continuous spectrum of scattering states.
- The **infinite square well** gives $E_n = n^2h^2/8mL^2$, a nonzero ground-state energy, and wave functions with $n-1$ interior nodes — all with no classical counterpart.
- A **potential step** produces partial reflection even when the particle's energy exceeds the step height, with $R = \left(\frac{k_1-k_2}{k_1+k_2}\right)^2$ and $T=1-R$ — a purely wave-mechanical effect.
- The **finite square well** allows the wave function to penetrate into the classically forbidden region outside the well; the same mechanism, applied to a finite-width barrier, produces **quantum tunneling**, with transmission probability falling off exponentially with barrier width and $\sqrt{m(V_0-E)}$, the basis of the scanning tunneling microscope's extreme distance sensitivity.
- The **quantum harmonic oscillator** has evenly spaced levels $E_n = (n+\tfrac12)\hbar\omega$, a selection rule $\Delta n = \pm1$ for radiative transitions, and a nonzero **zero-point energy** $E_0 = \tfrac12\hbar\omega$; it is the generic small-oscillation approximation to any smooth potential near a stable minimum.
- Bohr's **correspondence principle** — quantum predictions merge into classical ones at large quantum numbers — is a recurring consistency check across all three model systems.

## Problems

:::{exercise}
:label: ex-the-schrodinger-equation-1

An electron is confined to an infinite square well of width $L = 0.20\ \text{nm}$ (roughly an atomic diameter). Find (a) the ground-state energy $E_1$ in eV, and (b) the energy of the photon emitted in a transition from $n=2$ to $n=1$.
:::

:::{solution} ex-the-schrodinger-equation-1
:label: sol-the-schrodinger-equation-1
:class: dropdown

For an electron in a well, $E_n=0.376\,n^2/L^2\ \text{eV}$ when $L$ is in nanometers.  Thus

$$E_1=\frac{0.376\ \text{eV}\cdot\text{nm}^2}{(0.20\ \text{nm})^2}=9.40\ \text{eV}.$$

Because $E_2=4E_1$, the emitted energy is $E_2-E_1=3E_1=28.2\ \text{eV}$.

```{figure} ../images/ch08-sol-infinite-well-levels.svg
:label: fig:ch08-sol-infinite-well-levels
:alt: Energy level ladder for an infinite square well showing levels n equals 1 through 4 growing as n squared, with an arrow marking the 28.2 electronvolt photon emitted from n equals 2 down to n equals 1.

The $n^2$ spacing of infinite-well levels: the gap between $n=1$ and $n=2$ is $3E_1$, not $E_1$, because $E_2=4E_1$.
```

Therefore, the ground-state energy is $9.40\ \text{eV}$ and the $n=2\to1$ photon has energy $28.2\ \text{eV}$.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-2

Show, by direct substitution into the time-independent Schrödinger equation, that $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ with $E_n = n^2\pi^2\hbar^2/2mL^2$ is indeed a solution for the infinite square well on $0<x<L$.
:::

:::{solution} ex-the-schrodinger-equation-2
:label: sol-the-schrodinger-equation-2
:class: dropdown

Differentiating twice gives

$$\frac{d^2\psi_n}{dx^2}=-\left(\frac{n\pi}{L}\right)^2\psi_n.$$

Consequently,

$$-\frac{\hbar^2}{2m}\frac{d^2\psi_n}{dx^2}=\frac{n^2\pi^2\hbar^2}{2mL^2}\psi_n=E_n\psi_n.$$

Also $\psi_n(0)=\psi_n(L)=0$.  Therefore, the stated sine function satisfies both the time-independent Schrödinger equation and the infinite-well boundary conditions.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-3

For the infinite-well state $\psi_2(x) = \sqrt{2/L}\sin(2\pi x/L)$ ($n=2$), use the symmetry of $|\psi_2(x)|^2$ about $x=L/2$ to state $\langle x\rangle$ without direct integration, and identify the location of the single interior node.
:::

:::{solution} ex-the-schrodinger-equation-3
:label: sol-the-schrodinger-equation-3
:class: dropdown

The density $|\psi_2(x)|^2$ is symmetric about $x=L/2$, so its mean position is $\langle x\rangle=L/2$.  The interior node follows from

$$\sin\left(\frac{2\pi x}{L}\right)=0\quad\Rightarrow\quad x=\frac L2$$

for $0<x<L$.  Therefore, $\langle x\rangle=L/2$ and the single interior node is at $x=L/2$.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-4

An electron with kinetic energy $E=3.00\ \text{eV}$ encounters a potential step of height $V_0 = 2.00\ \text{eV}$. (a) Compute $k_2/k_1$. (b) Compute the reflection coefficient $R$ and the transmission coefficient $T$. (c) Repeat for $V_0 = 0.500\ \text{eV}$, and comment on how $R$ changes as the step height decreases toward zero.
:::

:::{solution} ex-the-schrodinger-equation-4
:label: sol-the-schrodinger-equation-4
:class: dropdown

For $V_0=2.00\ \text{eV}$,

$$\frac{k_2}{k_1}=\sqrt{\frac{E-V_0}{E}}=\sqrt{\frac{1.00}{3.00}}=0.577,$$

$$R=\left(\frac{1-0.577}{1+0.577}\right)^2=0.0718,\qquad T=1-R=0.928.$$

For $V_0=0.500\ \text{eV}$, $k_2/k_1=\sqrt{2.50/3.00}=0.913$, so $R=0.00207$ and $T=0.998$.

```{figure} ../images/ch08-sol-step-reflection.svg
:label: fig:ch08-sol-step-reflection
:alt: Reflection coefficient versus the ratio of step height to incident energy, rising smoothly from zero, with the two computed cases at 2.00 electronvolts and 0.500 electronvolts marked.

$R$ depends only on the ratio $V_0/E$ and falls smoothly to zero as $V_0\to0$; both computed cases sit on this one curve.
```

Therefore, the reflection falls from $7.18\%$ to $0.207\%$ as the step is lowered.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-5

Show algebraically, starting from the amplitude ratios $B/A = (k_1-k_2)/(k_1+k_2)$ and using $R = |B/A|^2$, $T = (k_2/k_1)|C/A|^2$ with $C/A = 2k_1/(k_1+k_2)$, that $R+T=1$ for the potential step.
:::

:::{solution} ex-the-schrodinger-equation-5
:label: sol-the-schrodinger-equation-5
:class: dropdown

The amplitude formulas give

$$R=\frac{(k_1-k_2)^2}{(k_1+k_2)^2},\qquad T=\frac{k_2}{k_1}\left(\frac{2k_1}{k_1+k_2}\right)^2=\frac{4k_1k_2}{(k_1+k_2)^2}.$$

Therefore,

$$R+T=\frac{k_1^2-2k_1k_2+k_2^2+4k_1k_2}{(k_1+k_2)^2}=\frac{(k_1+k_2)^2}{(k_1+k_2)^2}=1.$$

Therefore, reflection plus transmission equals one, as required by probability-current conservation.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-6

A proton with $5.0\ \text{MeV}$ of kinetic energy strikes a rectangular potential barrier of height $10.0\ \text{MeV}$ and width $2.0\times10^{-15}\ \text{m}$ (roughly a nuclear dimension). (a) Compute $\kappa = \sqrt{2m(V_0-E)}/\hbar$ for the proton in the barrier. (b) Estimate the tunneling transmission probability $T \approx e^{-2\kappa L}$. (c) Repeat for an alpha particle (mass four times the proton mass) under the same conditions and compare, explaining qualitatively why the heavier particle tunnels less readily.
:::

:::{solution} ex-the-schrodinger-equation-6
:label: sol-the-schrodinger-equation-6
:class: dropdown

Here $V_0-E=5.0\ \text{MeV}$.  Using $\hbar c=197.3\ \text{MeV fm}$ and $m_pc^2=938\ \text{MeV}$,

$$\kappa_p=\frac{\sqrt{2(938\ \text{MeV})(5.0\ \text{MeV})}}{197.3\ \text{MeV fm}}=0.491\ \text{fm}^{-1}.$$

Thus $T_p\simeq e^{-2\kappa_pL}=e^{-2(0.491)(2.0)}=0.140$.  For an alpha particle, the mass is four times larger, so $\kappa_\alpha=2\kappa_p=0.982\ \text{fm}^{-1}$ and $T_\alpha=e^{-3.93}=0.0197$.

```{figure} ../images/ch08-sol-tunneling-barrier.svg
:label: fig:ch08-sol-tunneling-barrier
:alt: Wavefunction amplitude envelope decaying exponentially inside a rectangular barrier, with the alpha particle's curve falling off faster than the proton's and settling at a lower plateau beyond the barrier.

The heavier alpha particle has twice the proton's decay constant $\kappa$, so its amplitude falls off twice as fast inside the barrier — the reason its transmission probability ($T=|{\rm amplitude\ ratio}|^2$) ends up smaller.
```

Therefore, the proton transmission is about $14\%$, while the alpha transmission is about $2.0\%$ because the heavier particle has a larger tunneling exponent.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-7

Using the STM worked example's value of $\kappa \approx 10.2\ \text{nm}^{-1}$, find the factor by which the tunneling current changes if the tip–surface gap increases by $0.20\ \text{nm}$ instead of $0.10\ \text{nm}$, and comment on why STM height measurements are typically precise to a small fraction of an angstrom.
:::

:::{solution} ex-the-schrodinger-equation-7
:label: sol-the-schrodinger-equation-7
:class: dropdown

Tunneling current varies as $I\propto e^{-2\kappa L}$, so an added gap $\Delta L$ changes it by

$$\frac{I'}{I}=e^{-2\kappa\Delta L}=e^{-2(10.2\ \text{nm}^{-1})(0.20\ \text{nm})}=e^{-4.08}=0.0169.$$

Therefore, a $0.20\ \text{nm}$ increase reduces the current by a factor of about $59$, which is why STM height measurements can resolve much less than an angstrom.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-8

Verify that the ground-state wave function of the harmonic oscillator, $\psi_0(x) = A\,e^{-m\omega x^2/2\hbar}$, satisfies the time-independent Schrödinger equation for $V(x) = \tfrac12 m\omega^2 x^2$ with energy $E_0 = \tfrac12\hbar\omega$, by direct substitution (you need not determine the normalization constant $A$).
:::

:::{solution} ex-the-schrodinger-equation-8
:label: sol-the-schrodinger-equation-8
:class: dropdown

For $\psi_0=Ae^{-m\omega x^2/(2\hbar)}$,

$$\frac{d^2\psi_0}{dx^2}=\left(\frac{m^2\omega^2x^2}{\hbar^2}-\frac{m\omega}{\hbar}\right)\psi_0.$$

Substitution gives

$$-\frac{\hbar^2}{2m}\psi_0''+\frac12m\omega^2x^2\psi_0=\left[-\frac12m\omega^2x^2+\frac12\hbar\omega+\frac12m\omega^2x^2\right]\psi_0=\frac12\hbar\omega\psi_0.$$

Therefore, the Gaussian satisfies the oscillator equation with $E_0=\tfrac12\hbar\omega$.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-9

A diatomic molecule vibrates approximately as a harmonic oscillator with classical frequency $f = \omega/2\pi = 8.7\times10^{13}\ \text{Hz}$. Find (a) the zero-point energy in eV, and (b) the energy of a photon emitted in a transition between adjacent vibrational levels ($\Delta n = 1$), and (c) identify the region of the electromagnetic spectrum (see [Chapter 6](#ch-particle-properties-of-waves)) in which this photon lies.
:::

:::{solution} ex-the-schrodinger-equation-9
:label: sol-the-schrodinger-equation-9
:class: dropdown

The spacing is

$$hf=(6.626\times10^{-34}\ \text{J s})(8.7\times10^{13}\ \text{s}^{-1})=5.77\times10^{-20}\ \text{J}=0.360\ \text{eV}.$$

Thus $E_0=\tfrac12hf=0.180\ \text{eV}$.  An adjacent-level photon has $0.360\ \text{eV}$ and wavelength $\lambda=1240/0.360=3440\ \text{nm}$.

```{figure} ../images/ch08-sol-oscillator-ladder-spread.svg
:label: fig:ch08-sol-oscillator-ladder-spread
:alt: Left panel: equally spaced harmonic oscillator energy levels with the 0.360 electronvolt spacing and 0.180 electronvolt zero-point energy marked. Right panel: a Gaussian probability distribution of width 8.7 picometers compared with the 74 picometer bond length of molecular hydrogen.

Left: the equally spaced ladder $E_n=(n+\tfrac12)hf$, with this problem's zero-point energy and level spacing marked. Right: [Problem 10](#ex-the-schrodinger-equation-10)'s zero-point position spread for H$_2$, $8.7\ \text{pm}$, shown against the $74\ \text{pm}$ bond length it must fit inside.
```

Therefore, the zero-point energy is $0.180\ \text{eV}$ and vibrational transitions emit $0.360\ \text{eV}$ mid-infrared photons.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-10

Using the general formula $\Delta x = \sqrt{\hbar/2m\omega}$, verify the zero-point spread quoted in the worked example for the $1.0\ \text{kg}$, $k=100\ \text{N/m}$ macroscopic oscillator, and separately for a hydrogen molecule ($\mu \approx 8.4\times10^{-28}\ \text{kg}$, $k \approx 570\ \text{N/m}$), comparing your result to the H–H bond length of about $74\ \text{pm}$.
:::

:::{solution} ex-the-schrodinger-equation-10
:label: sol-the-schrodinger-equation-10
:class: dropdown

For the $1.0\ \text{kg}$ oscillator, $\omega=\sqrt{k/m}=10\ \text{s}^{-1}$, so

$$\Delta x=\sqrt{\frac{\hbar}{2m\omega}}=\sqrt{\frac{1.055\times10^{-34}\ \text{J s}}{2(1.0\ \text{kg})(10\ \text{s}^{-1})}}=2.30\times10^{-18}\ \text{m}.$$

For $\text{H}_2$, $\omega=\sqrt{570/(8.4\times10^{-28})}=8.24\times10^{14}\ \text{s}^{-1}$ and $\Delta x=8.7\ \text{pm}$, shown to scale against the bond length in {numref}`Figure %s <fig:ch08-sol-oscillator-ladder-spread>`.  Therefore, the molecular zero-point spread is about $12\%$ of the $74\ \text{pm}$ bond length, whereas the macroscopic spread is negligible.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-11

Explain, using the uncertainty principle rather than solving the Schrödinger equation directly, why both the infinite square well and the harmonic oscillator must have a ground-state energy strictly greater than the classical minimum ($E=0$ in both cases), and why this argument would not apply to a classical (macroscopic) oscillator or box.
:::

:::{solution} ex-the-schrodinger-equation-11
:label: sol-the-schrodinger-equation-11
:class: dropdown

Confinement requires a finite position uncertainty $\Delta x$, which by $\Delta x\Delta p\gtrsim\hbar/2$ requires nonzero momentum uncertainty and therefore positive kinetic energy.  An oscillator likewise cannot have both exact equilibrium position and zero momentum.  Therefore, both systems have a ground-state energy above the classical minimum; for macroscopic masses the resulting quantum energy is far too small to observe.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-12

A hydrogen molecule vibrates with quantized energy levels $E_n = (n+\tfrac12)\hbar\omega$. If the molecule is initially in the $n=2$ state, list the possible photon energies (in terms of $\hbar\omega$) it could emit in a single transition consistent with the selection rule $\Delta n = \pm1$, and explain why a transition directly from $n=2$ to $n=0$ does not occur by single-photon emission.
:::

:::{solution} ex-the-schrodinger-equation-12
:label: sol-the-schrodinger-equation-12
:class: dropdown

The selection rule is $\Delta n=\pm1$.  Starting at $n=2$, the only downward one-photon transition is $2\to1$, and

$$E_2-E_1=(2+\tfrac12)\hbar\omega-(1+\tfrac12)\hbar\omega=\hbar\omega.$$

The $2\to0$ transition has $\Delta n=-2$ and is forbidden for a single photon.

```{figure} ../images/ch08-sol-selection-rule.svg
:label: fig:ch08-sol-selection-rule
:alt: Three equally spaced harmonic oscillator levels n equals 0, 1, and 2, with a solid arrow for the allowed 2 to 1 transition and a dashed crossed-out arrow for the forbidden 2 to 0 transition.

Only $\Delta n=\pm1$ transitions emit or absorb a single photon; the direct $2\to0$ path is forbidden regardless of how much energy it would release.
```

Therefore, the only allowed emitted photon has energy $\hbar\omega$.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-13

Explain qualitatively, using the correspondence principle, why the probability density $|\psi_n(x)|^2$ of a highly excited ($n \gg 1$) harmonic-oscillator state should be largest near the classical turning points and smallest near $x=0$ — the opposite of the ground-state ($n=0$) distribution — and relate this to how much time a classical oscillator of the same energy spends near each of those locations.
:::

:::{solution} ex-the-schrodinger-equation-13
:label: sol-the-schrodinger-equation-13
:class: dropdown

A classical oscillator moves slowest near its turning points and fastest through $x=0$, so it spends most of its time near the turning points.  The correspondence principle requires the averaged probability density of a large-$n$ quantum state to reproduce that classical time distribution.

```{figure} ../images/ch08-sol-correspondence-principle.svg
:label: fig:ch08-sol-correspondence-principle
:alt: Side by side plots of oscillator probability density for the ground state, peaked at the center, and for a highly excited state, oscillating around a classical envelope that is peaked at the two turning points.

$n=0$ is peaked at the center, the opposite of the classical expectation. By $n=20$, the fine quantum oscillations average out to the classical time-averaged density (dashed), which piles up at the turning points where the classical oscillator moves slowest.
```

Therefore, highly excited oscillator states have their largest probability density near turning points and their smallest near the origin.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-14

A particle of energy $E$ is incident on a potential step of height $V_0 > E$ (rather than $V_0 < E$ as in the worked example). (a) Explain why $R=1$ exactly in this case, in terms of the number of available propagating modes on the far side of the step. (b) Despite total reflection, explain (referring to the finite-well discussion) why the probability density is not simply zero for $x>0$.
:::

:::{solution} ex-the-schrodinger-equation-14
:label: sol-the-schrodinger-equation-14
:class: dropdown

When $V_0>E$, the wave number beyond the step is imaginary, so that region has no propagating wave capable of carrying transmitted probability current; hence $R=1$.  The acceptable solution there is nevertheless an exponentially decaying evanescent wave.  Therefore, reflection is total even though the probability density penetrates a finite distance into $x>0$.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-15

A particle in an infinite square well of width $L$ is prepared in the $n=3$ state. (a) Sketch (in words) the shape of $|\psi_3(x)|^2$, stating the number and approximate locations of its nodes. (b) If the well width is doubled to $2L$ with the particle remaining in the state with the same quantum number $n=3$, by what factor does $E_3$ change?
:::

:::{solution} ex-the-schrodinger-equation-15
:label: sol-the-schrodinger-equation-15
:class: dropdown

The $n=3$ probability density has three lobes and two interior nodes, at $x=L/3$ and $x=2L/3$; the walls are additional zeros.  Since $E_n\propto n^2/L^2$,

$$\frac{E_3(2L)}{E_3(L)}=\frac{L^2}{(2L)^2}=\frac14.$$

Therefore, the state has two interior nodes and its energy becomes one-quarter as large when the well width doubles.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-16

Explain why a free-particle plane wave $\Psi \propto e^{i(kx-\omega t)}$ cannot be normalized, and explain, referring to the uncertainty principle, why this is an unavoidable consequence of the wave having a perfectly sharp, definite momentum $p=\hbar k$.
:::

:::{solution} ex-the-schrodinger-equation-16
:label: sol-the-schrodinger-equation-16
:class: dropdown

A plane wave has constant $|\Psi|^2$, so $\int_{-\infty}^{\infty}|\Psi|^2dx$ diverges and no finite normalization constant exists.  It has one exact wave number and momentum $p=\hbar k$, which requires completely indefinite position.  Therefore, non-normalizability is the unavoidable position-space consequence of perfectly sharp momentum.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-17

Using the even-solution matching condition $k\tan(kL/2)=\kappa$ for the symmetric finite square well, explain (without solving numerically) why increasing the well depth $V_0$ at fixed width $L$ tends to increase the number of bound states, referring to how $\kappa$ depends on $V_0$.
:::

:::{solution} ex-the-schrodinger-equation-17
:label: sol-the-schrodinger-equation-17
:class: dropdown

At fixed width, increasing $V_0$ increases $\kappa=\sqrt{2m(V_0-E)}/\hbar$.  In $k\tan(kL/2)=\kappa$, a larger right-hand side allows intersections on additional tangent branches, each corresponding to another bound-state energy.

```{figure} ../images/ch08-sol-finite-well-bound-states.svg
:label: fig:ch08-sol-finite-well-bound-states
:alt: Graphical solution of the even-parity finite square well matching condition, showing tangent branches of z tan z intersected by two quarter-circle curves of different radius, with the larger radius crossing more branches.

The matching condition plotted graphically: each branch of $z\tan z$ that the quarter-circle $\sqrt{z_0^2-z^2}$ reaches gives one even bound state. Since $z_0\propto\sqrt{V_0}$, a deeper well (larger circle) reaches farther out and crosses more branches — here, one branch for the shallow well and two for the deep well, among the even-parity solutions alone.
```

Therefore, a deeper finite well supports more bound states.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-18

Repeat the alpha-decay order-of-magnitude estimate in the worked example, but for a barrier width of $L=10\ \text{fm}$ instead of $7\ \text{fm}$, keeping $\Delta E = 20\ \text{MeV}$ unchanged. Find the new tunneling probability $T$ and the resulting order-of-magnitude half-life estimate, and comment on how sensitively the result depends on the assumed barrier width.
:::

:::{solution} ex-the-schrodinger-equation-18
:label: sol-the-schrodinger-equation-18
:class: dropdown

The worked example gives $\kappa=1.96\times10^{15}\ \text{m}^{-1}$.  For $L=10\ \text{fm}=10\times10^{-15}\ \text{m}$,

$$T=e^{-2\kappa L}=e^{-2(1.96\times10^{15})(10\times10^{-15})}=e^{-39.2}=9.4\times10^{-18}.$$

With assault frequency $10^{21}\ \text{s}^{-1}$, the decay rate is about $9.4\times10^3\ \text{s}^{-1}$ and $t_{1/2}\sim0.693/(9.4\times10^3)=7.4\times10^{-5}\ \text{s}$.  Therefore, increasing the width by only $3\ \text{fm}$ changes the model half-life from about $10^{-9}\ \text{s}$ to about $10^{-4}\ \text{s}$, illustrating the exponential sensitivity.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-19

State the number of nodes you expect for the harmonic-oscillator wave function $\psi_4(x)$ ($n=4$), and compare this to the number of interior nodes of the $n=5$ infinite-square-well wave function, explaining the one-node difference between the two counting conventions in words.
:::

:::{solution} ex-the-schrodinger-equation-19
:label: sol-the-schrodinger-equation-19
:class: dropdown

The harmonic-oscillator state $\psi_n$ has exactly $n$ nodes, so $\psi_4$ has four.  The infinite-well state $\psi_n$ has $n-1$ interior nodes, so its $n=5$ state also has four interior nodes.  Therefore, both specified states have four nodes in the stated convention; the one-node difference comes from counting the two fixed wall zeros of the well separately from its interior nodes.
:::

:::{exercise}
:label: ex-the-schrodinger-equation-20

A macroscopic pendulum of mass $0.50\ \text{kg}$ and angular frequency $\omega = 2.0\ \text{rad/s}$ is released from an amplitude corresponding to a total energy of $1.0\times10^{-3}\ \text{J}$. Estimate its effective quantum number $n$ (from $E_n \approx n\hbar\omega$ for large $n$), and comment on why this pendulum's motion appears entirely classical and continuous despite formally obeying the same quantized-energy law as the harmonic oscillator of this chapter.
:::

:::{solution} ex-the-schrodinger-equation-20
:label: sol-the-schrodinger-equation-20
:class: dropdown

For large $n$, $E\simeq n\hbar\omega$, so

$$n\simeq\frac{E}{\hbar\omega}=\frac{1.0\times10^{-3}\ \text{J}}{(1.055\times10^{-34}\ \text{J s})(2.0\ \text{s}^{-1})}=4.7\times10^{30}.$$

The spacing $\hbar\omega=2.11\times10^{-34}\ \text{J}$ is negligible beside the pendulum energy.  Therefore, the pendulum occupies a quantum number of order $10^{30}$ and its quantization appears completely continuous and classical.
:::
