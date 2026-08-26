"""Generate the computed figure for Chapter 13, Nuclear Physics."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GREEN, GRAY, ORANGE, save, use_style


def binding_energy_curve():
    """Binding energy per nucleon vs. mass number -- the central curve of nuclear physics.

    Each (A, label, E_B/A) triple is computed from standard tabulated atomic
    masses via E_B = [Z m(1H) + N m_n - M(A,Z)] c^2 (m(1H) = 1.007825 u,
    m_n = 1.008665 u, 1 u c^2 = 931.494 MeV), and cross-checked against
    published binding-energy-per-nucleon values (e.g. Wikipedia's "Nuclear
    binding energy" table for 56Fe/62Ni, OpenStax University Physics Vol. 3
    S10.2 for 4He, and standard textbook values for the others); see
    scripts/figures/README.md for the source notes.
    """
    data = [
        (2, "2H", 1.112),
        (4, "4He", 7.074),
        (7, "7Li", 5.606),
        (12, "12C", 7.680),
        (16, "16O", 7.976),
        (28, "28Si", 8.448),
        (40, "40Ca", 8.551),
        (56, "56Fe", 8.790),
        (62, "62Ni", 8.795),
        (84, "84Kr", 8.718),
        (120, "120Sn", 8.506),
        (136, "136Xe", 8.395),
        (208, "208Pb", 7.868),
        (235, "235U", 7.591),
        (238, "238U", 7.570),
    ]
    A = np.array([d[0] for d in data], dtype=float)
    E = np.array([d[2] for d in data], dtype=float)

    fig, ax = plt.subplots(figsize=(7.8, 5.2))
    ax.plot(A, E, color=BLUE, lw=1.6, marker="o", ms=5.0,
            mfc="white", mec=BLUE, mew=1.3, zorder=5)

    # Direct labels for a handful of representative nuclides.
    call_outs = {
        "2H": (2, 1.112, (10, -14)),
        "4He": (4, 7.074, (8, -16)),
        "7Li": (7, 5.606, (-4, -20)),
        "12C": (12, 7.680, (-2, 10)),
        "56Fe": (56, 8.790, (-30, 12)),
        "62Ni": (62, 8.795, (8, 10)),
        "208Pb": (208, 7.868, (6, 10)),
        "238U": (238, 7.570, (-2, -20)),
    }
    for label, (a, e, offset) in call_outs.items():
        ax.annotate(label, (a, e), textcoords="offset points", xytext=offset,
                    fontsize=8.7, color="#333333")

    # Peak marker.
    ax.axvline(62, color=GRAY, lw=0.7, ls=":", zorder=1)
    ax.annotate("peak near A=56-62\n(iron/nickel, ~8.8 MeV/nucleon)",
                xy=(62, 8.795), xytext=(98, 6.05), fontsize=9.3, color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.9))

    # Fusion: light nuclei climb the steep left flank toward the peak.
    ax.annotate("", xy=(46, 8.55), xytext=(7, 3.3),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.0,
                                 mutation_scale=16))
    ax.text(11, 2.35, "fusion\n(light $\\to$ heavy)", color=GREEN,
            fontsize=10.5, fontweight="bold")

    # Fission: heavy nuclei descend the shallow right flank toward the peak.
    ax.annotate("", xy=(150, 8.60), xytext=(233, 7.60),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.0,
                                 mutation_scale=16))
    ax.text(157, 9.05, "fission\n(heavy $\\to$ lighter)", color=ORANGE,
            fontsize=10.5, fontweight="bold")

    ax.set_xlabel(r"mass number $A$")
    ax.set_ylabel(r"binding energy per nucleon $E_B/A$ (MeV)")
    ax.set_xlim(-4, 248)
    ax.set_ylim(0, 9.9)
    ax.set_title("Binding energy per nucleon vs. mass number")
    fig.tight_layout()
    save(fig, "ch13-binding-energy-curve")


if __name__ == "__main__":
    use_style()
    print("Chapter 13 figures:")
    binding_energy_curve()
