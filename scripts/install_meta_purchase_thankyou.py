#!/usr/bin/env python3
"""Add META_PURCHASE_* to SITE_CONFIG and meta-purchase-thankyou.js on all thank-you pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Meta Purchase value (USD) per Kreadora geo — affiliate CPA
KREADORA_META_CPA: dict[str, float] = {
    "pt/kreadora-pro-2146": 19.0,
    "de/kreadora-pro-2147": 18.0,
    "lt/kreadora-pro-2148": 18.0,
    "pl/kreadora-pro-2150": 19.0,
    "hu/kreadora-pro-2151": 18.0,
    "es/kreadora-pro-3490": 17.0,
}

OLD_LOAD = re.compile(
    r"<script>\s*// Trigger Purchase / conversion event after page load\s*"
    r"window\.addEventListener\('load', function \(\) \{\s*"
    r"if \(window\.trackPurchase\) window\.trackPurchase\([^)]+\);\s*"
    r"\}\);\s*</script>",
    re.DOTALL,
)

META_SNIPPET = '<script src="/assets/js/meta-purchase-thankyou.js" defer></script>'


def gtag_conversion_value(html: str) -> float | None:
    m = re.search(r"gtag\('event', 'conversion',\s*\{[^}]*'value':\s*([0-9.]+)", html, re.DOTALL)
    return float(m.group(1)) if m else None


def price_from_config(html: str) -> float | None:
    m = re.search(r"PRICE:\s*([0-9.]+)", html)
    return float(m.group(1)) if m else None


def ensure_meta_config(html: str, value: float) -> str:
    if "META_PURCHASE_VALUE:" in html:
        html = re.sub(
            r"META_PURCHASE_VALUE:\s*[0-9.]+",
            f"META_PURCHASE_VALUE: {value}",
            html,
            count=1,
        )
        if "META_PURCHASE_CURRENCY:" not in html:
            html = html.replace(
                f"META_PURCHASE_VALUE: {value},",
                f"META_PURCHASE_VALUE: {value},\n  META_PURCHASE_CURRENCY: 'USD',",
            )
        else:
            html = re.sub(
                r"META_PURCHASE_CURRENCY:\s*'[^']*'",
                "META_PURCHASE_CURRENCY: 'USD'",
                html,
                count=1,
            )
        return html
    insert = f"  META_PURCHASE_VALUE: {value},\n  META_PURCHASE_CURRENCY: 'USD',\n"
    return re.sub(r"(PRICE:\s*[0-9.]+,\n)", r"\1" + insert, html, count=1)


def patch_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    folder = path.parent.relative_to(ROOT).as_posix()
    html = path.read_text(encoding="utf-8")
    original = html

    if folder in KREADORA_META_CPA:
        value = KREADORA_META_CPA[folder]
    else:
        value = gtag_conversion_value(html)
        if value is None:
            value = price_from_config(html)
        if value is None:
            print(f"skip (no value): {rel}")
            return False

    html = ensure_meta_config(html, value)
    if OLD_LOAD.search(html):
        html = OLD_LOAD.sub(META_SNIPPET, html)
    elif META_SNIPPET not in html:
        html = html.replace(
            '<script src="/assets/js/main.js" defer></script>',
            '<script src="/assets/js/main.js" defer></script>\n' + META_SNIPPET,
        )

    if html != original:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def main() -> None:
    updated = 0
    for path in sorted(ROOT.glob("**/thank-you.html")):
        if patch_file(path):
            updated += 1
            print("updated", path.relative_to(ROOT))
    print(f"done: {updated} files")


if __name__ == "__main__":
    main()
