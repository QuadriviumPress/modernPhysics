---
title: Quantum Mechanics in Three Dimensions
short_title: Chapter 7. Quantum Mechanics in Three Dimensions
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Write the time-independent Schrödinger equation in three dimensions and apply it to separable Cartesian potentials such as the 3D infinite box.
- Explain why central (spherically symmetric) potentials are naturally treated in spherical coordinates, and describe the separation of variables $\psi(r,\theta,\phi) = R(r)Y(\theta,\phi)$.
- Identify the three quantum numbers ($n$, $\ell$, $m_\ell$) that arise from solving a central-potential problem and state the physical quantity each one labels.
- State the quantization of orbital angular momentum magnitude and $z$-component, and explain the physical meaning of each.
- Explain why the three-dimensional treatment is the necessary foundation for the hydrogen atom, developed in Chapter 8.

## Introduction

Chapter 6 solved the Schrödinger equation for several one-dimensional potentials, but every atom, molecule, and nucleus is a three-dimensional object, and the most important potential in atomic physics — the Coulomb attraction between an electron and a nucleus — depends only on the distance $r$ from a fixed center, not on a single Cartesian coordinate. This chapter extends the Schrödinger equation to three dimensions and develops the machinery — separation of variables in spherical coordinates, and the angular momentum quantum numbers that emerge from it — needed to solve any **central-potential** problem, of which the hydrogen atom (Chapter 8) is the most important example. The results obtained here, especially the quantization of angular momentum, apply unchanged to every central potential, not just the Coulomb potential, and reappear throughout atomic, molecular, and nuclear physics.

## The Schrödinger Equation in Three Dimensions

Generalizing Chapter 6 to three spatial dimensions, the time-independent Schrödinger equation for a particle of mass $m$ in a potential $V(x,y,z)$ is

$$
-\frac{\hbar^2}{2m}\left(\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2}\right) + V(x,y,z)\,\psi = E\psi,
$$

or, compactly, $-\dfrac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$, where $\nabla^2$ is the Laplacian operator. As in one dimension, $|\psi(x,y,z)|^2\,dV$ gives the probability of finding the particle in the volume element $dV$ about $(x,y,z)$, and $\psi$ must be normalizable: $\int |\psi|^2\, dV = 1$.

When the potential is **separable in Cartesian coordinates**, $V(x,y,z) = V_1(x) + V_2(y) + V_3(z)$, the equation can be solved by seeking product solutions $\psi(x,y,z) = X(x)Y(y)Z(z)$, which reduces the problem to three independent one-dimensional Schrödinger equations, one per coordinate, each solved exactly as in Chapter 6. For a **3D infinite box** of side lengths $L_x, L_y, L_z$ (a direct generalization of the infinite square well), this gives

$$
E_{n_x,n_y,n_z} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2}\right), \qquad n_x, n_y, n_z = 1, 2, 3, \ldots,
$$

with three independent quantum numbers, one per dimension. A notable feature not seen in one dimension: for a cubic box ($L_x=L_y=L_z=L$), distinct combinations of $(n_x,n_y,n_z)$ — e.g., $(2,1,1)$, $(1,2,1)$, $(1,1,2)$ — can give the *same* total energy. This is called **degeneracy**, and it is a recurring feature of higher-dimensional quantum systems, generally traceable to an underlying symmetry of the potential (here, the equivalence of the three directions in a cube).

## Central Potentials and Spherical Coordinates

The Coulomb potential, and most potentials of physical interest in atomic and nuclear physics, depend only on the distance from a fixed point: $V(x,y,z) = V(r)$, where $r = \sqrt{x^2+y^2+z^2}$. Such a potential is not separable in Cartesian coordinates, but it *is* separable in **spherical coordinates** $(r,\theta,\phi)$, precisely because its symmetry matches that coordinate system. Written in spherical coordinates, the Schrödinger equation for a central potential admits solutions of the separable form

$$
\psi(r,\theta,\phi) = R(r)\, Y(\theta,\phi),
$$

where $R(r)$, the **radial wave function**, depends on the specific form of $V(r)$ and carries the information about the particle's radial probability distribution, while $Y(\theta,\phi)$, the **angular wave function**, turns out to be *completely independent of the specific form of $V(r)$* — it is determined entirely by the requirement that $\psi$ be single-valued and well-behaved on the sphere, and is therefore the same set of functions for the hydrogen atom, a 3D harmonic oscillator, or any other central potential.

## Orbital Angular Momentum

The separation above is not a mathematical accident: it reflects the fact that a central potential exerts no torque about the force center (the force is always radial), so **orbital angular momentum**, $\vec L = \vec r\times\vec p$, is conserved, exactly as in classical central-force motion (e.g., Kepler orbits). Solving the angular equation subject to the single-valuedness of $Y(\theta,\phi)$ shows that the magnitude and one Cartesian component (conventionally the $z$-component) of $\vec L$ are simultaneously quantized:

$$
L = \sqrt{\ell(\ell+1)}\,\hbar, \qquad \ell = 0, 1, 2, \ldots, n-1,
$$

$$
L_z = m_\ell\hbar, \qquad m_\ell = -\ell, -\ell+1, \ldots, 0, \ldots, \ell-1, \ell,
$$

where $\ell$ is the **orbital angular momentum quantum number** and $m_\ell$ is the **magnetic quantum number**, so named because $L_z$ determines how the system's energy shifts in an external magnetic field (Chapter 9). For a given $\ell$, there are $2\ell+1$ allowed values of $m_\ell$, corresponding to $2\ell+1$ distinct orientations of the angular momentum vector relative to the chosen $z$-axis — a specific, testable manifestation of **space quantization**: the orbital angular momentum vector does not merely have a quantized *length*, it can only point in a discrete set of directions relative to an external axis, rather than any direction whatsoever as classical mechanics would allow.

Two features are worth emphasizing, since both run against classical intuition. First, $L = \sqrt{\ell(\ell+1)}\hbar$, not $\ell\hbar$ — the "extra" factor means the angular momentum vector's length is always slightly *larger* than its maximum possible $z$-component, $m_{\ell,\max}\hbar = \ell\hbar$; the vector can never point exactly along the $z$-axis. Second, because $L_x$ and $L_y$ are not simultaneously measurable with $L_z$ (an uncertainty relation analogous to $\Delta x\,\Delta p_x \geq \hbar/2$ holds among the components of angular momentum), only the magnitude $L$ and a single component $L_z$ can be assigned definite values at once — the other two components remain fundamentally indeterminate, consistent with the vector never lying exactly along any single axis.

Historically, states of a given $\ell$ are labeled by spectroscopic letters inherited from early atomic spectroscopy: $\ell = 0,1,2,3,4,\ldots$ are denoted $s, p, d, f, g,\ldots$ respectively — a labeling convention used throughout atomic physics (Chapters 8–9) and retained today purely by tradition.

## The Three Quantum Numbers of a Central-Potential Bound State

Solving the full three-dimensional problem for a bound state in a central potential $V(r)$ produces exactly three quantum numbers, each arising from a separate boundary condition in the separation of variables:

- $n$, the **principal quantum number**, arising from solving the radial equation subject to normalizability, and primarily governing the energy (in a form depending on the specific $V(r)$; for the Coulomb potential this dependence takes an especially simple form, worked out in Chapter 8);
- $\ell$, the **orbital angular momentum quantum number**, $\ell = 0, 1, \ldots, n-1$, governing the magnitude of orbital angular momentum;
- $m_\ell$, the **magnetic quantum number**, $m_\ell = -\ell,\ldots,\ell$, governing the orientation of orbital angular momentum relative to a chosen axis.

This same trio of quantum numbers, with the same allowed ranges and the same physical meaning, appears in every central-potential problem in this book — it is a consequence of three-dimensional rotational symmetry, not a special feature of any one potential — and Chapter 8 specializes this general machinery to the specific radial equation of the hydrogen atom's Coulomb potential.

## Summary

- The 3D Schrödinger equation, $-\dfrac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$, reduces to three independent 1D equations for a Cartesian-separable potential (e.g., the 3D infinite box), which can produce **degeneracy** — distinct quantum states sharing the same energy — as a signature of underlying symmetry.
- A **central potential**, $V(r)$, is separable in spherical coordinates as $\psi(r,\theta,\phi)=R(r)Y(\theta,\phi)$; the angular part $Y(\theta,\phi)$ is universal, independent of the specific form of $V(r)$.
- Orbital angular momentum is quantized in both magnitude, $L = \sqrt{\ell(\ell+1)}\hbar$ ($\ell = 0,1,\ldots,n-1$), and $z$-component, $L_z = m_\ell\hbar$ ($m_\ell = -\ell,\ldots,\ell$) — **space quantization** — with $2\ell+1$ allowed orientations for each $\ell$; $L_x$ and $L_y$ remain simultaneously indeterminate.
- Three quantum numbers, $n$, $\ell$, $m_\ell$, universally characterize a bound state in any central potential; states are conventionally labeled $s,p,d,f,\ldots$ for $\ell=0,1,2,3,\ldots$.

## Problems

1. For a cubic 3D infinite box of side $L$, list the three lowest-lying distinct energy levels (in units of $h^2/8mL^2$) and the quantum-number triples $(n_x,n_y,n_z)$ that produce each, noting any degeneracies.

2. An electron is in a state with $\ell = 2$. (a) List all allowed values of $m_\ell$. (b) Compute the magnitude $L$ of its orbital angular momentum (in units of $\hbar$). (c) Compute the maximum possible value of $L_z$, and show it is strictly less than $L$, explaining why physically.

3. How many distinct $(\ell, m_\ell)$ combinations are allowed for principal quantum number $n=3$? List them, grouped by $\ell$, and give the spectroscopic letter for each $\ell$ value.

4. Explain, using the uncertainty relation among the components of angular momentum, why an electron in a state of definite $L$ and $L_z$ cannot simultaneously have a definite value of $L_x$, and why this is consistent with the angular momentum vector never lying exactly along the $z$-axis.

5. A particle is in a central-potential bound state with $n=4$. What is the maximum possible orbital angular momentum quantum number $\ell$ it can have, and how many total $(\ell,m_\ell)$ states are available at that $n$ (summed over all allowed $\ell$)?

6. Explain qualitatively why the *angular* part of the wave function, $Y(\theta,\phi)$, does not depend on the specific functional form of $V(r)$, while the *radial* part, $R(r)$, does — referring to which term(s) in the separated Schrödinger equation involve $V(r)$ and which involve only the angular derivatives.
