"""Generic fallback card for the {simulation} directive.

Every simulation embedded by ``plugins/simulation.mjs`` carries a screenshot for
the outputs that cannot run JavaScript -- PDF, DOCX, Markdown, and print. The
OpenPhysics and PhET providers supply one automatically, and an author can point
at their own with ``:placeholder:``. This card is what is left: the default for a
simulation embedded by bare URL from a host this plugin knows nothing about.

Unlike the chapter figures this writes **PNG**, not SVG. LaTeX accepts only
``.pdf .png .jpg .jpeg`` and DOCX only ``.png .jpg .jpeg``; an SVG placeholder
would need Inkscape or ImageMagick on the build machine to survive an export.

Regenerate with::

    python3 scripts/figures/simulation_placeholder.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

from figstyle import BLUE, GRAY, use_style

IMAGES = Path(__file__).resolve().parents[2] / "images"

# The SceneryStack frame, which is also the aspect ratio the MyST theme assumes.
WIDTH_PX, HEIGHT_PX = 1024, 618
DPI = 100


def build():
    """Draw the card: a rounded frame, a play glyph, and a line of explanation."""
    use_style()
    fig = plt.figure(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_facecolor("white")

    # Frame, inset far enough that the rounded corners are not clipped.
    ax.add_patch(
        FancyBboxPatch(
            (0.05, 0.08),
            0.90,
            0.84,
            boxstyle="round,pad=0.0,rounding_size=0.03",
            linewidth=2.0,
            edgecolor=BLUE,
            facecolor="#f4f8fb",
            mutation_aspect=WIDTH_PX / HEIGHT_PX,
        )
    )

    # Play glyph: an equilateral triangle inside a ring.
    cx, cy, r = 0.5, 0.58, 0.105
    ax.add_patch(
        plt.Circle((cx, cy), r, transform=ax.transAxes, linewidth=2.4, edgecolor=BLUE, facecolor="none")
    )
    # Nudged right so the triangle looks centred rather than measuring centred.
    tip = 0.42 * r
    ax.add_patch(
        Polygon(
            [
                (cx - tip * 0.75 + 0.012, cy + tip * 1.15),
                (cx - tip * 0.75 + 0.012, cy - tip * 1.15),
                (cx + tip * 1.15 + 0.012, cy),
            ],
            closed=True,
            facecolor=BLUE,
            edgecolor="none",
        )
    )

    ax.text(0.5, 0.36, "Interactive simulation", ha="center", va="center",
            fontsize=27, fontweight="bold", color=BLUE)
    ax.text(0.5, 0.26, "Open the link in the caption to run it in a browser.",
            ha="center", va="center", fontsize=16, color=GRAY)

    return fig


def main():
    IMAGES.mkdir(exist_ok=True)
    path = IMAGES / "simulation-placeholder.png"
    fig = build()
    fig.savefig(path, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
