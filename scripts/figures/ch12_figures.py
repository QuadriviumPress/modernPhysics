"""Generate the computed figures for Chapter 12, Molecular Structure.

Two figures:

- ``ch12-mo-diagram-n2-o2``: side-by-side molecular-orbital energy-level
  diagrams for N2 and O2, showing the s-p-mixing-driven swap of the
  sigma_2p / pi_2p ordering between the two molecules (sigma_2p below
  pi_2p for N2; pi_2p below sigma_2p for O2), electrons filled in from
  the bottom with Hund's rule applied to the degenerate pi levels, and
  the resulting bond order and magnetic behavior.

  Ordering verified against OpenStax *Chemistry 2e* Sec. 8.4 "Molecular
  Orbital Theory": for B2, C2, N2 the pi_2p orbitals lie below sigma_2p
  (s-p mixing is strong enough, given the small 2s-2p gap in these light
  atoms, to push sigma_2p above pi_2p); for O2, F2, Ne2 the order
  reverts to sigma_2p below pi_2p.

- ``ch12-rovibrational-spectrum``: a stick spectrum of a rovibrational
  (vibration-rotation) absorption band, showing the P-branch
  (Delta J = -1) and R-branch (Delta J = +1) lines spaced by 2B, the
  missing Q-branch (Delta J = 0, forbidden for a simple diatomic) at
  the band origin, and a schematic Boltzmann-weighted intensity
  envelope.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from figstyle import BLUE, RED, GREEN, PURPLE, ORANGE, GRAY, save, use_style

DARK = "#333333"


def _electron_pair(ax, x, y, half_width=0.16, n=2, color=DARK):
    """Draw n=1 or n=2 electron arrows centered at (x, y) on an orbital level."""
    if n == 2:
        xs = [x - half_width, x + half_width]
        dirs = [1, -1]
    else:
        xs = [x]
        dirs = [1]
    for xi, d in zip(xs, dirs):
        ax.annotate("", xy=(xi, y + d * 0.16), xytext=(xi, y - d * 0.16),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4,
                                     mutation_scale=9))


def _level(ax, xc, y, width, label=None, label_side="right", color=DARK, lw=2.0):
    ax.plot([xc - width / 2, xc + width / 2], [y, y], color=color, lw=lw, zorder=3)
    if label is not None:
        dx = width / 2 + 0.08
        if label_side == "right":
            ax.text(xc + dx, y, label, fontsize=9.5, va="center", ha="left", color=color)
        else:
            ax.text(xc - dx, y, label, fontsize=9.5, va="center", ha="right", color=color)


def _mo_panel(ax, title, mo_order, ao2s_y, ao2p_y, n_valence, note):
    """Draw one molecule's MO diagram.

    mo_order: list of (label, y, kind, degeneracy) from lowest to highest
    energy, kind in {'bonding', 'antibonding'}, degeneracy 1 (sigma) or 2 (pi).
    """
    xL, xR, xM = -2.1, 2.1, 0.0

    # Atomic-orbital levels on both sides, with dashed correlation lines to
    # the nearest molecular-orbital level(s).
    for x in (xL, xR):
        _level(ax, x, ao2s_y, 0.9, label=r"$2s$" if x == xL else None,
               label_side="left", color=GRAY, lw=1.8)
        _level(ax, x, ao2p_y, 0.9, label=r"$2p$" if x == xL else None,
               label_side="left", color=GRAY, lw=1.8)
        if x == xR:
            ax.text(x + 0.55, ao2s_y, r"$2s$", fontsize=9.5, va="center", ha="left", color=GRAY)
            ax.text(x + 0.55, ao2p_y, r"$2p$", fontsize=9.5, va="center", ha="left", color=GRAY)

    remaining = n_valence
    for label, y, kind, deg in mo_order:
        ao_y = ao2s_y if "2s" in label else ao2p_y
        for x in (xL, xR):
            ax.plot([x, xM - (0.55 if deg == 2 else 0.5)], [ao_y, y],
                    color=LIGHT_GRAY, lw=0.8, ls=":", zorder=1)
            ax.plot([x, xM + (0.55 if deg == 2 else 0.5)], [ao_y, y],
                    color=LIGHT_GRAY, lw=0.8, ls=":", zorder=1)

        color = BLUE if kind == "bonding" else RED
        if deg == 1:
            _level(ax, xM, y, 1.0, label=label, color=color)
            fill = min(2, remaining)
            if fill > 0:
                _electron_pair(ax, xM, y, n=fill, color=DARK)
            remaining -= fill
        else:
            centers = (xM - 0.35, xM + 0.35)
            for i, xc in enumerate(centers):
                _level(ax, xc, y, 0.55, color=color)
            ax.text(xM + 0.35 + 0.55 / 2 + 0.08, y, label, fontsize=9.5,
                    va="center", ha="left", color=color)
            # Hund's rule: fill each of the two degenerate orbitals with one
            # electron before pairing either one.
            slots = [(centers[0], 0), (centers[1], 0)]
            two_e_left = remaining
            order_fill = [0, 1, 0, 1]  # singly-occupy both, then pair both
            for idx in order_fill:
                if two_e_left <= 0:
                    break
                slots[idx] = (slots[idx][0], slots[idx][1] + 1)
                two_e_left -= 1
            for xc, ne in slots:
                if ne > 0:
                    _electron_pair(ax, xc, y, n=ne, color=DARK)
            remaining -= (remaining - two_e_left)

    ax.set_xlim(-3.6, 3.6)
    ax.set_ylim(0.1, 4.9)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.text(0, -0.15, note, transform=ax.get_xaxis_transform(),
            ha="center", va="top", fontsize=9.5, color=DARK)


LIGHT_GRAY = "#c9c9c9"


def mo_diagram_n2_o2():
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 7.4))

    ao2s_y, ao2p_y = 1.0, 3.3

    n2_order = [
        (r"$\sigma_{2s}$", 0.55, "bonding", 1),
        (r"$\sigma_{2s}^{*}$", 1.55, "antibonding", 1),
        (r"$\pi_{2p}$", 2.55, "bonding", 2),
        (r"$\sigma_{2p}$", 3.05, "bonding", 1),
        (r"$\pi_{2p}^{*}$", 3.75, "antibonding", 2),
        (r"$\sigma_{2p}^{*}$", 4.55, "antibonding", 1),
    ]
    o2_order = [
        (r"$\sigma_{2s}$", 0.55, "bonding", 1),
        (r"$\sigma_{2s}^{*}$", 1.55, "antibonding", 1),
        (r"$\sigma_{2p}$", 2.55, "bonding", 1),
        (r"$\pi_{2p}$", 3.05, "bonding", 2),
        (r"$\pi_{2p}^{*}$", 3.75, "antibonding", 2),
        (r"$\sigma_{2p}^{*}$", 4.55, "antibonding", 1),
    ]

    _mo_panel(axes[0], r"N$_2$  (10 valence e$^-$)", n2_order, ao2s_y, ao2p_y, 10,
              "bond order $= (8-2)/2 = 3$\nall electrons paired: diamagnetic")
    _mo_panel(axes[1], r"O$_2$  (12 valence e$^-$)", o2_order, ao2s_y, ao2p_y, 12,
              "bond order $= (8-4)/2 = 2$\ntwo unpaired e$^-$ in $\\pi_{2p}^{*}$: paramagnetic")

    fig.suptitle(
        r"Second-row homonuclear diatomics: the $\sigma_{2p}/\pi_{2p}$ order swaps",
        fontsize=13, fontweight="bold", y=1.01)
    fig.tight_layout()
    save(fig, "ch12-mo-diagram-n2-o2")


def rovibrational_spectrum():
    """Stick spectrum: P-branch and R-branch lines spaced by 2B, missing Q branch."""
    B = 1.0  # rotational constant, in arbitrary units (photon energy / hc)
    kT_over_B = 6.0  # sets how many lines carry appreciable intensity

    Jmax = 11

    def intensity(J):
        # Schematic population factor (2J+1) exp[-B J(J+1)/kT], normalized to 1 at peak.
        return (2 * J + 1) * np.exp(-J * (J + 1) / kT_over_B)

    J_R = np.arange(0, Jmax)          # R(J): Delta J = +1, from lower state J
    x_R = 2 * B * (J_R + 1)
    I_R = intensity(J_R)

    J_P = np.arange(1, Jmax)          # P(J): Delta J = -1, from lower state J
    x_P = -2 * B * J_P
    I_P = intensity(J_P)

    I_R /= I_R.max()
    I_P /= I_P.max()

    fig, ax = plt.subplots(figsize=(8.4, 4.4))

    ax.vlines(x_P, 0, I_P, color=ORANGE, lw=1.6)
    ax.vlines(x_R, 0, I_R, color=BLUE, lw=1.6)
    ax.plot(x_P, I_P, "o", color=ORANGE, ms=3)
    ax.plot(x_R, I_R, "o", color=BLUE, ms=3)

    # Missing Q branch (Delta J = 0) at the band origin.
    ax.axvline(0, color=GRAY, lw=1.2, ls="--")
    ax.text(0, 1.30, r"$Q$ branch: forbidden" "\n" r"($\Delta J = 0$)",
            ha="center", va="bottom", fontsize=9.5, color=GRAY)

    ax.annotate("", xy=(2 * B, 1.06), xytext=(0, 1.06),
                arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.0))
    ax.text(B, 1.09, r"$2B$", ha="center", fontsize=9.5, color=DARK)

    ax.annotate("", xy=(x_R[0], -0.14), xytext=(x_P[0], -0.14),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
    ax.text(0, -0.20, r"gap $\approx 4B$ at band origin $\nu_0$", ha="center",
            fontsize=9, color=GRAY, va="top")

    ax.text(x_P[len(x_P) // 2], 0.62, r"$P$ branch" "\n" r"$\Delta J = -1$",
            ha="center", fontsize=10.5, color=ORANGE, fontweight="bold")
    ax.text(x_R[len(x_R) // 2], 0.62, r"$R$ branch" "\n" r"$\Delta J = +1$",
            ha="center", fontsize=10.5, color=BLUE, fontweight="bold")

    ax.set_xlim(x_P.min() - 2, x_R.max() + 2)
    ax.set_ylim(-0.32, 1.45)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlabel(r"photon energy $\longrightarrow$   (band origin $\nu_0$ at center; lines spaced by $2B$)")
    ax.set_title("A rovibrational (vibration-rotation) absorption band")
    fig.tight_layout()
    save(fig, "ch12-rovibrational-spectrum")


if __name__ == "__main__":
    use_style()
    print("Chapter 12 figures:")
    mo_diagram_n2_o2()
    rovibrational_spectrum()
