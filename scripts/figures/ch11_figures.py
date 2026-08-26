"""Generate the computed figures for Chapter 11, Many-Electron Atoms."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, RED, GREEN, PURPLE, ORANGE, GRAY, save, use_style

# First ionization energies, Z = 1-36, in eV. NIST Atomic Spectra Database values
# (physics.nist.gov/PhysRefData/ASD/ionEnergy.html), cross-checked against the
# CRC Handbook compilation reproduced at
# https://en.wikipedia.org/wiki/Ionization_energies_of_the_elements_(data_page).
IONIZATION_ENERGY_EV = {
    1: 13.59844, 2: 24.58738, 3: 5.39171, 4: 9.32269, 5: 8.29803,
    6: 11.26030, 7: 14.53414, 8: 13.61806, 9: 17.42282, 10: 21.5646,
    11: 5.13908, 12: 7.64624, 13: 5.98577, 14: 8.15169, 15: 10.48669,
    16: 10.36001, 17: 12.96764, 18: 15.75962, 19: 4.34066, 20: 6.11316,
    21: 6.5615, 22: 6.8281, 23: 6.7462, 24: 6.7665, 25: 7.43402,
    26: 7.9024, 27: 7.8810, 28: 7.6398, 29: 7.72638, 30: 9.3942,
    31: 5.99930, 32: 7.8994, 33: 9.7886, 34: 9.75238, 35: 11.81381,
    36: 13.99961,
}

SYMBOLS = {
    1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O",
    9: "F", 10: "Ne", 11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P",
    16: "S", 17: "Cl", 18: "Ar", 19: "K", 20: "Ca", 21: "Sc", 22: "Ti",
    23: "V", 24: "Cr", 25: "Mn", 26: "Fe", 27: "Co", 28: "Ni", 29: "Cu",
    30: "Zn", 31: "Ga", 32: "Ge", 33: "As", 34: "Se", 35: "Br", 36: "Kr",
}

NOBLE_GASES = {2, 10, 18, 36}
ALKALI_METALS = {3, 11, 19}


def ionization_energy_periodicity():
    """First ionization energy vs. Z: the periodic sawtooth, Z = 1-36."""
    Z = np.array(sorted(IONIZATION_ENERGY_EV))
    E = np.array([IONIZATION_ENERGY_EV[z] for z in Z])

    fig, ax = plt.subplots(figsize=(9.4, 5.4))

    # Shade each period so the sawtooth's periodicity is visible at a glance.
    period_edges = [0, 2, 10, 18, 36]
    shade = True
    for lo, hi in zip(period_edges[:-1], period_edges[1:]):
        if shade:
            ax.axvspan(lo + 0.5, hi + 0.5, color="#eef2f6", zorder=0)
        shade = not shade

    ax.plot(Z, E, color=BLUE, lw=1.6, marker="o", ms=3.6, zorder=3)

    for z in NOBLE_GASES:
        ax.plot([z], [IONIZATION_ENERGY_EV[z]], marker="o", ms=7, color=GREEN,
                zorder=4, mec="white", mew=0.8)
    for z in ALKALI_METALS:
        ax.plot([z], [IONIZATION_ENERGY_EV[z]], marker="o", ms=7, color=RED,
                zorder=4, mec="white", mew=0.8)

    for z in NOBLE_GASES:
        ax.annotate(SYMBOLS[z], (z, IONIZATION_ENERGY_EV[z]), textcoords="offset points",
                    xytext=(0, 7), fontsize=9.5, color=GREEN, ha="center", fontweight="bold")
    for z in ALKALI_METALS:
        ax.annotate(SYMBOLS[z], (z, IONIZATION_ENERGY_EV[z]), textcoords="offset points",
                    xytext=(0, -14), fontsize=9.5, color=RED, ha="center", fontweight="bold")

    # A few interior labels to orient the reader without cluttering the plot.
    for z in [7, 24, 30]:
        ax.annotate(SYMBOLS[z], (z, IONIZATION_ENERGY_EV[z]), textcoords="offset points",
                    xytext=(0, 7), fontsize=8, color=GRAY, ha="center")

    ax.text(0.985, 0.95, "noble gases: filled shell,\nhardest to ionize",
            transform=ax.transAxes, ha="right", va="top", fontsize=9, color=GREEN)
    ax.text(0.985, 0.06, "alkali metals: one loosely\nbound $s$ electron",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=9, color=RED)

    ax.set_xlim(0.5, 36.5)
    ax.set_ylim(0, 26.5)
    ax.set_xticks([1, 2, 10, 18, 19, 36])
    ax.set_xlabel(r"atomic number $Z$")
    ax.set_ylabel("first ionization energy (eV)")
    ax.set_title("First ionization energy is periodic in $Z$, not monotonic")
    fig.tight_layout()
    save(fig, "ch11-ionization-energy")


if __name__ == "__main__":
    use_style()
    print("Chapter 11 figures:")
    ionization_energy_periodicity()
