"""Shared matplotlib styling for figures in *Modern Physics*.

All generated figures are written as SVG into ``images/`` and committed, because
the MyST build on GitHub Pages runs ``myst build --html`` only -- there is no
Python kernel at build time. Regenerate with::

    python3 scripts/figures/ch04_figures.py
    python3 scripts/figures/ch05_figures.py

The palette matches the hand-authored SVG schematics in ``images/``.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

IMAGES = Path(__file__).resolve().parents[2] / "images"

# Palette shared with the hand-drawn SVG schematics.
BLUE = "#1769aa"
RED = "#b33a3a"
GREEN = "#2e7d5b"
PURPLE = "#6a4c93"
ORANGE = "#d97706"
GRAY = "#555555"
LIGHT = "#c9d6e0"

CYCLE = [BLUE, RED, GREEN, PURPLE, ORANGE]

RC = {
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "axes.facecolor": "white",
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.9,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "legend.frameon": False,
    "legend.fontsize": 10,
    "lines.linewidth": 1.8,
    "mathtext.fontset": "dejavusans",
    "svg.fonttype": "path",
    # Stable element ids make regenerated SVGs byte-for-byte comparable in CI.
    "svg.hashsalt": "modern-physics",
    "path.simplify": True,
    "path.simplify_threshold": 1.0,
}


def use_style():
    plt.rcParams.update(RC)


def save(fig, name):
    """Save *fig* as ``images/<name>.svg`` and report the byte size."""
    IMAGES.mkdir(exist_ok=True)
    path = IMAGES / f"{name}.svg"
    fig.savefig(
        path,
        format="svg",
        bbox_inches="tight",
        pad_inches=0.12,
        metadata={"Date": "2026-01-01"},
    )
    plt.close(fig)
    print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size // 1024} KB)")
    return path


def mono_cmap(color=RED, name="mono"):
    """Black-to-*color* colormap, so an intensity strip reads like laser light on a screen."""
    from matplotlib.colors import LinearSegmentedColormap, to_rgb

    r, g, b = to_rgb(color)
    # Push the top end toward white so saturated fringes look bright, not muddy.
    return LinearSegmentedColormap.from_list(
        name, [(0.0, "#000000"), (0.75, (r, g, b)), (1.0, (min(r + 0.35, 1), min(g + 0.55, 1), min(b + 0.55, 1)))]
    )


def fringe_strip(ax, x, intensity, cmap=None, gamma=1.0):
    """Render an intensity profile as the bright/dark band pattern seen on a screen.

    ``gamma < 1`` brightens faint bands so they survive reproduction; say so in the
    caption whenever it is used, since the strip is then no longer linear in intensity.
    """
    ax.imshow(
        (intensity ** gamma)[None, :],
        aspect="auto",
        cmap=cmap if cmap is not None else mono_cmap("#d94a3d"),
        vmin=0.0,
        vmax=1.0,
        extent=(x[0], x[-1], 0, 1),
        interpolation="bilinear",
    )
    ax.set_yticks([])
    ax.set_xticks([])
    for side in ("top", "bottom", "left", "right"):
        ax.spines[side].set_visible(True)
        ax.spines[side].set_color("#333333")
        ax.spines[side].set_linewidth(0.8)
