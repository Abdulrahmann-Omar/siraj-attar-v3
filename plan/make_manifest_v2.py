"""v2 manifest. Client hard constraints: realistic photography that shows the product itself; minimal environment
(only the product on one plain real surface and a plain backdrop, no props).
Engine: seedream_5_0_flash (won the realism bake-off: most faithful to the real product, real-photo look).
Ids are prefixed R_ so the v1 ledger entries stay separate. Run from the project root."""
import json, glob


def R(*ids):
    return [glob.glob(f"data/images/{i}.*")[0].replace("\\", "/") for i in ids]


MIN = "Minimal set: only the product on one plain real surface against a plain seamless backdrop; no props, no decorations, no extra objects."
HERO = ("The product is the hero: it fills about two-thirds of the frame, fully visible, nothing cropped, tack sharp. "
        "Real commercial photograph shot on a full-frame camera, natural daylight, realistic soft contact shadow, true colours, real material texture, "
        "no CGI look, no added text or letters. " + MIN)
WORN = ("Real editorial photograph, not a render: natural skin texture, real fabric folds, natural daylight, true colours, full-frame camera, 85mm, f/2.8. "
        "Plain seamless backdrop, nothing else in frame. The product is the focus and clearly visible. The man is an adult Saudi, not a celebrity. No added text or letters.")
J = []


def g(id, ar, refs, keep, scene, kind=HERO):
    J.append({"id": "R_" + id, "model": "seedream_5_0_flash",
              "prompt": f"Keep the product EXACTLY as in the reference photos: {keep}. {scene} {kind}",
              "images": refs, "params": {"aspect_ratio": ar, "resolution": "2k"}})


BOX = "the dark green box with its gold-foil round seal and gold lettering"
STONE = "on a plain honed beige stone surface against a plain warm-white backdrop"
# ---- 16 product shots (3:4, exported to 4:5) ----
g("P01", "3:4", R("966965063_2", "966965063_1"), "the red-and-white Yaqoot shemagh (same red houndstooth field, same white border with red stripes) and the black agal",
  "An adult Saudi man in his 30s wears this exact shemagh in the classic Saudi style with the black agal and a white Saudi thobe; waist-up, three-quarter view, plain warm-beige seamless backdrop, soft daylight; the shemagh pattern is crisp and fills much of the frame.", WORN)
g("P02", "3:4", R("966965063_1", "966965063_2"), f"{BOX}, and the red-and-white Yaqoot shemagh folded inside with one corner draped out",
  f"The open box {STONE}, three-quarter high angle, 100mm lens, window light from the left.")
g("P03", "3:4", R("1988908934_2", "1988908934_1"), "the red-and-white shemagh fabric: same red houndstooth pattern, same white border with red stripes, same woven seal mark, same cotton weave",
  "Macro close-up of the fabric in soft natural folds filling the whole frame, 100mm macro lens, raking window light showing every thread; only the fabric in frame.")
g("P04", "3:4", R("1740470085_1", "1740470085_2"), f"the bright white Swiss cotton voile ghutra with its woven selvedge line, and {BOX}",
  "Top-down flat lay: the ghutra folded into a neat triangle in its open box on a plain deep green linen cloth, soft daylight.")
g("P05", "3:4", R("502827333_2", "502827333_1"), "the bright white ghutra (same drape and weight)",
  "An adult Saudi man in his late 30s wears this exact white ghutra in the classic Saudi style with a black agal and a white Saudi thobe; waist-up, side profile, plain light-grey seamless backdrop, soft window light; the ghutra is the focus.", WORN)
g("P06", "3:4", R("1664674203_1", "1664674203_2"), f"{BOX}, and the red-and-white Naqsh shemagh folded inside (same pattern, same red tone, same white border stripes)",
  "The open box on a plain dark walnut wood surface against a plain warm-grey backdrop, three-quarter view, 100mm lens, soft daylight.")
g("P07", "3:4", R("2124457749_6", "2124457749_1"), "the bright white Zumurrud shemagh with its tone-on-tone laser-cut geometric pattern",
  "Close-up of the fabric hanging in a soft curve against a plain light backdrop with soft backlight so the pattern shows clearly, 100mm macro lens; only the fabric in frame.")
g("P08", "3:4", R("1292393513_1"), "the soft lilac-white Japanese thobe fabric with its gold printed selvedge mark",
  "Top-down: the fabric folded in neat soft layers on a plain light oak surface, soft daylight, the gold selvedge print visible.")
g("P09", "3:4", R("1449104353_4", "1449104353_1", "1449104353_5"), "the Italian Super 140 wool with its fine pinstripe, same colours and sheen",
  "Four folded lengths of this wool stacked on a plain dark oak surface against a plain warm-grey backdrop, three-quarter view, 85mm lens, window light from the left.")
g("P10", "3:4", R("821325048_1", "821325048_3"), "the cream pashmina shawl with the navy embroidered paisley border and corner medallion",
  "An adult Saudi man in a white thobe and red shemagh stands with the shawl draped over his shoulders, seen at three-quarter back view against a plain warm-grey seamless backdrop; the embroidered shawl fills most of the frame.", WORN)
g("P11", "3:4", R("663088504_2", "663088504_1"), "the cream Al-Baidaa wool shawl with the navy embroidered border and medallion, shown clean without any pins",
  "The shawl folded neatly on a plain light stone surface, 45-degree overhead, soft daylight.")
g("P12", "3:4", R("672063087_1", "672063087_2"), "the open dark green gift box with its three glass perfume bottles, same caps, labels and arrangement",
  "The open box on a plain warm stone surface against a plain warm-beige backdrop, low three-quarter view, 85mm lens, soft daylight.")
g("P13", "3:4", R("265256366_2", "265256366_1", "265256366_3"), "the silver cufflinks (same shape, engraving and finish)",
  "Close-up of an adult man's hands fastening one cufflink on the French cuff of a white thobe sleeve, plain light backdrop, 100mm macro, hands complete and natural; nothing else in frame.")
g("P14", "3:4", R("892978768_2", "892978768_1"), "the Wathir Italian undershirt and its kraft gift box with the botanical print and window, same printed marks",
  "The open box with the white undershirt folded inside on a plain cream surface, overhead three-quarter view, soft window light.")
g("P15", "3:4", R("1113769137_1", "1113769137_4"), "the black Siraj Attar agal (same cord and double ring) resting on its dark green box with the gold-foil seal",
  f"Top-down: the agal on its green box {STONE}, soft daylight.")
g("P16", "3:4", R("1292393513_1", "1668806182_1", "1449104353_4", "1029444903_1", "563952490_1"),
  "the five fabrics with their true colours, weave and printed selvedges: lilac-white Japanese fabric with gold print, white Korean fabric with gold print, Italian pinstripe wool, solid navy English wool, cream-white Italian voile",
  "The five fabrics as neatly folded lengths stacked in a column on a plain light oak surface against a plain warm-grey backdrop, three-quarter view, 85mm lens, window light.")
# ---- catalogue images (4:3 for the poster photo panel) ----
g("C03", "4:3", R("1604079293_1", "1604079293_2"), "the light grey box printed with the word AUDEMAR (exactly these seven letters) and its mark, and the red-and-white Audemar 4 shemagh folded inside with a corner draped out",
  f"The box {STONE}, three-quarter high angle, 100mm lens, window light.")
g("C04", "4:3", R("1949762576_1", "1949762576_2"), f"{BOX}, and the red-and-white European shemagh folded inside with a corner draped out",
  f"The box {STONE}, three-quarter high angle, 100mm lens, window light.")
g("C05", "4:3", R("1471159401_1", "1471159401_2", "1471159401_3"), f"{BOX}, and the red-and-white Hafawa shemagh folded inside with a corner draped out",
  "The box on a plain light wood surface against a plain warm-white backdrop, three-quarter high angle, 100mm lens, window light.")
g("C06", "4:3", R("1546150268_1", "1546150268_3", "1546150268_4"), f"{BOX}, and the classic red Al-Wisam 26 shemagh folded inside with a corner draped out",
  f"The box {STONE}, three-quarter high angle, 100mm lens, window light.")
g("C08", "4:3", R("1029444903_1"), "the solid navy English wool, same colour and fine twill sheen",
  "Three folded lengths stacked on a plain dark oak surface against a plain warm-grey backdrop, three-quarter view, 85mm lens, window light.")
# ---- campaign images ----
g("K02", "9:16", R("966965063_2", "966965063_1"), "the red-and-white Yaqoot shemagh (same pattern and border) and the black agal",
  "Vertical portrait: an adult Saudi man wears this exact shemagh in the classic Saudi style with the black agal and a white Saudi thobe, chest-up, looking slightly off camera, plain warm-beige seamless backdrop, soft natural light.", WORN)
g("K04a", "1:1", R("966965063_2", "966965063_1"), "the red-and-white Yaqoot shemagh and the black agal",
  "Square portrait: an adult Saudi man wears this exact shemagh with the black agal and a white Saudi thobe, chest-up, front three-quarter view, plain warm-beige seamless backdrop, soft window light.", WORN)
g("K05", "1:1", R("1740470085_2", "1740470085_1"), "the bright white Swiss cotton voile ghutra with its woven selvedge",
  "Close-up: the ghutra laid flat on a plain white ironing surface, an adult man's hand in a white thobe sleeve guiding a steam iron across it, light steam, 45-degree view, soft daylight; nothing else in frame.")
g("K06", "3:4", R("966965063_1", "663088504_2", "189452492_1", "1113769137_1"),
  "the four products with their true colours, patterns and logos: the green box with the red-and-white Yaqoot shemagh, the cream Al-Baidaa shawl with navy embroidery (no pins), the Attar 3 glass perfume bottle with its label, and the black agal on its green box",
  "Top-down flat lay: the four products evenly spaced on a plain deep green linen cloth, soft daylight, empty linen at the top for text.")
g("K08", "3:4", R("966965063_1", "1292393513_1"), f"{BOX} holding the red-and-white shemagh, and the lilac-white thobe fabric with gold selvedge",
  "The open shemagh box and a folded length of the fabric side by side on a plain worn wooden counter against a plain dark backdrop, soft daylight from the left, three-quarter view, 85mm lens.")
g("K09", "3:4", R("1381142749_3", "1381142749_1"), "the black Siraj Attar gift box with gold seal holding the folded red-and-white shemagh, the perfume bottle and the cufflinks, same arrangement",
  "The open gift box on a plain warm stone surface against a plain warm-beige backdrop, three-quarter high angle, 85mm lens, soft daylight.")

json.dump(J, open("plan/gen_manifest_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(J), "jobs")
