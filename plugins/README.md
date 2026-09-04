# MyST plugins

Two plugins, both about the same problem: the website can do things paper
cannot, and the book has to survive being printed anyway.

- [`simulation.mjs`](simulation.mjs) — embeds a running browser simulation on
  the website and falls back to a screenshot, a caption, and a link everywhere
  else. Provides `{simulation}`, `{openphysics}`, `{phet}`, `{phet-legacy}`.
- [`simulation.css`](simulation.css) — hides the fallback on screen, restores it
  for browser print.
- [`export.mjs`](export.mjs) — rewrites the node types no export renderer
  handles into ones every renderer handles. Inert unless `MYST_PRINT` is set.

All three are registered in [`../myst.yml`](../myst.yml):

```yaml
project:
  plugins:
    - plugins/simulation.mjs
    - plugins/export.mjs
site:
  options:
    style: plugins/simulation.css
```

Edits to a `.mjs` plugin do **not** hot-reload. Restart `myst start` after
changing it.

# The simulation plugin

## Usage

````markdown
```{openphysics} InterferometryLab
:label: fig:ch04-interferometry-sim

Move a mirror and count fringes; shorten the coherence length and watch the
visibility collapse.
```
````

The figure is numbered and cross-referenced like any other:
`@fig:ch04-interferometry-sim`.

Four directives, one implementation:

| Directive | Argument | Resolves to |
|---|---|---|
| `{openphysics}` | repository name | `https://openphysics.github.io/<Repo>/` |
| `{phet}` | simulation name | `https://phet.colorado.edu/sims/html/<sim>/latest/<sim>_<locale>.html` |
| `{phet-legacy}` | simulation name, or `project/sim` | `https://phet.colorado.edu/sims/cheerpj/<project>/latest/<project>.html?simulation=<sim>` |
| `{simulation}` (alias `{sim}`) | a URL, or `provider:name` | whatever you give it |

So these three are the same embed:

````markdown
```{openphysics} SpecialRelativity
```
```{simulation} openphysics:SpecialRelativity
```
```{simulation} https://openphysics.github.io/SpecialRelativity/
:placeholder: ../images/my-screenshot.png
```
````

Anything that runs in an iframe works — the plugin is not tied to SceneryStack.
A bare URL just needs a `:placeholder:` to look right in a PDF.

## PhET's Java simulations

Several topics in a modern physics course — the photoelectric effect, quantum
bound states, tunneling, lasers, gas discharge, the nuclear-physics family —
have no HTML5 PhET simulation, only the original Java one. PhET still publishes
those, run in the browser by [CheerpJ](https://cheerpj.com/), and `{phet-legacy}`
addresses them:

````markdown
```{phet-legacy} photoelectric
```
```{phet-legacy} nuclear-physics/alpha-decay
```
````

The launcher takes the *project* in the path and the *simulation* in the query
string. Usually they are the same word, and a bare name is enough; where they
differ — one project shipping several sims, as `nuclear-physics` and
`bound-states` do — write `project/sim`. Both halves are visible on PhET's own
URLs, and the sim half is what names the figure and the caption link.

Two things to know before reaching for it:

- **It is slow to start.** A CheerpJ sim downloads a Java runtime before its
  first paint — tens of seconds on a cold cache. The first caption in the book
  to use one ([Chapter 6](../chapters/ch-06-particle-properties-of-waves.md))
  says so; the rest do not repeat it.
- **It is mouse-only.** Neither touch nor keyboard navigation works the way it
  does in an HTML5 sim, and there is no screen-reader support.

So prefer `{phet}` or `{openphysics}` wherever either has something equivalent.
`screens` and `screen` are joist query parameters and do nothing here; the
flavor of a multi-sim project is chosen by the `sim` half of the argument.

## Options

| Option | Default | Notes |
|---|---|---|
| `width` | `100%` | **Percentages only.** The theme mangles `px` values. |
| `aspect` | `1024:618` (OpenPhysics), `768:504` (PhET), `4:3` (PhET legacy) | Other ratios need a matching rule in `simulation.css`. |
| `placeholder` | provider screenshot | Relative to the `.md` file, `/`-prefixed for the project root, or a URL. Use **PNG or JPEG**. |
| `no-placeholder` | — | Drop the static fallback entirely. |
| `alt` | derived | Alternative text for the fallback image. |
| `title` | derived | Accessible title for the iframe. |
| `align` | `center` | `left`, `center`, `right`. |
| `label` | — | Makes the figure cross-referenceable. |
| `class` | — | Extra classes on the simulation frame. |
| `enumerated` | — | Whether the figure is numbered. |
| `params` | — | Raw query string, e.g. `snapToGrid=true&gridSpacing=2`. |
| `screens` | — | `?screens=` — restrict to particular screens. |
| `screen` | — | `?initialScreen=` — which screen to open on. |
| `locale` | `en` | SceneryStack reads `?locale=`; PhET puts it in the filename. |
| `sim-name` | the id made readable | Display name — caption link, iframe title, and alt text. Needed when the publisher's title is not its URL slug (`mri` is "Simplified MRI"). |
| `link-text` | the simulation name | Text of the caption link. |
| `no-link` | — | Suppress the caption link. |

## How the fallback works

A simulation is a JavaScript application, so it can only ever *run* on the
website. MyST reflects that: the `iframe` node is rendered by the site theme and
by nothing else. `myst-to-tex` and `myst-to-docx` have no handler for it at all.

MyST plugins cannot supply renderers for export formats — that part of the
plugin API is documented as planned, not implemented — and transforms run at the
`document`/`project` stage, before any format-specific rendering, so nothing in
the tree can tell a plugin which format is being built. The fallback therefore
has to be structural. (`export.mjs` sidesteps the same limitation from the other
side, by reading an environment variable the build script sets; that works for a
whole build, not for one node in one format.)

Each directive emits **both** an `iframe` node and a plain `image` node as
siblings inside one `figure` container, and each renderer keeps whichever of the
two it understands:

| Output | `iframe` | fallback `image` | Result |
|---|---|---|---|
| HTML site | live simulation | hidden by `simulation.css` | the simulation |
| Browser print | hidden by `@media print` | shown by `@media print` | the screenshot |
| `--pdf` / `--tex` | dropped | `\includegraphics` | screenshot + caption |
| `--typst` | renders nothing | `#image` | screenshot + caption |
| `--docx` | unsupported, skipped | embedded image | screenshot + caption |
| `--md` | folded away | becomes the `{figure}` argument | figure + link |

The caption always ends with a link to the live simulation. That link is the one
piece of the fallback that survives in every format, so a reader holding a
printed PDF still knows where to find the running thing.

Two deliberate non-choices, both of which look like obvious simplifications and
are not:

- **The iframe gets no `placeholder` child.** `myst-to-typst`'s `iframe` handler
  renders `children[0]` when it is marked `placeholder: true`. Leaving it off is
  what stops Typst from printing the screenshot twice.
- **The fallback image is not marked `placeholder: true`.** MyST's placeholder
  promotion runs only for tex/typst/docx, only if the URL extension is valid for
  that format, and leaves `myst-to-md`'s figure handler dereferencing an
  undefined `node.source`. A plain image needs none of that machinery.

`simulation.css` is load-bearing for the website: without it every simulation
has its own screenshot sitting underneath it. That is a graceful degradation
rather than a break, but it is why the stylesheet is registered in `myst.yml`.

## Screenshots

`{openphysics}` uses `Baton/screenshots/<Repo>.png`, not the `screenshots/wide.png`
each simulation publishes on its own Pages site. The latter is the PWA manifest
asset — a generic splash screen, byte-identical across most of the fleet. Baton's
are captures of the running simulation, refreshed by its own workflow, and cover
all 37 catalogued simulations one for one.

`{phet}` uses `<sim>-600.png`, which is the largest size PhET publishes.
`{phet-legacy}` uses the same name from the project directory rather than from
`sims/html`. Beware that for the oldest simulations the `-600` file is not
600 px wide: Lasers, Neon Lights and Simplified MRI publish nothing larger than
300 px, which is thin for print. A print edition should capture those three
locally and point `:placeholder:` at the capture.

Both are remote URLs. MyST downloads and caches them into `_build/`, so exports
work offline after the first build, but the *first* build of a new simulation
needs network access.

Placeholders must be **PNG or JPEG**. LaTeX accepts `.pdf .png .jpg .jpeg` and
DOCX only `.png .jpg .jpeg`; an SVG or WebP placeholder needs Inkscape or
ImageMagick on the build machine to survive an export.

A `{simulation}` given a bare URL and no `:placeholder:` falls back to
[`../images/simulation-placeholder.png`](../images/simulation-placeholder.png), a
generic card generated by
[`../scripts/figures/simulation_placeholder.py`](../scripts/figures/simulation_placeholder.py).

## Adding a provider

`PROVIDERS` at the top of `simulation.mjs` is a plain object. An entry needs a
`resolve( id, options )` returning the simulation URL and a screenshot URL, plus
the frame's aspect ratio:

```js
myhost: {
  label: 'My Host',
  aspect: '16:9',
  resolve( id, opts ) {
    return {
      url: `https://example.org/sims/${ id }/${ buildQuery( {}, opts.params ) }`,
      placeholder: `https://example.org/sims/${ id }/thumb.png`
    };
  }
}
```

If the aspect ratio is not already in `simulation.css`, add a rule for it there.
These URL patterns are conventions of the hosts, not contracts — if OpenPhysics
or PhET changes its Pages layout, `PROVIDERS` is the only thing to update.

# The export plugin

`myst-to-tex` renders a fixed set of node types and reports anything else as
`Unhandled LaTeX conversion for node of "<type>"` — then drops it. Five of the
types this book leans on are not in that set:

| Node | Written as | Count | Without the plugin |
|---|---|---|---|
| `exercise` | `:::{exercise}` | 210 | every chapter's Problems section vanishes |
| `solution` | `:::{solution}` | 210 | every worked solution vanishes |
| `aside` | `:::{margin}` | 49 | every margin note vanishes |
| `details` | `:::{dropdown}` | 14 | every dropdown body vanishes |
| `iframe` | the simulation directives | 41 | intended — the sibling screenshot carries it |

Since a plugin cannot supply a renderer, `export.mjs` rewrites those nodes into
ones the renderer already understands, and only while an export is being built:

| Node | Becomes |
|---|---|
| `exercise` | a bold **Exercise 4.1** run-in title, a `\label`, then the body |
| `solution` | the same, indented — or nothing at all, in the student edition |
| `aside` | a `blockquote`, which the template styles as a tinted rule |
| `details` | the summary as a bold lead-in, then the body, always open |
| `iframe` | removed |
| `link` (cross-page) | `\hyperref` into the PDF, or a link back to the website |

Three things make that work, and each is easy to get wrong:

- **`stage: 'project'`.** Project-stage transforms run *after*
  `resolveReferencesTransform`, so every `enumerator` is already assigned
  ("4.1") and every cross-reference's link text is already resolved. The same
  transform at `document` stage would lose both.
- **Nothing may be boxed.** About a quarter of the worked solutions contain a
  `{figure}`, and LaTeX cannot open a float inside `framed`, `minipage`, or any
  other box: it fails with *Not in outer par mode* and loses the figure, its
  caption, and every `{numref}` pointing at it. The template brackets exercises
  with plain spacing commands for exactly this reason.
- **No custom environment.** The same `.tex` feeds pandoc for the Word edition,
  and pandoc discards the entire body of an environment it does not know. Bare
  commands it cannot read are skipped harmlessly instead.

## Editions

Two environment variables steer it. Neither is set for `myst start` or
`myst build --html`, where the plugin returns immediately.

| Variable | Values | Effect |
|---|---|---|
| `MYST_PRINT` | `full`, `student` | Which edition. `student` drops all 210 solutions. Unset means the website — the plugin does nothing. |
| `MYST_SITE_URL` | a base URL | Only for chapter offprints. An offprint holds one chapter, so its "see Chapter 7" references leave the file and point at the website. Leave unset for the whole book, where the jump should stay inside the PDF. |

`../scripts/build-exports.sh` sets both correctly for each artifact; prefer it
to calling `myst build` by hand.

## Cross-references in the PDF

The book says "see Chapter 7" 251 times, and MyST resolves each one to a `link`
node carrying both the target's identifier and its *website* URL. Left alone,
`myst-to-tex` writes the URL — `\href{/ch-07-wave-properties-of-particles}{...}`
— which in a PDF is a dead relative path. `export.mjs` rewrites them to
`\hyperref`, and puts a matching `\label` at the top of each chapter, taken from
that file's own frontmatter. (`{numref}` and `{eq}` references are
`crossReference` nodes, not links; those already come out as `\ref` and are left
alone.)

Exercise labels get the same treatment, with one extra step: `\label` records
whatever counter LaTeX last stepped, which inside a Problems section is the
enclosing `\section`. Each exercise's label therefore pins `\@currentlabel` to
MyST's own enumerator first, so the printed number is the website's number
rather than whatever LaTeX happened to be holding.
