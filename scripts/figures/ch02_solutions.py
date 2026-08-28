"""Figures embedded in Chapter 2 worked solutions (not the main chapter body)."""

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch, Rectangle

from figstyle import BLUE, GREEN, GRAY, ORANGE, PURPLE, RED, save, use_style

DARK = "#333333"


def muon_two_frames():
    """Earth and muon-frame descriptions of one atmospheric crossing (Problem 4)."""
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.4), sharey=False)

    ax = axes[0]
    ax.add_patch(Rectangle((-0.55, 0), 1.1, 15, facecolor="#e8f2f8", edgecolor=BLUE, lw=1.1))
    ax.plot([-0.8, 0.8], [0, 0], color=GREEN, lw=3.0)
    ax.plot([0], [15], "o", color=RED, ms=7, zorder=5)
    ax.annotate("", xy=(0, 4.6), xytext=(0, 14.6),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2))
    ax.annotate(r"mean range $=10.4\ \mathrm{km}$", xy=(0.04, 4.6), xytext=(0.72, 7.7),
                color=RED, fontsize=9.5, arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
    ax.text(0, 15.7, "muon created", ha="center", fontsize=9.5, color=RED)
    ax.text(0, -0.75, "ground", ha="center", fontsize=9.5, color=GREEN)
    ax.annotate("", xy=(-0.38, 0), xytext=(-0.38, 15), arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
    ax.text(-0.47, 7.5, r"$15.0\ \mathrm{km}$", ha="right", va="center", rotation=90, color=GRAY, fontsize=10)
    ax.text(0, 2.2, r"$\tau=34.8\ \mu\mathrm{s}$", ha="center", color=DARK, fontsize=10)
    ax.set_title("Earth frame", fontsize=11)
    ax.set_xlim(-1.4, 1.7)
    ax.set_ylim(-1.2, 16.5)
    ax.axis("off")

    ax = axes[1]
    ax.add_patch(Rectangle((-0.55, 0), 1.1, 0.948, facecolor="#e8f2f8", edgecolor=BLUE, lw=1.1))
    ax.plot([-0.8, 0.8], [0, 0], color=GREEN, lw=3.0)
    ax.plot([0], [0.948], "o", color=RED, ms=7, zorder=5)
    ax.annotate("", xy=(0, 0.06), xytext=(0, 0.87),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.2))
    ax.text(0.1, 0.48, r"ground approaches at $0.998c$", fontsize=9.5, color=GREEN, va="center")
    ax.text(0, 1.18, "muon at rest", ha="center", fontsize=9.5, color=RED)
    ax.annotate("", xy=(-0.38, 0), xytext=(-0.38, 0.948), arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
    ax.text(-0.47, 0.474, r"$0.948\ \mathrm{km}$", ha="right", va="center", rotation=90, color=GRAY, fontsize=10)
    ax.text(0, -0.3, r"ground arrives after $3.17\ \mu\mathrm{s}$", ha="center", color=DARK, fontsize=10)
    ax.set_title("Muon frame", fontsize=11)
    ax.set_xlim(-1.4, 2.45)
    ax.set_ylim(-0.55, 1.35)
    ax.axis("off")

    fig.suptitle("One event, two consistent descriptions: time dilation and length contraction", y=1.01,
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch02-sol-muon-frames")


def worldline_angles():
    """Worldlines and their angles from the ct axis (Problem 6)."""
    fig, ax = plt.subplots(figsize=(6.2, 5.2))
    ax.axhline(0, color=DARK, lw=1.0)
    ax.axvline(0, color=DARK, lw=1.0)
    ct = [0, 5]
    ax.plot([2, 2], ct, color=GREEN, lw=2.2, label=r"rest: $x=2\ \mathrm{m}$")
    ax.plot([0, 2.5], ct, color=BLUE, lw=2.2, label=r"particle: $x=0.5ct$")
    ax.plot([0, 5], ct, color=ORANGE, lw=2.2, label=r"light: $x=ct$")
    ax.add_patch(Arc((0, 0), 1.55, 1.55, theta1=0, theta2=26.565, color=BLUE, lw=1.0))
    ax.text(0.78, 0.22, r"$26.6^\circ$", color=BLUE, fontsize=10)
    ax.add_patch(Arc((0, 0), 2.55, 2.55, theta1=0, theta2=45, color=ORANGE, lw=1.0))
    ax.text(1.35, 0.82, r"$45.0^\circ$", color=ORANGE, fontsize=10)
    ax.text(2.08, 4.7, r"$0^\circ$", color=GREEN, fontsize=10)
    ax.set_xlim(-0.55, 5.6)
    ax.set_ylim(-0.35, 5.6)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$x$ (light-seconds)")
    ax.set_ylabel(r"$ct$ (light-seconds)")
    ax.set_title(r"Worldline angle from the vertical: $\tan\theta=x/(ct)=v/c$")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(color="#d7dfe5", lw=0.8)
    save(fig, "ch02-sol-worldline-angles")


def twin_worldlines():
    """Earth-frame worldlines for the 0.80c twin-trip calculation (Problem 7)."""
    fig, ax = plt.subplots(figsize=(6.7, 5.2))
    ax.plot([0, 0], [0, 20], color=GREEN, lw=2.4, label="Alice / Earth")
    ax.plot([0, 8, 0], [0, 10, 20], color=RED, lw=2.6, label="Bob")
    ax.plot([8, 8], [0, 20], color=GRAY, lw=1.5, ls="--", label="star")
    ax.plot([8], [10], "o", color=ORANGE, ms=8, zorder=5)
    ax.annotate("turnaround\n(frame change)", xy=(8, 10), xytext=(4.45, 12.8), color=ORANGE, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.0))
    ax.text(0.2, 17.8, "Alice: 20 y", color=GREEN, fontsize=10)
    ax.text(3.7, 6.2, "Bob: 12 y proper time", color=RED, fontsize=10, rotation=51)
    ax.set_xlim(-0.7, 9.3)
    ax.set_ylim(-0.7, 21.2)
    ax.set_xlabel("distance from Earth (light-years)")
    ax.set_ylabel("Earth-frame time (years)")
    ax.set_title("Twin trip in Earth's frame: Bob's non-inertial turn breaks the symmetry")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(color="#d7dfe5", lw=0.8)
    save(fig, "ch02-sol-twin-worldlines")


if __name__ == "__main__":
    use_style()
    print("Chapter 2 solution figures:")
    muon_two_frames()
    worldline_angles()
    twin_worldlines()
