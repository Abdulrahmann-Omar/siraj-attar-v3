"""Builds plan/assets.json: the 40 assets. Run from the project root."""
import json

A = []


def a(id, kind, layout, fmt, image, products, brief, title):
    A.append({"id": id, "kind": kind, "layout": layout, "format": fmt, "image": image,
              "product_ids": products, "brief": brief, "title_en": title})


# ---- 16 product shots (no text, one perspective each) ----
shots = [
    ("P01", "gen/out/BAKE_NBP.png", ["966965063"], "Yaqoot red shemagh worn: three-quarter waist-up, Diriyah mud-brick terrace, golden hour"),
    ("P02", "gen/out/P02.png", ["966965063"], "Yaqoot shemagh in its green box: three-quarter high angle on travertine by a mud-brick wall"),
    ("P03", "gen/out/P03.png", ["1988908934"], "Yaqoot Shalsh red shemagh: macro weave texture, sculptural folds"),
    ("P04", "gen/out/P04.png", ["1740470085"], "Zumurrud white Swiss ghutra: overhead flat lay on green linen with its box"),
    ("P05", "gen/out/P05.png", ["502827333"], "Classic white ghutra worn: side profile, Riyadh business district morning"),
    ("P06", "gen/out/P06.png", ["1664674203"], "Naqsh 26 red shemagh: low-angle hero on a carved majlis chest, lantern night"),
    ("P07", "gen/out/P07.png", ["2124457749"], "Zumurrud laser-pattern white shemagh: backlit macro"),
    ("P08", "gen/out/P08.png", ["1292393513"], "Japanese thobe fabric 909: top-down on a tailor's cutting table"),
    ("P09", "gen/out/P09.png", ["1449104353"], "Italian Super 140 wool: stacked folds on an oak shelf, side light"),
    ("P10", "gen/out/P10.png", ["821325048"], "Pashmina shawl worn: three-quarter back view by a desert campfire, blue hour"),
    ("P11", "gen/out/P11.png", ["663088504"], "Al-Baidaa shawl: 45-degree overhead on a camel-hair rug with dallah, winter camp"),
    ("P12", "gen/out/P12.png", ["672063087"], "Attar perfume trio box: low-angle hero on a brass tray, incense smoke"),
    ("P13", "gen/out/P13.png", ["265256366"], "Silver cufflinks: in-hand macro on a white thobe cuff"),
    ("P14", "gen/out/P14.png", ["892978768"], "Wathir Italian undershirt: overhead three-quarter in its gift box on linen"),
    ("P15", "gen/out/P15.png", ["1113769137", "966965063"], "Attar agal: top-down on its box with a shemagh corner"),
    ("P16", "gen/out/P16.png", ["1292393513", "1668806182", "1449104353", "1029444903", "563952490"], "Fabric library: Japanese, Korean, Italian wool, English wool and Italian voile stacked"),
]
for id, img, prods, t in shots:
    a(id, "product_shot", None, "4:5", img, prods, None, t)

# ---- 10 catalogue posters (layout 'catalogue': photo panel top, paper panel below; 4:5) ----
cat = [
    ("C01", "gen/out/P02.png", "966965063", "Yaqoot classic shemagh"),
    ("C02", "gen/out/P04.png", "1740470085", "Zumurrud white Swiss ghutra"),
    ("C03", "gen/out/C03.png", "1604079293", "Audemar 4 shemagh (open-ended offer)"),
    ("C04", "gen/out/C04.png", "1949762576", "European shemagh (open-ended offer)"),
    ("C05", "gen/out/C05.png", "1471159401", "Hafawa 1 red shemagh"),
    ("C06", "gen/out/C06.png", "1546150268", "Al-Wisam 26 red shemagh (Asala collection)"),
    ("C07", "gen/out/P11.png", "663088504", "Al-Baidaa half-termeh wool shawl (open-ended offer)"),
    ("C08", "gen/out/C08.png", "1029444903", "William Halstead Super 130 English wool"),
    ("C09", "gen/out/P14.png", "892978768", "Wathir Italian undershirt"),
]
for id, img, pid, t in cat:
    a(id, "poster", "catalogue", "4:5", img, [pid],
      {"hook": "catalogue", "message": "Name the product verbatim, one short benefit line built ONLY from its catalogue specs (material, origin, size range or metres), the price, a short CTA."}, t)

# ---- 14 campaign pieces: «موسم الوسم» (winter / shemagh season, launch 16 Oct 2026) ----
K = [
    ("K01", "campaign_feed", "hero", "4:5", "gen/out/BAKE_NBP.png", ["966965063"],
     {"hook": "season", "message": "Campaign launch: the Wasm season has begun (winter, shemagh season). Pride, heritage of 80+ years, the Yaqoot shemagh. Headline 2-5 words, subline one line, price, CTA."}, "Launch hero feed"),
    ("K02", "campaign_story", "story", "9:16", "gen/out/BAKE_G25H.png", ["966965063"],
     {"hook": "season", "message": "Story teaser for the launch: short punchy line about the Wasm season and the shemagh, price, swipe-up CTA."}, "Launch story"),
    ("K03", "campaign_story", "story", "9:16", "gen/out/P05.png", ["502827333"],
     {"hook": "how", "message": "The white ghutra specialist. HOW hook: 100% Swiss cotton is why it stays bright white and holds its crease all day (only claims from specs: Swiss made, 100% cotton, sizes 50-62). Price, CTA."}, "Ghutra story (HOW)"),
    ("K04a", "carousel_slide", "look-cover", "1:1", "gen/out/BAKE_G25M.png", ["966965063", "1113769137", "1292393513", "672063087", "265256366"],
     {"hook": "look", "message": "Carousel cover: from head to toe, one house (shemagh, agal, thobe fabric, perfume, cufflinks). Swipe cue. Register must be pure in each version: فصحى 'من الرأس إلى القدم' vs سعودي 'من راسك لرجلينك'."}, "Complete look carousel cover"),
    ("K04b", "carousel_slide", "look-item", "1:1", "gen/out/P15.png", ["1113769137"], {"hook": "look", "message": "Slide 2: the head: agal (German mohair wool, made in Saudi Arabia). Name + price."}, "Carousel: agal"),
    ("K04c", "carousel_slide", "look-item", "1:1", "gen/out/P08.png", ["1292393513"], {"hook": "look", "message": "Slide 3: the thobe: Japanese fabric 909 (90% tetron 10% tencel, 5 m, one width, enough for one thobe). Name + price."}, "Carousel: thobe fabric"),
    ("K04d", "carousel_slide", "look-item", "1:1", "gen/out/P12.png", ["672063087"], {"hook": "look", "message": "Slide 4: the scent: Attar perfume collection (three bottles in the green box). Name + price."}, "Carousel: perfume"),
    ("K04e", "carousel_slide", "look-item", "1:1", "gen/out/P13.png", ["265256366"], {"hook": "look", "message": "Slide 5: the finishing touch: silver cufflinks (multiple options). Name + price + final CTA."}, "Carousel: cufflinks"),
    ("K05a", "carousel_slide", "how-step", "1:1", "gen/out/K05.png", ["1740470085"], {"hook": "care", "message": "HOW carousel slide 1 of 2: how to keep your ghutra bright white: iron at 110 degrees Celsius, no more no less (from the store's care notes). Step number 1."}, "Care carousel: ironing"),
    ("K05b", "carousel_slide", "how-step", "1:1", "gen/out/P04.png", ["1740470085"], {"hook": "care", "message": "HOW carousel slide 2 of 2: wash in cold or lukewarm water only, never bleach (from the care notes). Step number 2. End with product name + price."}, "Care carousel: washing"),
    ("K06", "campaign_feed", "bundle", "4:5", "gen/out/K06.png", ["966965063", "663088504", "189452492", "1113769137"],
     {"hook": "offer", "message": "White Friday (27 Nov) winter set: shemagh, shawl, perfume, agal. Do NOT invent a discount: list the four items with their prices; mention paying in instalments (Tabby/Tamara) only if BRAND_FACTS confirms the store offers them. Headline, CTA."}, "White Friday winter set"),
    ("K07", "campaign_story", "story", "9:16", "gen/out/P10.png", ["821325048"],
     {"hook": "season", "message": "Al-Murabba'aniyah has begun (7 Dec, the coldest 40 nights): pashmina shawl, warmth with elegance. Price, CTA."}, "Murabba'aniyah story"),
    ("K08", "campaign_feed", "heritage", "4:5", "gen/out/K08.png", [],
     {"hook": "heritage", "message": "Heritage: 80+ years of craft. Jeddah 1377H, Riyadh 1389H, roots in Makkah trade, 9 branches today (Riyadh 4, Jeddah 3, Makkah 1, Khobar 1). No price. CTA: visit a branch or the store."}, "Heritage feed"),
    ("K09", "campaign_feed", "hero", "4:5", "gen/out/K09.png", ["1381142749"],
     {"hook": "occasion", "message": "Gifting: the special gift box (shemagh, perfume, cufflinks) for occasions and Eid. Price, CTA."}, "Gift box feed"),
    ("K10", "campaign_feed", "fabric-library", "4:5", "gen/out/P16.png", ["1292393513", "1668806182", "1449104353", "1029444903", "563952490"],
     {"hook": "how", "message": "Pre-Ramadan tailoring (fabric peak): how many metres does your thobe need? Use ONLY spec facts: Japanese 909 = 5 m one width enough for one thobe; Italian wool = 3.5 m one thobe; English wool = 3.5 m one thobe; Italian voile = 3.5 m. List 4 fabrics with origin and 'from' price. CTA: order before tailors close for Eid."}, "Fabric library feed (HOW)"),
]
for k in K:
    a(*k[:6], k[6], k[7])

assert len(A) == 40, len(A)
json.dump(A, open("plan/assets.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(A), "assets;", sum(1 for x in A if x["kind"] != "product_shot"), "posters x 2 tones")
