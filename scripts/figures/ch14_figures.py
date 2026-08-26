"""Generate the computed/schematic figures for Chapter 14, Elementary Particles
and the Standard Model.

Both figures are original schematics, drawn from scratch with matplotlib
(no source diagram is traced or copied): a pair of simple Feynman diagrams,
and a redrawn grid of the Standard Model's fundamental particles laid out in
the book's own palette rather than the familiar CERN/Wikipedia chart layout.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from figstyle import BLUE, RED, GREEN, PURPLE, ORANGE, GRAY, save, use_style

DARK = "#333333"


def _fermion_line(ax, p0, p1, color=DARK, reversed_arrow=False, lw=2.0):
    """A straight fermion line from p0 to p1 (time increasing upward).

    The arrowhead points in the direction of particle flow; for an
    antiparticle (``reversed_arrow=True``) the arrowhead points backward
    against the line's forward-in-time direction, per the usual Feynman-
    diagram convention that an outgoing antiparticle is drawn as its
    particle's line traversed backward.
    """
    p0, p1 = np.array(p0, dtype=float), np.array(p1, dtype=float)
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=color, lw=lw, zorder=3, solid_capstyle="round")
    d = p1 - p0
    mid = p0 + 0.55 * d
    eps = 0.05
    # Forward (particle-flow) arrow: head sits ahead of mid, toward p1.
    # Reversed (antiparticle) arrow: head sits behind mid, toward p0, even
    # though the line itself still extends from p0 to p1 forward in time.
    start = mid - eps * d if not reversed_arrow else mid + eps * d
    end = mid + eps * d if not reversed_arrow else mid - eps * d
    ax.annotate("", xy=tuple(end), xytext=tuple(start),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=16),
                zorder=4)


def _wavy_line(ax, p0, p1, color=BLUE, n=7, amp=0.045, lw=1.9, dashed=False):
    """A wavy (boson-propagator) line from p0 to p1."""
    p0, p1 = np.array(p0), np.array(p1)
    t = np.linspace(0, 1, 200)
    axis = p1 - p0
    length = np.hypot(*axis)
    perp = np.array([-axis[1], axis[0]]) / length
    wave = amp * np.sin(2 * np.pi * n * t)
    pts = p0[None, :] + t[:, None] * axis[None, :] + wave[:, None] * perp[None, :]
    style = dict(color=color, lw=lw, zorder=3)
    if dashed:
        ax.plot(pts[:, 0], pts[:, 1], ls=(0, (1, 1)), **style)
    else:
        ax.plot(pts[:, 0], pts[:, 1], **style)


def feynman_diagrams():
    """Two simple, original Feynman diagrams: e-e scattering and beta decay."""
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 5.0))

    # --- Panel 1: electron-electron (Moller) scattering via photon exchange ---
    ax = axes[0]
    A = (-0.32, 0.46)
    B = (0.32, 0.58)
    _fermion_line(ax, (-1.05, -0.05), A, color=BLUE)
    _fermion_line(ax, A, (-1.05, 1.05), color=BLUE)
    _fermion_line(ax, (1.05, -0.05), B, color=BLUE)
    _fermion_line(ax, B, (1.05, 1.05), color=BLUE)
    _wavy_line(ax, A, B, color=ORANGE, n=4)

    ax.text(-1.16, -0.10, r"$e^-$", color=BLUE, fontsize=12, ha="right", va="center")
    ax.text(-1.16, 1.10, r"$e^-$", color=BLUE, fontsize=12, ha="right", va="center")
    ax.text(1.16, -0.10, r"$e^-$", color=BLUE, fontsize=12, ha="left", va="center")
    ax.text(1.16, 1.10, r"$e^-$", color=BLUE, fontsize=12, ha="left", va="center")
    ax.text(0.0, 0.52, r"$\gamma$", color=ORANGE, fontsize=13, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))
    ax.plot(*A, marker="o", ms=6, color=DARK, zorder=5)
    ax.plot(*B, marker="o", ms=6, color=DARK, zorder=5)
    ax.set_title(r"$e^- e^- \to e^- e^-$ via photon exchange", fontsize=11.5)

    # --- Panel 2: beta decay via W- exchange ---
    ax2 = axes[1]
    C = (0.0, 0.42)
    D = (0.55, 0.70)
    _fermion_line(ax2, (0.0, -0.05), C, color=GREEN)
    _fermion_line(ax2, C, (0.0, 1.05), color=GREEN)
    _wavy_line(ax2, C, D, color=PURPLE, n=4, dashed=True)
    _fermion_line(ax2, D, (1.05, 1.15), color=RED)                    # e- out
    _fermion_line(ax2, D, (1.25, 0.85), color=GRAY, reversed_arrow=True)  # anti-nu out

    ax2.text(-0.10, -0.10, r"$n\ (udd)$", color=GREEN, fontsize=11, ha="left", va="center")
    ax2.text(-0.10, 1.12, r"$p\ (uud)$", color=GREEN, fontsize=11, ha="left", va="center")
    ax2.text(0.30, 0.68, r"$W^-$", color=PURPLE, fontsize=12, ha="center", va="center",
             bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none"))
    ax2.text(1.16, 1.18, r"$e^-$", color=RED, fontsize=12, ha="left", va="center")
    ax2.text(1.34, 0.83, r"$\bar\nu_e$", color=GRAY, fontsize=12, ha="left", va="center")
    ax2.plot(*C, marker="o", ms=6, color=DARK, zorder=5)
    ax2.plot(*D, marker="o", ms=6, color=DARK, zorder=5)
    ax2.set_title(r"$n \to p + e^- + \bar\nu_e$ via $W^-$ exchange", fontsize=11.5)

    for a in axes:
        a.set_xlim(-1.5, 1.5)
        a.set_ylim(-0.25, 1.35)
        a.set_aspect("equal")
        a.axis("off")
        a.annotate("", xy=(-1.42, 1.28), xytext=(-1.42, -0.18),
                    arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.2))
        a.text(-1.48, 0.55, "time", color=DARK, fontsize=10, rotation=90, ha="center", va="center")

    fig.suptitle("Reading a Feynman diagram: time runs upward, a vertex is an interaction,\n"
                  "an internal wavy line is the exchanged (virtual) boson",
                  fontsize=11, y=1.03)
    fig.tight_layout()
    save(fig, "ch14-feynman-diagrams")


def standard_model_chart():
    """A redrawn grid of the Standard Model's fundamental particles."""
    fig, ax = plt.subplots(figsize=(9.2, 5.6))

    def box(x, y, w, h, color, symbol, name, extra):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor="white",
                                lw=1.6, alpha=0.92, zorder=2))
        ax.text(x + w / 2, y + h * 0.62, symbol, ha="center", va="center",
                fontsize=15, color="white", zorder=3)
        ax.text(x + w / 2, y + h * 0.24, name, ha="center", va="center",
                fontsize=8, color="white", zorder=3)
        ax.text(x + w * 0.08, y + h * 0.86, extra, ha="left", va="center",
                fontsize=7.5, color="white", zorder=3, alpha=0.9)

    w, h, gap = 1.15, 1.15, 0.14
    quark_up = [(r"$u$", "up", r"$+\frac{2}{3}e$"), (r"$c$", "charm", r"$+\frac{2}{3}e$"),
                (r"$t$", "top", r"$+\frac{2}{3}e$")]
    quark_down = [(r"$d$", "down", r"$-\frac{1}{3}e$"), (r"$s$", "strange", r"$-\frac{1}{3}e$"),
                  (r"$b$", "bottom", r"$-\frac{1}{3}e$")]
    lep_charged = [(r"$e^-$", "electron", r"$-e$"), (r"$\mu^-$", "muon", r"$-e$"),
                   (r"$\tau^-$", "tau", r"$-e$")]
    lep_neutral = [(r"$\nu_e$", "e-neutrino", "$0$"), (r"$\nu_\mu$", r"$\mu$-neutrino", "$0$"),
                    (r"$\nu_\tau$", r"$\tau$-neutrino", "$0$")]

    x0, y0 = 0.0, 0.0
    for col in range(3):
        x = x0 + col * (w + gap)
        box(x, y0 + 3 * (h + gap), w, h, BLUE, *quark_up[col])
        box(x, y0 + 2 * (h + gap), w, h, BLUE, *quark_down[col])
        box(x, y0 + 1 * (h + gap), w, h, GREEN, *lep_charged[col])
        box(x, y0, w, h, GREEN, *lep_neutral[col])

    ax.text(x0 + 1.5 * (w + gap) - gap / 2, y0 + 4 * (h + gap) + 0.05,
            "three generations of matter fermions", ha="center", fontsize=11,
            fontweight="bold", color=DARK)
    for col, label in enumerate(["I", "II", "III"]):
        ax.text(x0 + col * (w + gap) + w / 2, y0 + 4 * (h + gap) - 0.10, label,
                ha="center", fontsize=10, color=GRAY)
    ax.text(x0 - 0.28, y0 + 3.5 * (h + gap), "quarks", rotation=90, ha="center",
            va="center", fontsize=10.5, color=BLUE, fontweight="bold")
    ax.text(x0 - 0.28, y0 + 1.5 * (h + gap), "leptons", rotation=90, ha="center",
            va="center", fontsize=10.5, color=GREEN, fontweight="bold")

    # Force carriers and the Higgs, off to the right -- no generation structure.
    xb = x0 + 3 * (w + gap) + 0.35
    bosons = [(r"$\gamma$", "photon", "EM", ORANGE),
              (r"$g$", "gluon", "strong", ORANGE),
              (r"$W^\pm$", "weak boson", "weak", ORANGE),
              (r"$Z^0$", "weak boson", "weak", ORANGE),
              (r"$H$", "Higgs boson", "mass", PURPLE)]
    for row, (sym, name, extra, color) in enumerate(bosons):
        box(xb, y0 + row * (h + gap), w, h, color, sym, name, extra)
    ax.text(xb + w / 2, y0 + 5 * (h + gap) + 0.05, "force carriers\n& Higgs",
            ha="center", fontsize=10.5, fontweight="bold", color=DARK)

    ax.set_xlim(x0 - 0.75, xb + w + 0.3)
    ax.set_ylim(y0 - 0.25, y0 + 5 * (h + gap) + 0.55)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    save(fig, "ch14-standard-model-chart")


if __name__ == "__main__":
    use_style()
    print("Chapter 14 figures:")
    feynman_diagrams()
    standard_model_chart()
