"""Figures embedded in Chapter 7 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def debroglie_scale():
    """de Broglie wavelengths across very different systems, on a log scale (Problem 1)."""
    items = [
        ("baseball\n40 m/s", 1.14e-34, GRAY),
        ("1.0 MeV proton", 2.86e-14, PURPLE),
        ("nuclear diameter\n(reference)", 1e-14, "#bbbbbb"),
        ("54 eV electron", 1.67e-10, BLUE),
        ("atomic diameter\n(reference)", 1e-10, "#bbbbbb"),
    ]
    labels = [i[0] for i in items]
    values = [i[1] for i in items]
    colors = [i[2] for i in items]

    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    y = np.arange(len(items))
    ax.hlines(y, 1e-36, values, color=colors, lw=2.5, zorder=2)
    ax.scatter(values, y, color=colors, s=70, zorder=3)
    for yi, v in zip(y, values):
        ax.text(v * 2.2, yi, f"{v:.2e} m", va="center", fontsize=9, color=DARK)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xscale("log")
    ax.set_xlim(1e-36, 1e-8)
    ax.set_xlabel(r"de Broglie wavelength (m)")
    ax.set_title("Seventy orders of magnitude separate a baseball from an electron")
    save(fig, "ch07-sol-debroglie-scale")


def bohr_standing_wave():
    """The n=1 Bohr orbit carries exactly one de Broglie wavelength around its circumference (Problem 6)."""
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.0))

    theta = np.linspace(0, 2 * np.pi, 800)
    R, A = 1.0, 0.16
    r = R + A * np.sin(theta)
    x, y = r * np.cos(theta), r * np.sin(theta)
    axes[0].plot(x, y, color=BLUE, lw=2.0)
    axes[0].plot(R * np.cos(theta), R * np.sin(theta), color=GRAY, lw=0.8, ls=":")
    axes[0].plot([0], [0], marker="+", color=DARK, ms=10)
    axes[0].set_aspect("equal")
    axes[0].axis("off")
    axes[0].set_title(r"$n=1$ orbit: one full wave" "\nwraps exactly once", fontsize=11)

    s = theta * R  # arc length
    axes[1].plot(s, A * np.sin(theta), color=BLUE, lw=2.0)
    axes[1].axhline(0, color=GRAY, lw=0.8)
    axes[1].annotate("", xy=(2 * np.pi * R, 0.22), xytext=(0, 0.22),
                      arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.0))
    axes[1].text(np.pi * R, 0.27, r"$\lambda = 2\pi r$  (one full cycle)", ha="center", fontsize=10, color=DARK)
    axes[1].set_xlim(0, 2 * np.pi * R)
    axes[1].set_ylim(-0.4, 0.45)
    axes[1].set_xlabel("distance around the orbit")
    axes[1].set_yticks([])
    axes[1].set_title("same wave, unrolled", fontsize=11)

    fig.suptitle(r"Standing-wave condition $2\pi r = n\lambda$ at $n=1$", fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch07-sol-bohr-standing-wave")


def linewidth():
    """Finite lifetime gives a Lorentzian energy spread, not a perfectly sharp level (Problem 8)."""
    dE = 1.0  # arbitrary units; the figure is about shape, not the (tiny) numeric width
    E = np.linspace(-6, 6, 2000)
    lorentzian = (dE / 2) ** 2 / (E ** 2 + (dE / 2) ** 2)

    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    ax.plot(E, lorentzian, color=BLUE, lw=1.8)
    ax.axvline(-dE / 2, color=GRAY, lw=0.9, ls="--")
    ax.axvline(dE / 2, color=GRAY, lw=0.9, ls="--")
    ax.annotate("", xy=(-dE / 2, 0.35), xytext=(dE / 2, 0.35),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.2))
    ax.text(0, 1.18, r"FWHM $=\Delta E\sim\hbar/(2\Delta t)$", ha="center", fontsize=10, color=RED)
    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 1.3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(r"energy, relative to line center $E_0$")
    ax.set_ylabel("emission intensity")
    ax.set_title(r"A finite lifetime $\Delta t$ smears a sharp level into a Lorentzian of width $\Delta E$")
    save(fig, "ch07-sol-linewidth")


def phase_group_velocity():
    """Relativistic phase velocity exceeds c while group velocity (the real particle speed) does not (Problem 19)."""
    u_over_c = np.linspace(0.02, 0.995, 500)
    vg = u_over_c
    vp = 1.0 / u_over_c

    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    ax.plot(u_over_c, vg, color=BLUE, lw=1.8, label=r"group velocity $v_g=u$")
    ax.plot(u_over_c, vp, color=RED, lw=1.8, label=r"phase velocity $v_p=c^2/u$")
    ax.axhline(1.0, color=GRAY, lw=1.0, ls="--")
    ax.text(0.03, 1.06, r"$c$", color=GRAY, fontsize=10)
    ax.set_ylim(0, 4)
    ax.set_xlim(0, 1)
    ax.set_xlabel(r"particle speed $u/c$")
    ax.set_ylabel(r"velocity $/\,c$")
    ax.legend(loc="upper center", fontsize=10)
    ax.set_title(r"$v_g\,v_p=c^2$: the observable particle never exceeds $c$, even though $v_p$ does")
    save(fig, "ch07-sol-phase-group-velocity")


def spreading_time_scale():
    """Wave-packet spreading time for an electron vs. a dust grain: 30+ orders of magnitude apart (Problem 16)."""
    items = [
        ("electron\n(atomic scale)", 8.6e-17, BLUE),
        ("typical lab\nmeasurement (ref.)", 1.0, "#bbbbbb"),
        ("age of the universe\n(ref.)", 4.3e17, "#bbbbbb"),
        ("1 mg dust grain", 9.5e15, RED),
    ]
    labels = [i[0] for i in items]
    values = [i[1] for i in items]
    colors = [i[2] for i in items]

    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    y = np.arange(len(items))
    ax.hlines(y, 1e-18, values, color=colors, lw=2.5, zorder=2)
    ax.scatter(values, y, color=colors, s=70, zorder=3)
    for yi, v in zip(y, values):
        ax.text(v * 2.5, yi, f"{v:.1e} s", va="center", fontsize=9, color=DARK)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xscale("log")
    ax.set_xlim(1e-18, 1e20)
    ax.set_xlabel(r"spreading time $\tau\sim m(\Delta x_0)^2/\hbar$ (s)")
    ax.set_title("Only the electron's spreading could ever show up in a lab")
    save(fig, "ch07-sol-spreading-time")


if __name__ == "__main__":
    use_style()
    print("Chapter 7 solution figures:")
    debroglie_scale()
    bohr_standing_wave()
    linewidth()
    phase_group_velocity()
    spreading_time_scale()
