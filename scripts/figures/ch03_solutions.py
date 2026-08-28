"""Figures embedded in Chapter 3 worked solutions (not the main chapter body)."""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

from figstyle import BLUE, GREEN, GRAY, ORANGE, PURPLE, RED, save, use_style

DARK = "#333333"


def two_body_conservation():
    """Back-to-back products for annihilation and pion decay (Problems 3--4)."""
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.7))

    ax = axes[0]
    ax.add_patch(Circle((0, 0), 0.24, facecolor="#f4d6d6", edgecolor=RED, lw=1.4))
    ax.text(0, 0, r"$e^-e^+$", ha="center", va="center", fontsize=10, color=DARK)
    ax.annotate("", xy=(-2.0, 0), xytext=(-0.30, 0), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.4))
    ax.annotate("", xy=(2.0, 0), xytext=(0.30, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.4))
    ax.text(-1.2, 0.25, r"$\gamma$: $E=0.511\ \mathrm{MeV}$", ha="center", color=ORANGE, fontsize=10)
    ax.text(1.2, 0.25, r"$\gamma$: $E=0.511\ \mathrm{MeV}$", ha="center", color=BLUE, fontsize=10)
    ax.text(0, -0.65, r"$\vec p_\gamma+(-\vec p_\gamma)=0$", ha="center", fontsize=11, color=DARK)
    ax.set_title("Electron--positron annihilation", fontsize=11)
    ax.set_xlim(-2.35, 2.35)
    ax.set_ylim(-1.0, 0.85)
    ax.axis("off")

    ax = axes[1]
    ax.add_patch(Circle((0, 0), 0.26, facecolor="#d7e8f4", edgecolor=BLUE, lw=1.4))
    ax.text(0, 0, r"$\pi^+$ at rest", ha="center", va="center", fontsize=9.5, color=DARK)
    ax.annotate("", xy=(-1.9, 0), xytext=(-0.32, 0), arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.4))
    ax.annotate("", xy=(1.9, 0), xytext=(0.32, 0), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.4))
    ax.text(-1.12, 0.25, r"$\mu^+$: $E=109.8\ \mathrm{MeV}$", ha="center", color=GREEN, fontsize=10)
    ax.text(1.18, 0.25, r"$\nu_\mu$: $E=pc$", ha="center", color=PURPLE, fontsize=10)
    ax.text(0, -0.65, r"$p_\mu=p_\nu$ in opposite directions", ha="center", fontsize=10.5, color=DARK)
    ax.set_title("Two-body pion decay", fontsize=11)
    ax.set_xlim(-2.35, 2.35)
    ax.set_ylim(-1.0, 0.85)
    ax.axis("off")

    fig.suptitle("A parent at rest has zero total momentum, so two final products recoil back-to-back", y=1.02,
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch03-sol-two-body-conservation")


def threshold_comparison():
    """Why CM collisions make particle production far more efficient (Problems 9 and 12)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.0))

    ax = axes[0]
    ax.plot([-2.0], [0], "o", ms=12, color=RED)
    ax.text(-2.0, -0.42, "beam proton", ha="center", fontsize=9.5, color=RED)
    ax.annotate("", xy=(-0.15, 0), xytext=(-1.75, 0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5))
    ax.plot([0], [0], "o", ms=12, color=BLUE)
    ax.text(0, -0.42, "target proton", ha="center", fontsize=9.5, color=BLUE)
    ax.annotate("", xy=(1.85, 0), xytext=(0.3, 0), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=2.5, ls="--"))
    ax.text(1.18, 0.28, r"final CM moves $\rightarrow$", ha="center", color=GRAY, fontsize=10)
    ax.text(0, 0.92, r"threshold: $K_b=70m_pc^2$", ha="center", color=DARK, fontsize=11)
    ax.text(0, 0.55, r"much energy remains as forward CM motion", ha="center", color=GRAY, fontsize=9.5)
    ax.set_title("Fixed target", fontsize=11)
    ax.set_xlim(-2.45, 2.45)
    ax.set_ylim(-0.75, 1.25)
    ax.axis("off")

    ax = axes[1]
    ax.plot([-1.75], [0], "o", ms=12, color=RED)
    ax.plot([1.75], [0], "o", ms=12, color=BLUE)
    ax.text(-1.75, -0.42, "beam proton", ha="center", fontsize=9.5, color=RED)
    ax.text(1.75, -0.42, "beam proton", ha="center", fontsize=9.5, color=BLUE)
    ax.annotate("", xy=(-0.16, 0), xytext=(-1.52, 0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5))
    ax.annotate("", xy=(0.16, 0), xytext=(1.52, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.5))
    ax.plot([0], [0], "o", ms=18, color=PURPLE, zorder=4)
    ax.text(0, -0.42, "CM at rest", ha="center", fontsize=9.5, color=PURPLE)
    ax.text(0, 0.92, r"threshold: $K_b=5m_pc^2$ per beam", ha="center", color=DARK, fontsize=11)
    ax.text(0, 0.55, r"all beam energy is available for new rest mass", ha="center", color=GRAY, fontsize=9.5)
    ax.set_title("Head-on collider", fontsize=11)
    ax.set_xlim(-2.45, 2.45)
    ax.set_ylim(-0.75, 1.25)
    ax.axis("off")

    fig.suptitle(r"Producing $X$ with $m_X=10m_p$: the collider threshold is 14 times lower per proton", y=1.02,
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch03-sol-threshold-comparison")


if __name__ == "__main__":
    use_style()
    print("Chapter 3 solution figures:")
    two_body_conservation()
    threshold_comparison()
