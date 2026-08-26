"""Generate the computed figures for Chapter 10, The Hydrogen Atom.

Radial wave functions R_nl(r) are the standard closed-form hydrogen
solutions (verified against OpenStax *University Physics Volume 3* §8.2,
Table 8.2.1, and standard references), written in units of the Bohr
radius a0 = 1.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from figstyle import BLUE, RED, GREEN, PURPLE, ORANGE, GRAY, save, use_style


# --- Hydrogen radial wave functions R_nl(rho), rho = r / a0, with a0 = 1 ---
# Each returns R_nl(rho) with the standard normalization (a0 == 1 so the
# a0^{-3/2} prefactor is just 1).

def R10(rho):
    return 2 * np.exp(-rho)


def R20(rho):
    return (1 / (2 * np.sqrt(2))) * (2 - rho) * np.exp(-rho / 2)


def R21(rho):
    return (1 / (2 * np.sqrt(6))) * rho * np.exp(-rho / 2)


def R30(rho):
    return (2 / (81 * np.sqrt(3))) * (27 - 18 * rho + 2 * rho ** 2) * np.exp(-rho / 3)


def R31(rho):
    return (4 / (81 * np.sqrt(6))) * (6 - rho) * rho * np.exp(-rho / 3)


def R32(rho):
    return (4 / (81 * np.sqrt(30))) * rho ** 2 * np.exp(-rho / 3)


STATES = [
    ("1s", R10, BLUE, 12),
    ("2s", R20, RED, 12),
    ("2p", R21, RED, 20),
    ("3s", R30, GREEN, 30),
    ("3p", R31, GREEN, 30),
    ("3d", R32, GREEN, 30),
]


def radial_probability():
    """P(r) = r^2 R_nl(r)^2 for 1s, 2s, 2p, 3s, 3p, 3d, showing the node count n-l-1."""
    fig = plt.figure(figsize=(7.8, 7.2))
    gs = GridSpec(3, 2, hspace=0.55, wspace=0.28, figure=fig)

    n_minus_l_minus_1 = {"1s": 0, "2s": 1, "2p": 0, "3s": 2, "3p": 1, "3d": 0}

    for i, (label, R, color, rmax) in enumerate(STATES):
        ax = fig.add_subplot(gs[i // 2, i % 2])
        rho = np.linspace(1e-4, rmax, 800)
        P = rho ** 2 * R(rho) ** 2
        ax.plot(rho, P, color=color, lw=1.8)

        # Mark interior nodes (zeros of R other than rho=0), by sign changes.
        Rvals = R(rho)
        sign_changes = np.where(np.diff(np.sign(Rvals)) != 0)[0]
        nodes = n_minus_l_minus_1[label]
        for idx in sign_changes[:nodes]:
            ax.axvline(rho[idx], color=GRAY, lw=0.8, ls=":")

        ax.set_yticks([])
        ax.set_xlim(0, rmax)
        ax.set_title(label, fontsize=11, fontweight="bold", color=color)
        ax.set_xlabel(r"$r / a_0$", fontsize=9.5)
        ax.text(0.96, 0.86, f"nodes: {nodes}", transform=ax.transAxes,
                ha="right", fontsize=8.5, color=GRAY)
        if i % 2 == 0:
            ax.set_ylabel(r"$P(r)=r^2|R_{n\ell}|^2$", fontsize=9.5)

    fig.suptitle(r"Radial probability distributions: $n-\ell-1$ nodes, one peak family per $n$",
                 fontsize=12, fontweight="bold", y=0.995)
    save(fig, "ch10-radial-probability")


def energy_level_diagram():
    """Energy levels n=1..5 (plus the ionization limit) with Lyman/Balmer/Paschen arrows."""
    E = lambda n: -13.6 / n ** 2
    # Plot position uses -1/n (not -1/n^2) purely to space the high-n levels
    # out legibly; the *labels* still quote the real energy E_n = -13.6 eV/n^2.
    y = lambda n: -1.0 / n
    ns = [1, 2, 3, 4, 5]

    fig, ax = plt.subplots(figsize=(7.6, 7.4))

    xw = 1.05  # half-width of each level line
    for n in ns:
        ax.plot([-xw, xw], [y(n), y(n)], color="#333333", lw=2.0, zorder=3)
        ax.text(xw + 0.08, y(n), rf"$n={n}$,  $E_{{{n}}}={E(n):.2f}$ eV",
                va="center", fontsize=9.5, zorder=3)
    ax.axhline(0, color=GRAY, lw=1.0, ls="--", zorder=1)
    ax.text(xw + 0.08, 0.06, r"$n=\infty$,  $E=0$  (ionization limit)",
            va="center", fontsize=9.5, color=GRAY)

    # Series: Lyman (-> n=1), Balmer (-> n=2), Paschen (-> n=3). Each series
    # gets its own small cluster of parallel arrows, spread in x so they
    # don't overlap, with an arrow per upper level actually drawn, running
    # within the level lines' own span so each arrow visibly lands on its line.
    series = [
        ("Lyman", [2, 3, 4, 5], 1, BLUE, -0.62),
        ("Balmer", [3, 4, 5], 2, RED, 0.0),
        ("Paschen", [4, 5], 3, GREEN, 0.62),
    ]
    for name, uppers, lower, color, xcenter in series:
        xs = np.linspace(xcenter - 0.15 * (len(uppers) - 1) / 2,
                          xcenter + 0.15 * (len(uppers) - 1) / 2, len(uppers))
        for xpos, upper in zip(xs, uppers):
            ax.annotate(
                "", xy=(xpos, y(lower) + 0.012), xytext=(xpos, y(upper) - 0.012),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.2,
                                 shrinkA=0, shrinkB=0, mutation_scale=9),
                zorder=2,
            )
        ax.text(xcenter, y(uppers[-1]) - 0.07, name, ha="center", fontsize=10.5,
                fontweight="bold", color=color)

    ax.set_xlim(-1.9, 4.1)
    ax.set_ylim(-1.08, 0.16)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylabel(r"$E_n = -13.6\ \mathrm{eV}/n^2$  (axis position $\propto -1/n$, for legibility)")
    ax.set_title("Hydrogen energy levels and the Lyman, Balmer, and Paschen series")
    fig.tight_layout()
    save(fig, "ch10-energy-levels")


if __name__ == "__main__":
    use_style()
    print("Chapter 10 figures:")
    radial_probability()
    energy_level_diagram()
