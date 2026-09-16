#!/usr/bin/env python3
"""Generate SewLuxe landing pages, index redirects, and thank-you pages for 6 geos."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IT_LP = (ROOT / "it/sewluxe/landing.html").read_text(encoding="utf-8")
IT_TY = (ROOT / "it/sewluxe/thank-you.html").read_text(encoding="utf-8")

_spec = importlib.util.spec_from_file_location(
    "_sewluxe_i18n", Path(__file__).with_name("_sewluxe_i18n.py")
)
_i18n = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_i18n)
GEOS = _i18n.GEOS
HREFLANG = _i18n.HREFLANG
COPY = _i18n.COPY

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
<p><a href="/{geo}/{slug}/landing.html">SewLuxe™</a></p>
</body>
</html>
"""

# Italian source strings from it/sewluxe/landing.html (replacement order matters for subsets)
IT_REPLACEMENTS = [
    ("title", "SewLuxe™ — Macchina da cucire automatica 80 punti, uso domestico | -50%"),
    ("meta_desc", "SewLuxe™: macchina da cucire automatica con 80 tipi di punto, tecnologia FabricSense™ e infilatura automatica. Compatibile con jeans, cotone, pelle e seta. Kit completo, pagamento alla consegna."),
    ("topbar", "🔥 SCONTO 50% + SPEDIZIONE GRATUITA — PAGAMENTO ALLA CONSEGNA 🔥"),
    ("rating", "<strong>4,9/5</strong> — Oltre <strong>6.240</strong> clienti soddisfatti"),
    ("gift_strip", "🚚 Spedizione gratuita + Garanzia di reso 30 giorni"),
    ("h1", 'Macchina da cucire automatica con <span class="hl">80 tipi di punto</span> — cuci qualsiasi capo a casa, senza esperienza'),
    ("lead", "Ripara, accorcia e rifinisci i tuoi capi senza andare dal sarto. <strong>Infilatura automatica dell'ago</strong> e compatibile con <strong>jeans, cotone, pelle e seta</strong>. <strong>SewLuxe™</strong> è pensata per chi vuole risultati professionali in casa, anche al primo utilizzo."),
    ("hero_alt", "SewLuxe macchina da cucire automatica per uso domestico"),
    ("cta", "ORDINA ORA →"),
    ("form_note", "🔒 Zero anticipo · Zero carta · Paghi solo quando la ricevi"),
    ("feat1_h", "Spedizione gratuita"),
    ("feat1_p", "Consegna in tutta Italia"),
    ("feat2_h", "Pagamento alla consegna"),
    ("feat2_p", "Paghi solo quando ricevi"),
    ("feat3_h", "Garanzia inclusa"),
    ("feat3_p", "Copertura completa nel prezzo"),
    ("feat4_h", "Reso 30 giorni"),
    ("feat4_p", "Rimborso semplice e gratuito"),
    ("countdown_label", "⏰ Lo sconto del 50% termina tra"),
    ("cd_h", "Ore"),
    ("cd_m", "Min"),
    ("cd_s", "Sec"),
    ("stock_left", "Disponibilità"),
    ("stock_right", "Solo 7 pezzi rimasti"),
    ("order_h2", "Completa il tuo ordine"),
    ("order_p", "Compila il modulo qui sotto: il nostro team ti contatterà per confermare tutti i dettagli."),
    ("label_name", "Nome e cognome*"),
    ("label_phone", "Numero di telefono*"),
    ("label_address", "Indirizzo di consegna*"),
    ("ph_name", "Mario Rossi"),
    ("ph_phone", "+39 312 345 6789"),
    ("ph_address", "Via Roma 45, Interno 12, 00100 Roma"),
    ("submit", "CONFERMA ORDINE"),
    ("why1_eyebrow", "01 — Adattamento automatico al tessuto"),
    ("why1_h3", "La tecnologia FabricSense™ regola la cucitura automaticamente"),
    ("why1_p1", "<strong>SewLuxe™</strong> incorpora la tecnologia speciale <strong>FabricSense™</strong>, che riconosce il tipo di tessuto e regola automaticamente lunghezza, larghezza e pressione del punto. Ogni cucitura è uniforme e ripetibile, senza regolazioni manuali né errori visibili."),
    ("why1_p2", "Garantisce cuciture stabili sia sui tessuti fini sia su quelli più spessi."),
    ("why1_alt", "SewLuxe FabricSense adattamento automatico al tessuto"),
    ("why2_eyebrow", "02 — Compatibile con tutti i tessuti"),
    ("why2_h3", "Rifiniture, riparazioni e decorazioni su qualsiasi materiale"),
    ("why2_p1", "La macchina è ideale per rifinire, riparare e decorare cotone, jeans, jersey, pile, lino, viscosa, raso e pelle. Si adatta bene a materiali leggeri e delicati, ma anche a tessuti elastici e resistenti."),
    ("why2_p2", "Perfetta per abiti di tutti i giorni, tende, tovaglie, fodere e altri tessili per la casa."),
    ("why2_alt", "SewLuxe compatibile con tutti i tessuti"),
    ("why3_eyebrow", "03 — 80 punti automatici"),
    ("why3_h3", "Selezioni il simbolo, la macchina si configura da sola"),
    ("why3_p1", "<strong>SewLuxe™</strong> offre 80 programmi di cucitura pronti all'uso, tra cui punti semplici, zigzag, elastici, orlo invisibile, overlock, asole, decorativi e di rinforzo. Basta selezionare il simbolo e la macchina si configura automaticamente."),
    ("why3_p2", "Il braccio libero consente di lavorare con precisione su maniche, pantaloni e polsini; l'infilatura automatica facilita l'uso anche ai principianti."),
    ("why3_alt", "SewLuxe 80 programmi di cucitura automatici"),
    ("compare_label", "Confronto diretto"),
    ("compare_h2", "Macchina tradizionale vs SewLuxe™"),
    ("compare_trad", "Tradizionale"),
    ("compare_new", "SewLuxe™"),
    ("test_h2", "Non fidarti solo della nostra parola — guarda cosa dicono gli altri!"),
    ("test_eyebrow", "★ 4,9/5 · Acquisto verificato · Recensioni controllate"),
    ("kit_eyebrow", "Cosa include il pacchetto"),
    ("kit_h2", "Kit completo SewLuxe™, pronto all'uso"),
    ("faq_h2", "Domande frequenti"),
    ("footer_blurb", "Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna."),
    ("footer_info", "Informazioni"),
    ("footer_contact", "Contatti"),
    ("footer_rights", "Tutti i diritti riservati"),
]

IT_WHY_TAGS = [
    ["FabricSense™", "Punti uniformi", "Nessuna regolazione manuale"],
    ["Cotone e jeans", "Pelle e seta", "Tende e tessili"],
    ["80 programmi", "Braccio libero", "Infilatura automatica"],
]

IT_COMPARE_ROWS = [
    ("Regolazione tessuto", "Manuale, per prova ed errore", "Automatica con FabricSense™"),
    ("Programmi di cucitura", "Limitati, regolazione manuale", "80 programmi automatici"),
    ("Infilatura ago", "Manuale, difficile", "Automatica, avvio rapido"),
    ("Materiali", "Solo alcuni tipi", "Tutti i tessuti"),
    ("Braccio libero", "Spesso assente", "Incluso — maniche e pantaloni"),
    ("Illuminazione", "Debole o assente", "LED integrato"),
]

IT_REVIEWS = [
    ("Risultati eccellenti anche a casa.", "«Non pensavo che una macchina da cucire domestica potesse dare risultati così buoni. La uso per foderare e riparare, e le cuciture sono molto estetiche. Ha anche tante funzioni. La consiglio!»", "Maria Rossi — Milano, Cliente verificata", "Risultati SewLuxe a casa"),
    ("Facile da usare, anche senza esperienza.", "«Non ho molta esperienza di cucito, ma gestisco questa macchina con sicurezza. L'illuminazione LED chiara permette di controllare con precisione ogni movimento dell'ago. La uso regolarmente per piccole riparazioni in casa.»", "Giulia Bianchi — Roma, Cliente verificata", "SewLuxe facile da usare"),
    ("Perfetta per chi inizia.", "«Volevo cucire da tempo, ma non avevo esperienza. Con questa macchina si lavora comodamente e il manuale spiega chiaramente tutte le funzioni. La uso spesso per le riparazioni di cui ho bisogno a casa.»", "Laura Conti — Napoli, Cliente verificata", "SewLuxe perfetta per principianti"),
]

IT_KIT_ITEMS = [
    "<strong>1× Macchina da cucire SewLuxe™</strong> — automatica per uso domestico",
    "1× Pedale di controllo della velocità",
    "1× Set di aghi per diversi materiali",
    "1× Set di bobine per cucire subito",
    "1× Piedino per punti diritti e zigzag",
    "1× Piedino per cerniere e asole",
    "1× Accessori per punti decorativi e rifiniture",
    "1× Istruzioni per l'uso",
    "Spedizione gratuita in 24 ore",
    "Pagamento alla consegna comodo e sicuro",
]

IT_FAQS = [
    ("Quanto ci mette ad arrivare?", "1-2 giorni lavorativi. Ti chiamiamo entro 24 ore per confermare l'ordine e l'orario di consegna."),
    ("Devo pagare in anticipo?", "No. Paghi in contanti direttamente al corriere quando SewLuxe™ è già a casa tua. Tieni pronti 69,99 €."),
    ("È adatta anche ai principianti?", "Sì. Con 80 programmi automatici, infilatura automatica dell'ago e tecnologia FabricSense™, SewLuxe™ è pensata anche per chi non ha mai cucito prima."),
    ("Posso cucire jeans e pelle?", "Sì. SewLuxe™ gestisce cotone, jeans, jersey, pile, lino, viscosa, raso, pelle e seta — con regolazione automatica del punto per ogni materiale."),
    ("E se non mi convince?", "Hai 30 giorni per restituirla gratuitamente e ricevere il rimborso completo, senza domande."),
    ("Ok, sono convinto. Come la ordino?", "Compila il modulo qui sopra con nome, telefono e indirizzo. Ti chiamiamo entro 24h per confermare, e SewLuxe™ arriva a casa tua in 1-2 giorni. Paghi solo alla consegna."),
]

IT_FOOTER_LINKS = [
    ("about-us.html", "Chi siamo"),
    ("contact-us.html", "Contattaci"),
    ("privacy-policy.html", "Privacy Policy"),
    ("terms-conditions.html", "Termini e Condizioni"),
    ("cookie-policy.html", "Cookie Policy"),
    ("shipping-policy.html", "Politica di spedizione"),
    ("refund-policy.html", "Politica di reso"),
]


def hreflang_block() -> str:
    lines = []
    for lang, path in HREFLANG:
        lines.append(
            f'<link rel="alternate" hreflang="{lang}" href="https://gadgetmarketworld.com{path}">'
        )
    return "\n".join(lines)


def site_config_block(cfg: dict, t: dict) -> str:
    geo = cfg["geo"]
    offer = cfg["offer"]
    slug = cfg["slug"]
    return f"""window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{cfg["currency"]}',
  PRICE: {cfg["price"]},
  OFFER_NAME: 'SewLuxe {offer}',
  LP_ID: '{geo}-{offer}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{t["submitting"]}',
  COOKIE_TEXT: '{t["cookie_text"]}',
  COOKIE_ACCEPT: '{t["cookie_accept"]}',
  COOKIE_LEARN: '{t["cookie_learn"]}'
}};"""


def render_landing(cfg: dict, t: dict) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    lang = cfg["lang"]
    html = IT_LP

    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = html.replace(
        '<link rel="canonical" href="https://gadgetmarketworld.com/it/sewluxe/landing.html">',
        f'<link rel="canonical" href="https://gadgetmarketworld.com/{geo}/{slug}/landing.html">',
    )
    old_hreflang = (
        '<link rel="alternate" hreflang="it" href="https://gadgetmarketworld.com/it/sewluxe/landing.html">\n'
        '<link rel="alternate" hreflang="en" href="https://gadgetmarketworld.com/en/sewluxe/landing.html">'
    )
    html = html.replace(old_hreflang, hreflang_block())

    html = re.sub(
        r"window\.SITE_CONFIG = \{.*?\};",
        site_config_block(cfg, t),
        html,
        count=1,
        flags=re.DOTALL,
    )

    for key, it_text in IT_REPLACEMENTS:
        if key in ("ph_name", "ph_phone", "ph_address"):
            continue
        html = html.replace(it_text, t[key])

    for (it_q, it_a), (loc_q, loc_a) in zip(IT_FAQS, t["faqs"]):
        html = html.replace(f"<span>{it_q}</span>", f"<span>{loc_q}</span>", 1)
        html = html.replace(f"<p>{it_a}</p>", f"<p>{loc_a}</p>", 1)

    html = html.replace("139,99 €", cfg["price_was"])
    html = html.replace("69,99 €", cfg["price_now"])

    for it_tags, loc_tags in zip(IT_WHY_TAGS, [t["why1_tags"], t["why2_tags"], t["why3_tags"]]):
        for it_tag, loc_tag in zip(it_tags, loc_tags):
            html = html.replace(f'<span class="tag">{it_tag}</span>', f'<span class="tag">{loc_tag}</span>', 1)

    html = html.replace("<th>Tradizionale</th>", f"<th>{t['compare_trad']}</th>")
    html = html.replace('<th class="highlight">SewLuxe™</th>', f'<th class="highlight">{t["compare_new"]}</th>')
    for it_row, loc_row in zip(IT_COMPARE_ROWS, t["compare_rows"]):
        html = html.replace(f"<td>{it_row[0]}</td>", f"<td>{loc_row[0]}</td>", 1)
        html = html.replace(f"<td>{it_row[1]}</td>", f"<td>{loc_row[1]}</td>", 1)
        html = html.replace(f'<td class="win">{it_row[2]}</td>', f'<td class="win">{loc_row[2]}</td>', 1)

    for it_rev, loc_rev in zip(IT_REVIEWS, t["reviews"]):
        for it_part, loc_part in zip(it_rev, loc_rev):
            html = html.replace(it_part, loc_part, 1)

    for it_item, loc_item in zip(IT_KIT_ITEMS, t["kit_items"]):
        html = html.replace(f"<li>{it_item}</li>", f"<li>{loc_item}</li>", 1)

    html = html.replace('alt="Kit completo SewLuxe macchina da cucire"', f'alt="{t["kit_h2"]}"')

    for (it_file, it_label), (loc_file, loc_label) in zip(IT_FOOTER_LINKS, t["footer_links"]):
        html = html.replace(
            f'<li><a href="/it/{it_file}">{it_label}</a></li>',
            f'<li><a href="/{geo}/{loc_file}">{loc_label}</a></li>',
        )

    live_old = '<span id="liveCount" data-live="<strong>{n} persone</strong> stanno guardando SewLuxe ora"><strong>35 persone</strong> stanno guardando SewLuxe ora</span>'
    live_new = f'<span id="liveCount" data-live="{t["live_data"]}">{t["live_default"]}</span>'
    html = html.replace(live_old, live_new)

    html = html.replace('placeholder="Mario Rossi"', f'placeholder="{cfg["ph_name"]}"')
    html = html.replace('placeholder="+39 312 345 6789"', f'placeholder="{cfg["ph_phone"]}"')
    html = html.replace('placeholder="Via Roma 45, Interno 12, 00100 Roma"', f'placeholder="{cfg["ph_address"]}"')

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
    html = re.sub(r"PRODUCT_SLUG:\s*'sewluxe'", f"PRODUCT_SLUG: '{slug}'", html)
    html = html.replace("CURRENCY: 'EUR'", f"CURRENCY: '{currency}'")
    html = re.sub(r"PRICE: 69\.99", f"PRICE: {price}", html)
    html = html.replace(
        "COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',\n  COOKIE_ACCEPT: 'Accetta',\n  COOKIE_LEARN: 'Scopri di più'",
        f"COOKIE_TEXT: '{t['cookie_text']}',\n  COOKIE_ACCEPT: '{t['cookie_accept']}',\n  COOKIE_LEARN: '{t['cookie_learn']}'",
    )
    html = html.replace("trackPurchase(69.99, 'EUR')", f"trackPurchase({price}, '{currency}')")

    html = html.replace("Il tuo ordine è stato registrato con successo!", t["ty_h1"])
    html = html.replace(
        "Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
        t["ty_sub"],
    )
    html = html.replace(
        "Il team gadgetmarketworld al lavoro: call center e logistica COD",
        t["ty_alt"],
    )
    html = html.replace("👇 Cosa devi fare adesso", t["ty_eyebrow"])
    html = html.replace("📞 Rispondi alla chiamata di conferma", t["ty_action_title"])
    html = html.replace(
        "Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine.",
        t["ty_action_body"],
    )
    html = html.replace(
        "Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
        t["ty_action_warn"],
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

    it_badges = ("🔒 Pagamento alla consegna", "🛡️ Garanzia inclusa", "🔐 Protezione SSL")
    for it_badge, loc_badge in zip(it_badges, t["ty_badges"]):
        html = html.replace(it_badge, loc_badge)

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
            for f, lbl in t["footer_links"]
        )
        + "      </ul>\n"
        "    </div>\n"
        "    <div>\n"
        f'      <h4 class="site-footer__heading">{t["footer_contact"]}</h4>'
    )
    html = html.replace(footer_it, footer_geo)
    html = html.replace("Tutti i diritti riservati.", t["footer_rights"] + ".")
    html = html.replace("/it/", f"/{geo}/")

    return html


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    entries = []
    lastmod = "2026-09-06"
    for cfg in GEOS:
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
        print("Sitemap: no new SewLuxe geo URLs to add")
        return
    marker = (
        "  <url><loc>https://gadgetmarketworld.com/en/sewluxe/landing.html</loc>"
        "<lastmod>2026-09-06</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n"
    )
    if marker in text:
        text = text.replace(marker, marker + "".join(entries))
    else:
        text = text.replace("</urlset>", "".join(entries) + "</urlset>")
    path.write_text(text, encoding="utf-8")
    print(f"Sitemap: added {len(entries)} SewLuxe geo URLs")


def main() -> list[str]:
    created: list[str] = []
    for cfg in GEOS:
        key = cfg["key"]
        t = COPY[key]
        geo = cfg["geo"]
        slug = cfg["slug"]
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

    update_sitemap()
    return created


if __name__ == "__main__":
    files = main()
    print(f"\nCreated {len(files)} files:")
    for f in sorted(files):
        print(f"  {f}")
