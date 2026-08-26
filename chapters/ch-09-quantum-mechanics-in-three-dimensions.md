---
title: Quantum Mechanics in Three Dimensions
short_title: Chapter 9. Quantum Mechanics in Three Dimensions
label: ch-quantum-mechanics-in-three-dimensions
numbering:
  enumerator: "9.%s"
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Write the time-independent Schrödinger equation in three dimensions and apply it to separable Cartesian potentials such as the 3D infinite box, including cases of partial and full degeneracy.
- Explain why central (spherically symmetric) potentials are naturally treated in spherical coordinates, and describe the separation of variables $\psi(r,\theta,\phi) = R(r)Y(\theta,\phi)$.
- Explain the origin and physical meaning of the centrifugal barrier term in the radial equation for a central potential.
- Identify the three quantum numbers ($n$, $\ell$, $m_\ell$) that arise from solving a central-potential problem and state the physical quantity each one labels.
- State the quantization of orbital angular momentum magnitude and $z$-component, and explain the physical meaning of each, including the commutation relations that forbid simultaneous knowledge of more than one Cartesian component.
- Describe the isotropic three-dimensional harmonic oscillator as a second exactly solvable central potential and relate its degeneracy structure to the nuclear shell model.
- Explain why the three-dimensional treatment is the necessary foundation for the hydrogen atom, developed in [Chapter 10](#ch-the-hydrogen-atom).

## Introduction

[Chapter 8](#ch-the-schrodinger-equation) solved the Schrödinger equation for several one-dimensional potentials, but every atom, molecule, and nucleus is a three-dimensional object, and the most important potential in atomic physics — the Coulomb attraction between an electron and a nucleus — depends only on the distance $r$ from a fixed center, not on a single Cartesian coordinate. This chapter extends the Schrödinger equation to three dimensions and develops the machinery — separation of variables in spherical coordinates, the centrifugal barrier in the radial equation, and the angular momentum quantum numbers that emerge from it — needed to solve any **central-potential** problem, of which the hydrogen atom ([Chapter 10](#ch-the-hydrogen-atom)) is the most important example. The results obtained here, especially the quantization of angular momentum, apply unchanged to every central potential, not just the Coulomb potential, and reappear throughout atomic, molecular, and nuclear physics.

## The Schrödinger Equation in Three Dimensions

Generalizing [Chapter 8](#ch-the-schrodinger-equation) to three spatial dimensions, the time-independent Schrödinger equation for a particle of mass $m$ in a potential $V(x,y,z)$ is

$$
-\frac{\hbar^2}{2m}\left(\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2}\right) + V(x,y,z)\,\psi = E\psi,
$$

or, compactly, $-\dfrac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$, where $\nabla^2$ is the Laplacian operator. As in one dimension, $|\psi(x,y,z)|^2\,dV$ gives the probability of finding the particle in the volume element $dV$ about $(x,y,z)$, and $\psi$ must be normalizable: $\int |\psi|^2\, dV = 1$.

When the potential is **separable in Cartesian coordinates**, $V(x,y,z) = V_1(x) + V_2(y) + V_3(z)$, the equation can be solved by seeking product solutions $\psi(x,y,z) = X(x)Y(y)Z(z)$, which reduces the problem to three independent one-dimensional Schrödinger equations, one per coordinate, each solved exactly as in [Chapter 8](#ch-the-schrodinger-equation). For a **3D infinite box** of side lengths $L_x, L_y, L_z$ (a direct generalization of the infinite square well), this gives

$$
E_{n_x,n_y,n_z} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2}\right), \qquad n_x, n_y, n_z = 1, 2, 3, \ldots,
$$ (eq:ch09-box-energy)

with three independent quantum numbers, one per dimension. A notable feature not seen in one dimension: for a cubic box ($L_x=L_y=L_z=L$), distinct combinations of $(n_x,n_y,n_z)$ — e.g., $(2,1,1)$, $(1,2,1)$, $(1,1,2)$ — can give the *same* total energy. This is called **degeneracy**, and it is a recurring feature of higher-dimensional quantum systems, generally traceable to an underlying symmetry of the potential (here, the equivalence of the three directions in a cube).

### Worked Example: A Rectangular Quantum Dot

A semiconductor quantum dot confines an electron in a box with $L_x = L_y = 5.0\ \text{nm}$ but $L_z = 10.0\ \text{nm}$ (a "square" cross-section, but elongated along $z$) — a shape with less symmetry than a cube, but more than a fully generic box. Using $E_n(\text{eV}) = 0.376\ \text{eV}\cdot\text{nm}^2 \times n^2/L^2(\text{nm})$ (a convenient rewriting of Equation {eq}`eq:ch09-box-energy` for an electron), the ground state has

$$
E_{1,1,1} = (0.376\ \text{eV}\cdot\text{nm}^2)\left[\frac{1}{(5.0\ \text{nm})^2}+\frac{1}{(5.0\ \text{nm})^2}+\frac{1}{(10.0\ \text{nm})^2}\right] = (0.376\ \text{eV}\cdot\text{nm}^2)(0.090\ \text{nm}^{-2}) \approx 34\ \text{meV},
$$

a confinement energy of a few tens of millielectronvolts, comparable to $k_BT$ at room temperature ($\approx 26\ \text{meV}$) — which is why quantum-dot devices are often cooled to enhance the visibility of their discrete energy levels. Because $L_x=L_y \ne L_z$, the box retains a *partial* symmetry: states $(n_x,n_y,n_z)$ and $(n_y,n_x,n_z)$ are degenerate for any choice of $n_z$ (swapping the two equal dimensions changes nothing), but states that instead permute the unequal dimension, such as $(1,1,2)$ versus $(2,1,1)$, are generally *not* degenerate with $(1,1,1)$ or with each other. A box with $L_x=L_y=L_z$ would restore full degeneracy among all permutations of a given $(n_x,n_y,n_z)$ triple, while a fully generic box ($L_x \ne L_y \ne L_z$) would show no degeneracy at all — the amount of degeneracy is a direct fingerprint of how much geometric symmetry the confining potential actually has.

## Central Potentials and Spherical Coordinates

The Coulomb potential, and most potentials of physical interest in atomic and nuclear physics, depend only on the distance from a fixed point: $V(x,y,z) = V(r)$, where $r = \sqrt{x^2+y^2+z^2}$. Such a potential is not separable in Cartesian coordinates, but it *is* separable in **spherical coordinates** $(r,\theta,\phi)$, precisely because its symmetry matches that coordinate system. Written in spherical coordinates, the Schrödinger equation for a central potential admits solutions of the separable form

$$
\psi(r,\theta,\phi) = R(r)\, Y(\theta,\phi),
$$

where $R(r)$, the **radial wave function**, depends on the specific form of $V(r)$ and carries the information about the particle's radial probability distribution, while $Y(\theta,\phi)$, the **angular wave function**, turns out to be *completely independent of the specific form of $V(r)$* — it is determined entirely by the requirement that $\psi$ be single-valued and well-behaved on the sphere, and is therefore the same set of functions for the hydrogen atom, a 3D harmonic oscillator, or any other central potential.

### Spherical Harmonics: The Lowest Few Explicitly

The angular functions $Y(\theta,\phi)$ that solve the angular equation are called **spherical harmonics**, conventionally written $Y_\ell^{m_\ell}(\theta,\phi)$ and labeled by exactly the two angular quantum numbers introduced below. The lowest few, up to overall normalization constants, are

$$
Y_0^0 = \text{constant}, \qquad Y_1^0 \propto \cos\theta, \qquad Y_1^{\pm1} \propto \sin\theta\, e^{\pm i\phi},
$$

and already illustrate the general pattern. The $\ell=0$ harmonic, $Y_0^0$, is completely independent of $\theta$ and $\phi$ — an $s$-state wave function is **spherically symmetric**, with a probability density depending only on $r$, the same in every direction from the center. The $\ell=1$ harmonics depend on angle: $Y_1^0$, proportional to $\cos\theta$, is largest along the $\pm z$-axis and vanishes in the $xy$-plane (a $p_z$-type angular distribution, in the language used for atomic orbitals in [Chapter 10](#ch-the-hydrogen-atom)), while $Y_1^{\pm1}$, proportional to $\sin\theta\,e^{\pm i\phi}$, is largest in the $xy$-plane and vanishes along the $z$-axis. Each higher $\ell$ introduces additional angular structure — more lobes, more angular nodes — but, crucially, the same three functions $Y_1^0, Y_1^{+1}, Y_1^{-1}$ describe the angular dependence of a $p$-state electron in hydrogen, a $p$-state neutron in a nuclear shell-model potential, or a $p$-state particle in the isotropic oscillator discussed later in this chapter, since (as already emphasized) the angular equation and its solutions never reference $V(r)$ at all.

### The Radial Equation and the Centrifugal Barrier

Substituting $\psi = R(r)Y(\theta,\phi)$ into the full Schrödinger equation and separating variables reduces the radial part to an ordinary differential equation for $R(r)$. It is standard, and illuminating, to write this in terms of $u(r) \equiv rR(r)$, in which case the radial equation takes a form directly analogous to a *one-dimensional* Schrödinger equation for $u(r)$ on the half-line $r>0$:

$$
-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[V(r) + \frac{\hbar^2\,\ell(\ell+1)}{2mr^2}\right] u = Eu,
$$

where $\ell$ is the orbital angular momentum quantum number introduced below. The extra term, $\hbar^2\ell(\ell+1)/2mr^2$, is called the **centrifugal barrier**: it behaves as an additional repulsive potential that grows without bound as $r\to 0$ (for any $\ell>0$), pushing the particle's radial probability density away from the origin — the quantum-mechanical counterpart of the classical fact that a particle with nonzero angular momentum orbiting a center cannot pass through that center without first radiating away or otherwise losing its angular momentum. For $\ell=0$ (an **s-state**, in the spectroscopic notation below), the centrifugal barrier vanishes entirely, and only $\ell=0$ states can have a nonvanishing probability density exactly at $r=0$ — a fact used directly in [Chapter 10](#ch-the-hydrogen-atom) to explain, for instance, which hydrogen atomic states can undergo processes that require the electron to overlap with the nucleus.

## Orbital Angular Momentum

The separation above is not a mathematical accident: it reflects the fact that a central potential exerts no torque about the force center (the force is always radial), so **orbital angular momentum**, $\vec L = \vec r\times\vec p$, is conserved, exactly as in classical central-force motion (e.g., Kepler orbits). Solving the angular equation subject to the single-valuedness of $Y(\theta,\phi)$ shows that the magnitude and one Cartesian component (conventionally the $z$-component) of $\vec L$ are simultaneously quantized:

$$
L = \sqrt{\ell(\ell+1)}\,\hbar, \qquad \ell = 0, 1, 2, \ldots, n-1,
$$

$$
L_z = m_\ell\hbar, \qquad m_\ell = -\ell, -\ell+1, \ldots, 0, \ldots, \ell-1, \ell,
$$

where $\ell$ is the **orbital angular momentum quantum number** and $m_\ell$ is the **magnetic quantum number**, so named because $L_z$ determines how the system's energy shifts in an external magnetic field ([Chapter 11](#ch-many-electron-atoms)). For a given $\ell$, there are $2\ell+1$ allowed values of $m_\ell$, corresponding to $2\ell+1$ distinct orientations of the angular momentum vector relative to the chosen $z$-axis — a specific, testable manifestation of **space quantization**: the orbital angular momentum vector does not merely have a quantized *length*, it can only point in a discrete set of directions relative to an external axis, rather than any direction whatsoever as classical mechanics would allow.

Two features are worth emphasizing, since both run against classical intuition. First, $L = \sqrt{\ell(\ell+1)}\hbar$, not $\ell\hbar$ — the "extra" factor means the angular momentum vector's length is always slightly *larger* than its maximum possible $z$-component, $m_{\ell,\max}\hbar = \ell\hbar$; the vector can never point exactly along the $z$-axis. Second, because $L_x$ and $L_y$ are not simultaneously measurable with $L_z$, only the magnitude $L$ and a single component $L_z$ can be assigned definite values at once — the other two components remain fundamentally indeterminate, consistent with the vector never lying exactly along any single axis.

Historically, states of a given $\ell$ are labeled by spectroscopic letters inherited from early atomic spectroscopy: $\ell = 0,1,2,3,4,\ldots$ are denoted $s, p, d, f, g,\ldots$ respectively — a labeling convention used throughout atomic physics (Chapters [10](#ch-the-hydrogen-atom)–[11](#ch-many-electron-atoms)) and retained today purely by tradition.

### Why $m_\ell$ Is Called the Magnetic Quantum Number

The name "magnetic quantum number" is not arbitrary bookkeeping. A charged particle with orbital angular momentum $\vec L$ circulating about a center behaves, classically and quantum mechanically alike, as a tiny current loop with an associated **orbital magnetic dipole moment**,

$$
\vec\mu_L = -\frac{e}{2m}\vec L
$$

for an electron of charge $-e$, directed opposite to $\vec L$ because the electron's charge is negative. Placed in an external magnetic field $\vec B$ along the $z$-axis, this moment contributes an additional term to the electron's energy, $-\vec\mu_L\cdot\vec B \propto m_\ell$, proportional directly to the magnetic quantum number: each of the $2\ell+1$ otherwise energy-degenerate orientations of $\vec L$ acquires a distinct energy shift once a magnetic field is applied, splitting a single spectral line into $2\ell+1$ closely spaced components. This splitting — the (normal) **Zeeman effect** — was observed spectroscopically well before quantum mechanics existed and is precisely why $m_\ell$ earned its name: it is the quantum number that controls how atomic energy levels respond to an external magnetic field, a connection developed quantitatively in [Chapter 10](#ch-the-hydrogen-atom) and [Chapter 11](#ch-many-electron-atoms), alongside the further complication (electron spin) required to explain the full richness of observed atomic spectra in a magnetic field.

That a magnetic field sorts a beam into a discrete number of orientations —
rather than the continuum a classical dipole would give — is the content of
{numref}`Figure %s <fig:ch09-stern-gerlach-sim>`. Firing spin-$\tfrac12$ atoms through a single
analyzer splits the beam in two; chaining analyzers at different angles shows
that the measurement does not simply read a pre-existing orientation.

```{openphysics} SternGerlach
:label: fig:ch09-stern-gerlach-sim

The Stern–Gerlach experiment, assembled from analyzers, magnets, and counters.
Monte Carlo counts accumulate alongside the analytic quantum prediction, so the
$2\ell+1$ (or, for spin, $2s+1$) discrete outcomes can be checked against the
statistics.
```

### Worked Example: The Vector Model for $\ell=2$

An electron is in a state with orbital angular momentum quantum number $\ell=2$ (a $d$-state). Its angular momentum magnitude is

$$
L = \sqrt{\ell(\ell+1)}\,\hbar = \sqrt{6}\,\hbar \approx 2.449\,\hbar,
$$

while the maximum possible $z$-component is $L_{z,\max} = m_{\ell,\max}\hbar = 2\hbar$. The smallest possible angle between $\vec L$ and the $z$-axis, achieved when $m_\ell$ takes its largest value, is

$$
\cos\theta = \frac{L_z}{L} = \frac{2\hbar}{2.449\,\hbar} = 0.816 \quad \Longrightarrow \quad \theta \approx 35.3°,
$$

confirming explicitly that $\vec L$ can never point exactly along $z$ (which would require $\theta=0°$) no matter how large $m_\ell$ is chosen for a given $\ell$; the discrepancy $\ell\hbar$ versus $\sqrt{\ell(\ell+1)}\hbar$ shrinks only in a relative sense as $\ell$ grows large, another instance of the correspondence principle encountered in [Chapter 8](#ch-the-schrodinger-equation).

The cone that this worked example describes is usually drawn as a static picture, which makes the indeterminacy of $L_x$ and $L_y$ look like an admission of ignorance about a vector that is really sitting still somewhere on the cone. The classical system that gets the geometry right is a gyroscope, {numref}`Figure %s <fig:ch09-precession-sim>`: gravity applies a torque perpendicular to the spin angular momentum, and the response is not to tip the axis over but to walk it around a cone at fixed polar angle, with $|\vec L|$ and $L_z$ both constant while $L_x$ and $L_y$ oscillate. Put a magnetic moment in a field instead of a top in gravity and the equation of motion is the same one; the quantum content is only that the cone's opening angle may take just $2\ell+1$ values.

```{openphysics} Precession
:label: fig:ch09-precession-sim

A spinning top under gravity. In steady precession the torque stays perpendicular to $\vec L$, so it changes the direction of the angular momentum without changing either its magnitude or its vertical component — the classical motion behind the vector model's cone, and behind the Larmor precession of a magnetic moment in a field ([Chapter 10](#ch-the-hydrogen-atom)).
```

### Angular Momentum Commutation Relations

The impossibility of simultaneously sharp values for more than one Cartesian component of $\vec L$ is not merely observed; it follows from the algebra of the angular momentum operators themselves, which satisfy the commutation relations

$$
[\hat L_x, \hat L_y] = i\hbar \hat L_z, \qquad [\hat L_y,\hat L_z] = i\hbar \hat L_x, \qquad [\hat L_z,\hat L_x] = i\hbar \hat L_y
$$

(a cyclic pattern in $x\to y\to z\to x$), together with $[\hat L^2, \hat L_z] = 0$. Two operators that do not commute cannot, in general, have simultaneous eigenstates — precisely the mathematical statement of the uncertainty principle applied to angular momentum, directly analogous to the position–momentum commutator underlying the Heisenberg relation of [Chapter 7](#ch-wave-properties-of-particles). Because $\hat L^2$ commutes with $\hat L_z$ (but not with $\hat L_x$ or $\hat L_y$ individually), a quantum state can be prepared with simultaneously sharp values of $L$ and $L_z$ — exactly the states labeled by $\ell$ and $m_\ell$ above — but never with sharp values of $L$, $L_z$, and $L_x$ all at once.

## The Three Quantum Numbers of a Central-Potential Bound State

Solving the full three-dimensional problem for a bound state in a central potential $V(r)$ produces exactly three quantum numbers, each arising from a separate boundary condition in the separation of variables:

- $n$, the **principal quantum number**, arising from solving the radial equation subject to normalizability, and primarily governing the energy (in a form depending on the specific $V(r)$; for the Coulomb potential this dependence takes an especially simple form, worked out in [Chapter 10](#ch-the-hydrogen-atom));
- $\ell$, the **orbital angular momentum quantum number**, $\ell = 0, 1, \ldots, n-1$, governing the magnitude of orbital angular momentum;
- $m_\ell$, the **magnetic quantum number**, $m_\ell = -\ell,\ldots,\ell$, governing the orientation of orbital angular momentum relative to a chosen axis.

This same trio of quantum numbers, with the same allowed ranges and the same physical meaning, appears in every central-potential problem in this book — it is a consequence of three-dimensional rotational symmetry, not a special feature of any one potential — and [Chapter 10](#ch-the-hydrogen-atom) specializes this general machinery to the specific radial equation of the hydrogen atom's Coulomb potential.

## A Second Exactly Solvable Central Potential: The Isotropic Harmonic Oscillator

The Coulomb potential of [Chapter 10](#ch-the-hydrogen-atom) is the most important central potential in atomic physics, but it is not the only one that can be solved exactly. The **isotropic three-dimensional harmonic oscillator**, $V(r) = \tfrac12 m\omega^2 r^2$, is a second example, and it is central (in the technical sense of depending only on $r$) even though it is also separable in Cartesian coordinates, since $r^2 = x^2+y^2+z^2$ splits into three independent one-dimensional oscillators. Solved in Cartesian form, using the one-dimensional harmonic-oscillator result of [Chapter 8](#ch-the-schrodinger-equation) three times over, the energy levels are

$$
E_{n_x,n_y,n_z} = \left(n_x+n_y+n_z+\tfrac32\right)\hbar\omega \equiv \left(N + \tfrac32\right)\hbar\omega, \qquad N \equiv n_x+n_y+n_z = 0,1,2,\ldots,
$$

depending only on the *sum* $N$, not on how it is distributed among $n_x$, $n_y$, $n_z$ individually — a much higher degree of degeneracy than the cubic infinite box, precisely because the isotropic oscillator has continuous rotational symmetry (any direction is equivalent to any other) rather than merely the discrete symmetry of a cube's faces. The same energy levels can equally well be labeled, via the spherical-coordinate separation of this chapter, by a radial quantum number and $\ell$, with $N = 2n_r+\ell$; the two labeling schemes describe the same physical states, related by a change of basis, and the total degeneracy of a given level $N$ works out to $(N+1)(N+2)/2$.

This may look like a mathematical curiosity, but the isotropic harmonic oscillator is directly useful: it is the starting point for the nuclear **shell model** ([Chapter 13](#ch-nuclear-physics)), in which each nucleon moves, to a first approximation, in an average central potential produced by all the other nucleons — a potential that resembles a finite well but is often approximated, for the purpose of a first, analytically tractable calculation, by an isotropic harmonic oscillator. The oscillator's degenerate energy levels, once a spin-orbit correction (introduced in [Chapter 13](#ch-nuclear-physics)) is added, reproduce the empirically observed nuclear **magic numbers** — proton or neutron counts (2, 8, 20, 28, 50, 82, 126) at which nuclei are unusually stable — in much the same way that filled electron shells explain the chemical stability of the noble gases ([Chapter 11](#ch-many-electron-atoms)).

### Comparing Degeneracy Across Three Central Potentials

It is worth pausing to compare the degeneracy patterns of the three central (or Cartesian-separable) potentials encountered so far, since the comparison sharpens exactly what "degeneracy reflects underlying symmetry" means in practice. The cubic infinite box has a *discrete* symmetry (the box is invariant only under swapping $x$, $y$, $z$ and reflections, not under arbitrary rotations), and correspondingly modest degeneracies, arising only from specific numerical coincidences among sums of squares of integers. The isotropic harmonic oscillator has full continuous rotational symmetry, and correspondingly much richer degeneracy, with every state of a given $N=n_x+n_y+n_z$ degenerate regardless of how $N$ is partitioned among the three Cartesian directions. The hydrogen atom's Coulomb potential ([Chapter 10](#ch-the-hydrogen-atom)) is the most degenerate of all the central potentials commonly encountered: not only is the energy independent of $m_\ell$ (true for *any* central potential, since no central potential singles out a preferred direction in space), but for the Coulomb potential specifically, the energy is *also* independent of $\ell$ for fixed $n$ — an extra, "accidental" degeneracy not explained by rotational symmetry alone, and one of the most distinctive mathematical features of the $1/r$ potential, examined further in [Chapter 10](#ch-the-hydrogen-atom).

## Summary

- The 3D Schrödinger equation, $-\dfrac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$, reduces to three independent 1D equations for a Cartesian-separable potential (e.g., the 3D infinite box), which can produce **degeneracy** — distinct quantum states sharing the same energy — as a signature of underlying symmetry; a box with partial symmetry (e.g., a square cross-section but different height) shows partial degeneracy, while a fully generic box shows none.
- A **central potential**, $V(r)$, is separable in spherical coordinates as $\psi(r,\theta,\phi)=R(r)Y(\theta,\phi)$; the angular part $Y(\theta,\phi)$ is universal, independent of the specific form of $V(r)$, while the radial equation for $u(r)=rR(r)$ contains a repulsive **centrifugal barrier** term $\hbar^2\ell(\ell+1)/2mr^2$ that vanishes only for $\ell=0$.
- Orbital angular momentum is quantized in both magnitude, $L = \sqrt{\ell(\ell+1)}\hbar$ ($\ell = 0,1,\ldots,n-1$), and $z$-component, $L_z = m_\ell\hbar$ ($m_\ell = -\ell,\ldots,\ell$) — **space quantization** — with $2\ell+1$ allowed orientations for each $\ell$. The commutation relations $[\hat L_x,\hat L_y]=i\hbar\hat L_z$ (and cyclic permutations) show algebraically why $L_x$ and $L_y$ remain simultaneously indeterminate once $L$ and $L_z$ are sharp.
- The **spherical harmonics** $Y_\ell^{m_\ell}(\theta,\phi)$ are the universal angular wave functions of any central potential; the $\ell=0$ harmonic is spherically symmetric, while $\ell=1$ harmonics have the angular shape familiar from $p$-orbitals in [Chapter 10](#ch-the-hydrogen-atom).
- Three quantum numbers, $n$, $\ell$, $m_\ell$, universally characterize a bound state in any central potential; states are conventionally labeled $s,p,d,f,\ldots$ for $\ell=0,1,2,3,\ldots$. The magnetic quantum number $m_\ell$ controls how a state's energy shifts in an external magnetic field (the Zeeman effect), which is the origin of its name.
- The **isotropic 3D harmonic oscillator**, $V(r)=\tfrac12m\omega^2r^2$, is a second exactly solvable central potential, with energies $E_N=(N+\tfrac32)\hbar\omega$ depending only on $N=n_x+n_y+n_z=2n_r+\ell$ and highly degenerate levels — the starting point for the nuclear shell model of [Chapter 13](#ch-nuclear-physics).

## Problems

1. For a cubic 3D infinite box of side $L$, list the three lowest-lying distinct energy levels (in units of $h^2/8mL^2$) and the quantum-number triples $(n_x,n_y,n_z)$ that produce each, noting any degeneracies.

2. For the rectangular quantum dot of the worked example ($L_x=L_y=5.0\ \text{nm}$, $L_z=10.0\ \text{nm}$), find the energy (in meV) of the state $(n_x,n_y,n_z)=(1,1,2)$, and determine whether it is degenerate with any other low-lying state, explaining your reasoning from the box's symmetry.

3. An electron is in a state with $\ell = 2$. (a) List all allowed values of $m_\ell$. (b) Compute the magnitude $L$ of its orbital angular momentum (in units of $\hbar$). (c) Compute the maximum possible value of $L_z$, and show it is strictly less than $L$, explaining why physically.

4. How many distinct $(\ell, m_\ell)$ combinations are allowed for principal quantum number $n=3$? List them, grouped by $\ell$, and give the spectroscopic letter for each $\ell$ value.

5. Explain, using the uncertainty relation among the components of angular momentum, why an electron in a state of definite $L$ and $L_z$ cannot simultaneously have a definite value of $L_x$, and why this is consistent with the angular momentum vector never lying exactly along the $z$-axis.

6. A particle is in a central-potential bound state with $n=4$. What is the maximum possible orbital angular momentum quantum number $\ell$ it can have, and how many total $(\ell,m_\ell)$ states are available at that $n$ (summed over all allowed $\ell$)?

7. Explain qualitatively why the *angular* part of the wave function, $Y(\theta,\phi)$, does not depend on the specific functional form of $V(r)$, while the *radial* part, $R(r)$, does — referring to which term(s) in the separated Schrödinger equation involve $V(r)$ and which involve only the angular derivatives.

8. Explain, using the centrifugal barrier term $\hbar^2\ell(\ell+1)/2mr^2$, why an $s$-state ($\ell=0$) electron can have a nonzero probability density at the nucleus ($r=0$), while a $p$-state ($\ell=1$) electron cannot — a fact revisited in [Chapter 11](#ch-many-electron-atoms)'s discussion of why $s$-electrons are especially effective at "penetrating" toward the nucleus in multi-electron atoms.

9. For an electron in a state with $\ell=3$ ($f$-state), find (using the method of the worked example) the smallest possible angle between $\vec L$ and the $z$-axis, and compare it to the $\ell=2$ result found in the text, commenting on the trend as $\ell$ increases.

10. Verify the commutation relation $[\hat L_z,\hat L_x]=i\hbar\hat L_y$ is consistent (in terms of index cycling $x\to y\to z\to x$) with the relation $[\hat L_x,\hat L_y]=i\hbar\hat L_z$ already stated, by writing out the analogous relation obtained by cycling indices twice, and state which single relation among $\hat L^2$, $\hat L_x$, $\hat L_y$, $\hat L_z$ guarantees that $L$ and one Cartesian component can be simultaneously sharp.

11. For the isotropic three-dimensional harmonic oscillator, list all the Cartesian quantum-number triples $(n_x,n_y,n_z)$ that give $N=n_x+n_y+n_z=2$, verify there are six of them, and compare this total to the formula $(N+1)(N+2)/2$ quoted in the text.

12. Explain, in terms of symmetry, why the isotropic harmonic oscillator shows a higher degree of degeneracy at a given energy than the cubic infinite box does at a comparable energy level, even though both potentials are invariant under the same set of coordinate permutations ($x\leftrightarrow y\leftrightarrow z$).

13. The nuclear shell model uses an isotropic-oscillator-like potential to explain why nuclei with certain "magic" numbers of protons or neutrons (2, 8, 20, ...) are unusually stable. Using only the degeneracy formula $(N+1)(N+2)/2$ (ignoring, for this problem, the spin-orbit correction mentioned in the text), compute the cumulative number of single-particle states available after filling oscillator shells $N=0$, $N=1$, and $N=2$ (counting each spatial state as available to 2 nucleons of a given type, for spin), and compare the resulting cumulative totals to the first few magic numbers.

14. A particle in a central potential is in a state with $n=2$. (a) List the allowed $(\ell, m_\ell)$ combinations. (b) If a measurement of $L_z$ yields the maximum possible value for the largest allowed $\ell$ at this $n$, state the values of $\ell$ and $m_\ell$, and compute $L$ and the angle between $\vec L$ and the $z$-axis.

15. An electron in a hydrogen-like atom is in a $p$-state ($\ell=1$, $m_\ell=0$), whose angular wave function is $Y_1^0 \propto \cos\theta$. (a) At what polar angle(s) $\theta$ does the angular probability density $|Y_1^0|^2$ vanish? (b) Explain, in terms of your answer, why this state is often called a "$p_z$" state, and contrast its angular shape with the spherically symmetric $\ell=0$ ($s$-state) probability density.

16. An atom in a state with $\ell=1$ is placed in an external magnetic field along the $z$-axis. Using the fact that the energy shift is proportional to $m_\ell$, state how many distinct energy levels the original (field-free) $\ell=1$ level splits into, and explain why an $s$-state ($\ell=0$) shows no such splitting from orbital angular momentum alone.

17. Verify, by explicit substitution of $n_x=n_y=n_z=0$ (so $N=0$), that the ground state of the isotropic three-dimensional harmonic oscillator has energy $E_0 = \tfrac32\hbar\omega$, and explain why this is exactly three times the one-dimensional zero-point energy $\tfrac12\hbar\omega$ found in [Chapter 8](#ch-the-schrodinger-equation).

18. Explain, referring to the "accidental" degeneracy discussed in the text, what would have to be true of a central potential $V(r)$ for its energy levels to depend on $\ell$ as well as $n$ — i.e., for the extra Coulomb-specific degeneracy to be absent — and state whether you would expect the isotropic harmonic oscillator (whose levels depend on $N=2n_r+\ell$, not on $n_r$ and $\ell$ separately) to show this same kind of extra degeneracy.

19. A beam of silver atoms (used in the Stern–Gerlach experiment discussed further in [Chapter 10](#ch-the-hydrogen-atom)) has its outer electron in an $s$-state ($\ell=0$). Using the magnetic-moment relation $\vec\mu_L = -(e/2m)\vec L$, explain why this electron's *orbital* angular momentum cannot be responsible for any splitting of the beam in an inhomogeneous magnetic field, foreshadowing the need for an additional angular-momentum-like degree of freedom (electron spin) introduced in [Chapter 10](#ch-the-hydrogen-atom).
