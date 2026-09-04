"""Figures embedded in Chapter 11 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def _orbital_boxes(ax, x0, occupations, title, color=BLUE):
    """Draw three p-orbital boxes at x0, x0+1, x0+2 with up/down arrows per occupations list."""
    for i, occ in enumerate(occupations):
        x = x0 + i
        ax.add_patch(Rectangle((x, 0), 0.8, 0.8, facecolor="white", edgecolor=DARK, lw=1.2))
        if occ >= 1:
            ax.annotate("", xy=(x + 0.3, 0.72), xytext=(x + 0.3, 0.08),
                        arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8))
        if occ >= 2:
            ax.annotate("", xy=(x + 0.5, 0.08), xytext=(x + 0.5, 0.72),
                        arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8))
    ax.text(x0 + 1.5, -0.35, title, ha="center", fontsize=10.5, color=DARK)


def hunds_rule_nitrogen():
    """Nitrogen 2p^3: Hund's rule fills all three orbitals singly before pairing (Problem 2)."""
    fig, ax = plt.subplots(figsize=(4.6, 2.6))
    _orbital_boxes(ax, 0, [1, 1, 1], r"N: $2p^3$" "\n" r"$S=\frac{3}{2}\hbar$")
    ax.set_xlim(-0.3, 3.3)
    ax.set_ylim(-0.9, 1.0)
    ax.axis("off")
    ax.set_title("Hund's rule: one electron per orbital before any pairing", fontsize=11)
    save(fig, "ch11-sol-hunds-rule-nitrogen")


def moseley_plot():
    """Moseley's law fit with two different assumptions for b, and the resulting predictions (Problems 4, 9)."""
    Z = np.array([29, 42])
    f = np.array([1.94e18, 4.226e18])
    sqrt_f = np.sqrt(f)

    a2 = (sqrt_f[1] - sqrt_f[0]) / (Z[1] - Z[0])
    b2 = Z[0] - sqrt_f[0] / a2
    a1 = sqrt_f[0] / (Z[0] - 1)

    zz = np.linspace(20, 48, 200)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(zz, a1 * (zz - 1) / 1e9, color=GREEN, lw=1.6, ls="--", label=r"single-point fit, $b=1$ (Problem 4)")
    ax.plot(zz, a2 * (zz - b2) / 1e9, color=BLUE, lw=1.8, label=rf"two-point fit, $b={b2:.2f}$ (Problem 9)")

    ax.plot(Z, sqrt_f / 1e9, "o", ms=8, color=DARK, zorder=5, label="Cu, Mo data")
    ax.plot([28], [a1 * 27 / 1e9], marker="s", ms=8, color=GREEN, zorder=5)
    ax.annotate("Ni predicted\n(b=1 model)", (28, a1 * 27 / 1e9), textcoords="offset points",
                xytext=(-55, -25), fontsize=9, color=GREEN)
    ax.plot([47], [a2 * (47 - b2) / 1e9], marker="^", ms=9, color=BLUE, zorder=5)
    ax.annotate("Ag predicted\n(two-point model)", (47, a2 * (47 - b2) / 1e9), textcoords="offset points",
                xytext=(-125, -30), fontsize=9, color=BLUE)

    ax.set_xlabel("$Z$")
    ax.set_ylabel(r"$\sqrt{f}$  ($10^9\ \sqrt{\mathrm{Hz}}$)")
    ax.set_ylim(0.85, 2.75)
    ax.legend(loc="upper left", fontsize=9)
    ax.set_title(r"Moseley's law $\sqrt{f}=a(Z-b)$: one point can only assume $b$; two points fit it")
    save(fig, "ch11-sol-moseley-plot")


def zeff_comparison():
    """Z_eff for the outer s/p electron grows across a period: Na, Mg, Cl (Problem 7)."""
    elements = ["Na $3s$", "Mg $3s$", "Cl $3p$"]
    zeff = [2.20, 2.85, 6.10]
    colors = [GREEN, BLUE, RED]
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    ax.bar(elements, zeff, color=colors, edgecolor=DARK, width=0.55, zorder=3)
    for i, z in enumerate(zeff):
        ax.text(i, z + 0.12, f"{z}", ha="center", fontsize=10, color=DARK)
    ax.set_ylabel(r"$Z_{\rm eff}$ (Slater's rules)")
    ax.set_ylim(0, 7)
    ax.set_title(r"Magnesium's outer-electron $Z_{\rm eff}$ sits between sodium's and chlorine's")
    save(fig, "ch11-sol-zeff-comparison")


def phosphorus_sulfur_exchange():
    """P (3p^3, half-filled) keeps its exchange bonus; S (3p^4) must pair one electron (Problem 8)."""
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    _orbital_boxes(ax, 0, [1, 1, 1], r"P: $3p^3$" "\n" r"$I_1=10.49$ eV", color=GREEN)
    _orbital_boxes(ax, 4, [2, 1, 1], r"S: $3p^4$" "\n" r"$I_1=10.36$ eV", color=RED)
    ax.set_xlim(-0.3, 7.3)
    ax.set_ylim(-1.0, 1.0)
    ax.axis("off")
    ax.set_title("Sulfur must pair one electron, losing part of phosphorus's exchange stabilization", fontsize=10.5)
    save(fig, "ch11-sol-phosphorus-sulfur")


def atomic_radius_anomaly():
    """Atomic radius falls across period 3 but jumps up at potassium, a new principal shell (Problem 12)."""
    elements = ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K"]
    radius = [186, 160, 143, 117, 110, 104, 99, 71, 227]
    colors = [BLUE] * 7 + [GRAY, RED]
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    ax.bar(elements, radius, color=colors, edgecolor=DARK, width=0.6, zorder=3)
    for i, r in enumerate(radius):
        ax.text(i, r + 4, f"{r}", ha="center", fontsize=9, color=DARK)
    ax.annotate("new principal shell:\n$4s$ far outside the\nfilled argon core",
                xy=(8, 227), xytext=(5.6, 195), fontsize=9.5, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
    ax.set_ylabel("atomic radius (pm)")
    ax.set_ylim(0, 260)
    ax.set_title(r"Radius shrinks across period 3, then jumps at potassium's new $n=4$ shell", fontsize=11.5)
    fig.tight_layout()
    save(fig, "ch11-sol-atomic-radius-anomaly")


if __name__ == "__main__":
    use_style()
    print("Chapter 11 solution figures:")
    hunds_rule_nitrogen()
    moseley_plot()
    zeff_comparison()
    phosphorus_sulfur_exchange()
    atomic_radius_anomaly()
