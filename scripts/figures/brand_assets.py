"""Brand assets for the *Modern Physics* site: social card, favicon, and header logos.

These are not chapter figures, so they sit slightly outside the conventions in
``README.md``:

* The **social card** is PNG, not SVG. Some social platforms will not render an
  SVG ``og:image``, which is the whole reason this file exists.
* The **favicon** is a genuine multi-size ``.ico``. MyST copies whatever
  ``site.options.favicon`` points at to ``/favicon.ico`` byte-for-byte and the
  theme hardcodes ``<link rel="icon" href="/favicon.ico">``, so the file has to
  really be an ICO rather than a PNG wearing the extension.
* The **logos** are hand-written SVG rather than matplotlib output. The mark is
  pure geometry, and ``svg.fonttype: "path"`` bloat buys nothing when there is
  no text to render.

No banner is generated: ``book-theme`` validates the ``banner`` frontmatter key
but has no render path for it (only ``article-theme`` draws one), so the asset
would never appear on this site.

The mark is a **light cone** -- the future and past cones meeting at an event.
It is the book's opening idea, and two triangles meeting at a point stay legible
down to 16 px.

Regenerate with::

    python3 scripts/figures/brand_assets.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Rectangle
from PIL import Image, ImageDraw

from figstyle import BLUE, CYCLE, GRAY, RED, use_style

IMAGES = Path(__file__).resolve().parents[2] / "images"

TITLE = "Modern Physics"
# Set two lines: one line at a readable size collides with the mark.
SUBTITLE = ("Relativity, Quantum Theory,", "and the Structure of Matter")
FOOTER = "Martin Veillette  ·  Open textbook  ·  CC BY-NC-SA 4.0"

# Light-cone mark. The past cone is muted so the mark is not a symmetric
# hourglass; the accent dot is the event at the vertex.
FUTURE = BLUE
PAST = "#8dabc4"
EVENT = RED
# Dark-theme variants: #1769aa disappears against a dark header.
FUTURE_DARK = "#5aa9e6"
PAST_DARK = "#5b7185"
EVENT_DARK = "#e8706b"

CARD_W, CARD_H = 1200, 630
DPI = 100


# --------------------------------------------------------------------------- mark


def _cone_points(cx, cy, half_w, half_h, up=True):
    """Triangle for one cone: apex at the event, opening away from it."""
    tip_y = cy + half_h if up else cy - half_h
    return [(cx, cy), (cx - half_w, tip_y), (cx + half_w, tip_y)]


def draw_mark(ax, cx, cy, half_w, half_h, future, past, event, cap_ry, lw=0.0):
    """Draw the light-cone mark in *ax*'s data coordinates (assumes equal aspect)."""
    # Past cone first, so the future cone reads as the nearer shape.
    for up, color in ((False, past), (True, future)):
        tip_y = cy + half_h if up else cy - half_h
        ax.add_patch(Polygon(_cone_points(cx, cy, half_w, half_h, up),
                             closed=True, facecolor=color, edgecolor="none", zorder=2))
        # Elliptical rim: what makes it a cone rather than an hourglass.
        ax.add_patch(Ellipse((cx, tip_y), 2 * half_w, 2 * cap_ry,
                             facecolor=color, edgecolor="none", zorder=2))
    ax.add_patch(plt.Circle((cx, cy), half_w * 0.115, facecolor=event,
                            edgecolor="none", zorder=4))


# --------------------------------------------------------------------- social card


def social_card():
    """1200x630 card used as ``project.thumbnail`` for link previews."""
    use_style()
    fig = plt.figure(figsize=(CARD_W / DPI, CARD_H / DPI), dpi=DPI)
    ax = fig.add_axes((0, 0, 1, 1))
    # Pixel coordinates with equal aspect, so ellipses are not sheared.
    ax.set_xlim(0, CARD_W)
    ax.set_ylim(0, CARD_H)
    ax.set_aspect("equal")
    ax.axis("off")

    # Accent stripe across the top, in the book's figure palette.
    band_h = 11
    seg = CARD_W / len(CYCLE)
    for i, color in enumerate(CYCLE):
        ax.add_patch(Rectangle((i * seg, CARD_H - band_h), seg, band_h,
                               facecolor=color, edgecolor="none"))

    x = 78
    ax.text(x, 390, TITLE, fontsize=60, fontweight="bold", color=BLUE,
            ha="left", va="baseline")
    for i, line in enumerate(SUBTITLE):
        ax.text(x, 318 - i * 38, line, fontsize=25, color="#333333",
                ha="left", va="baseline")
    ax.plot([x, x + 132], [230, 230], color=RED, lw=3.2, solid_capstyle="butt")
    ax.text(x, 174, FOOTER, fontsize=16.5, color=GRAY, ha="left", va="baseline")

    draw_mark(ax, cx=975, cy=318, half_w=133, half_h=158,
              future=FUTURE, past=PAST, event=EVENT, cap_ry=30)

    path = IMAGES / "social-card.png"
    fig.savefig(path, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size // 1024} KB)  {CARD_W}x{CARD_H}")
    return path


# ------------------------------------------------------------------------ favicon


def _favicon_layer(size, scale=8):
    """Render the mark at *size* px, supersampled then downsampled for clean edges."""
    s = size * scale
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    cx, cy = s / 2, s / 2
    half_w, half_h, cap_ry = s * 0.36, s * 0.43, s * 0.085

    for up, color in ((False, PAST), (True, FUTURE)):
        tip_y = cy - half_h if up else cy + half_h  # PIL y grows downward
        d.polygon([(cx, cy), (cx - half_w, tip_y), (cx + half_w, tip_y)], fill=color)
        d.ellipse([cx - half_w, tip_y - cap_ry, cx + half_w, tip_y + cap_ry], fill=color)

    r = half_w * 0.135
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=EVENT)

    return img.resize((size, size), Image.LANCZOS)


def favicon():
    """Multi-size .ico -- MyST copies this to /favicon.ico verbatim."""
    sizes = [16, 32, 48, 64, 128, 256]
    layers = [_favicon_layer(n) for n in sizes]
    path = IMAGES / "favicon.ico"
    layers[-1].save(path, format="ICO", sizes=[(n, n) for n in sizes])
    print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size // 1024} KB)  sizes {sizes}")
    return path


# -------------------------------------------------------------------------- logos


def _logo_svg(future, past, event):
    """The mark as standalone SVG, on a viewBox fitted to the art.

    The rim ellipses stick out past the cone tips, so the viewBox is computed
    from the real bounds -- a nominal square box clips them top and bottom while
    padding the sides with dead space, and the site header sizes by height.
    """
    cx = cy = 32.0
    half_w, half_h, cap_ry = 23.0, 25.0, 5.5
    top, bot = cy - half_h, cy + half_h  # SVG y grows downward
    pad = 1.5

    vb_x = cx - half_w - pad
    vb_y = top - cap_ry - pad
    vb_w = 2 * (half_w + pad)
    vb_h = (bot + cap_ry) - (top - cap_ry) + 2 * pad

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb_x:g} {vb_y:g} {vb_w:g} {vb_h:g}" role="img" aria-label="Modern Physics">
  <title>Modern Physics</title>
  <g>
    <polygon points="{cx:g},{cy:g} {cx - half_w:g},{bot:g} {cx + half_w:g},{bot:g}" fill="{past}"/>
    <ellipse cx="{cx:g}" cy="{bot:g}" rx="{half_w:g}" ry="{cap_ry:g}" fill="{past}"/>
    <polygon points="{cx:g},{cy:g} {cx - half_w:g},{top:g} {cx + half_w:g},{top:g}" fill="{future}"/>
    <ellipse cx="{cx:g}" cy="{top:g}" rx="{half_w:g}" ry="{cap_ry:g}" fill="{future}"/>
    <circle cx="{cx:g}" cy="{cy:g}" r="{half_w * 0.135:.2f}" fill="{event}"/>
  </g>
</svg>
"""


def logos():
    out = []
    for name, colors in (
        ("logo", (FUTURE, PAST, EVENT)),
        ("logo-dark", (FUTURE_DARK, PAST_DARK, EVENT_DARK)),
    ):
        path = IMAGES / f"{name}.svg"
        path.write_text(_logo_svg(*colors), encoding="utf-8")
        print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size} B)")
        out.append(path)
    return out


def main():
    IMAGES.mkdir(exist_ok=True)
    social_card()
    favicon()
    logos()


if __name__ == "__main__":
    main()
