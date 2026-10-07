#!/usr/bin/env python3
"""Generate Hungarian Embera Flame Start LP from CZ template (offer #2400)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEO = "hu"
SLUG = "electric-fireplace-2400"
OUT = ROOT / GEO / SLUG
BASE = ROOT / "cz" / SLUG
TARGET = "https://gadgetmarketworld.com"
TY = f"{TARGET}/{GEO}/{SLUG}/thank-you.html"

INDEX = f"""<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{GEO}/{SLUG}/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{GEO}/{SLUG}/landing.html">
<link rel="canonical" href="{TARGET}/{GEO}/{SLUG}/landing.html">
</head>
<body>
<p><a href="/{GEO}/{SLUG}/landing.html">Embera: Flame Start</a></p>
</body>
</html>
"""


def patch_landing(html: str) -> str:
    html = html.replace('lang="cs"', 'lang="hu"', 1)
    html = html.replace("/cz/", f"/{GEO}/")
    html = html.replace(
        "<title>Elektrický krb — Embera: Flame Start | gadgetmarketworld.com</title>",
        "<title>Elektromos kandalló — Embera: Flame Start | gadgetmarketworld.com</title>",
    )
    html = html.replace(
        'content="Embera: Flame Start — elektrický krb s chytrým termostatem a grafenovou technologií. Vyhřeje až 65 m². Platba dobírkou."',
        'content="Embera: Flame Start — elektromos kandalló okos termosztáttal és grafén technológiával. Akár 65 m² fűtése. Utánvétes fizetés."',
    )
    html = html.replace(
        f"https://gadgetmarketworld.com/cz/{SLUG}/landing.html",
        f"{TARGET}/{GEO}/{SLUG}/landing.html",
    )
    html = html.replace("GEO: 'cz'", "GEO: 'hu'")
    html = html.replace("CURRENCY: 'CZK'", "CURRENCY: 'HUF'")
    html = html.replace("PRICE: 2290", "PRICE: 39999")
    html = html.replace(
        "OFFER_NAME: 'Embera Flame Start 2400 CZ'",
        "OFFER_NAME: 'Embera Flame Start 2400 HU'",
    )
    html = html.replace(
        f"LP_ID: 'cz-{SLUG}'",
        f"LP_ID: 'hu-{SLUG}'",
    )
    html = html.replace("SUBMITTING_LABEL: 'Odesílání...'", "SUBMITTING_LABEL: 'Küldés...'")

    html = html.replace(
        "4,8 / 5 – Vynikající hodnocení",
        "4,8 / 5 – Kiváló értékelés",
    )
    html = html.replace(
        "Embera: Flame Start — <b>Elektrický krb s chytrým termostatem, grafenovou technologií a nastavitelným výkonem, který za 15 minut vyhřeje 65 m² a ušetří až 40 % na energiích.</b>",
        "Embera: Flame Start — <b>Okos termosztátos, grafén technológiás, állítható teljesítményű elektromos kandalló, amely 15 perc alatt akár 65 m²-t fűt, akár 40%-kal alacsonyabb rezsiköltséggel.</b>",
    )
    html = html.replace(
        "<strong>[Limitovaná edice]</strong> Proměňte každý prostor v teplé a útulné místo. Dekorativní 6D plamen okamžitě navodí atmosféru, grafen a chytrý termostat rovnoměrně šíří sálavé teplo s nízkou spotřebou.",
        "<strong>[Limitált kiadás]</strong> Alakítson bármely helyiséget meleg, otthonos térré. A dekoratív 6D láng azonnal hangulatot teremt, a grafén és az okos termosztát egyenletes sugárzó hőt ad alacsony fogyasztással.",
    )
    html = html.replace('aria-label="Hlavní vlastnosti"', 'aria-label="Fő jellemzők"')

    benefits = [
        ("Více tepla, méně plýtvání", "Több meleg, kevesebb pazarlás", "Efektivně vyhřívá a optimalizuje spotřebu každý den.", "Hatékonyan fűt és minden nap optimalizálja a fogyasztást."),
        ("Rychlé a rovnoměrné teplo", "Gyors, egyenletes hő", "Rozprostírá teplo rovnoměrně v celé místnosti.", "Egyenletesen oszlik el a hő az egész szobában."),
        ("3 úrovně výkonu", "3 teljesítményszint", "Snadno zvolíte vhodnou intenzitu topení.", "Könnyen választhatja a megfelelő fűtési erősséget."),
        ("Realistický 6D efekt plamene", "Valósághű 6D láng", "Vytvoří hřejivou atmosféru jako u pravého krbu.", "Meleg, otthonos hangulatot ad, mint egy igazi kandalló."),
        ("Tichý i v noci", "Csendes éjszaka is", "Diskrétní provoz bez rušení odpočinku.", "Diszkrét működés, nem zavarja a pihenést."),
        ("Pohodlné ovládání dálkovým ovladačem", "Kényelmes távirányító", "Teplota, časovač a funkce bez vstávání.", "Hőmérséklet, időzítő és funkciók felkelés nélkül."),
        ("Větší bezpečnost", "Nagyobb biztonság", "Vestavěné ochrany pro klidnější používání.", "Beépített védelmek a nyugodtabb használatért."),
        ("Kompaktní a snadno umístitelný", "Kompakt, könnyen elhelyezhető", "Vejde se do obýváku, ložnice nebo pracovny.", "Belefér a nappaliba, hálószobába vagy irodába."),
    ]
    for cz_t, hu_t, cz_p, hu_p in benefits:
        html = html.replace(f"<h3>{cz_t}</h3><p>{cz_p}</p>", f"<h3>{hu_t}</h3><p>{hu_p}</p>")

    html = html.replace("Jen dziś za pouhých", "Csak ma mindössze")  # safety
    html = html.replace("Jen dnes za pouhých", "Csak ma mindössze")
    html = html.replace("Exkluzivní cena pro online objednávky", "Exkluzív ár online rendelésre")
    html = html.replace("2 290 <span class=\"currency\">Kč</span>", "39 999 <span class=\"currency\">Ft</span>")
    html = html.replace("7 633 Kč", "133 000 Ft")
    html = html.replace("UŠETŘÍTE 70 %", "70%-OT MEGTAKARÍT")
    html = html.replace("📦 Dostupnost", "📦 Elérhetőség")
    html = html.replace("POSLEDNÍ KUSKY SKLADEM", "UTOLSÓ DARABOK RAKTÁRON")

    html = html.replace("ZAMÓW TERAZ", "RENDELJEN MOST")  # pl safety
    html = html.replace("<h2>OBJEDNEJTE TEĎ</h2>", "<h2>RENDELJEN MOST</h2>")
    html = html.replace("<h3>Vyplňte formulář</h3>", "<h3>Töltse ki az űrlapot</h3>")
    html = html.replace("<label for=\"name\">Jméno a příjmení</label>", "<label for=\"name\">Teljes név</label>")
    html = html.replace("<label for=\"street-address\">Adresa</label>", "<label for=\"street-address\">Szállítási cím</label>")
    html = html.replace("<label for=\"tel\">Telefon</label>", "<label for=\"tel\">Telefonszám</label>")
    html = html.replace('placeholder="Jan Novák"', 'placeholder="Gábor Tóth"')
    html = html.replace('placeholder="Václavské náměstí 10, 110 00 Praha"', 'placeholder="Andrássy út 12, 1061 Budapest"')
    html = html.replace('placeholder="+420 777 123 456"', 'placeholder="+36 30 123 4567"')
    html = html.replace('for="name-bottom">Jméno a příjmení', 'for="name-bottom">Teljes név')
    html = html.replace('for="street-address-bottom">Adresa', 'for="street-address-bottom">Szállítási cím')
    html = html.replace('for="tel-bottom">Telefon', 'for="tel-bottom">Telefonszám')
    html = html.replace('placeholder="Jan Novák"', 'placeholder="Gábor Tóth"')

    html = html.replace(TY.replace("hu", "cz"), TY)
    html = html.replace(
        f"https://gadgetmarketworld.com/cz/{SLUG}/thank-you.html",
        TY,
    )

    html = html.replace(
        "<button name=\"submit\" type=\"submit\">Potvrdit objednávku — 2 290 Kč</button>",
        "<button name=\"submit\" type=\"submit\">Rendelés megerősítése — 39 999 Ft</button>",
    )
    html = html.replace(
        "Akceptuji <a href=\"/cz/privacy-policy.html\">zásady ochrany soukromí</a>",
        "Elfogadom az <a href=\"/hu/privacy-policy.html\">adatvédelmi szabályzatot</a>",
    )

    html = html.replace('aria-label="Časté dotazy"', 'aria-label="Gyakori kérdések"')
    html = html.replace("<li>Časté dotazy</li>", "<li>Gyakori kérdések</li>")

    faqs = [
        ("JAK OBJEDNAT?", "HOGYAN RENDELJEN?", "Po odeslání formuláře vás telefonicky kontaktuje operátor pro potvrzení objednávky.", "Az űrlap elküldése után operátor hívja telefonon a rendelés megerősítésére."),
        ("MOHU PLATIT DOBÍRKOU?", "FIZETHETEK UTÁNVÉTTEL?", "Ano — platíte hotově kurýrovi při doručení.", "Igen — készpénzzel fizet a futárnak átvételkor."),
        ("CO JE CHYTRÉ TOPENÍ?", "MI AZ OKOS FŰTÉS?", "Automaticky reguluje výkon, aby se neplýtvalo energií.", "Automatikusan szabályozza a teljesítményt, hogy ne pazaroljon energiát."),
        ("CO JE SÁLAVÉ TOPENÍ?", "MI A SUGÁRZÓ FŰTÉS?", "Topí lidi a předměty, nejen vzduch — teplo je hlubší a účinnější.", "Embereket és tárgyakat fűt, nem csak a levegőt — mélyebb, hatékonyabb meleg."),
        ("JAKÉ JSOU ROZMĚRY?", "MILYEN A MÉRET?", "Výška 43 cm bez podstavce · 53 cm s podstavcem · Šířka 46 cm · Hloubka 27 cm.", "Magasság 43 cm talp nélkül · 53 cm talppal · Szélesség 46 cm · Mélység 27 cm."),
        ("JAKÉ JSOU NÁKLADY NA ENERGII?", "MENNYI AZ ENERGIaköltség?", "Při 15 hodinách provozu cca 8–9 €. Energetická třída A++.", "15 óra használatnál kb. 8–9 €. A++ energiaosztály."),
        ("JE BEZPEČNÝ?", "BIZTONSÁGOS?", "Automatické vypnutí, neznečišťuje vzduch, tichý provoz.", "Automatikus kikapcsolás, nem szennyezi a levegőt, csendes működés."),
        ("JAK VRÁTIT ZBOŽÍ?", "HOGYAN KÜLDHETEM VISSZA?", "Do 14 dnů od převzetí, pokud je produkt nepoškozený.", "14 napon belül átvételtől, ha a termék sértetlen."),
        ("JAKÁ JE ZÁRUKA?", "MILYEN A GARANCIA?", "Bezplatná oprava nebo výměna při vadě dle podmínek.", "Ingyenes javítás vagy csere hibánál a feltételek szerint."),
    ]
    for cz_s, hu_s, cz_b, hu_b in faqs:
        html = html.replace(f"<summary>{cz_s}</summary><div class=\"faq-body\">{cz_b}</div>", f"<summary>{hu_s}</summary><div class=\"faq-body\">{hu_b}</div>")

    html = html.replace("Objednat nyní", "Rendeljen most")
    html = html.replace("Objednejte nyní", "Rendeljen most")

    prose_cz = [
        "Chcete vyhřát místnost během pár sekund?",
        "Szeretné másodpercek alatt felmelegíteni a szobát?",
    ]
    html = html.replace(prose_cz[0], prose_cz[1])

    html = html.replace(
        "Element s <strong>hexagonálním grafenem</strong> rychle a <strong>rovnoměrně</strong> šíří teplo. Vyhřeje až <strong>65 m² za 15 minut</strong> s nastavitelným výkonem <strong>1000 W</strong> a <strong>1500 W</strong>.",
        "A <strong>hexagonális grafén</strong> elem gyorsan és <strong>egyenletesen</strong> oszlatja a hőt. Akár <strong>65 m²-t 15 perc alatt</strong> fűt, <strong>1000 W</strong> és <strong>1500 W</strong> állítható teljesítménnyel.",
    )
    html = html.replace(
        "Jednoduchá montáž s nohami a kompletní sada v balení. Rychlé teplo v celé místnosti včetně sálavého. Plášť se nepřehřívá — bezpečnější pro děti a domácí mazlíčky.",
        "Egyszerű szerelés lábakkal, teljes készlet a csomagban. Gyors hő az egész szobában, sugárzó fűtéssel is. A burkolat nem forrósodik túl — biztonságosabb gyerekeknek és háziállatoknak.",
    )

    html = html.replace(
        "Ultra realistické LED plameny <strong>3D</strong> vytvářejí atmosféru pravého krbu. <strong>Chytrý termostat</strong> od 15° do 35°: snižuje výkon a <strong>neplýtvá energií</strong>. Ovládání i <strong>mobilní aplikací</strong>.",
        "Ultra valósághű <strong>3D</strong> LED lángok igazi kandalló hangulatot adnak. <strong>Okos termosztát</strong> 15° és 35° között: csökkenti a teljesítményt, <strong>nem pazarol</strong>. <strong>Mobilapp</strong> is.",
    )
    html = html.replace(
        "Dálkové ovládání do 20 m: plameny, teplota a časovač.",
        "Távirányító 20 m-ig: láng, hőmérséklet és időzítő.",
    )

    html = html.replace(
        "Až <strong>4 režimy topení</strong> pro podzim, jaro nebo chladnější dny s optimalizovanou spotřebou.",
        "Akár <strong>4 fűtési mód</strong> őszre, tavaszra vagy hidegebb napokra, optimalizált fogyasztással.",
    )
    html = html.replace(
        "Pokročilá technologie pro <strong>úsporu až 40 % na energiích</strong> s přesnou regulací teploty.",
        "Fejlett technológia akár <strong>40% energiamegtakarításhoz</strong> precíz hőszabályozással.",
    )

    html = html.replace('aria-label="Recenze zákazníků"', 'aria-label="Vásárlói vélemények"')
    html = html.replace("★ 4,8/5 · Ověřený nákup", "★ 4,8/5 · Ellenőrzött vásárlás")
    html = html.replace("<h2>Recenze zákazníků</h2>", "<h2>Vásárlói vélemények</h2>")

    reviews = [
        ("Jana Nováková — Brno", "Katalin Nagy — Debrecen", "Atmosféra a nízká spotřeba", "Hangulat és alacsony fogyasztás",
         "«Konečně firma, která dobře balí! Lehký a hezký. Dělá skvělou atmosféru. Až se místnost vyhřeje, po cca 20 minutách lze vypnout topení a nechat jen plameny. Doporučuji hlavně kvůli spotřebě.»",
         "«Végre egy cég, ami jól csomagol! Könnyű és szép. Nagyszerű hangulatot ad. Amint felmelegedett a szoba, kb. 20 perc után kikapcsolható a fűtés, maradhat csak a láng. Főleg a fogyasztás miatt ajánlom.»"),
        ("Petra Svobodová — Ostrava", "Eszter Horváth — Szeged", "Realistický plamen, rychlé topení", "Valós láng, gyors fűtés",
         "«Efekt plamene je opravdu realistický, rychle topí, spotřeba velmi nízká. Fantastický produkt.»",
         "«A láng hatás tényleg valósághű, gyorsan fűt, nagyon alacsony a fogyasztás. Fantasztikus termék.»"),
        ("Martin Dvořák — Plzeň", "Tamás Kovács — Pécs", "Druhý nákup, malá spotřeba", "Második vásárlás, alacsony fogyasztás",
         "«Kupuji podruhé a jsem velmi spokojený. Okamžité a účinné teplo. Odběr opravdu nízký, navíc lze zvolit režim topení.»",
         "«Másodszor veszem, nagyon elégedett vagyok. Azonnali, hatékony meleg. Tényleg alacsony fogyasztás, ráadásul választható fűtési mód.»"),
    ]
    for cz_a, hu_a, cz_h, hu_h, cz_p, hu_p in reviews:
        html = html.replace(f'alt="{cz_a}"', f'alt="{hu_a}"')
        html = html.replace(f"<h4>{cz_h}</h4>", f"<h4>{hu_h}</h4>")
        html = html.replace(f"<p>{cz_p}</p>", f"<p>{hu_p}</p>", 1)
        html = html.replace(f"<div class=\"author\">{cz_a.split(' — ')[0]} — {cz_a.split(' — ')[1]}", f"<div class=\"author\">{hu_a.split(' — ')[0]} — {hu_a.split(' — ')[1]}")

    html = html.replace(
        "<h3 class=\"order-summary__title\">Shrnutí — co dostanete domů</h3>",
        "<h3 class=\"order-summary__title\">Összegzés — mit kap otthonába</h3>",
    )
    html = html.replace(
        "<span>Krb s 6D efektem plamene · chytrý termostat · grafen</span>",
        "<span>6D láng hatás · okos termosztát · grafén</span>",
    )
    html = html.replace("<li>1× Krb s 6D efektem plamene</li>", "<li>1× 6D láng hatású kandalló</li>")
    html = html.replace("<li>1× Dálkové ovládání</li>", "<li>1× Távirányító</li>")
    html = html.replace("<li>1× Montážní sada + díly</li>", "<li>1× Szerelőkészlet + alkatrészek</li>")
    html = html.replace("<li>1× Návod v češtině</li>", "<li>1× Magyar nyelvű útmutató</li>")
    html = html.replace("<li>1× Napájecí kabel</li>", "<li>1× Tápkábel</li>")
    html = html.replace("<li>Záruka 3 roky · Vrácení do 14 dnů</li>", "<li>3 év garancia · 14 napos visszaküldés</li>")
    html = html.replace("<span class=\"order-summary__price-label\">Celkem objednávka</span>", "<span class=\"order-summary__price-label\">Rendelés összege</span>")
    html = html.replace("<small>Platíte až při doručení</small>", "<small>Csak átvételkor fizet</small>")
    html = html.replace("<span class=\"order-summary__price-old\">7 633 Kč</span>", "<span class=\"order-summary__price-old\">133 000 Ft</span>")
    html = html.replace("<strong class=\"order-summary__price-now\">2 290 Kč</strong>", "<strong class=\"order-summary__price-now\">39 999 Ft</strong>")
    html = html.replace("<span class=\"order-summary__price-save\">Ušetříte 5 343 Kč</span>", "<span class=\"order-summary__price-save\">93 001 Ft-ot megtakarít</span>")
    html = html.replace(
        "<p class=\"order-summary__note\">🚚 Doprava v ceně · 💵 Hotově kurýrovi · Bez karty</p>",
        "<p class=\"order-summary__note\">🚚 Ingyenes szállítás · 💵 Készpénz a futárnak · Kártya nélkül</p>",
    )
    html = html.replace("<strong>Poslední kusy skladem</strong>", "<strong>Utolsó darabok raktáron</strong>")
    html = html.replace(
        "<h2>ZADEJTE SVÉ ÚDAJE<br>PRO OBJEDNÁVKU</h2>",
        "<h2>ADJA MEG ADATAIT<br>A RENDELÉSHEZ</h2>",
    )
    html = html.replace(
        "<button name=\"submit\" type=\"submit\">Potvrdit objednávku — 2 290 Kč</button>",
        "<button name=\"submit\" type=\"submit\">Rendelés megerősítése — 39 999 Ft</button>",
    )

    html = html.replace(
        "<p class=\"site-footer__blurb\">Praktické produkty pro každý den, doručení do 24–48 hodin s platbou dobírkou.</p>",
        "<p class=\"site-footer__blurb\">Hasznos termékek mindennapra, 24–48 órás szállítás utánvéttel.</p>",
    )
    html = html.replace("<h4 class=\"site-footer__heading\">Informace</h4>", "<h4 class=\"site-footer__heading\">Információ</h4>")
    html = html.replace("<li><a href=\"/hu/about-us.html\">O nás</a></li>", "<li><a href=\"/hu/about-us.html\">Rólunk</a></li>")
    html = html.replace("<li><a href=\"/hu/contact-us.html\">Kontakt</a></li>", "<li><a href=\"/hu/contact-us.html\">Kapcsolat</a></li>")
    html = html.replace("Ochrana soukromí", "Adatvédelem")
    html = html.replace("Obchodní podmínky", "Felhasználási feltételek")
    html = html.replace("Doprava", "Szállítás")
    html = html.replace("Vrácení zboží", "Visszaküldés")
    html = html.replace("Všechna práva vyhrazena.", "Minden jog fenntartva.")

    html = html.replace(
        "var tpl = '<strong>__N__ lidí</strong> si právě prohlíží Embera';",
        "var tpl = '<strong>__N__ ember</strong> nézi most az Embera-t';",
    )
    return html


def patch_thank_you(html: str) -> str:
    html = html.replace('lang="cs"', 'lang="hu"', 1)
    html = html.replace("/cz/", f"/{GEO}/")
    html = html.replace(
        "<title>Objednávka přijata — Zvedněte telefon | Embera: Flame Start™</title>",
        "<title>Rendelés rögzítve — Vegye fel a telefont | Embera: Flame Start™</title>",
    )
    html = html.replace(
        'content="Vaše objednávka Embera: Flame Start™ byla zaregistrována. Zvedněte potvrzovací hovor od operátora."',
        'content="Embera: Flame Start™ rendelését rögzítettük. Vegye fel az operátor megerősítő hívását."',
    )
    html = html.replace("GEO: 'cz'", "GEO: 'hu'")
    html = html.replace("CURRENCY: 'CZK'", "CURRENCY: 'HUF'")
    html = html.replace("PRICE: 2290.0", "PRICE: 39999.0")
    html = html.replace(
        "COOKIE_TEXT: 'Používáme technické cookies a cookies třetích stran pro lepší zážitek a analýzu.',",
        "COOKIE_TEXT: 'Technikai és harmadik féltől származó sütiket használunk a jobb élményért és elemzéshez.',",
    )
    html = html.replace("COOKIE_ACCEPT: 'Přijmout'", "COOKIE_ACCEPT: 'Elfogadom'")
    html = html.replace("COOKIE_LEARN: 'Více informací'", "COOKIE_LEARN: 'Tudjon meg többet'")

    html = html.replace(
        "<h1 class=\"ty-headline\">Vaše objednávka byla úspěšně zaregistrována!</h1>",
        "<h1 class=\"ty-headline\">Rendelését sikeresen rögzítettük!</h1>",
    )
    html = html.replace(
        "<p class=\"ty-subhead\">Výborně — objednávka se zpracovává. Zbývá už jen <strong>poslední krok</strong> k dokončení a odeslání zásilky.</p>",
        "<p class=\"ty-subhead\">Remek — a rendelés feldolgozás alatt. Már csak <strong>egy utolsó lépés</strong> van a szállításig.</p>",
    )
    html = html.replace(
        'alt="gadgetmarketworld"',
        'alt="gadgetmarketworld csapat: call center és utánvétes logisztika"',
    )
    html = html.replace("👇 Co udělat teď", "👇 Mit tegyen most")
    html = html.replace("📞 Zvedněte potvrzovací hovor", "📞 Vegye fel a megerősítő hívást")
    html = html.replace(
        "<p class=\"ty-action__body\">Operátor vás během <strong>nejbližších hodin</strong> kontaktuje a potvrdí objednávku <strong>Embera: Flame Start™</strong>.</p>",
        "<p class=\"ty-action__body\">Munkatársunk <strong>a következő órákban</strong> hívja, hogy megerősítse <strong>Embera: Flame Start™</strong> rendelését.</p>",
    )
    html = html.replace(
        "Pokud hovor nezvednete, objednávka bude automaticky zrušena.",
        "Ha nem veszi fel, a rendelés automatikusan törlődik.",
    )
    html = html.replace("🕒 Kontaktní hodiny", "🕒 Elérhetőség")
    html = html.replace("<strong>Pondělí – Sobota</strong>", "<strong>Hétfő – Szombat</strong>")
    html = html.replace("📋 Co bude následovat", "📋 Mi történik ezután")
    html = html.replace("Zvedněte hovor a <strong>potvrďte údaje</strong>", "Vegye fel a hívást és <strong>erősítse meg adatait</strong>")
    html = html.replace("Odeslání do <strong>24–48 hodin</strong>", "Feladás <strong>24–48 órán</strong> belül")
    html = html.replace("Doručení domů a <strong>platba dobírkou</strong>", "Házhoz szállítás és <strong>utánvét</strong>")
    html = html.replace("🔒 Platba dobírkou", "🔒 Utánvét")
    html = html.replace("🛡️ Záruka 3 roky", "🛡️ 3 év garancia")
    html = html.replace("🔐 Ochrana SSL", "🔐 SSL védelem")
    html = html.replace("Informace", "Információ")
    html = html.replace("O nás", "Rólunk")
    html = html.replace("Kontakt</a>", "Kapcsolat</a>")
    html = html.replace("Ochrana soukromí", "Adatvédelem")
    html = html.replace("Obchodní podmínky", "Felhasználási feltételek")
    html = html.replace(">Cookies<", ">Cookie szabályzat<")
    html = html.replace(">Doprava<", ">Szállítás<")
    html = html.replace("Vrácení zboží", "Visszaküldés")
    html = html.replace("Všechna práva vyhrazena.", "Minden jog fenntartva.")
    html = html.replace("'currency': 'EUR',", "'currency': 'USD',")
    return html


def add_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    lastmod = "2026-10-07"
    entries = []
    for suffix in ("/", "/landing.html"):
        loc = f"{TARGET}/{GEO}/{SLUG}{suffix}"
        if loc not in text:
            entries.append(
                f'  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>'
                f"<changefreq>weekly</changefreq><priority>0.95</priority></url>\n"
            )
    if entries:
        text = text.replace("</urlset>", "".join(entries) + "</urlset>")
        path.write_text(text, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    landing = patch_landing((BASE / "landing.html").read_text(encoding="utf-8"))
    thank = patch_thank_you((BASE / "thank-you.html").read_text(encoding="utf-8"))
    (OUT / "landing.html").write_text(landing, encoding="utf-8")
    (OUT / "thank-you.html").write_text(thank, encoding="utf-8")
    (OUT / "index.html").write_text(INDEX, encoding="utf-8")
    add_sitemap()
    print("wrote", OUT)


if __name__ == "__main__":
    main()
