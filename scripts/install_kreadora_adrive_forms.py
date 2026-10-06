#!/usr/bin/env python3
"""Install / refresh Adrice network forms on Kreadora geo landings (3 fields, localized)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBHOOK = "https://hook.eu2.make.com/p379ghguoxvm0qnbwyb6ij9e2shqjphq"
UID = "0197a185-b0bf-7062-9c73-c30ab45065b7"

CONFIG = {
    "pt/kreadora-pro-2146": {
        "offer": "2146",
        "lp": "2169",
        "ty": "https://gadgetmarketworld.com/pt/kreadora-pro-2146/thank-you.html",
        "_key": "e11412d4114f08476846174068c8952404cdb12f",
        "label_name": "Nome completo*",
        "label_addr": "Morada de entrega*",
        "label_tel": "Telemóvel*",
        "ph_name": "João Silva",
        "ph_addr": "Rua Augusta 45, 2.º Esq., 1100-048 Lisboa",
        "ph_tel": "+351 912 345 678",
        "submit": "Encomendar agora",
    },
    "de/kreadora-pro-2147": {
        "offer": "2147",
        "lp": "2170",
        "ty": "https://gadgetmarketworld.com/de/kreadora-pro-2147/thank-you.html",
        "_key": "24fa52be50545d49078319327cc8b3c48237e64e",
        "label_name": "Vor- und Nachname*",
        "label_addr": "Lieferadresse*",
        "label_tel": "Telefonnummer*",
        "ph_name": "Anna Schmidt",
        "ph_addr": "Musterstraße 12, 10115 Berlin",
        "ph_tel": "+49 151 23456789",
        "submit": "Jetzt bestellen",
    },
    "lt/kreadora-pro-2148": {
        "offer": "2148",
        "lp": "2171",
        "ty": "https://gadgetmarketworld.com/lt/kreadora-pro-2148/thank-you.html",
        "_key": "51e2a52d75dcf263e0730c6bbb4b992ba05eeb69",
        "label_name": "Vardas ir pavardė*",
        "label_addr": "Pristatymo adresas*",
        "label_tel": "Mobiliojo telefono nr.*",
        "ph_name": "Tomas Vaitkus",
        "ph_addr": "Gedimino pr. 12-5, 01103 Vilnius",
        "ph_tel": "+370 612 34567",
        "submit": "Užsisakykite dabar",
    },
    "pl/kreadora-pro-2150": {
        "offer": "2150",
        "lp": "2173",
        "ty": "https://gadgetmarketworld.com/pl/kreadora-pro-2150/thank-you.html",
        "_key": "d2c0ce9385935e78b841e0e5158215670ed376d4",
        "label_name": "Imię i nazwisko*",
        "label_addr": "Adres dostawy*",
        "label_tel": "Telefon komórkowy*",
        "ph_name": "Piotr Kowalski",
        "ph_addr": "ul. Marszałkowska 45/12, 00-001 Warszawa",
        "ph_tel": "+48 512 345 678",
        "submit": "Zamów teraz",
    },
    "hu/kreadora-pro-2151": {
        "offer": "2151",
        "lp": "2174",
        "ty": "https://gadgetmarketworld.com/hu/kreadora-pro-2151/thank-you.html",
        "_key": "f8f5ac40683cdecd3ac8fccceb62db084ed91b7d",
        "label_name": "Teljes név*",
        "label_addr": "Szállítási cím*",
        "label_tel": "Mobiltelefon*",
        "ph_name": "Gábor Tóth",
        "ph_addr": "Andrássy út 12, 1061 Budapest",
        "ph_tel": "+36 30 123 4567",
        "submit": "Rendeljen most",
    },
    "es/kreadora-pro-3490": {
        "offer": "3490",
        "lp": "3526",
        "ty": "https://gadgetmarketworld.com/es/kreadora-pro-3490/thank-you.html",
        "_key": "24f5ff7d145455977ccf68d9ccee744a1dad1650",
        "label_name": "Nombre y apellidos*",
        "label_addr": "Dirección de entrega*",
        "label_tel": "Teléfono móvil*",
        "ph_name": "Carlos Martínez",
        "ph_addr": "Calle Mayor 45, 3.º B, 28013 Madrid",
        "ph_tel": "+34 612 345 678",
        "submit": "Haz tu pedido",
    },
}

FORM_RE = re.compile(
    r'<form class="tm-order-form order-form" action="https://offers\.adricenetwork\.com/forms/html/" method="post">.*?</form>',
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
        <div class="cod-form__field">
          <label for="name{sid}">{cfg["label_name"]}</label>
          <input class="cod-form__input" id="name{sid}" type="text" name="name" autocomplete="name" placeholder="{cfg["ph_name"]}" required>
        </div>
        <div class="cod-form__field">
          <label for="street-address{sid}">{cfg["label_addr"]}</label>
          <input class="cod-form__input" id="street-address{sid}" type="text" name="street-address" autocomplete="street-address" placeholder="{cfg["ph_addr"]}" required>
        </div>
        <div class="cod-form__field">
          <label for="tel{sid}">{cfg["label_tel"]}</label>
          <input class="cod-form__input" id="tel{sid}" type="tel" name="tel" autocomplete="tel" placeholder="{cfg["ph_tel"]}" required>
        </div>
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
        raise SystemExit(f"{path}: expected 2 Adrice forms, found {len(matches)}")
    form1 = build_form(cfg, "", include_script=True)
    form2 = build_form(cfg, "-kit", include_script=False)
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
