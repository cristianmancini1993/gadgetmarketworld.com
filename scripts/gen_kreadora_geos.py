#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Kreadora Pro landings for pt/de/lt/pl/hu/es from IT chefmix-pro base."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IT_LP = (ROOT / "it/chefmix-pro/landing.html").read_text(encoding="utf-8")
IT_TY = (ROOT / "it/chefmix-pro/thank-you.html").read_text(encoding="utf-8")

_spec = importlib.util.spec_from_file_location(
    "_kreadora_i18n", Path(__file__).with_name("_kreadora_i18n.py")
)
_i18n = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_i18n)
OFFERS = _i18n.OFFERS
LOCALES = _i18n.LOCALES

INDEX_TMPL = """<!DOCTYPE html>
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
<link rel="canonical" href="https://gadgetmarketworld.com/{geo}/{slug}/landing.html">
</head>
<body>
<p><a href="/{geo}/{slug}/landing.html">Kreadora Pro™</a></p>
</body>
</html>
"""

IT_TITLE = "Kreadora Pro™ — Impastatrice planetaria 10 L con bilancia e riscaldamento | -70%"
IT_META = (
    "Kreadora Pro™: impastatrice planetaria da 10 litri in acciaio inox, 1800 W classe A++, "
    "bilancia integrata, riscaldamento ciotola, touch a colori con 200+ ricette e 6 programmi. "
    "Kit accessori in omaggio. 99€, pagamento alla consegna."
)
IT_TOPBAR = "🔥 SCONTO 70% + SPEDIZIONE EXPRESS — PAGAMENTO ALLA CONSEGNA 🔥"
IT_RATING = (
    "<strong>4,8/5</strong> — Scelta di <strong>panificatori e chef casalinghi</strong> in tutta Italia"
)
IT_GIFT = "🎁 IN OMAGGIO: SET COMPLETO GANCI, FRUSTE E SPATOLA"
IT_H1 = (
    'Pesa, scalda e impasta fino a <span class="hl">10 litri</span> — '
    "tutto in un’unica ciotola in acciaio inox"
)
IT_LEAD = (
    "<strong>Kreadora Pro™</strong> unisce impastatrice planetaria da laboratorio, "
    "<strong>bilancia integrata</strong>, <strong>riscaldamento ciotola</strong> e "
    "<strong>ricettario touch con oltre 200 ricette</strong>. Ideale per casa e per piccole attività: "
    "impasti, creme e cioccolato fuso con la precisione di un professionista."
)
IT_HERO_ALT = "Kreadora Pro impastatrice planetaria 10 litri con display touch"
IT_CTA = "SÌ, VOGLIO Kreadora Pro A 99 € →"
IT_FORM_NOTE_HERO = "🔒 Zero anticipo · Tieni pronti 99 € in contanti · Paghi solo alla consegna"
IT_BULLETS = [
    "<strong>Bilancia integrata</strong> — pesi farina, lievito e liquidi direttamente nella ciotola, senza bilancia da banco",
    "<strong>Riscaldamento ciotola</strong> — sciogli cioccolato, burro e ingredienti sensibili al posto giusto, senza bagnomaria",
    "<strong>Ciotola da 10 litri</strong> in acciaio inox — batch generosi per casa, pizza artigianale e piccolo laboratorio",
    "<strong>Touch a colori</strong> con <strong>6 programmi</strong> preimpostati e <strong>oltre 200 ricette</strong> integrate",
    "<strong>1800 W</strong> in <strong>classe energetica A++</strong> — potenza da professionista con consumi contenuti",
    "<strong>Kit completo in omaggio</strong> — 3 ganci, Frusta K, gancio impastatore, frusta a filo, frusta e spatola gommata",
    "<strong>Spedizione express</strong> e <strong>pagamento alla consegna</strong> — nessun anticipo online",
]
IT_COUNTDOWN = "⏰ Lo sconto del 70% termina tra"
IT_CD = ("Ore", "Min", "Sec")
IT_STOCK = ("Disponibilità promo", "Solo 9 pezzi rimasti")
IT_LIVE_DATA = "<strong>{n} persone</strong> stanno guardando Kreadora Pro ora"
IT_LIVE_DEFAULT = "<strong>28 persone</strong> stanno guardando Kreadora Pro ora"
IT_OFFER_NOTE = "⚡ Spedizione express · Pagamento alla consegna"
IT_ORDER_H2 = "Completa il tuo ordine Kreadora Pro™"
IT_ORDER_P = (
    "Compila il modulo: ti chiamiamo entro 24 ore per confermare indirizzo e consegna. "
    "<strong>Prezzo finale: 99 € in contanti al corriere.</strong>"
)
IT_LABELS = ("Nome e cognome*", "Numero di telefono*", "Indirizzo di consegna*")
IT_SUBMIT = "CONFERMO Kreadora Pro — 99 €"
IT_FORM_NOTE = "🔒 Spedizione express · Pagamento alla consegna · Garanzia 30 giorni"

IT_WHY = [
    (
        "01 — Bilancia integrata",
        "Pesa gli ingredienti nella ciotola: zero bilancia da banco, zero errori",
        ["Grammi precisi", "Meno lavaggio", "Ricette ripetibili"],
        "Con <strong>Kreadora Pro™</strong> non alterni bilancia, ciotole e planetaria: pesi farina, lievito e liquidi <strong>direttamente nella ciotola da 10 litri</strong>. Ciò che significa per te: impasti più omogenei, tempi di preparazione più corti e risultati da laboratorio anche in casa o in pasticceria.",
        "Perfetto per pizza, pane, brioche e impasti lievitati dove ogni grammo conta.",
    ),
    (
        "02 — Riscaldamento ciotola",
        "Sciogli cioccolato e burro nella ciotola — senza pentolini e bagnomaria",
        ["Temperatura controllata", "Creme lisce", "Meno attrezzi"],
        "La funzione di <strong>riscaldamento</strong> porta la ciotola alla temperatura giusta per fondere cioccolato, burro e ingredienti sensibili, poi continui a mescolare con lo stesso apparecchio. Niente doppia pentola, niente grumi da recuperare a mano.",
        "Ideale per ganache, creme, glassature e preparazioni da pasticceria che richiedono controllo termico.",
    ),
    (
        "03 — Touch a colori + ricettario",
        "6 programmi preimpostati e oltre 200 ricette sul display",
        ["6 programmi", "200+ ricette", "1800 W · Classe A++"],
        "Scegli il programma sullo <strong>schermo touch a colori</strong>, segui i passaggi a video sul ricettario integrato e lasci che il motore da <strong>1800 W</strong> (in <strong>classe energetica A++</strong>) lavori l’impasto fino a <strong>10 litri</strong>. Struttura in <strong>acciaio inox</strong> pensata per uso intensivo, domestico o semi-professionale.",
        "Dalla pizza del weekend al batch da laboratorio: una macchina, un flusso di lavoro pulito.",
    ),
]

IT_CMP = (
    "Confronto diretto",
    "Planetaria base vs Kreadora Pro™",
    "Planetaria classica",
    [
        ("Pesatura ingredienti", "Bilancia separata, più tempo", "Bilancia integrata in ciotola"),
        ("Cioccolato / burro", "Bagnomaria o microonde", "Riscaldamento ciotola integrato"),
        ("Ricette", "Libri o video sparsi", "200+ ricette sul touch"),
        ("Capacità", "Spesso 4–5 litri", "Ciotola da 10 litri"),
        ("Programmi", "Velocità manuali", "6 programmi preimpostati"),
        ("Accessori", "Spesso solo gancio", "Kit completo in omaggio"),
    ],
)

IT_REV_H = "Cosa dicono chi l’ha già in cucina (o in laboratorio)"
IT_REV_SUB = "★ 4,8/5 · Acquisto verificato"
IT_REVIEWS = [
    (
        "Finalmente impasti consistenti ogni volta.",
        "«Gestisco una piccola pizzeria artigianale. La bilancia in ciotola mi ha tolto mezz’ora di preparazione al giorno. Con 10 litri faccio il batch serale senza stress.»",
        "Antonio M. — Napoli, Cliente verificato",
    ),
    (
        "Cioccolato fuso senza grumi — e meno pentole da lavare.",
        "«Ero scettica sul riscaldamento, ma per ganache e burro temperato è comodissimo. Il ricettario sul touch aiuta anche mia figlia quando cucina da sola.»",
        "Elena R. — Torino, Cliente verificata",
    ),
    (
        "Panettiere per hobby, risultati da vetrina.",
        "«Pane e focacce ogni weekend. Gancio + fruste in omaggio coprono tutto: impasti duri, meringhe, creme. Pagamento alla consegna: ho preferito non anticipare nulla online.»",
        "Luca B. — Bologna, Cliente verificato",
    ),
]

IT_KIT_E = "Cosa include il pacchetto"
IT_KIT_H = "Kreadora Pro™ + dotazione completa in omaggio"
IT_KIT_ALT = "Kit Kreadora Pro con accessori"
IT_KIT_LI = [
    "<strong>1× Kreadora Pro™</strong> — impastatrice planetaria 10 L, acciaio inox, 1800 W classe A++",
    "1× Ciotola da 10 litri con bilancia integrata",
    "1× Display touch a colori con ricettario (200+ ricette) e 6 programmi",
    "<strong>In omaggio:</strong> 3 ganci di miscelazione",
    "In omaggio: Frusta K per ingredienti secchi",
    "In omaggio: Gancio impastatore",
    "In omaggio: Frusta a filo per composti spugnosi",
    "In omaggio: Frusta gommata e spatola gommata",
    "Spedizione express",
    "Pagamento alla consegna — tieni pronti <strong>99 €</strong> in contanti",
]
IT_ORDER2_H = "Ordina Kreadora Pro™ adesso"
IT_ORDER2_P = (
    "Hai visto tutto il kit incluso? Compila qui sotto — ti richiamiamo entro 24 ore. "
    "<strong>Prezzo finale: 99 € in contanti al corriere.</strong>"
)
IT_FAQ_H = "Domande frequenti"
IT_FAQS = [
    (
        "Quanto impasto regge in un batch?",
        "La ciotola ha capacità <strong>10 litri</strong>, adatta a impasti per famiglie numerose, batch da laboratorio ridotto o preparazioni multiple in pasticceria artigianale.",
    ),
    (
        "Devo pagare online o in anticipo?",
        "No. Confermi l’ordine dal modulo, ti chiamiamo entro 24 ore, e paghi <strong>99 € in contanti</strong> al corriere quando Kreadora Pro™ è a casa tua.",
    ),
    (
        "Va bene sia per casa che per lavoro?",
        "Sì. È pensata per uso domestico intensivo e per piccole attività (pizzerie artigianali, pasticcerie, catering) che vogliono precisione, capacità e flusso di lavoro pulito in un solo apparecchio.",
    ),
    (
        "Cosa ricevo esattamente in omaggio?",
        "3 ganci di miscelazione, Frusta K, Gancio impastatore, Frusta a filo, Frusta gommata e Spatola gommata — tutto incluso nel pacchetto promo attuale.",
    ),
    (
        "E se non mi convince?",
        "Hai <strong>30 giorni</strong> per il reso e rimborso secondo la nostra politica. È una scelta consapevole: verifica che tu possa ricevere il pacco entro 24–48h e rispondere alla chiamata di conferma.",
    ),
    (
        "Ok, sono convinto. Come ordino?",
        "Scorri al modulo, inserisci nome, telefono e indirizzo, e conferma. Ti richiamiamo per validare l’ordine; spedizione express e paghi 99 € al corriere.",
    ),
]

IT_FOOTER_BLURB = (
    "Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna."
)
IT_FOOTER_INFO = "Informazioni"
IT_FOOTER_CONTACT = "Contatti"
IT_FOOTER_LINKS = [
    ("Chi siamo", "about-us.html"),
    ("Contattaci", "contact-us.html"),
    ("Privacy Policy", "privacy-policy.html"),
    ("Termini e Condizioni", "terms-conditions.html"),
    ("Cookie Policy", "cookie-policy.html"),
    ("Politica di spedizione", "shipping-policy.html"),
    ("Politica di reso", "refund-policy.html"),
]
IT_FOOTER_RIGHTS = "Tutti i diritti riservati."


def offer_cfg(row: dict) -> dict:
    geo = row["geo"]
    offer_id = row["offer"]
    slug = f"kreadora-pro-{offer_id}"
    t = LOCALES[geo]
    return {
        "geo": geo,
        "offer": offer_id,
        "slug": slug,
        "lang": t.get("html_lang", t["lang"]),
        "currency": row["currency"],
        "price": row["price_num"],
        "price_now": row["price_now"],
        "price_was": row["price_was"],
        "ph_name": t["ph_name"],
        "ph_phone": t["ph_phone"],
        "ph_address": t["ph_address"],
        "meta_cpa_usd": row["meta_cpa_usd"],
    }


def esc_js(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def site_config_block(cfg: dict, t: dict) -> str:
    geo = cfg["geo"]
    offer = cfg["offer"]
    slug = cfg["slug"]
    return f"""window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{cfg["currency"]}',
  PRICE: {cfg["price"]},
  OFFER_NAME: 'Kreadora Pro {offer}',
  LP_ID: '{geo}-{slug}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{esc_js(t["submitting"])}',
  COOKIE_TEXT: '{esc_js(t["cookie_text"])}',
  COOKIE_ACCEPT: '{esc_js(t["cookie_accept"])}',
  COOKIE_LEARN: '{esc_js(t["cookie_learn"])}'
}};"""


def render_landing(cfg: dict, t: dict) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    lang = cfg["lang"]
    html = IT_LP

    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = html.replace(IT_TITLE, t["title"])
    html = html.replace(f'content="{IT_META}"', f'content="{t["meta_desc"]}"')
    html = html.replace(
        '<link rel="canonical" href="https://gadgetmarketworld.com/it/chefmix-pro/landing.html">',
        f'<link rel="canonical" href="https://gadgetmarketworld.com/{geo}/{slug}/landing.html">',
    )

    html = re.sub(
        r"window\.SITE_CONFIG = \{.*?\};",
        site_config_block(cfg, t),
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = html.replace("/it/", f"/{geo}/")
    html = html.replace(f"/{geo}/chefmix-pro/", f"/{geo}/{slug}/")

    html = html.replace(IT_TOPBAR, t["topbar"])
    html = html.replace(IT_RATING, t["rating"])
    html = html.replace(IT_GIFT, t["gift_strip"])
    html = html.replace(IT_H1, t["h1"])
    html = html.replace(IT_LEAD, t["lead"])
    html = html.replace(IT_HERO_ALT, t["hero_alt"])
    html = html.replace(IT_CTA, t["cta_hero"])
    html = html.replace(IT_FORM_NOTE_HERO, t["form_note_hero"])

    bullets_loc = [t["b1"], t["b2"], t["b3"], t["b4"], t["b5"], t["b6"], t["b7"]]
    for it_b, loc_b in zip(IT_BULLETS, bullets_loc):
        html = html.replace(f"<li>{it_b}</li>", f"<li>{loc_b}</li>", 1)

    html = html.replace(IT_COUNTDOWN, t["countdown_label"])
    html = html.replace(f'<div class="lbl">{IT_CD[0]}</div>', f'<div class="lbl">{t["cd_h"]}</div>', 1)
    html = html.replace(f'<div class="lbl">{IT_CD[1]}</div>', f'<div class="lbl">{t["cd_m"]}</div>', 1)
    html = html.replace(f'<div class="lbl">{IT_CD[2]}</div>', f'<div class="lbl">{t["cd_s"]}</div>', 1)
    html = html.replace(f'<span class="left">{IT_STOCK[0]}</span>', f'<span class="left">{t["stock_left"]}</span>', 1)
    html = html.replace(f'<span class="right">{IT_STOCK[1]}</span>', f'<span class="right">{t["stock_right"]}</span>', 1)

    live_old = (
        f'<span id="liveCount" data-live="{IT_LIVE_DATA}">{IT_LIVE_DEFAULT}</span>'
    )
    live_new = f'<span id="liveCount" data-live="{t["live"]}">{t["live_default"]}</span>'
    html = html.replace(live_old, live_new)

    html = html.replace(IT_OFFER_NOTE, t["offer_note"])
    html = html.replace(IT_ORDER_H2, t["order_h2"])
    html = html.replace(IT_ORDER_P, t["order_p"])
    html = html.replace(IT_LABELS[0], t["label_name"])
    html = html.replace(IT_LABELS[1], t["label_phone"])
    html = html.replace(IT_LABELS[2], t["label_address"])
    html = html.replace(IT_SUBMIT, t["submit"])
    html = html.replace(IT_FORM_NOTE, t["form_note"])

    why_keys = [
        ("why1_e", "why1_h", "why1_t1", "why1_t2", "why1_t3", "why1_p1", "why1_p2"),
        ("why2_e", "why2_h", "why2_t1", "why2_t2", "why2_t3", "why2_p1", "why2_p2"),
        ("why3_e", "why3_h", "why3_t1", "why3_t2", "why3_t3", "why3_p1", "why3_p2"),
    ]
    for it_w, keys in zip(IT_WHY, why_keys):
        html = html.replace(f'<div class="num-eyebrow">{it_w[0]}</div>', f'<div class="num-eyebrow">{t[keys[0]]}</div>', 1)
        html = html.replace(f"<h3>{it_w[1]}</h3>", f"<h3>{t[keys[1]]}</h3>", 1)
        for it_tag, k in zip(it_w[2], keys[2:5]):
            html = html.replace(f'<span class="tag">{it_tag}</span>', f'<span class="tag">{t[k]}</span>', 1)
        html = html.replace(f"<p>{it_w[3]}</p>", f"<p>{t[keys[5]]}</p>", 1)
        html = html.replace(f'<p class="italic">{it_w[4]}</p>', f'<p class="italic">{t[keys[6]]}</p>', 1)
        html = html.replace(IT_CTA, t["cta_why"], 1)

    html = html.replace(f'<div class="section-label">{IT_CMP[0]}</div>', f'<div class="section-label">{t["cmp_label"]}</div>')
    html = html.replace(f"<h2>{IT_CMP[1]}</h2>", f"<h2>{t['cmp_h']}</h2>", 1)
    html = html.replace(f"<th>{IT_CMP[2]}</th>", f"<th>{t['cmp_th1']}</th>", 1)
    cmp_rows = [
        ("cmp_r1a", "cmp_r1b", "cmp_r1c"),
        ("cmp_r2a", "cmp_r2b", "cmp_r2c"),
        ("cmp_r3a", "cmp_r3b", "cmp_r3c"),
        ("cmp_r4a", "cmp_r4b", "cmp_r4c"),
        ("cmp_r5a", "cmp_r5b", "cmp_r5c"),
        ("cmp_r6a", "cmp_r6b", "cmp_r6c"),
    ]
    for it_row, keys in zip(IT_CMP[3], cmp_rows):
        html = html.replace(f"<td>{it_row[0]}</td>", f"<td>{t[keys[0]]}</td>", 1)
        html = html.replace(f"<td>{it_row[1]}</td>", f"<td>{t[keys[1]]}</td>", 1)
        html = html.replace(f'<td class="win">{it_row[2]}</td>', f'<td class="win">{t[keys[2]]}</td>', 1)

    html = html.replace(f"<h2>{IT_REV_H}</h2>", f"<h2>{t['rev_h']}</h2>", 1)
    html = html.replace(IT_REV_SUB, t["rev_sub"])
    for it_rev, n in zip(IT_REVIEWS, (1, 2, 3)):
        html = html.replace(f"<h4>{it_rev[0]}</h4>", f"<h4>{t[f'rev{n}_h']}</h4>", 1)
        html = html.replace(f"<p>{it_rev[1]}</p>", f"<p>{t[f'rev{n}_p']}</p>", 1)
        html = html.replace(f'<div class="author">{it_rev[2]}</div>', f'<div class="author">{t[f"rev{n}_a"]}</div>', 1)

    html = html.replace(f'<span class="eyebrow">{IT_KIT_E}</span>', f'<span class="eyebrow">{t["kit_e"]}</span>', 1)
    html = html.replace(f"<h2>{IT_KIT_H}</h2>", f"<h2>{t['kit_h']}</h2>", 1)
    html = html.replace(f'alt="{IT_KIT_ALT}"', f'alt="{t["kit_alt"]}"', 1)
    for it_li, loc_li in zip(IT_KIT_LI, t["kit_li"]):
        html = html.replace(f"<li>{it_li}</li>", f"<li>{loc_li}</li>", 1)

    html = html.replace(IT_ORDER2_H, t["order2_h"])
    html = html.replace(IT_ORDER2_P, t["order2_p"])
    html = html.replace(f"<h2>{IT_FAQ_H}</h2>", f"<h2>{t['faq_h']}</h2>", 1)
    for (it_q, it_a), (loc_q, loc_a) in zip(IT_FAQS, t["faq"]):
        html = html.replace(f"<span>{it_q}</span>", f"<span>{loc_q}</span>", 1)
        html = html.replace(f"<p>{it_a}</p>", f"<p>{loc_a}</p>", 1)

    html = html.replace(IT_FOOTER_BLURB, t["footer_blurb"])
    html = html.replace(f'>{IT_FOOTER_INFO}</h4>', f'>{t["footer_info"]}</h4>', 1)
    for (it_label, it_file), (loc_label, loc_file) in zip(IT_FOOTER_LINKS, t["footer_links"]):
        html = html.replace(
            f'<li><a href="/{geo}/{it_file}">{it_label}</a></li>',
            f'<li><a href="/{geo}/{loc_file}">{loc_label}</a></li>',
            1,
        )

    html = html.replace("330 €", cfg["price_was"])
    html = html.replace("99 €", cfg["price_now"])

    html = html.replace('placeholder="Mario Rossi"', f'placeholder="{cfg["ph_name"]}"')
    html = html.replace('placeholder="+39 312 345 6789"', f'placeholder="{cfg["ph_phone"]}"')
    html = html.replace(
        'placeholder="Via Roma 45, Interno 12, 00100 Roma"',
        f'placeholder="{cfg["ph_address"]}"',
    )

    return html


def render_thank_you(cfg: dict, t: dict) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    lang = cfg["lang"]
    price = cfg["price"]
    currency = cfg["currency"]
    html = IT_TY

    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = re.sub(r"<title>.*?</title>", f"<title>{t['ty_title']}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content=".*?"\s*/?>',
        f'<meta name="description" content="{t["ty_desc"]}">',
        html,
        count=1,
    )

    html = html.replace("GEO: 'it'", f"GEO: '{geo}'")
    html = re.sub(r"PRODUCT_SLUG:\s*'chefmix-pro'", f"PRODUCT_SLUG: '{slug}'", html)
    html = html.replace("CURRENCY: 'EUR'", f"CURRENCY: '{currency}'")
    meta_cpa = cfg["meta_cpa_usd"]
    html = re.sub(r"PRICE: 99\.00", f"PRICE: {price}", html)
    html = html.replace(
        "PRICE: 99.00,\n  META_PIXEL_ID:",
        f"PRICE: {price},\n  META_PURCHASE_VALUE: {meta_cpa},\n  META_PURCHASE_CURRENCY: 'USD',\n  META_PIXEL_ID:",
    )
    html = html.replace(
        "COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',\n  COOKIE_ACCEPT: 'Accetta',\n  COOKIE_LEARN: 'Scopri di più'",
        f"COOKIE_TEXT: '{esc_js(t['cookie_text'])}',\n  COOKIE_ACCEPT: '{esc_js(t['cookie_accept'])}',\n  COOKIE_LEARN: '{esc_js(t['cookie_learn'])}'",
    )
    html = html.replace(
        "<script>\n// Trigger Purchase / conversion event after page load\nwindow.addEventListener('load', function () {\n  if (window.trackPurchase) window.trackPurchase(99.00, 'EUR');\n});\n</script>",
        '<script src="/assets/js/meta-purchase-thankyou.js" defer></script>',
    )

    html = html.replace("Il tuo ordine è stato registrato con successo!", t["ty_h1"])
    html = html.replace(
        "Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
        t["ty_sub"],
    )
    html = html.replace(
        "Il team gadgetmarketworld al lavoro: call center e logistica COD",
        t["ty_hero_alt"],
    )
    html = html.replace("👇 Cosa devi fare adesso", t["ty_act_e"])
    html = html.replace("📞 Rispondi alla chiamata di conferma", t["ty_act_h"])
    html = html.replace(
        "Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine.",
        t["ty_act_p"],
    )
    html = html.replace(
        "Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
        t["ty_act_w"],
    )
    html = html.replace("🕒 Orari di contatto", t["ty_hours_h"])
    html = html.replace("<strong>Lunedì – Sabato</strong> · 9:00 – 18:00", t["ty_hours"])
    html = html.replace("📋 Cosa succede dopo", t["ty_next_h"])

    it_steps = [
        "Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>",
        "Il tuo ordine verrà spedito entro <strong>24–48 ore</strong>",
        "Consegna a domicilio e <strong>pagamento alla consegna</strong>",
    ]
    for it_step, loc_step in zip(it_steps, t["ty_steps"]):
        html = html.replace(f"<li>{it_step}</li>", f"<li>{loc_step}</li>")

    for it_b, loc_b in zip(
        ("🔒 Pagamento alla consegna", "🛡️ Garanzia inclusa", "🔐 Protezione SSL"),
        t["ty_badges"],
    ):
        html = html.replace(it_b, loc_b)

    footer_it = (
        "    <div>\n"
        '      <h4 class="site-footer__heading">Informazioni</h4>\n'
        '      <ul class="site-footer__list">\n'
        '        <li><a href="/it/about-us.html">Chi siamo</a></li>\n'
        '        <li><a href="/it/contact-us.html">Contattaci</a></li>\n'
        '        <li><a href="/it/privacy-policy.html">Privacy Policy</a></li>\n'
        '        <li><a href="/it/terms-conditions.html">Termini e Condizioni</a></li>\n'
        '        <li><a href="/it/cookie-policy.html">Cookie Policy</a></li>\n'
        '        <li><a href="/it/shipping-policy.html">Politica di Spedizione</a></li>\n'
        '        <li><a href="/it/refund-policy.html">Politica di Rimborso</a></li>\n'
        "      </ul>\n"
        "    </div>\n"
        "    <div>\n"
        '      <h4 class="site-footer__heading">Contatti</h4>'
    )
    footer_geo = (
        "    <div>\n"
        f'      <h4 class="site-footer__heading">{t["footer_info"]}</h4>\n'
        '      <ul class="site-footer__list">\n'
        + "".join(
            f'        <li><a href="/{geo}/{f}">{lbl}</a></li>\n'
            for lbl, f in t["footer_links"]
        )
        + "      </ul>\n"
        "    </div>\n"
        "    <div>\n"
        f'      <h4 class="site-footer__heading">{t["footer_contact"]}</h4>'
    )
    html = html.replace(footer_it, footer_geo)
    html = html.replace(IT_FOOTER_RIGHTS, t["footer_rights"])
    html = html.replace("/it/", f"/{geo}/")

    return html


def update_sitemap(configs: list[dict]) -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    entries = []
    lastmod = "2026-10-06"
    for cfg in configs:
        geo = cfg["geo"]
        slug = cfg["slug"]
        for suffix in ("/", "/landing.html"):
            loc = f"https://gadgetmarketworld.com/{geo}/{slug}{suffix}"
            if loc not in text:
                entries.append(
                    f'  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>'
                    f"<changefreq>weekly</changefreq><priority>0.95</priority></url>\n"
                )
    if not entries:
        print("Sitemap: no new Kreadora geo URLs to add")
        return
    text = text.replace("</urlset>", "".join(entries) + "</urlset>")
    path.write_text(text, encoding="utf-8")
    print(f"Sitemap: added {len(entries)} Kreadora geo URLs")


def main() -> list[str]:
    created: list[str] = []
    configs = [offer_cfg(row) for row in OFFERS]
    for cfg in configs:
        geo = cfg["geo"]
        slug = cfg["slug"]
        t = LOCALES[geo]
        out_dir = ROOT / geo / slug
        out_dir.mkdir(parents=True, exist_ok=True)

        for name, content in (
            ("landing.html", render_landing(cfg, t)),
            ("index.html", INDEX_TMPL.format(lang=cfg["lang"], geo=geo, slug=slug)),
            ("thank-you.html", render_thank_you(cfg, t)),
        ):
            path = out_dir / name
            path.write_text(content, encoding="utf-8")
            created.append(str(path.relative_to(ROOT)))

        print(f"Wrote {geo}/{slug}/ — {cfg['price_now']}")

    update_sitemap(configs)
    return created


if __name__ == "__main__":
    files = main()
    print(f"\nCreated {len(files)} files:")
    for f in sorted(files):
        print(f"  {f}")
