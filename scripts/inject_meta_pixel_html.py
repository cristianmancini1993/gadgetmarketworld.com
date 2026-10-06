#!/usr/bin/env python3
"""Inject Meta Pixel snippet into HTML pages that do not load tracking.js."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIXEL_MARK = "3995973087204921"
SNIPPET = """<!-- Meta Pixel Code -->
<script src="/assets/js/meta-pixel.js"></script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=3995973087204921&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
"""


def main() -> None:
    n = 0
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if PIXEL_MARK in text or "meta-pixel.js" in text:
            continue
        if "tracking.js" in text:
            continue
        if "<head>" not in text:
            continue
        text = text.replace("<head>", "<head>\n" + SNIPPET, 1)
        path.write_text(text, encoding="utf-8")
        n += 1
    print(f"Injected Meta Pixel into {n} HTML files (non-tracking pages)")


if __name__ == "__main__":
    main()
