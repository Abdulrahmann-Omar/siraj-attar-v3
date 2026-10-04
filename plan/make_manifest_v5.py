"""v5: every poster image regenerated at the EXACT aspect of its poster frame so the whole product shows (no crop):
4:5 posters use a 4:3 photo panel (1080x810), 1:1 posters and K10 use a 3:2 panel (1080x720).
Also: Al-Baidaa shawl removed everywhere (P11 -> Attar 3 perfume, C07 -> Korean fabric 974, K06 without the shawl).
Rules: realistic product photograph, product only (no people/hands), minimal set. Engine: seedream_5_0_flash."""
import json, glob


def R(*ids):
    return [glob.glob(f"data/images/{i}.*")[0].replace("\\", "/") for i in ids]


RULE = ("Real commercial product photograph, not a render: natural daylight, realistic soft contact shadow, true colours, real material texture, no CGI look. "
        "Product only: no people, no hands, no mannequin. No added text or letters. "
        "Minimal set: only the product on one plain real surface against a plain seamless backdrop; no props. "
        "The whole product is fully visible and centred with a clear margin of empty space on every side; nothing touches or crosses the frame edges.")
J = []


def g(id, ar, refs, keep, scene):
    J.append({"id": id, "model": "seedream_5_0_flash", "prompt": f"Keep the product EXACTLY as in the reference photos: {keep}. {scene} {RULE}",
              "images": refs, "params": {"aspect_ratio": ar, "resolution": "2k"}})


BOX = "the dark green box with its gold-foil round seal and gold lettering"
STONE = "on a plain honed beige stone surface against a plain warm-white backdrop"
YQ = "the red-and-white Yaqoot shemagh (same red houndstooth field, same white border with red stripes, same fringe)"
# ---- 4:3 images for 4:5 posters ----
g("R5_C01", "4:3", R("966965063_1", "966965063_2"), f"{BOX}, and {YQ} folded inside with one corner draped out", f"The open box {STONE}, three-quarter high angle, 85mm lens, window light from the left.")
g("R5_C02", "4:3", R("1740470085_1", "1740470085_2"), f"the bright white Swiss cotton voile ghutra with its woven selvedge line, and {BOX}", "Top-down: the ghutra folded into a neat triangle in its open box on a plain deep green linen cloth, soft daylight.")
g("R5_C07", "4:3", R("1668806182_1", "1668806182_2"), "the white Korean thobe-length fabric with its gold printed selvedge mark and logo, same weave and sheen",
  "The fabric folded flat into neat rectangular layers like a cloth merchant's bolt, the gold selvedge print visible along the top edge, on a plain light oak surface against a plain warm-white backdrop, three-quarter view, 85mm lens. It is plain cloth only; there is no clothing anywhere in the image.")
g("R5_C09", "4:3", R("892978768_2", "892978768_1"), "the Wathir Italian undershirt and its kraft gift box with the botanical print and window, same printed marks", "The box standing upright, slightly angled, on a plain cream surface against a plain warm-white backdrop, soft window light, 85mm lens.")
g("R5_K01", "4:3", R("966965063_1", "966965063_2", "1113769137_1"), f"{YQ} and the black Siraj Attar agal (same cord, double ring)", f"The shemagh folded into a neat triangle with the black agal resting on top, {STONE}, three-quarter high angle, 85mm lens.")
g("R5_K06", "4:3", R("966965063_1", "189452492_1", "1113769137_1", "265256366_2"),
  "the four products with their true colours, patterns and logos: the green box with the red-and-white Yaqoot shemagh, the Attar 3 glass perfume bottle with its label, the black agal on its green box, and the silver knot cufflinks",
  "Top-down flat lay: the four products evenly spaced in a clean row-and-column grid on a plain deep green linen cloth, soft daylight.")
g("R5_K08", "4:3", R("966965063_1", "1292393513_1"), f"{BOX} holding the red-and-white shemagh, and the lilac-white Japanese fabric with its gold selvedge print",
  "The open shemagh box and a neatly folded flat stack of the plain fabric side by side on a plain worn wooden counter against a plain dark backdrop, soft daylight from the left, three-quarter view, 85mm lens. The fabric is plain cloth only; there is no clothing anywhere in the image.")
g("R5_K09", "4:3", R("1381142749_3", "1381142749_1"), "the black Siraj Attar gift box with gold seal holding the folded red-and-white shemagh, the perfume bottle and the cufflinks, same arrangement",
  "The open gift box on a plain warm stone surface against a plain warm-beige backdrop, three-quarter high angle, 85mm lens, soft daylight.")
# ---- 3:2 images for 1:1 posters and K10 ----
g("R5_K04a", "3:2", R("966965063_1", "1113769137_1", "1292393513_1", "672063087_1", "265256366_2"),
  "the five products with their true colours, patterns and logos: the green box with the red-and-white Yaqoot shemagh, the black agal on its green box, the lilac-white Japanese fabric folded flat, the green perfume box with three bottles, and the silver knot cufflinks",
  "Top-down flat lay: the five products arranged in one clean row with even spacing on a plain warm-beige surface, soft daylight.")
g("R5_K04b", "3:2", R("1113769137_1", "1113769137_4"), "the black Siraj Attar agal (same cord and double ring) resting on its dark green box with the gold-foil round seal and its printed lettering exactly as in the reference",
  f"Top-down: the agal on its box {STONE}, soft daylight.")
g("R5_K04c", "3:2", R("1292393513_1"), "the soft lilac-white Japanese cotton-blend fabric with its gold printed selvedge mark",
  "The fabric folded flat into neat rectangular layers like a cloth merchant's bolt on a plain light oak surface, the gold selvedge print visible, three-quarter view, soft daylight. It is plain cloth only; there is no clothing anywhere in the image.")
g("R5_K04d", "3:2", R("672063087_1", "672063087_2"), "the open dark green gift box with its three glass perfume bottles, same caps, labels and arrangement",
  "The open box on a plain warm stone surface against a plain warm-beige backdrop, three-quarter view, 85mm lens, soft daylight.")
g("R5_K04e", "3:2", R("265256366_2", "265256366_1", "265256366_3"), "the silver knot cufflinks (same shape, engraving and finish)",
  "The pair of cufflinks resting on the folded French cuff of a white thobe sleeve laid flat on a plain light surface, 100mm macro lens, soft window light.")
g("R5_K05a", "3:2", R("1740470085_2", "1740470085_1"), "the bright white Swiss cotton voile ghutra with its woven selvedge",
  "The ghutra laid flat on a plain white ironing surface with a modern steam iron resting on it, a light wisp of steam, 45-degree view, soft daylight.")
g("R5_K05b", "3:2", R("1740470085_1", "1740470085_2"), f"the bright white Swiss cotton voile ghutra with its woven selvedge line, and {BOX}",
  "Top-down: the ghutra folded into a neat triangle beside its open box on a plain deep green linen cloth, soft daylight.")
g("R5_K10", "3:2", R("1292393513_1", "1668806182_1", "1449104353_4", "1029444903_1", "563952490_1"),
  "the five fabrics with their true colours, weave and printed selvedges: lilac-white Japanese fabric with gold print, white Korean fabric with gold print, Italian pinstripe wool, solid navy English wool, cream-white Italian voile",
  "The five fabrics as neatly folded flat lengths stacked in one column on a plain light oak surface against a plain warm-grey backdrop, three-quarter view, 85mm lens, window light. Plain cloth only; no clothing anywhere.")
# ---- product shot replacing the shawl (3:4, exported 4:5) ----
g("R5_P11", "3:4", R("189452492_1", "189452492_2", "189452492_3"), "the Attar 3 glass perfume bottle with its cap and label exactly as in the reference",
  f"The bottle standing upright {STONE}, eye-level, 100mm lens, soft window light from the left.")
json.dump(J, open("plan/gen_manifest_v5.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(J), "jobs")
