"""Figures embedded in Chapter 9 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def angular_momentum_cones():
    """Vector-model diagram for ell=2 (all m_ell), and the narrowing minimum angle as ell grows (Problems 3, 9)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.6))

    ax0 = axes[0]
    L = np.sqrt(6)
    phi = np.linspace(0, np.pi, 200)
    ax0.plot(L * np.sin(phi), L * np.cos(phi), color=GRAY, lw=1.0, ls=":")
    for m in range(-2, 3):
        theta = np.arccos(m / L)
        color = RED if m == 2 else BLUE
        lw = 2.4 if m == 2 else 1.4
        ax0.plot([0, L * np.sin(theta)], [0, L * np.cos(theta)], color=color, lw=lw)
        ax0.axhline(m, color=GRAY, lw=0.6, ls="--")
        ax0.text(L + 0.15, m, f"$m_\\ell={m}$", va="center", fontsize=9, color=DARK)
    ax0.annotate("", xy=(0, 0), xytext=(0, L + 0.3), arrowprops=dict(arrowstyle="-", color=DARK, lw=0.8))
    ax0.text(0.05, L + 0.35, "$z$", fontsize=10)
    ax0.text(0.5, 2.55, r"$35.3^\circ$", color=RED, fontsize=10)
    ax0.set_xlim(-L - 0.3, L + 1.6)
    ax0.set_ylim(-L - 0.3, L + 0.7)
    ax0.set_aspect("equal")
    ax0.axis("off")
    ax0.set_title(r"$\ell=2$: five allowed orientations of $\vec L$", fontsize=11)

    ax1 = axes[1]
    for ell, color in [(2, BLUE), (3, RED)]:
        Lmag = np.sqrt(ell * (ell + 1))
        theta_min = np.arccos(ell / Lmag)
        ax1.plot([0, Lmag * np.sin(theta_min)], [0, Lmag * np.cos(theta_min)], color=color, lw=2.2,
                 label=rf"$\ell={ell}$: ${np.degrees(theta_min):.1f}^\circ$")
        arc = np.linspace(0, theta_min, 60)
        r_arc = 0.6 + 0.15 * ell
        ax1.plot(r_arc * np.sin(arc), r_arc * np.cos(arc), color=color, lw=1.0)
    ax1.annotate("", xy=(0, 0), xytext=(0, 4.0), arrowprops=dict(arrowstyle="-", color=DARK, lw=0.8))
    ax1.text(0.05, 4.05, "$z$", fontsize=10)
    ax1.set_xlim(-0.3, 4.0)
    ax1.set_ylim(-0.3, 4.2)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.legend(loc="upper right", fontsize=10)
    ax1.set_title(r"Minimum angle narrows as $\ell$ grows", fontsize=11)

    fig.tight_layout()
    save(fig, "ch09-sol-angular-momentum-cones")


def centrifugal_barrier():
    """The centrifugal term vanishes for ell=0 but diverges for ell=1 as r -> 0 (Problem 8)."""
    r = np.linspace(0.05, 3, 500)
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.plot(r, np.zeros_like(r), color=BLUE, lw=2.2, label=r"$\ell=0$: no barrier")
    ax.plot(r, 2.0 / r ** 2, color=RED, lw=2.2, label=r"$\ell=1$: $\propto 1/r^2$")
    ax.set_ylim(0, 10)
    ax.set_xlim(0, 3)
    ax.axvline(0, color=DARK, lw=1.0)
    ax.text(0.05, 8.6, r"$s$-state $\psi(0)\neq0$ allowed", color=BLUE, fontsize=9.5)
    ax.text(1.1, 6.0, r"$p$-state: barrier forces $\psi(0)=0$", color=RED, fontsize=9.5)
    ax.set_xlabel(r"$r$ (arbitrary units)")
    ax.set_ylabel(r"centrifugal term $\dfrac{\hbar^2\ell(\ell+1)}{2mr^2}$ (arb. units)")
    ax.legend(loc="upper right", fontsize=9.5)
    ax.set_title(r"Only $\ell=0$ has no potential barrier keeping the electron away from $r=0$")
    save(fig, "ch09-sol-centrifugal-barrier")


def oscillator_shells():
    """Isotropic 3D oscillator shells and their cumulative capacity match the first nuclear magic numbers (11, 13)."""
    shells = [(0, 1, 2, 2), (1, 3, 6, 8), (2, 6, 12, 20)]
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    for N, deg, cap, cumulative in shells:
        ax.hlines(N, 0, 1.4, color=BLUE, lw=2.4)
        ax.text(1.5, N, f"$N={N}$: spatial degeneracy ${deg}$, capacity ${cap}$", va="center", fontsize=9.8, color=DARK)
        ax.text(-0.15, N, f"cumulative\n{cumulative}", va="center", ha="right", fontsize=9.5, color=RED, fontweight="bold")
    ax.set_xlim(-1.3, 6.4)
    ax.set_ylim(-0.6, 2.6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Oscillator shell filling reproduces the first magic numbers 2, 8, 20")
    save(fig, "ch09-sol-oscillator-shells")


def p_orbital_shape():
    """Angular probability density: isotropic s-state vs. the dumbbell-shaped p_z state (Problem 15)."""
    theta = np.linspace(0, 2 * np.pi, 400)
    s_density = 0.5 * np.ones_like(theta)
    pz_density = 0.9 * np.cos(theta) ** 2

    fig, axes = plt.subplots(1, 2, figsize=(8.0, 4.2), subplot_kw=dict(projection="polar"))
    axes[0].plot(theta, s_density, color=BLUE, lw=2.0)
    axes[0].fill(theta, s_density, color=BLUE, alpha=0.25)
    axes[0].set_title(r"$s$-state: $|Y_0^0|^2$ isotropic", fontsize=11, pad=18)

    axes[1].plot(theta, pz_density, color=RED, lw=2.0)
    axes[1].fill(theta, pz_density, color=RED, alpha=0.25)
    axes[1].set_title(r"$p_z$-state: $|Y_1^0|^2\propto\cos^2\theta$" "\nnode at the equator", fontsize=11, pad=18)

    for ax in axes:
        ax.set_theta_zero_location("N")
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.grid(alpha=0.3)

    fig.tight_layout()
    save(fig, "ch09-sol-p-orbital-shape")


def zeeman_orbital_splitting():
    """An l=1 level splits into three in a field; an l=0 level does not split at all (Problem 16)."""
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.2), sharey=True)

    axes[0].hlines(0, 0, 1, color=BLUE, lw=2.4)
    axes[0].hlines([-1, 0, 1], 1.6, 2.6, color=[RED, GREEN, PURPLE], lw=2.4)
    for m, color in zip([-1, 0, 1], [RED, GREEN, PURPLE]):
        axes[0].text(2.7, m, f"$m_\\ell={m}$", va="center", fontsize=9.5, color=color)
    axes[0].annotate("", xy=(1.5, 0.9), xytext=(1.1, 0.15), arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0))
    axes[0].text(0.4, -1.6, r"$\ell=1$" "\nfield off $\\to$ on", ha="center", fontsize=10, color=DARK)
    axes[0].set_xlim(-0.3, 3.6)

    axes[1].hlines(0, 0, 1, color=BLUE, lw=2.4)
    axes[1].hlines(0, 1.6, 2.6, color=BLUE, lw=2.4)
    axes[1].text(2.7, 0, "$m_\\ell=0$", va="center", fontsize=9.5, color=BLUE)
    axes[1].annotate("", xy=(1.5, 0.05), xytext=(1.1, 0.05), arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0))
    axes[1].text(0.4, -1.6, r"$\ell=0$" "\nfield off $\\to$ on", ha="center", fontsize=10, color=DARK)
    axes[1].set_xlim(-0.3, 3.6)

    for ax in axes:
        ax.set_ylim(-2.0, 1.6)
        ax.set_xticks([])
        ax.set_yticks([])
    fig.suptitle(r"Orbital Zeeman splitting: $\ell=1$ gives three levels, $\ell=0$ gives one", fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch09-sol-zeeman-splitting")


if __name__ == "__main__":
    use_style()
    print("Chapter 9 solution figures:")
    angular_momentum_cones()
    centrifugal_barrier()
    oscillator_shells()
    p_orbital_shape()
    zeeman_orbital_splitting()
