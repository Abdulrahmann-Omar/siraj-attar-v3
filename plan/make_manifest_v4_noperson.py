"""v4: client hard constraint 'no characters': every image with a person or hands is replaced by a product-only photograph.
Same constraints as v2: realistic, product as hero, minimal set. Engine: seedream_5_0_flash."""
import json, glob


def R(*ids):
    return [glob.glob(f"data/images/{i}.*")[0].replace("\\", "/") for i in ids]


RULE = ("Real commercial product photograph, not a render: natural daylight, realistic soft contact shadow, true colours, real material texture, no CGI look. "
        "Product only: no people, no hands, no mannequin, no faces anywhere in the image. No added text or letters. "
        "Minimal set: only the product on one plain real surface against a plain seamless backdrop; no props. The product fills about two-thirds of the frame, fully visible.")
J = []


def g(id, ar, refs, keep, scene):
    J.append({"id": id, "model": "seedream_5_0_flash",
              "prompt": f"Keep the product EXACTLY as in the reference photos: {keep}. {scene} {RULE}",
              "images": refs, "params": {"aspect_ratio": ar, "resolution": "2k"}})


YQ = "the red-and-white Yaqoot shemagh (same red houndstooth field, same white border with red stripes, same fringe) and the black Siraj Attar agal (same cord, double ring)"
g("R4_P01", "3:4", R("966965063_1", "966965063_2", "1113769137_1"), YQ,
  "The shemagh folded into a neat triangle with the black agal resting on top of it, on a plain honed beige stone surface against a plain warm-beige backdrop, three-quarter high angle, 85mm lens.")
g("R4_P05", "3:4", R("502827333_1", "502827333_3"), "the bright white Classic ghutra, Swiss cotton, with its fine woven border",
  "The ghutra folded into a crisp triangle, standing in its open dark green box with the gold-foil seal, on a plain light-grey stone surface against a plain light-grey backdrop, three-quarter view, 100mm lens, soft window light.")
g("R4_P10", "3:4", R("821325048_1", "821325048_3"), "the cream pashmina shawl with the navy embroidered paisley border and corner medallion",
  "The shawl draped in soft vertical folds over a plain warm-grey seamless backdrop edge so the embroidered border and medallion face the camera, 85mm lens.")
g("R4_P13", "3:4", R("265256366_2", "265256366_1", "265256366_3"), "the silver knot cufflinks (same shape, engraving and finish)",
  "Macro: one cufflink fastened through the folded French cuff of a white thobe sleeve laid flat on a plain light surface, the second cufflink lying beside it, 100mm macro lens, soft window light.")
g("R4_K02", "9:16", R("966965063_2", "966965063_1", "1113769137_1"), YQ,
  "Vertical: the shemagh hanging in long natural folds from the top of the frame so the full pattern and striped border show, the black agal resting on a plain stone ledge below it, plain warm-beige backdrop, 85mm lens.")
g("R4_K03", "9:16", R("502827333_1", "502827333_3"), "the bright white Classic ghutra, Swiss cotton, with its fine woven border",
  "Vertical: the white ghutra hanging in long soft folds against a plain light-grey seamless backdrop, the woven border visible, soft window light, 85mm lens.")
g("R4_K04a", "1:1", R("966965063_1", "1113769137_1", "1292393513_1", "672063087_1", "265256366_2"),
  "the five products with their true colours, patterns and logos: the green box with the red-and-white Yaqoot shemagh, the black agal on its green box, the lilac-white Japanese fabric folded flat, the green perfume box with three bottles, and the silver knot cufflinks",
  "Top-down flat lay: the five products arranged in a clean grid with even spacing on a plain warm-beige surface, soft daylight.")
g("R4_K05", "1:1", R("1740470085_2", "1740470085_1"), "the bright white Swiss cotton voile ghutra with its woven selvedge",
  "The ghutra laid flat on a plain white ironing surface with a modern steam iron resting on it, a light wisp of steam, 45-degree view, soft daylight.")
g("R4_K07", "9:16", R("821325048_1", "821325048_3"), "the cream pashmina shawl with the navy embroidered paisley border and corner medallion",
  "Vertical: the shawl hanging in long soft folds against a plain warm-grey seamless backdrop, the embroidered border and medallion facing the camera, 85mm lens.")
json.dump(J, open("plan/gen_manifest_v4.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(J), "jobs")
