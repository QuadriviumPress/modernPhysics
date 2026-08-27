"""Figures embedded in Chapter 14 worked solutions (not the main chapter body)."""

import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style
from ch14_figures import _fermion_line, _wavy_line

DARK = "#333333"


def conservation_checklist():
    """Which conservation laws each proposed reaction satisfies (Problems 3, 8)."""
    rows = [
        (r"(a) $p\to e^++\gamma$", {"Q": True, "B": False, "L": False, "S": None}),
        (r"(b) $n\to p+e^-+\bar\nu_e$", {"Q": True, "B": True, "L": True, "S": None}),
        (r"(c) $\mu^-\to e^-+\gamma$", {"Q": True, "B": None, "L": False, "S": None}),
        (r"(d) $p+p\to p+p+\pi^0$", {"Q": True, "B": True, "L": True, "S": None}),
        (r"(P8) $K^-+p\to\Lambda^0+\pi^0$", {"Q": True, "B": True, "L": None, "S": True}),
    ]
    cols = ["Q", "B", "L", "S"]

    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    for j, col in enumerate(cols):
        ax.text(j + 1, len(rows) + 0.3, col, ha="center", fontsize=11, fontweight="bold", color=DARK)
    for i, (label, verdicts) in enumerate(rows):
        y = len(rows) - i
        ax.text(-0.15, y, label, ha="right", va="center", fontsize=9.5, color=DARK)
        for j, col in enumerate(cols):
            v = verdicts[col]
            x = j + 1
            if v is None:
                ax.text(x, y, "–", ha="center", va="center", fontsize=12, color=GRAY)
            elif v:
                ax.add_patch(Rectangle((x - 0.42, y - 0.32), 0.84, 0.64, facecolor="#dcefdc", edgecolor=GREEN, lw=1.0))
                ax.text(x, y, "OK", ha="center", va="center", fontsize=9.5, color="#1a7a1a", fontweight="bold")
            else:
                ax.add_patch(Rectangle((x - 0.42, y - 0.32), 0.84, 0.64, facecolor="#f6dede", edgecolor=RED, lw=1.0))
                ax.text(x, y, "X", ha="center", va="center", fontsize=9.5, color="#a12424", fontweight="bold")

    ax.set_xlim(-2.6, 5.0)
    ax.set_ylim(0.2, len(rows) + 1.0)
    ax.axis("off")
    ax.set_title("Charge, baryon number, lepton number, strangeness: pass or fail per reaction", fontsize=11)
    save(fig, "ch14-sol-conservation-checklist")


def kaon_antiparticle():
    """K- and K+ have opposite charge and strangeness, as any particle/antiparticle pair must (Problem 7)."""
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    for x, label, q, s, color in [(0.0, r"$K^-=\bar us$", -1, -1, BLUE), (2.6, r"$K^+=u\bar s$", +1, +1, RED)]:
        ax.text(x, 1.0, label, ha="center", fontsize=13, color=color)
        ax.text(x, 0.35, f"$Q={'+e' if q>0 else '-e'}$", ha="center", fontsize=11, color=DARK)
        ax.text(x, -0.15, f"$S={'+' if s>0 else ''}{s}$", ha="center", fontsize=11, color=DARK)
    ax.annotate("", xy=(2.0, 0.5), xytext=(0.6, 0.5),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.2))
    ax.text(1.3, 0.65, "antiparticles:\nopposite $Q$, opposite $S$", ha="center", fontsize=9, color=GRAY)
    ax.set_xlim(-1.2, 3.8)
    ax.set_ylim(-0.5, 1.4)
    ax.axis("off")
    ax.set_title(r"$K^-$ and $K^+$: every additive quantum number flips sign")
    save(fig, "ch14-sol-kaon-antiparticle")


def muon_decay_feynman():
    """Two-vertex Feynman diagram for muon decay via W- exchange, in the style of the body's figure (Problem 9)."""
    fig, ax = plt.subplots(figsize=(5.0, 5.0))
    C = (0.0, 0.42)
    D = (0.55, 0.70)
    _fermion_line(ax, (0.0, -0.05), C, color=BLUE)
    _fermion_line(ax, C, (0.0, 1.05), color=GRAY, reversed_arrow=False)
    _wavy_line(ax, C, D, color=PURPLE, n=4, dashed=True)
    _fermion_line(ax, D, (1.05, 1.15), color=RED)
    _fermion_line(ax, D, (1.25, 0.85), color=GRAY, reversed_arrow=True)

    ax.text(-0.10, -0.10, r"$\mu^-$", color=BLUE, fontsize=12, ha="left", va="center")
    ax.text(-0.10, 1.12, r"$\nu_\mu$", color=GRAY, fontsize=12, ha="left", va="center")
    ax.text(0.30, 0.68, r"$W^-$", color=PURPLE, fontsize=12, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none"))
    ax.text(1.16, 1.18, r"$e^-$", color=RED, fontsize=12, ha="left", va="center")
    ax.text(1.34, 0.83, r"$\bar\nu_e$", color=GRAY, fontsize=12, ha="left", va="center")
    ax.plot(*C, marker="o", ms=6, color=DARK, zorder=5)
    ax.plot(*D, marker="o", ms=6, color=DARK, zorder=5)

    ax.text(0.0, 0.20, "vertex 1", fontsize=8.5, color=DARK, ha="right", va="top")
    ax.text(0.55, 0.92, "vertex 2", fontsize=8.5, color=DARK, ha="right", va="bottom")

    ax.set_xlim(-1.6, 2.1)
    ax.set_ylim(-0.25, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.annotate("", xy=(-1.42, 1.28), xytext=(-1.42, -0.18),
                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.2))
    ax.text(-1.48, 0.55, "time", color=DARK, fontsize=10, rotation=90, ha="center", va="center")
    ax.set_title(r"$\mu^-\to e^-+\bar\nu_e+\nu_\mu$ via $W^-$ exchange", fontsize=11.5)
    save(fig, "ch14-sol-muon-decay-feynman")


def muon_decay_length():
    """Mean lab-frame decay length grows with beam energy (with gamma), comparing two beams (Problem 10)."""
    m_mu = 105.7  # MeV
    tau0 = 2.20e-6  # s
    c = 3.00e8
    E = np.linspace(m_mu * 1.01, 3000, 400)
    gamma = E / m_mu
    beta = np.sqrt(1 - 1 / gamma ** 2)
    length_km = beta * c * gamma * tau0 / 1000

    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    ax.plot(E / 1000, length_km, color=BLUE, lw=1.8)
    # Locate the worked example's beam (2.4 km decay length) by inverting the curve numerically,
    # rather than assuming its energy/gamma value.
    target_len_we = 2.4
    idx_we = np.argmin(np.abs(length_km - target_len_we))
    idx_p10 = np.argmin(np.abs(E - 1200))

    for idx, label, color in [(idx_we, "worked example\n(2.4 km)", GREEN), (idx_p10, "Problem 10\n(E=1.20 GeV)", RED)]:
        ax.plot([E[idx] / 1000], [length_km[idx]], marker="o", ms=8, color=color, zorder=5)
        ax.annotate(label, (E[idx] / 1000, length_km[idx]), textcoords="offset points",
                    xytext=(10, -5), fontsize=9, color=color)

    ax.set_xlabel("total energy $E$ (GeV)")
    ax.set_ylabel(r"mean decay length $\beta c\gamma\tau_0$ (km)")
    ax.set_title(r"A more energetic muon beam travels farther, in step with $\gamma$")
    save(fig, "ch14-sol-muon-decay-length")


def gravity_em_ratio():
    """Gravity-to-electromagnetism force ratio for two electrons vs. two protons, on a log scale (Problem 11)."""
    ratios = {"two protons\n(worked example)": 8.1e-37, "two electrons\n(this problem)": 2.4e-43}
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    labels = list(ratios.keys())
    values = list(ratios.values())
    ax.bar(labels, values, color=[ORANGE, BLUE], edgecolor=DARK, width=0.55, zorder=3)
    ax.set_yscale("log")
    for i, v in enumerate(values):
        ax.text(i, v * 2, f"{v:.1e}", ha="center", fontsize=10, color=DARK)
    ax.set_ylabel(r"$F_G/F_E = Gm^2/(ke^2)$")
    ax.set_ylim(1e-45, 1e-34)
    ax.set_title(r"Same charge, six orders of magnitude less mass:" "\ngravity falls even further behind")
    save(fig, "ch14-sol-gravity-em-ratio")


if __name__ == "__main__":
    use_style()
    print("Chapter 14 solution figures:")
    conservation_checklist()
    kaon_antiparticle()
    muon_decay_feynman()
    muon_decay_length()
    gravity_em_ratio()
