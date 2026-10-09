#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Heaterax / AirCurtain GEO landings + thank-you pages."""

from __future__ import annotations

import html
from pathlib import Path

from heaterax_geo_data import COPY, FORM_ACTION, OFFERS, UID, WEBHOOK

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://gadgetmarketworld.com"

STORY_TAGS = {
    "ro": (["Până la 85 m²", "13 minute", "FastHeating"], ["Sub 2 minute", "Fără tuburi", "Fără tehnician"], ["Telecomandă", "App oficială", "Display LED"]),
    "pt": (["Até 85 m²", "13 minutos", "FastHeating"], ["Menos de 2 min", "Zero tubos", "Sem técnico"], ["Comando", "App oficial", "Ecrã LED"]),
    "pl": (["Do 85 m²", "13 minut", "FastHeating"], ["Poniżej 2 min", "Bez rur", "Bez technika"], ["Pilot", "Aplikacja", "Wyświetlacz LED"]),
    "es": (["Hasta 85 m²", "13 minutos", "FastHeating"], ["Menos de 2 min", "Sin tubos", "Sin técnico"], ["Mando", "App oficial", "Pantalla LED"]),
    "de": (["Bis 85 m²", "13 Min.", "FastHeating"], ["Unter 2 Min.", "Keine Rohre", "Ohne Techniker"], ["Fernbedienung", "Offizielle App", "LED-Display"]),
    "hu": (["Akár 85 m²", "13 perc", "FastHeating"], ["Kevesebb mint 2 perc", "Cső nélkül", "Szerelő nélkül"], ["Távirányító", "Hivatalos app", "LED kijelző"]),
}

FOOTER_LINKS = {
    "about": {"ro": "Despre noi", "pt": "Sobre nós", "pl": "O nas", "es": "Sobre nosotros", "de": "Über uns", "hu": "Rólunk"},
    "contact": {"ro": "Contact", "pt": "Contacto", "pl": "Kontakt", "es": "Contacto", "de": "Kontakt", "hu": "Kapcsolat"},
}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def checklist_html(items: list[str]) -> str:
    rows = []
    for item in items:
        rows.append(
            f'      <li><span class="product-checklist__icon" aria-hidden="true"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5"/></svg></span>{item}</li>'
        )
    return "\n".join(rows)


def tags_html(tags: tuple[str, ...]) -> str:
    return "".join(f'<span class="tag">{t}</span>' for t in tags)


def faq_html(faq: list[tuple[str, str]]) -> str:
    out = []
    for i, (q, a) in enumerate(faq):
        open_cls = " open" if i == 0 else ""
        out.append(
            f'  <div class="faq-item{open_cls}">\n'
            f'    <button class="faq-q" type="button">{esc(q)}</button>\n'
            f'    <div class="faq-a"><p>{a}</p></div>\n'
            f"  </div>"
        )
    return "\n".join(out)


def form_block(
    c: dict,
    offer: dict,
    ty_url: str,
    *,
    suffix: str = "",
    form_id: str = "order-form",
) -> str:
    sid = suffix
    key = offer.get("form_key") or ""
    return f"""    <form class="tm-order-form order-form" action="{FORM_ACTION}" method="post">
      <label for="name{sid}">{esc(c['label_name'])}</label>
      <input id="name{sid}" type="text" name="name" autocomplete="name" placeholder="{esc(c['ph_name'])}" required>
      <label for="tel{sid}">{esc(c['label_tel'])}</label>
      <input id="tel{sid}" type="tel" name="tel" autocomplete="tel" placeholder="{esc(c['ph_tel'])}" required>
      <label for="street-address{sid}">{esc(c['label_addr'])}</label>
      <input id="street-address{sid}" type="text" name="street-address" autocomplete="street-address" placeholder="{esc(c['ph_addr'])}" required>
      <input name="uid" type="hidden" value="{UID}">
      <input name="offer" type="hidden" value="{offer['offer_id']}">
      <input name="lp" type="hidden" value="{offer['lp_id']}">
      <input name="thankyoupage" type="hidden" value="{ty_url}">
      <input name="webhook" type="hidden" value="{WEBHOOK}">
      <input name="_key" type="hidden" value="{key}">
      <button name="submit" type="submit">{esc(c['submit'])}</button>
      <p class="form-trust">{c['form_trust']}</p>
    </form>"""


def render_landing(offer: dict, c: dict) -> str:
    geo = offer["geo"]
    slug = offer["slug"]
    lang = offer["lang"]
    brand = c["brand"]
    base_path = f"/{geo}/{slug}"
    canonical = f"{BASE}{base_path}/landing.html"
    ty_url = f"{BASE}{base_path}/thank-you.html"
    t1, t2, t3 = STORY_TAGS[offer["locale_key"]]
    fl = FOOTER_LINKS

    offer_stack_id = "order-form"
    kit_form_id = "order-form-kit"

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18429742678"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-18429742678');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{esc(c['title'])}</title>
<meta name="description" content="{esc(c['meta_desc'])}">
<meta name="contact" content="info@gadgetmarketworld.com">
<meta name="theme-color" content="#2f7cf6">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="/assets/img/products/wall-convector/hero.jpg?v=3" as="image" type="image/jpeg">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/heaterax-landing.css?v=3">
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{offer['currency']}',
  PRICE: {offer['price']},
  OFFER_NAME: '{brand} {offer['offer_id']} {geo.upper()}',
  LP_ID: '{geo}-{offer['offer_id']}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{esc(c['submitting'])}',
  COOKIE_TEXT: '{esc(c['cookie_text'])}',
  COOKIE_ACCEPT: '{esc(c['cookie_accept'])}',
  COOKIE_LEARN: '{esc(c['cookie_learn'])}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
</head>
<body class="hx-lp">

<div class="hx-ticker" aria-label="Offer">
  • {c['ticker_pay']} <span class="pill">{c['ticker_cod']}</span> <span class="dot">•</span>
  {c['ticker_guarantee']} <span class="pill">{c['ticker_refund']}</span>
  <span class="hx-ticker__repeat"><span class="dot"> • </span>{c['ticker_pay']} <span class="pill">{c['ticker_cod']}</span> •</span>
</div>

<header class="hx-header">
  <a class="hx-header__reviews" href="#recensioni">{c['reviews_link']}</a>
  <div class="hx-header__brand">{c['header_line1']}<br><strong>{brand}</strong></div>
  <a class="hx-header__cta" href="#{offer_stack_id}">{c['order_cta']}</a>
</header>

<div class="hx-hero-banner">
  <img decoding="async" src="/assets/img/products/wall-convector/hero.jpg?v=3" alt="{esc(brand)}" width="1024" height="1024" loading="eager" fetchpriority="high">
</div>

<div class="hx-hero-text wrap--narrow">
  <h1>{c['h1']}</h1>
  <p class="lead">{c['lead']}</p>
</div>

<div class="wrap wrap--narrow">
  <section class="product-checklist" aria-label="Features">
    <ul class="product-checklist__list">
{checklist_html(c['checklist'])}
    </ul>
  </section>
  <div class="hx-rating-link">
    <span class="stars">★★★★★</span>
    {c['rating']}
  </div>
</div>

<section class="hx-offer-stack" id="{offer_stack_id}">
  <div class="hx-countdown-bar">
    <div class="hx-countdown-bar__label">{c['countdown_label']}<span>{c['countdown_sub']}</span></div>
    <div class="hx-countdown-bar__timer" aria-live="polite">
      <span class="d" data-cd-h">00</span>:<span class="d" data-cd-m">00</span>:<span class="d" data-cd-s">00</span>
    </div>
  </div>
  <div class="hx-countdown-bar__progress" aria-hidden="true"></div>
  <div class="hx-price-card">
    <h2>{c['offer_h2']}</h2>
    <p class="sub">{c['offer_sub']}</p>
    <div class="price-row">
      <div class="price-label">{c['price_label']}</div>
      <div class="now">{offer['price_now']}</div>
      <div class="was">{offer['price_was']}</div>
      <div class="discount-pill">{c['discount']}</div>
    </div>
    <p class="scroll-hint">{c['scroll_hint']}</p>
  </div>
  <div class="hx-form-card">
    <span class="stock-badge">{c['stock_badge']}</span>
    <p class="stock-warn">{c['stock_warn']}</p>
    <div class="live-row">
      <span class="dot"></span>
      <span class="js-live-count" data-live="{c['live']}"><strong>4</strong></span>
    </div>
    <h3>{c['form_h3']}</h3>
    <p class="form-intro">{c['form_intro']}</p>
{form_block(c, offer, ty_url, suffix="", form_id=offer_stack_id)}
    <ul class="hx-trust-list">
      <li>{c['trust1']}</li>
      <li>{c['trust2']}</li>
      <li>{c['trust3']}</li>
    </ul>
  </div>
</section>

<section class="hx-story">
  <div class="wrap--narrow story-grid">
    <div class="hx-story-img"><img src="/assets/img/products/wall-convector/desc-1.jpg" alt="{esc(brand)}" width="1024" height="1024" loading="lazy" decoding="async"></div>
    <div>
      <div class="eyebrow">{c['story1_eyebrow']}</div>
      <h3>{c['story1_h3']}</h3>
      <div class="tag-row">{tags_html(t1)}</div>
      <p>{c['story1_p1']}</p>
      <p>{c['story1_p2']}</p>
    </div>
  </div>
</section>

<section class="hx-story">
  <div class="wrap--narrow story-grid">
    <div class="hx-story-img"><img src="/assets/img/products/wall-convector/desc-2.jpg?v=3" alt="{esc(brand)}" width="1024" height="1024" loading="lazy" decoding="async"></div>
    <div>
      <div class="eyebrow">{c['story2_eyebrow']}</div>
      <h3>{c['story2_h3']}</h3>
      <div class="tag-row">{tags_html(t2)}</div>
      <p>{c['story2_p1']}</p>
      <p>{c['story2_p2']}</p>
    </div>
  </div>
</section>

<section class="hx-story">
  <div class="wrap--narrow story-grid">
    <div class="hx-story-img"><img src="/assets/img/products/wall-convector/desc-3.jpg" alt="{esc(brand)}" width="1024" height="1024" loading="lazy" decoding="async"></div>
    <div>
      <div class="eyebrow">{c['story3_eyebrow']}</div>
      <h3>{c['story3_h3']}</h3>
      <div class="tag-row">{tags_html(t3)}</div>
      <p>{c['story3_p1']}</p>
      <p>{c['story3_p2']}</p>
    </div>
  </div>
</section>

<section class="hx-reviews" id="recensioni">
  <div class="section-head">
    <h2>{c['reviews_h2']}</h2>
    <p>{c['reviews_sub']}</p>
  </div>
  <div class="t-grid wrap">
    <article class="testimonial">
      <img class="t-photo" src="/assets/img/reviews/wall-convector/review-1.jpg" alt="" width="1024" height="1024" loading="lazy" decoding="async">
      <div class="t-inner">
        <div class="stars">★★★★★</div>
        <h4>{c['rev1_h']}</h4>
        <p>{c['rev1_p']}</p>
        <div class="author">{c['rev1_a']}</div>
      </div>
    </article>
    <article class="testimonial">
      <img class="t-photo" src="/assets/img/reviews/wall-convector/review-2.jpg" alt="" width="1024" height="1024" loading="lazy" decoding="async">
      <div class="t-inner">
        <div class="stars">★★★★★</div>
        <h4>{c['rev2_h']}</h4>
        <p>{c['rev2_p']}</p>
        <div class="author">{c['rev2_a']}</div>
      </div>
    </article>
    <article class="testimonial">
      <img class="t-photo" src="/assets/img/reviews/wall-convector/review-3.jpg" alt="" width="1024" height="1024" loading="lazy" decoding="async">
      <div class="t-inner">
        <div class="stars">★★★★★</div>
        <h4>{c['rev3_h']}</h4>
        <p>{c['rev3_p']}</p>
        <div class="author">{c['rev3_a']}</div>
      </div>
    </article>
  </div>
</section>

<section class="hx-kit-section">
  <div class="section-heading">
    <span class="eyebrow">{c['kit_eyebrow']}</span>
    <h2>{c['kit_h2']}</h2>
  </div>
  <div class="hx-kit-box">
    <img src="/assets/img/products/wall-convector/kit.jpg" alt="{esc(brand)}" width="1024" height="1024" loading="lazy" decoding="async">
    <div class="kit-inner">
      <ul>
        <li>{c['kit_li1']}</li>
        <li>{c['kit_li2']}</li>
        <li>{c['kit_li3']}</li>
        <li>{c['kit_li4']}</li>
        <li>{c['kit_li5']}</li>
      </ul>
      <div class="hx-kit-order" id="{kit_form_id}">
        <div class="hx-price-card hx-price-card--kit">
          <h2>{c['offer_h2']}</h2>
          <p class="sub">{c['offer_sub']}</p>
          <div class="price-row">
            <div class="price-label">{c['price_label']}</div>
            <div class="now">{offer['price_now']}</div>
            <div class="was">{offer['price_was']}</div>
            <div class="discount-pill">{c['discount']}</div>
          </div>
          <p class="scroll-hint">{c['scroll_hint']}</p>
        </div>
        <div class="hx-form-card">
          <span class="stock-badge">{c['stock_badge']}</span>
          <p class="stock-warn">{c['stock_warn']}</p>
          <div class="live-row">
            <span class="dot"></span>
            <span class="js-live-count" data-live="{c['live']}"><strong>4</strong></span>
          </div>
          <h3>{c['form_h3']}</h3>
          <p class="form-intro">{c['form_intro']}</p>
{form_block(c, offer, ty_url, suffix="-kit", form_id=kit_form_id)}
          <ul class="hx-trust-list">
            <li>{c['trust1']}</li>
            <li>{c['trust2']}</li>
            <li>{c['trust3']}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="hx-faq wrap--narrow">
  <h2>{c['faq_h2']}</h2>
{faq_html(c['faq'])}
</section>

<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="/" class="site-logo" aria-label="gadgetmarketworld.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">gadgetmarketworld</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">{c['footer_blurb']}</p>
      </div>
      <div>
        <h4 class="site-footer__heading">{c['footer_info']}</h4>
        <ul class="site-footer__list">
          <li><a href="/{geo}/about-us.html">{fl['about'][offer['locale_key']]}</a></li>
          <li><a href="/{geo}/contact-us.html">{fl['contact'][offer['locale_key']]}</a></li>
          <li><a href="/{geo}/privacy-policy.html">Privacy Policy</a></li>
          <li><a href="/{geo}/terms-conditions.html">Terms</a></li>
          <li><a href="/{geo}/cookie-policy.html">Cookies</a></li>
          <li><a href="/{geo}/shipping-policy.html">Shipping</a></li>
          <li><a href="/{geo}/refund-policy.html">Refund</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">{c['footer_contact']}</h4>
        <ul class="site-footer__list">
          <li><strong>Eazy Commerce SRLS</strong></li>
          <li>STRADA IV DESTRA — Via Lemitone, 13, 81030 Casaluce, Italia</li>
          <li><a href="mailto:info@gadgetmarketworld.com">info@gadgetmarketworld.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Eazy Commerce SRLS</strong> — {c['footer_rights']}
      <a href="/">gadgetmarketworld.com</a>
    </div>
  </div>
</footer>

<script src="https://offers.adricenetwork.com/forms/html/js-v2/" defer></script>
<script src="/assets/js/heaterax-landing.js?v=2" defer></script>
<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {{
    el.textContent = String(new Date().getFullYear());
  }});
</script>
</body>
</html>
"""


def render_thank_you(offer: dict, c: dict) -> str:
    geo = offer["geo"]
    slug = offer["slug"]
    lang = offer["lang"]
    brand = c["brand"]
    steps = "\n".join(f"        <li>{s}</li>" for s in c["ty_steps"])
    trust = "\n".join(f'    <span class="ty-trust__badge">{t}</span>' for t in c["ty_trust"])
    meta_cpa = offer["meta_cpa"]

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18429742678"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-18429742678');
</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(c['ty_title'])}</title>
<meta name="description" content="{esc(c['ty_desc'])}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="/assets/css/variables.css">
<link rel="stylesheet" href="/assets/css/reset.css">
<link rel="stylesheet" href="/assets/css/components.css">
<style>
body {{ background: #f8fafc; }}
.ty-page {{ max-width: 540px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }}
.ty-check {{ width: 64px; height: 64px; border-radius: 9999px; background: #fff; border: 2px solid var(--color-primary); display: flex; align-items: center; justify-content: center; margin: 1rem auto 1.5rem; font-size: 2rem; color: var(--color-primary); font-weight: 800; }}
.ty-headline {{ font-size: 1.625rem; font-weight: 800; line-height: 1.2; text-align: center; margin-bottom: 0.875rem; }}
.ty-subhead {{ text-align: center; color: var(--color-text-muted); font-size: 1rem; line-height: 1.5; margin-bottom: 1.5rem; max-width: 440px; margin-left: auto; margin-right: auto; }}
.ty-hero {{ border-radius: 0.75rem; overflow: hidden; aspect-ratio: 2848 / 1331; background: var(--color-bg-alt); margin-bottom: 1.5rem; }}
.ty-hero img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
.ty-action {{ background: #fef9e7; border: 1.5px solid #f5d07a; border-radius: 0.75rem; padding: 1.25rem 1.25rem 1.5rem; margin-bottom: 1rem; }}
.ty-action__eyebrow {{ font-size: 0.7rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; color: #92400e; margin-bottom: 0.625rem; text-align: center; }}
.ty-action__title {{ font-size: 1.25rem; font-weight: 800; text-align: center; margin-bottom: 0.625rem; }}
.ty-action__body {{ text-align: center; color: var(--color-text-muted); font-size: 0.95rem; line-height: 1.5; margin-bottom: 0.75rem; }}
.ty-action__warning {{ text-align: center; color: var(--color-urgency); font-weight: 700; font-size: 0.9rem; }}
.ty-box {{ background: #fff; border: 1px solid var(--color-border); border-radius: 0.75rem; margin-bottom: 1rem; overflow: hidden; }}
.ty-box__header {{ background: var(--color-bg-alt); padding: 0.75rem 1rem; font-weight: 800; font-size: 0.95rem; }}
.ty-box__body {{ padding: 1rem 1.25rem; }}
.ty-steps-list {{ list-style: none; margin: 0; padding: 0; counter-reset: ty-step; }}
.ty-steps-list li {{ padding: 0.75rem 0; border-bottom: 1px solid var(--color-border); display: flex; gap: 0.5rem; counter-increment: ty-step; }}
.ty-steps-list li:last-child {{ border-bottom: none; }}
.ty-steps-list li::before {{ content: counter(ty-step) "."; font-weight: 800; color: var(--color-primary); min-width: 1.25rem; }}
.ty-trust {{ display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center; margin-top: 1.25rem; }}
.ty-trust__badge {{ background: #fff; border: 1px solid var(--color-border); border-radius: 9999px; padding: 0.4rem 0.875rem; font-size: 0.75rem; font-weight: 600; }}
</style>
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{offer['currency']}',
  PRICE: {offer['price']},
  META_PURCHASE_VALUE: {meta_cpa},
  META_PURCHASE_CURRENCY: 'USD',
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/main.js" defer></script>
<script src="/assets/js/meta-purchase-thankyou.js" defer></script>
</head>
<body>
<header class="site-header"><div class="site-header__inner"><a href="/" class="site-logo"><span class="site-logo__text"><span class="site-logo__text-primary">gadgetmarketworld</span><span class="site-logo__text-accent">.com</span></span></a></div></header>
<main class="ty-page">
  <div class="ty-check" aria-hidden="true">✓</div>
  <h1 class="ty-headline">{c['ty_h1']}</h1>
  <p class="ty-subhead">{c['ty_sub']}</p>
  <figure class="ty-hero"><img src="/assets/img/site/thank_you_draftin.png" alt="" width="2848" height="1331" loading="lazy"></figure>
  <section class="ty-action">
    <div class="ty-action__eyebrow">{c['ty_action_eyebrow']}</div>
    <h2 class="ty-action__title">{c['ty_action_title']}</h2>
    <p class="ty-action__body">{c['ty_action_body']}</p>
    <p class="ty-action__warning">{c['ty_action_warn']}</p>
  </section>
  <section class="ty-box">
    <div class="ty-box__header">{c['ty_hours_h']}</div>
    <div class="ty-box__body"><div class="ty-hours-line">{c['ty_hours']}</div></div>
  </section>
  <section class="ty-box">
    <div class="ty-box__header">{c['ty_next_h']}</div>
    <div class="ty-box__body"><ol class="ty-steps-list">
{steps}
    </ol></div>
  </section>
  <div class="ty-trust">
{trust}
  </div>
</main>
<footer class="site-footer"><div class="container"><div class="site-footer__bottom">© <span data-year>2026</span> <strong>Eazy Commerce SRLS</strong> · <a href="/">gadgetmarketworld.com</a></div></div></footer>
<script>
  gtag('event', 'conversion', {{ 'send_to': 'AW-18429742678/vPFmCKrole4cENac_tNE', 'value': {meta_cpa}, 'currency': 'USD' }});
</script>
</body>
</html>
"""


def render_index(offer: dict, c: dict) -> str:
    geo = offer["geo"]
    slug = offer["slug"]
    lang = offer["lang"]
    path = f"/{geo}/{slug}/landing.html"
    brand = c["brand"]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>window.location.replace('{path}' + window.location.search + window.location.hash);</script>
<meta http-equiv="refresh" content="0;url={path}">
<link rel="canonical" href="{BASE}{path}">
</head>
<body><p><a href="{path}">{brand}</a></p></body>
</html>
"""


def main() -> None:
    for offer in OFFERS:
        c = COPY[offer["locale_key"]]
        out_dir = ROOT / offer["geo"] / offer["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "landing.html").write_text(render_landing(offer, c), encoding="utf-8")
        (out_dir / "thank-you.html").write_text(render_thank_you(offer, c), encoding="utf-8")
        (out_dir / "index.html").write_text(render_index(offer, c), encoding="utf-8")
        print("Wrote", out_dir.relative_to(ROOT))


if __name__ == "__main__":
    main()
