"""Builds plan/gen_manifest.json: one Higgsfield job per distinct image. Run from the project root."""
import json, glob


def R(*ids):
    return [glob.glob(f"data/images/{i}.*")[0].replace("\\", "/") for i in ids]


LIGHT = ("House light: late-afternoon Najdi sun, warm and low, raking from camera-left, soft long shadows, gentle fill; "
         "warm-neutral grade, creamy highlights, deep greens, natural contrast, true-to-life colour. "
         "Photorealistic, tack sharp, editorial still life. No added text or letters anywhere.")
NIGHT = ("House night light: warm lantern and firelight from camera-left, deep blue ambient, soft shadows; "
         "warm-neutral grade, true-to-life colour. Photorealistic, tack sharp. No added text or letters anywhere.")
CAT = "The product sits centred with generous breathing room on all sides, nothing cropped. "
J = []


def g(id, model, q, ar, refs, prompt):
    p = {"aspect_ratio": ar, "resolution": "2k"}
    if model == "gpt_image_2_5":
        p["quality"] = q
    J.append({"id": id, "model": model, "prompt": prompt, "images": refs, "params": p})


# ---------- product shots (high quality) ----------
g("P02", "gpt_image_2_5", "high", "4:5", R("966965063_1", "966965063_2"),
  "Keep EXACTLY the product from the references: the dark green Siraj Attar box with its gold-foil round seal and gold Arabic lettering, the lid, and the red-and-white Yaqoot shemagh (same red houndstooth field, same white border with red stripes, same fringe) folded in the box with one corner draped out. New scene: the open box rests on a honed travertine ledge beside a Najdi mud-brick wall; camera three-quarter high angle, 50mm. " + LIGHT + " Clean empty travertine and wall in the top third for later typography.")
g("P03", "gpt_image_2_5", "high", "4:5", R("1988908934_2", "1988908934_1"),
  "Keep EXACTLY the red-and-white shemagh fabric from the references: same red houndstooth pattern, same white border with red stripes, same woven seal mark in the corner, same weave. New image: a macro texture study, the fabric gathered in soft sculptural folds filling the whole frame, camera low and close at 30 degrees, 100mm macro, the cotton weave and every thread visible. " + LIGHT + " Folds catch the raking light on their ridges.")
g("P04", "gpt_image_2_5", "high", "4:5", R("1740470085_1", "1740470085_2"),
  "Keep EXACTLY the products from the references: the bright white Swiss cotton voile ghutra (with its subtle woven selvedge line) and the dark green box with the gold-foil round seal. New scene: overhead flat lay, perfectly top-down; the ghutra folded into a crisp triangle on a deep green linen cloth, the open green box beside it at a slight angle, a few dried palm fronds at the edge of frame. " + LIGHT + " Generous empty green linen in the upper third for later typography.")
g("P05", "gpt_image_2_5", "high", "4:5", R("502827333_2", "502827333_1"),
  "Keep EXACTLY the white ghutra from the references (bright white Swiss cotton, same drape and weight). A DIFFERENT adult Saudi man in his late 30s, neatly trimmed beard, calm and focused, wears the white ghutra in the classic Saudi style with a black agal and a crisp white Saudi thobe with a plain collar. Side profile, waist-up, 85mm; he stands by floor-to-ceiling glass in a modern Riyadh business district in the morning, city towers softly out of focus behind. Soft morning daylight from camera-left, warm-neutral grade, natural skin texture, true-to-life colour. Photorealistic, tack sharp. No added text. Clean soft background on the right third for typography.")
g("P06", "gpt_image_2_5", "high", "4:5", R("1664674203_1", "1664674203_2"),
  "Keep EXACTLY the products from the references: the dark green box with gold-foil seal and the red-and-white Naqsh shemagh (same pattern, same red tone, same white border stripes). New scene: low-angle hero, camera at table height, 35mm; the shemagh folded in its open box on a carved dark wooden majlis chest, a hand-woven Sadu cushion in red, black and cream softly behind, a brass lantern glowing. " + NIGHT + " Dark calm space above the box for typography.")
g("P07", "gpt_image_2_5", "high", "4:5", R("2124457749_6", "2124457749_1"),
  "Keep EXACTLY the white Zumurrud shemagh from the references: bright white cotton with its tone-on-tone laser-cut geometric pattern. New image: a backlit macro, the fabric hanging in a soft curve in front of a sunlit window so the laser pattern glows through the cotton; camera 45 degrees, 100mm macro, shallow depth of field. Warm late-afternoon sun from behind and camera-left, creamy highlights, warm-neutral grade. Photorealistic, tack sharp on the pattern. No added text.")
g("P08", "gpt_image_2_5", "high", "4:5", R("1292393513_1"),
  "Keep EXACTLY the fabric from the reference: the soft lilac-white Japanese thobe fabric with its gold printed selvedge mark. New scene: perfectly top-down on a tailor's wooden cutting table; the fabric unrolled from its bolt across the table, brass tailor's scissors, a cloth measuring tape, a sliver of white tailor's chalk, and a hand-drawn paper thobe pattern at the edge. " + LIGHT + " Clean empty wood in the top quarter for typography.")
g("P09", "gpt_image_2_5", "high", "4:5", R("1449104353_4", "1449104353_1", "1449104353_5"),
  "Keep EXACTLY the fabric from the references: the Italian Super 140 wool with its fine pinstripe, same colours and sheen. New scene: five folded lengths of this wool stacked on a dark oak shelf in an old fabric merchant's shop, three-quarter view from slightly below, 50mm, warm daylight raking from a side window at camera-left, soft long shadows, dust motes in the light. Warm-neutral grade, deep shadows, true-to-life colour. Photorealistic, tack sharp. No added text. Calm dark wall above the shelf for typography.")
g("P10", "gpt_image_2_5", "high", "4:5", R("821325048_1", "821325048_3"),
  "Keep EXACTLY the pashmina shawl from the references: cream wool with the navy embroidered paisley border and corner medallion, same motif and colours. An adult Saudi man in a white Saudi thobe and red shemagh sits beside a desert campfire in winter at blue hour, the shawl draped over his shoulders; camera behind his shoulder at a three-quarter back view, 50mm, his face turned toward the fire in soft profile. Dunes and a deep blue sky behind. " + NIGHT + " Dark sky in the top third for typography.")
g("P11", "gpt_image_2_5", "high", "4:5", R("663088504_2", "663088504_1"),
  "Keep EXACTLY the Al-Baidaa shawl from the references: cream wool with the navy embroidered border and medallion, same motif. Show it clean, without any pins. New scene: a winter desert camp, camera 45 degrees overhead, the shawl folded neatly on a woven camel-hair rug beside a brass dallah and two small finjan cups, embers of a fire glowing at the frame edge. " + NIGHT + " Empty rug space in the upper third for typography.")
g("P12", "gpt_image_2_5", "high", "4:5", R("672063087_1", "672063087_2"),
  "Keep EXACTLY the product from the references: the open dark green Siraj Attar gift box with its three glass perfume bottles, same caps, same labels, same arrangement. New scene: low-angle hero at tray height, 50mm; the box on a polished brass tray on a majlis floor rug, a small incense burner releasing a thin ribbon of smoke behind, a carved wooden door softly out of focus. " + NIGHT + " Calm dark space above for typography.")
g("P13", "gpt_image_2_5", "high", "4:5", R("265256366_2", "265256366_1", "265256366_3"),
  "Keep EXACTLY the silver cufflinks from the references (same shape, engraving and finish). New image: close-up of an adult Saudi man's hands fastening one cufflink on the French cuff of a crisp white thobe sleeve, the second cufflink resting on a dark green box lid below; camera at 30 degrees, 100mm macro, only hands and cuff in frame, hands complete and natural. " + LIGHT + " Clean soft background in the upper half for typography.")
g("P14", "gpt_image_2_5", "high", "4:5", R("892978768_2", "892978768_1"),
  "Keep EXACTLY the product from the references: the Wathir Italian undershirt and its kraft gift box with the botanical print and window, same printed marks. New scene: overhead three-quarter view on a cream linen surface, the box open with the soft white undershirt folded inside, a sprig of cotton bolls beside it. Soft late-morning window light from camera-left, gentle shadows, warm-neutral grade, clean and calm. Photorealistic, tack sharp. No added text. Clean empty linen in the upper third for typography.")
g("P15", "gpt_image_2_5", "high", "4:5", R("1113769137_1", "1113769137_4", "966965063_1"),
  "Keep EXACTLY the products from the references: the black Siraj Attar agal (same cord and double ring) and its dark green box with the gold-foil seal, and the red-and-white Yaqoot shemagh pattern. New scene: perfectly top-down; the agal resting on its green box, a folded corner of the red-and-white shemagh entering from the lower edge, on a honed travertine surface. " + LIGHT + " Empty travertine in the upper third for typography.")
g("P16", "nano_banana_pro", None, "4:5", R("1292393513_1", "1668806182_1", "1449104353_4", "1029444903_1", "563952490_1"),
  "Keep EXACTLY the five fabrics from the references, each with its true colour, weave and printed selvedge: the lilac-white Japanese fabric with gold selvedge print, the white Korean fabric with gold selvedge print, the Italian pinstripe wool, the solid navy English wool, the cream-white Italian voile. New scene: a fabric library: the five fabrics as neatly folded lengths stacked in a staggered column on a dark oak table in an old merchant's shop, camera three-quarter at 30 degrees, 50mm. " + LIGHT + " Calm space above the stack for typography.")
# ---------- catalogue images (5:4 for the poster's photo panel) ----------
g("C03", "gpt_image_2_5", "medium", "5:4", R("1604079293_1", "1604079293_2"),
  "Keep EXACTLY the product from the references: the light grey box with its printed mark and the red-and-white Audemar 4 shemagh (same pattern and border) folded in it with a corner draped out. New scene: the box on a honed travertine ledge against a warm mud-plaster wall, three-quarter high angle, 50mm. " + CAT + LIGHT)
g("C04", "gpt_image_2_5", "medium", "5:4", R("1949762576_1", "1949762576_2"),
  "Keep EXACTLY the product from the references: the dark green box with gold-foil seal and the red-and-white European shemagh (same pattern, same border stripes) folded in it with a corner draped out. New scene: on a honed travertine ledge against a warm mud-plaster wall, three-quarter high angle, 50mm. " + CAT + LIGHT)
g("C05", "gpt_image_2_5", "medium", "5:4", R("1471159401_1", "1471159401_2", "1471159401_3"),
  "Keep EXACTLY the product from the references: the dark green box with gold-foil seal and the red-and-white Hafawa shemagh (same pattern, same border) folded in it with a corner draped out. New scene: on a palm-wood bench against a warm mud-plaster wall, three-quarter high angle, 50mm. " + CAT + LIGHT)
g("C06", "gpt_image_2_5", "medium", "5:4", R("1546150268_1", "1546150268_3", "1546150268_4"),
  "Keep EXACTLY the product from the references: the dark green box with gold-foil seal and the classic red Al-Wisam 26 shemagh (same pattern, same red tone, same border) folded in it with a corner draped out. New scene: on a honed travertine ledge against a warm mud-plaster wall, three-quarter high angle, 50mm. " + CAT + LIGHT)
g("C08", "gpt_image_2_5", "medium", "5:4", R("1029444903_1"),
  "Keep EXACTLY the fabric from the reference: the solid navy English wool, same colour and fine twill sheen. New scene: three folded lengths of this navy wool stacked on a dark oak tailor's table next to brass scissors and a cloth measuring tape, three-quarter view at 30 degrees, 50mm. " + CAT + LIGHT)
# ---------- campaign images ----------
g("K05", "gpt_image_2_5", "medium", "1:1", R("1740470085_2", "1740470085_1"),
  "Keep EXACTLY the bright white Swiss cotton voile ghutra from the references, with its subtle woven selvedge. New scene: the ghutra laid flat on a padded ironing board, an adult man's hand guiding a modern steam iron across it, a soft cloud of steam rising; camera 45 degrees, 50mm, only the hand and forearm in a white thobe sleeve visible. " + LIGHT)
g("K06", "nano_banana_pro", None, "4:5", R("966965063_1", "663088504_2", "189452492_1", "1113769137_1"),
  "Keep EXACTLY the four products from the references with their true colours, patterns and logos: the dark green box with the red-and-white Yaqoot shemagh, the cream Al-Baidaa wool shawl with navy embroidery, the Attar 3 glass perfume bottle with its label, and the black agal on its green box. New scene: a winter set, perfectly top-down, the four products arranged with even spacing on a deep green linen cloth, a few dried palm fronds at one edge. " + LIGHT + " Empty linen in the upper third for typography.")
g("K08", "gpt_image_2_5", "high", "4:5", R("966965063_1", "1292393513_1"),
  "Keep EXACTLY the products from the references: the dark green box with gold-foil seal holding the red-and-white shemagh, and the lilac-white thobe fabric with gold selvedge. New scene: inside an old merchant's fabric shop in historic Jeddah, a worn wooden counter in the foreground with the open shemagh box and a bolt of the fabric unrolled, behind it carved wooden roshan shutters with sunlight slicing through, shelves of folded fabric in soft focus; three-quarter view, 35mm. " + LIGHT + " Calm shadowed area at the top for typography.")
g("K09", "gpt_image_2_5", "medium", "4:5", R("1381142749_3", "1381142749_1"),
  "Keep EXACTLY the product from the references: the black Siraj Attar gift box with gold seal, holding the folded red-and-white shemagh, the perfume bottle and the cufflinks, same arrangement. New scene: an Eid morning majlis, the open gift box on a low carved wooden table, a brass dallah and a plate of dates softly out of focus behind; three-quarter high angle, 50mm. " + LIGHT + " Clean space in the upper third for typography.")

json.dump(J, open("plan/gen_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(J), "jobs")
