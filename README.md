# StayWatch — discussion deck

A 30-slide deck for StayWatch, a service that watches a refundable hotel booking after it is
made and alerts the guest when the same room gets cheaper.

`index.html` is the whole deck in one self-contained file (~1.2 MB): photos and fonts are
inlined, so it opens offline, can be sent as a single attachment, and makes no network
requests. Open it in any browser.

**Navigate:** arrow keys, space, Page Up/Down, Home/End, or click the right/left side of the
slide. `#12` in the URL opens slide 12. Print to PDF gives one landscape page per slide.

## Edit and rebuild

Never edit `index.html` by hand — it is generated.

```
src/head.html          styles and page shell (top)
src/slides/sNN_*.html  one file per slide, in order
src/tail.html          navigation script and the PRODUCT_NAME constant
src/fonts/             Instrument Serif + Geist (woff2, SIL OFL 1.1)
images/                source photographs and CREDITS.md
build.py               assembles the slides and inlines photos and fonts
```

```bash
pip install pillow
python3 build.py
```

To rename the product, change `PRODUCT_NAME` in `src/tail.html` and rebuild.
Design rules and the slide list are in `DESIGN_SPEC.md`; the original content brief is
`PRESENTATION_BRIEF.md`.

## Deploy on Vercel

The repo is ready for Vercel as a static site — no framework, no build step on Vercel.

1. In Vercel, **Add New → Project** and import this GitHub repository.
2. Leave **Framework Preset** as **Other**, and leave the build command and output directory
   empty.
3. Deploy.

`.vercelignore` uploads only `index.html` and `vercel.json`; the sources, notes and photos
stay in the repo but are not served. `vercel.json` sends `X-Robots-Tag: noindex` because the
deck is an internal discussion document — remove that header if it should appear in search.
After editing slides, run `python3 build.py` and commit the new `index.html`; Vercel
redeploys on push.

## Credits

Photographs are from Wikimedia Commons under CC BY, CC BY-SA and Free Art licences — see
`images/CREDITS.md` and the deck's Sources slide. Fonts are under the SIL Open Font Licence
(`src/fonts/OFL-*.txt`).
