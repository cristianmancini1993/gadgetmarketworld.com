#!/usr/bin/env python3
"""Copy offer folders from devicehubspot.com into gadgetmarketworld.com."""
from __future__ import annotations

import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://devicehubspot.com"
TARGET = "https://gadgetmarketworld.com"

OFFERS = [
    {
        "geo": "pl",
        "slug": "electric-fireplace-stove-1987",
        "lang": "pl",
    },
    {
        "geo": "cz",
        "slug": "electric-fireplace-2400",
        "lang": "cs",
    },
]

ASSET_PATHS = [
    "/assets/css/stufa-effetto-camino.css",
    "/assets/img/products/x-kalor/hero.jpg",
    "/assets/img/products/x-kalor/desc-1.jpg",
    "/assets/img/products/x-kalor/desc-2.jpg",
    "/assets/img/products/x-kalor/desc-3.jpg",
]

OLD_LOAD = re.compile(
    r"<script>\s*window\.addEventListener\('load', function \(\) \{\s*"
    r"if \(window\.trackPurchase\) window\.trackPurchase\([^)]+\);\s*"
    r"\}\);\s*</script>",
    re.DOTALL,
)
META_SNIPPET = '<script src="/assets/js/meta-purchase-thankyou.js" defer></script>'


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "gadgetmarketworld-port/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def rewrite_html(html: str) -> str:
    html = html.replace(SOURCE, TARGET)
    html = html.replace("info@devicehubspot.com", "info@gadgetmarketworld.com")
    html = html.replace("devicehubspot", "gadgetmarketworld")
    html = re.sub(r"\?v=\d+", "", html)
    return html


def gtag_conversion_value(html: str) -> float | None:
    m = re.search(r"gtag\('event', 'conversion',\s*\{[^}]*'value':\s*([0-9.]+)", html, re.DOTALL)
    return float(m.group(1)) if m else None


def patch_thank_you(html: str) -> str:
    value = gtag_conversion_value(html)
    if value is not None:
        if "META_PURCHASE_VALUE:" in html:
            html = re.sub(
                r"META_PURCHASE_VALUE:\s*[0-9.]+",
                f"META_PURCHASE_VALUE: {value}",
                html,
                count=1,
            )
        else:
            html = re.sub(
                r"(PRICE:\s*[0-9.]+,\n)",
                rf"\1  META_PURCHASE_VALUE: {value},\n  META_PURCHASE_CURRENCY: 'USD',\n",
                html,
                count=1,
            )
    if OLD_LOAD.search(html):
        html = OLD_LOAD.sub(META_SNIPPET, html)
    elif META_SNIPPET not in html:
        html = html.replace(
            '<script src="/assets/js/main.js" defer></script>',
            '<script src="/assets/js/main.js" defer></script>\n' + META_SNIPPET,
        )
    return html


def index_html(geo: str, slug: str, lang: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{geo}/{slug}/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{geo}/{slug}/landing.html">
<link rel="canonical" href="{TARGET}/{geo}/{slug}/landing.html">
</head>
<body>
<p><a href="/{geo}/{slug}/landing.html">Embera: Flame Start</a></p>
</body>
</html>
"""


def download_asset(path: str) -> None:
    local = ROOT / path.lstrip("/")
    if local.is_file() and local.stat().st_size > 0:
        return
    local.parent.mkdir(parents=True, exist_ok=True)
    data = fetch(SOURCE + path)
    local.write_bytes(data)
    print("asset", local.relative_to(ROOT))


def add_sitemap_entries(geo: str, slug: str) -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    lastmod = "2026-10-07"
    entries = []
    for suffix in ("/", "/landing.html"):
        loc = f"{TARGET}/{geo}/{slug}{suffix}"
        if loc not in text:
            entries.append(
                f'  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>'
                f"<changefreq>weekly</changefreq><priority>0.95</priority></url>\n"
            )
    if entries:
        text = text.replace("</urlset>", "".join(entries) + "</urlset>")
        path.write_text(text, encoding="utf-8")
        print(f"sitemap +{len(entries)} urls")


def main() -> None:
    for asset in ASSET_PATHS:
        download_asset(asset)

    for offer in OFFERS:
        geo = offer["geo"]
        slug = offer["slug"]
        lang = offer["lang"]
        out = ROOT / geo / slug
        out.mkdir(parents=True, exist_ok=True)

        for name in ("landing.html", "thank-you.html"):
            raw = fetch(f"{SOURCE}/{geo}/{slug}/{name}").decode("utf-8")
            html = rewrite_html(raw)
            if name == "thank-you.html":
                html = patch_thank_you(html)
            (out / name).write_text(html, encoding="utf-8")
            print("wrote", out / name)

        (out / "index.html").write_text(index_html(geo, slug, lang), encoding="utf-8")
        print("wrote", out / "index.html")
        add_sitemap_entries(geo, slug)


if __name__ == "__main__":
    main()
