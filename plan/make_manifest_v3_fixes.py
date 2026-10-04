"""Re-rolls after QA of v2: correct agal placement on worn shots (nano_banana_pro), garbled box lettering (P15),
and fabric shown as a sewn thobe instead of uncut fabric (P08, K08). Same hard constraints: realistic, product as hero, minimal set."""
import json, glob


def R(*ids):
    return [glob.glob(f"data/images/{i}.*")[0].replace("\\", "/") for i in ids]


WORN = ("Real editorial photograph, not a render: natural skin texture, real fabric folds, soft natural daylight, true colours, 85mm lens. "
        "Plain warm-beige seamless backdrop, nothing else in frame. The man is an adult Saudi, not a celebrity. No added text or letters. "
        "Correct Saudi styling: the black agal sits HIGH on the crown of the head, level, well above the forehead; the shemagh drapes straight down on both sides of the face, "
        "framing it neatly, both ends falling over the chest; a crisp white Saudi thobe with a plain collar.")
MIN = ("Real commercial photograph, natural daylight, realistic soft contact shadow, true colours, real material texture, no CGI look, no added text. "
       "Minimal set: only the product on one plain real surface against a plain seamless backdrop; no props, no extra objects. The product fills about two-thirds of the frame.")
J = []


def g(id, model, ar, refs, prompt):
    p = {"aspect_ratio": ar, "resolution": "2k"}
    J.append({"id": id, "model": model, "prompt": prompt, "images": refs, "params": p})


YQ = "Keep EXACTLY the red-and-white Yaqoot shemagh from the references (same red houndstooth field, same white border with red stripes) and the black agal."
g("R2_P01", "nano_banana_pro", "4:5", R("966965063_2", "966965063_3", "966965063_1"),
  YQ + " An adult Saudi man in his 30s wears it; waist-up, three-quarter view, calm confident expression; the shemagh pattern is crisp and fills much of the frame. " + WORN)
g("R2_K02", "nano_banana_pro", "9:16", R("966965063_2", "966965063_3", "966965063_1"),
  YQ + " Vertical portrait: an adult Saudi man wears it, chest-up, looking slightly off camera. " + WORN)
g("R2_K04a", "nano_banana_pro", "1:1", R("966965063_3", "966965063_2", "966965063_1"),
  YQ + " Square portrait: an adult Saudi man wears it, chest-up, front three-quarter view. " + WORN)
g("R2_P15", "nano_banana_pro", "4:5", R("1113769137_1", "1113769137_4"),
  "Keep EXACTLY the products from the references: the black Siraj Attar agal (same cord and double ring) resting on its dark green box, and the box's gold-foil round calligraphy seal and its printed lettering exactly as in the reference. "
  "Top-down on a plain honed beige stone surface, soft daylight. " + MIN)
FAB = "It is an uncut length of fabric sold by the metre, NOT a garment: no collar, no buttons, no seams, no sleeves."
g("R2_P08", "seedream_5_0_flash", "3:4", R("1292393513_1"),
  "Keep EXACTLY the fabric from the reference: the soft lilac-white Japanese thobe fabric with its gold printed selvedge mark. " + FAB +
  " Top-down: the fabric folded into a neat flat stack of soft layers on a plain light oak surface, the gold selvedge print visible along one edge. " + MIN)
g("R2_K08", "seedream_5_0_flash", "3:4", R("966965063_1", "1292393513_1"),
  "Keep EXACTLY the products from the references: the dark green box with its gold-foil round seal holding the red-and-white shemagh, and the lilac-white thobe fabric with its gold selvedge print. "
  + FAB + " The open shemagh box and a neatly folded flat stack of the uncut fabric side by side on a plain worn wooden counter against a plain dark backdrop, soft daylight from the left, three-quarter view, 85mm lens. " + MIN)
json.dump(J, open("plan/gen_manifest_v3_fixes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(J), "jobs")
