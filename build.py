#!/usr/bin/env python3
"""Build the deck into one self-contained index.html.

    python3 build.py

Reads src/head.html + src/slides/s*.html (in file-name order) + src/tail.html, then
inlines everything the page needs so it works offline and as a single attachment:
  - photos in images/ are re-encoded at display size and inlined as base64 JPEG
    (hero 1920 px wide, everything else 640 px)
  - fonts in src/fonts/ are inlined as base64 woff2 in place of the @fonts marker

Needs Pillow (pip install pillow). Makes no network requests.
"""
import base64
import io
import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("build.py needs Pillow:  pip install pillow")

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "index.html"
FONT_MARKER = "<!-- @fonts: build.py inlines src/fonts/fonts.css here -->"


def assemble() -> str:
    slides = sorted((SRC / "slides").glob("s*.html"))
    if not slides:
        sys.exit("no slides found in src/slides/")
    body = "\n\n".join(p.read_text().rstrip() for p in slides)
    print(f"slides: {len(slides)}")
    return (SRC / "head.html").read_text() + body + "\n\n" + (SRC / "tail.html").read_text()


def inline_photos(html: str) -> str:
    total = 0
    for rel in sorted(set(re.findall(r'src="(images/[^"]+\.jpe?g)"', html))):
        hero = "hero" in rel
        width, quality = (1920, 80) if hero else (640, 82)
        im = Image.open(ROOT / rel).convert("RGB")
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
        data = buf.getvalue()
        total += len(data)
        uri = "data:image/jpeg;base64," + base64.b64encode(data).decode()
        html = html.replace(f'src="{rel}"', f'src="{uri}"')
        print(f"  {rel}: {len(data) // 1024} KB")
    print(f"photos: {total // 1024} KB")
    return html


def inline_fonts(html: str) -> str:
    if html.count(FONT_MARKER) != 1:
        sys.exit("src/head.html must contain the @fonts marker exactly once")
    css = (SRC / "fonts" / "fonts.css").read_text()
    blocks = re.findall(r"@font-face\s*\{.*?\}", css, re.S)
    cache, total = {}, 0
    faces = []
    for block in blocks:
        name = re.search(r"url\(([^)]+\.woff2)\)", block).group(1)
        if name not in cache:
            data = (SRC / "fonts" / name).read_bytes()
            total += len(data)
            cache[name] = "data:font/woff2;base64," + base64.b64encode(data).decode()
        faces.append(block.replace(name, cache[name]))
    print(f"fonts: {len(faces)} faces, {len(cache)} files, {total // 1024} KB")
    return html.replace(FONT_MARKER, "<style>\n" + "\n".join(faces) + "\n</style>")


def main() -> None:
    html = inline_fonts(inline_photos(assemble()))
    leftovers = re.findall(r'(?:src|href)="images/|fonts\.googleapis', html)
    if leftovers:
        sys.exit(f"build left external references behind: {leftovers[:3]}")
    OUT.write_text(html)
    print(f"wrote {OUT.name}: {len(html.encode()) // 1024} KB")


if __name__ == "__main__":
    main()
