#!/usr/bin/env python3
"""Replace COD JS forms with Adrice network POST forms on Kreadora geo landings."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBHOOK = "https://hook.eu2.make.com/p379ghguoxvm0qnbwyb6ij9e2shqjphq"
UID = "0197a185-b0bf-7062-9c73-c30ab45065b7"

# geo_path -> form copy + network ids
CONFIG = {
    "es/kreadora-pro-3490": {
        "offer": "3490",
        "lp": "3526",
        "ty": "https://gadgetmarketworld.com/es/kreadora-pro-3490/thank-you.html",
        "_key": "24f5ff7d145455977ccf68d9ccee744a1dad1650",
        "label_name": "Nombre Apellidos*",
        "ph_name": "Nombre Apellidos",
        "label_addr": "Dirección*",
        "ph_addr": "Dirección",
        "label_tel": "Teléfono*",
        "ph_tel": "Teléfono",
        "submit": "Haz tu pedido",
    },
    "hu/kreadora-pro-2151": {
        "offer": "2151",
        "lp": "2174",
        "ty": "https://gadgetmarketworld.com/hu/kreadora-pro-2151/thank-you.html",
        "_key": "f8f5ac40683cdecd3ac8fccceb62db084ed91b7d",
        "label_name": "Keresztnév Vezetéknév*",
        "ph_name": "Keresztnév Vezetéknév",
        "label_addr": "Cím*",
        "ph_addr": "Cím",
        "label_tel": "Telefon*",
        "ph_tel": "Telefon",
        "submit": "Rendeljen most",
    },
    "pl/kreadora-pro-2150": {
        "offer": "2150",
        "lp": "2173",
        "ty": "https://gadgetmarketworld.com/pl/kreadora-pro-2150/thank-you.html",
        "_key": "d2c0ce9385935e78b841e0e5158215670ed376d4",
        "label_name": "Imię Nazwisko*",
        "ph_name": "Imię Nazwisko",
        "label_addr": "Adres*",
        "ph_addr": "Adres",
        "label_tel": "Telefon*",
        "ph_tel": "Telefon",
        "submit": "Zamów teraz",
    },
    "lt/kreadora-pro-2148": {
        "offer": "2148",
        "lp": "2171",
        "ty": "https://gadgetmarketworld.com/lt/kreadora-pro-2148/thank-you.html",
        "_key": "51e2a52d75dcf263e0730c6bbb4b992ba05eeb69",
        "label_name": "Vardas Pavardė*",
        "ph_name": "Vardas Pavardė",
        "label_addr": "Adresas*",
        "ph_addr": "Adresas",
        "label_tel": "Telefonas*",
        "ph_tel": "Telefonas",
        "submit": "Užsisakykite dabar",
    },
    "de/kreadora-pro-2147": {
        "offer": "2147",
        "lp": "2170",
        "ty": "https://gadgetmarketworld.com/de/kreadora-pro-2147/thank-you.html",
        "_key": "24fa52be50545d49078319327cc8b3c48237e64e",
        "label_name": "Vor- und Nachname*",
        "ph_name": "Max Mustermann",
        "label_addr": "Lieferadresse*",
        "ph_addr": "Musterstraße 10, 10115 Berlin",
        "label_tel": "Telefonnummer*",
        "ph_tel": "+49 170 1234567",
        "submit": "Jetzt bestellen",
    },
    "pt/kreadora-pro-2146": {
        "offer": "2146",
        "lp": "2169",
        "ty": "https://gadgetmarketworld.com/pt/kreadora-pro-2146/thank-you.html",
        "_key": "e11412d4114f08476846174068c8952404cdb12f",
        "label_name": "Nome próprio Apelido*",
        "ph_name": "Nome próprio Apelido",
        "label_addr": "Endereço*",
        "ph_addr": "Endereço",
        "label_tel": "Telefone*",
        "ph_tel": "Telefone",
        "submit": "Encomendar agora",
    },
}

FORM_RE = re.compile(
    r'<form class="tm-order-form order-form cod-form" novalidate>.*?</form>',
    re.DOTALL,
)


def build_form(cfg: dict, id_suffix: str = "", include_script: bool = False) -> str:
    sid = id_suffix
    script = (
        '\n        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>'
        if include_script
        else ""
    )
    return f"""      <form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name{sid}">{cfg["label_name"]}</label>
        <input id="name{sid}" type="text" name="name" autocomplete="name" placeholder="{cfg["ph_name"]}" required><br>
        <label for="street-address{sid}">{cfg["label_addr"]}</label>
        <input id="street-address{sid}" type="text" name="street-address" autocomplete="street-address" placeholder="{cfg["ph_addr"]}" required><br>
        <label for="tel{sid}">{cfg["label_tel"]}</label>
        <input id="tel{sid}" type="tel" name="tel" autocomplete="tel" placeholder="{cfg["ph_tel"]}" required><br>
        <input name="uid" type="hidden" value="{UID}" />
        <input name="offer" type="hidden" value="{cfg["offer"]}" />
        <input name="lp" type="hidden" value="{cfg["lp"]}" />
        <input name="thankyoupage" type="hidden" value="{cfg["ty"]}"/>
        <input name="webhook" type="hidden" value="{WEBHOOK}"/>
        <input name="_key" type="hidden" value="{cfg["_key"]}" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">{cfg["submit"]}</button>
        </div>{script}
      </form>"""


def patch_landing(path: Path, cfg: dict) -> None:
    html = path.read_text(encoding="utf-8")
    html = html.replace('<script src="/assets/js/form-handler.js" defer></script>\n', "")
    matches = list(FORM_RE.finditer(html))
    if len(matches) != 2:
        raise SystemExit(f"{path}: expected 2 cod forms, found {len(matches)}")
    form1 = build_form(cfg, "", include_script=True)
    form2 = build_form(cfg, "-kit", include_script=False)
    # replace from end to keep offsets
    for i, m in enumerate(reversed(matches)):
        repl = form2 if i == 0 else form1
        html = html[: m.start()] + repl + html[m.end() :]
    path.write_text(html, encoding="utf-8")
    print(f"Patched {path.relative_to(ROOT)}")


def main() -> None:
    for rel, cfg in CONFIG.items():
        patch_landing(ROOT / rel / "landing.html", cfg)


if __name__ == "__main__":
    main()
