# Review of the previous Siraj Attar pitch (creative-director pass)

Inputs: `ref/old_proposal/` (24 pages, re-rendered at 2x in `research/old_renders/pNN.png`), the old assets folder `everyside-review/pdf/assets/siraj/`, `ref/FEEDBACK.md`, the 2026-09-28 catalogue scrape, and the old render source (opened read-only).
Evidence crops are in `research/old_renders/crops/`. Font specimens are in `research/old_renders/fontcheck/`.
Page numbers: p1–p12 are the English edition and p13–p24 the Arabic edition (the same pages mirrored, so p1 = p13, p4 = p16, and so on).

**Summary.** The thinking was right: a clear problem, the heritage line, a catalogue system and the scenario idea. The finish was not. Four things lost the room:
1. The client's logo was a 220 px tile on the cover.
2. Images were visibly composited.
3. "ر.س" appeared on every price, and the prices were probably shown without VAT.
4. The "how" was a software screenshot instead of a method.

v3 keeps the strategy and the poster typeface. It rebuilds everything else to measurable gates. A consolidated checklist is in section 7.

---

## 1. Feedback point by point: where it happens, what is wrong, the v3 rule

### G1. "The customer's logo must stand out on the first page … 'made specifically for you'"
- **Where:** p1 (English cover), p13 (Arabic cover), the footer of every page, and every poster.
- **What is wrong:**
  - The logo is `mark.png`, a 220×210 px RGB raster on a near-white #F8F8F8 background, so it has no transparency. It sits on the cream page as a white tile, 84.75 pt wide on an 842 pt page. That is **10.1 % of page width**, and the round mark inside it is only about **3 % of page width**. It reads as pasted.
  - The only nod to the client is the eyebrow "PREPARED FOR M. SIRAJ ATTAR & BROS" at **9 pt**, next to a 40 pt title.
  - Nothing says "made specifically for you".
  - The cover hero is the weakest composite in the set (see 2.1).
  - The footer gives Everyside equal billing ("Everyside × M. Siraj Attar & Bros", 7.5 pt).
- **v3 rules:**
  1. The client logo on the cover is **≥ 18 % of page width** (≥ 152 pt on an 842 pt A4-landscape page), on its own solid field (brand green ≈ #024339 or cream ≈ #F5F1E9). Clear space must be **≥ 50 % of the logo height** on every side. No tile, frame or drop shadow.
  2. The logo source is vector (SVG) or a transparent PNG at least 2000 px wide. The 220 px `mark.png` is banned.
  3. On a dark field, use the brand's own reversed lockup (gold foil on green, exactly as printed on the shemagh box). Never use the green wordmark on a dark ground.
  4. The cover carries the line *"Made specifically for M. Siraj Attar & Bros"* and its Arabic counterpart *"صُمِّم خصيصاً لمحمد سراج عطار وأخويه"*. It is set at **≥ 16 pt** (≥ 40 % of the title size) and is visible without scrolling.
  5. The Everyside mark appears only in the bottom corner and is **≤ 1/3 of the client logo's width**.
  6. Put the Arabic edition first, or ship it as its own PDF. A Saudi family business should not have to reach "page 13" for its own language.
  7. The client logo appears on every page (≥ 22 pt high) and in every asset. It must have ≥ 3:1 contrast against its local ground (see 2.1: the old logo measured 1.27:1).

### G2. "Images are critical … bad crops, wrong transparencies, poor contrast … unfinished-looking"
- **Where:** almost everywhere. The full inventory with file names is in section 2. The worst offenders shown to the client:
  - p1/p13: the cover composite.
  - p4/p16: floating socks, a pasted perfume box, and the shemagh box with its lid missing.
  - p5/p17: four unrelated visual styles in one campaign grid.
  - p6/p18: white ghutra on light grey.
  - p12/p24: the "لشتاك" poster with a swatch strip in place of a product.
- **v3 rule:** no image enters the deck or the asset set until it passes the image gate in section 7.B. The gate covers native resolution, product scale and margins, a contact shadow, one light recipe, product truth, contrast, and no text over the product.

### G3. "'ر.س' reads as not knowing the market"
- **Where:**
  - "ر.س" is on every price in every poster: `feed_01/02/04/07`, `stories_03/08`, `carousel_06-02..05`, and `product_pages_01..15`.
  - The deck repeats them on p3, p5, p6, p7, p8, p9, p10, p11, p12, p15, p17 to p24.
  - `realprod.jpg` writes "450 ريال" in body copy, a third format.
  - The source data carries "SAR".
- **Related defects found while checking:**
  - **Prices are probably ex-VAT.** Of the 85 scraped prices with decimals, 36 become whole numbers after ×1.15, and 44 get a retail-style ending (.00, .50 or .99). Before multiplying, only 13 look tidy. Examples: 17.39 → 20.00, 260.87 → 300.00, 52.17 → 60.00, 139.13 → 160.00, 201.74 → 232.00, 252.17 → 290.00. So `carousel_06-05` showed "17.39" while the customer most likely pays 20.00. This is also why the posters were full of odd decimals (157.82, 240.21, 221.73).
  - **Precision is inconsistent.** The same product shows "330" (`feed_01`) and "330.00" (`product_pages_06`), next to "595" and "92.00".
  - **Discounts are never stated.** The 52 % off on the زفير shemagh and 49 % on نقش 25 are left for the viewer to work out.
- **v3 rules:**
  1. Every price uses the official Saudi Riyal symbol (`brand/riyal.png` vectorised to SVG). It is never "ر.س", "SAR", "ريال" or "SR", in any asset, caption or deck page.
  2. The symbol matches the **lining-figure height** of the price font (Cairo digit height ±5 %), is the **same colour** as the figures, and is never faux-bolded.
  3. The symbol sits **left of the number with a 0.2–0.25 em gap** (SAMA usage guidance; confirm against SAMA's published guide before final). The number and symbol together are set as one LTR-isolated unit so the RTL layout cannot flip them.
  4. The price shown is the **VAT-inclusive price** the customer pays, checked against the live product page for every SKU before render. Whole riyals have no decimals ("20", not "20.00"). Fractional prices keep two decimals and are flagged to the client.
  5. When a compare-at price exists:
     - Show a discount badge ("-52 %" / "خصم 52 %").
     - The struck old price is **≥ 45 % of the new price's size**, with **≥ 4.5:1 contrast**. The old `feed_01` struck price measured **2.68:1**, white at partial opacity on a grey wall.
  6. Use Western digits (0–9) everywhere, as the old set did and as Saudi e-commerce does. Never mix them with Eastern Arabic digits.

### G4. "The Arabic font INSIDE the images works; the font in the PRESENTATION should be reconsidered"
- **Where:**
  - Inside the images: **Cairo** (section 6).
  - The Arabic deck pages p13 to p24: **Amiri Bold** for headlines and **IBM Plex Sans Arabic** for body text and labels.
  - The English pages: Playfair Display and Manrope.
- **What is wrong:**
  - Amiri is a classical, book-style Naskh. Next to the geometric Kufi-modern Cairo inside the posters it gives the deck a second, unrelated voice.
  - Amiri headlines are set too tight. On p24, the hamza of «أكتوبر» touches the descender of «حملتكم» on the line above (`crops/p24_head.png`).
  - Arabic display lines end with full stops («ما الذي يتغيّر؟» is fine; «من متجركم مباشرة.» is not).
  - **The PDF's Arabic text layer is corrupt.** Extracting text from the IBM Plex runs gives «رساج» instead of «سراج», «إىل» for «إلى», «سبتمرب», «مزيانية», «تزنيل» and «اإلنجلزيية». A client who copies a line, or searches the PDF, gets garbage.
- **v3 rules:**
  1. The Arabic face in the presentation is **Cairo**, the same family as the posters (variable, weights 200–1000, OFL):
     - Display text at 700–900 with **line-height ≥ 1.35**.
     - Body text at 300–400 with **line-height ≥ 1.6**.
     - Labels at 600.
  2. The Latin pair is **Inter**, the poster's own Latin face. The deck uses at most 2 type families in total. No Amiri, no IBM Plex Sans Arabic, no Playfair next to Arabic.
  3. No full stop at the end of an Arabic or English display headline. Line breaks fall at phrase boundaries, never inside a name or a verb phrase.
  4. **Text round-trip test:** running `pymupdf get_text()` on the final PDF must return these strings exactly: «محمد سراج عطار وأخويه», «إلى», «ميزانية», «تنزيل», «ثمانين», «الإنجليزية». If the test fails, rebuild with a different PDF path or font before delivery.

### S1. "80+ years of craft. Every post should show it." (keep)
See section 4.1.

### S2. Catalogue posters look good and polished (keep)
See section 4.2.

### S3. Scenario imagery is excellent, but every image must be finished to the concept's standard
See section 4.3, and section 2 for what "unfinished" meant in practice.

### Main question: "HOW?" and "Not clear the before and after at all, you have to dig deep"
- **Where:**
  - p3/p15 "Same product. A new story.": three panels.
  - p4/p16 "A photo studio, without the photoshoot": four before/after pairs.
  - p9/p21: the app screenshot, which was the only "how" offered.
  - p10/p22 "What changes.": a table plus a thumbnail.
- **What is wrong:**
  - On p3, step 02 looks almost the same as step 01: the same box, the same angle, the background changed from light grey to grey. The eye cannot see a transformation.
  - Step 02 is labelled "Everyside studio shot", which describes an internal tool, not a method.
  - On p4, each BEFORE is a 108 pt thumbnail and each AFTER a 174 pt crop of a different aspect ratio. Labels are 7.5 pt, and the pairs are stacked vertically. The "after" is often *less* legible than the "before": the shemagh is smaller, the fabric floats in a light beam, the lid is gone.
  - On p10, a 108 pt "before" floats above a full poster on the far side of a five-row text table.
  - The only explanation of *how* was "change a price in our app" (p9), which is forbidden in v3 and does not answer the question.
- **v3 rule:** use the hook, the 4-step method and the 2-second before/after layout in section 5.

### Register: "Either رأس or لرجلينك. This is a mix of عامي وفصحى"
- **Where:**
  - `carousel_06-01.jpg`: the headline «من الراس للقدم».
  - Repeated in the deck on p7, p8, p19, p20, and in the p19 title «"من الراس للقدم" في منشور واحد».
  - «الراس» is the colloquial spelling; «القدم» is the formal noun (a Saudi says «رجل/رجلين»). One phrase, two registers.
  - The full register inventory is in section 3.
- **v3 rule:** every poster ships in two complete versions with the same layout:
  - **فصحى (MSA):** «من الرأس إلى القدم».
  - **سعودي (Saudi):** «من راسك لرجلينك».
  - The register is decided per *version*, not per line. The kicker, headline, sub-line, CTA and caption all follow it. Neutral data such as product names, «قطن 100%» or sizes may appear in both. Section 3.4 gives a lint list of words that must not appear in the wrong version.

---

## 2. Image-quality defects in the old assets

Sizes: feeds are 800×1000, carousels 1000×1000 and stories 562×1000. The render engine's native sizes are 1080×1350, 1080×1080 and 1080×1920, so **every exported asset is below platform-native resolution** (stories at 52 %).

### 2.1 Composites and scenario shots
| File (also used on) | Defect |
|---|---|
| `feed_01.jpg` (cover p1/p13 hero, p3, p5, p9, p15, p17, p21) | • A **stray white thread or mask remnant** hangs below the shemagh tip (a V-shaped line, `crops/feed01_product.png`, `crops/p01_hero.png`).<br>• **No contact shadow** under the tip or the box.<br>• The box corner sits at the plinth edge as if floating.<br>• The JPEG is soft and upscaled.<br>• The logo's dark-green Arabic wordmark on the dark-grey wall measures **1.27:1** and is illegible (`crops/feed01_logo.png`).<br>• The struck price is 2.68:1.<br>• The product sits in the bottom-left 40 % of the frame, below an empty grey wall. |
| `feed_02.jpg` = `product_pages_01.jpg` (p5, p10, p17, p22) | • The lifestyle panel has a warm gold-lit wall over a cool, flatly lit box: **two light sources that disagree**, and no shadow under the box.<br>• The same product appears twice (scene plus cutout).<br>• The cutout is a flat frontal elevation.<br>• The perfume labels are mush («EAU DE PARFUM» is illegible). |
| `shotsheet.jpg`: `4a7821a5` perfume (p4/p16 "after") | • The box is photographed **straight-on** but pasted onto a plinth seen from about 35° above, a **perspective mismatch**.<br>• The box touches both side edges of the frame.<br>• There is no contact shadow. |
| `shotsheet.jpg`: `b28ed248` shemagh (p4/p16 "after") | • **Product detail lost:** the green lid with the gold-foil logo has disappeared. Only the base rim remains.<br>• The product takes about 15 % of an empty plinth and has hard cutout edges. |
| `shotsheet.jpg`: `1889f9f0` white fabric (p4/p16 "after") | • A flat cutout triangle **floats in a light beam**, and the beam's floor/wall geometry is ambiguous.<br>• No shadow, no folds, no texture.<br>• It does not read as a premium fabric. |
| `shotsheet.jpg`: `c46a61b6`, `fc9a3f51` socks (p4/p16 "after") | • Ghost socks stand on a marble plinth **with no shadow** and the wrong perspective.<br>• `fc9a3f51` cuts the socks at the left edge and shows a solid black block at the bottom. |
| `shotsheet.jpg`: rejected `0b6146d9`, `ced147c0`, `6d128361`, `1c8bc350` | • The box hangs over the plinth edge.<br>• **Boxers stand upright on a plinth with no body or hanger.**<br>• A T-shirt is pasted onto a grey block.<br>• A T-shirt has a blue cast plus a **hand-drawn lamp line-art artifact** at the top (an AI hallucination).<br>• The rejects show the same failure classes as the accepted shots. |
| Whole shot series | **Inconsistent light:** a warm ceiling spot, a cold spot, a window beam and flat studio light across one "series", each with a different white balance and camera height. |
| `carousel_06-03.jpg` = `product_pages_09.jpg` | • **Wrong product:** the poster sells «قميص داخلي وثير إيطالي (قطعة واحدة)», but the hero box reads **"men's boxer / بوكسر رجالي"** and **"2 Pack / قطعتان"** (`crops/car03_label.png`). Both the product type and the quantity contradict the copy.<br>• The warm window-blind light belongs to a different visual world from the rest of the set. |

### 2.2 Catalogue and packshot posters
| File | Defect |
|---|---|
| `feed_04.jpg` = `product_pages_03.jpg`, `product_pages_13.jpg`, `product_pages_15.jpg` | • **White ghutra on a light-grey ground:** product-to-ground contrast is **1.02:1** (`feed_04`) and **1.04:1** (`pp15`).<br>• The ghutra's edge dissolves and its jacquard is invisible (`crops/feed04_product.png`).<br>• The source photo is upscaled and soft. |
| `product_pages_07.jpg` (boxers), `product_pages_08.jpg` (undershirt) | • **White garment on a white ground: 1.21:1 and 1.16:1.**<br>• E-commerce ghost-mannequin look with a hard cutout edge.<br>• The garment top sits about 45–60 px from the top edge while about 40 % of the canvas is empty below it. |
| `carousel_06-04.jpg` | • A flat packaging mockup with a hard drop shadow. **The product itself is not visible.**<br>• The image fills about 30 % of the canvas. |
| `carousel_06-05.jpg`, `product_pages_04/05.jpg` | • Floating sock cutouts with no shadow.<br>• About 40 % of the canvas is blank. |
| `product_pages_02/06/10/12/14` and the `feed_04/07` family | • A two-tone page: a grey photo panel butts against a white card, leaving a **visible seam**.<br>• The product scale varies from page to page, from about 25 % to 45 % of the photo zone. |
| `feed_05.jpg` (p5, p12, p17, p24) | • **Off-system:** a black slab band in Cairo Black, unlike every other poster.<br>• The product appears only as a 680×190 swatch strip, with no form, no box and no price.<br>• The headline «نقشة ذهبية» ("golden pattern") sits on a red-and-white swatch, which misleads (the product name is «نقش العطار 25 الذهبي»).<br>• It looks unfinished. |
| `feed_07.jpg` = `product_pages_14.jpg` | • The hero shot puts **"100% POLYESTER … MADE IN JAPAN"** in gold print at the centre of a luxury post, which undercuts the premium story.<br>• Grey cast over a white fabric. |
| `realprod.jpg` (six fabric posters) | White-on-white fabric throughout, a grey cast and flat contrast. Copy defects are in section 3. |

### 2.3 Model posters (store photos, real models)
| File | Defect |
|---|---|
| `stories_03.jpg` (p5, p12, p17, p24) | • The headline block is set over the ghutra tail, the product being sold.<br>• **Both hands are cut by the bottom edge.**<br>• The logo sits about 13–21 % from the top, inside the Instagram profile-bar zone.<br>• Exported at 562×1000. |
| `stories_08.jpg` (p8, p20) | • The shemagh tail touches the «كلاسيك ما يغيب» headline (`crops/st08_head.png`).<br>• Hands are cut at the bottom edge.<br>• The logo crowds the shemagh. |
| `carousel_06-01.jpg` | • The headline block butts against the shemagh tail, with about 10 px of clearance.<br>• The bottom edge crops the shemagh tail at the knee line. |
| `carousel_06-06.jpg` | «كمّل طلّتك» is **set directly over the red-and-white shemagh border**, a busy pattern under black type. |
| Deck p5/p17 campaign grid | **Four unrelated styles in one campaign:** a dark marble full-bleed, a white catalogue card, a black-slab type poster and a model on white. There is no single system. |

### 2.4 Deck-level image issues
- **p1/p13:** the logo tile (see G1) and the hero composite (see 2.1).
- **p2/p14 "your store photos today":** four tiles on three different grounds (lavender-white, pure white, grey).
- **p4/p16:** BEFORE tiles are 108 pt and AFTER images 174 pt, cut from 554×1500 strips. They are upscaled in print, cropped to different aspect ratios, and the fabric "before" is wider than the rest.
- **p9/p21:** a low-resolution app screenshot. It is also forbidden content in v3.

---

## 3. Arabic copy problems (quoted)

### 3.1 Register mixing (فصحى and عامية in one piece or one series)
| Asset | Quote | Problem | MSA version / Saudi version |
|---|---|---|---|
| `carousel_06-01` (p7, p8, p19, p20) | «من الراس للقدم» + «كل قطعة من بيت واحد» + «اسحب وشوف» | Colloquial «الراس» with formal «القدم», an MSA sub-line and a Saudi CTA, all on one slide. **This is the client's quote.** | «من الرأس إلى القدم» / «اسحب لترى المزيد» — «من راسك لرجلينك» / «اسحب وشوف» |
| Carousel kickers (`carousel_06-02`, `-05`) | «الراس» … «القدم» | Slide 2 uses the colloquial spelling and slide 5 the formal noun, inside one carousel. | «الرأس» … «القدم» — «الراس» … «الرجل» |
| `feed_01` | «بيت العطار، أكثر من ثمانين سنة» + «اطلبه الحين» | An MSA-leaning headline with a Saudi CTA. | «بيت العطار / أكثر من ثمانين عاماً» + «اطلبه الآن» — «بيت العطار / من أكثر من ثمانين سنة» + «اطلبه الحين» |
| `feed_07` vs `product_pages_14` (same product) | «ثوبك يبدأ من قماشه» vs «قماش ياباني خفيف، ما يشف ولا يتكسر» | The same SKU gets two registers. | «قماش ياباني خفيف، لا يشفّ ولا يتجعّد» — «قماش ياباني خفيف، ما يشف ولا يتكسّر» |
| Catalogue series (`product_pages_*`) | «كلاسيك بسعر ما يتكرر»، «الأحمر اللي يعرفه الكل»، «كلاسيك ما يغيب»، «آخر لمسة قبل ما تطلع» vs «لمسة عصرية على الأصل» | Saudi kickers sit above MSA spec lines, and one kicker in the series is MSA. | «كلاسيكيّ بسعر لا يتكرر»، «الأحمر الذي يعرفه الجميع»، «كلاسيكيّ لا يغيب»، «اللمسة الأخيرة قبل أن تخرج» — keep the Saudi lines as written in the Saudi version only. |
| `stories_03` | «للمناسبات اللي تستاهل» + «اطلبها الحين» | Consistently Saudi, but no MSA version exists. | «للمناسبات التي تستحق» + «اطلبها الآن» |
| `carousel_06-06` | «كمّل طلّتك من بيت واحد» + «اطلبه الحين من المتجر» | Saudi only, with no MSA twin. | «أكمِل إطلالتك من بيت واحد» + «اطلبه الآن من المتجر» |
| `feed_05` | «لشتاك» + «اطلبه الحين» | Saudi only. | «استعدّ للشتاء» — «جهّز شتاك» |
| `realprod` type-led | «اطلب الآن عبر الواتساب أو اضغط الرابط في البايو» | MSA imperatives mixed with the slang «البايو». | «اطلب الآن عبر واتساب أو من الرابط في الصفحة الشخصية» — «اطلب الحين من الواتساب أو الرابط في البايو» |
| Deck p5/p10/p17/p22 | «captions in Gulf Arabic»، «بلهجة خليجية» | The market is Saudi, and the posters mixed registers anyway. | «بالفصحى وباللهجة السعودية» |

### 3.2 Awkward phrasing, grammar and logic
- **Truncated sentence:** «غترة العطار بريميوم تجمع بين الأصالة والرفاهية **لتمنحك**» (`realprod` hero) ends mid-sentence.
- **Subject/verb agreement:** «**غتر** العطار زمرد **يضيف** لمسة أصيلة وأناقة» (`realprod` story). A plural subject needs a feminine verb: «تضيف». «لمسة أصيلة وأناقة» is also weak.
- **Ungrammatical coordination:** «اطلب الآن وشحن مجاني للطلبات فوق 450 ريال.» (imperative + noun phrase). Fix: «اطلب الآن، والشحن مجاني للطلبات فوق 450 [symbol]».
- **Missing unit:** «للطلبات فوق 450.» (`realprod` type-led).
- **Illogical claim:** «قماش فاخر بألوان ثابتة **تدوم طوال اليوم**». Colourfastness lasts years, not "all day".
- **Wrong coordination:** «قطن **وصناعة** سويسرية» (`product_pages_15`). Fix: «قطن، صناعة سويسرية».
- **Awkward:** «صناعة إيطالية، خفيفة للاستخدام الرسمي» (`product_pages_05`). Fix: «صناعة إيطالية، خفيفة تناسب الإطلالة الرسمية».
- **Filler or tautology:** «سروال داخلي رجالي كومفورت من وثير في بيت العطار.» (`product_pages_07`) repeats the title.
- **Name broken mid-name:** «شماغ نقش العطار 25 / الذهبي» (`product_pages_11`, `feed_05`), «قميص داخلي / رجالي كومفورت» and «سروال داخلي / رجالي كومفورت». The name's second line reads like a subtitle.
- **Spelling inconsistency inside the set:** «غترة العطار **إ**سبيشل» (`feed_04`) vs «قماش العطار **ا**سبيشل» (`feed_07`). «شماغ العطار **الأوربي**» sits over «صناعة **أوروبية**» on one poster (`product_pages_12`). Keep store product names verbatim, but make the descriptive line agree, and flag the store's own inconsistency to the client.
- **Copy contradicts the image:** «(قطعة واحدة)» over a box printed "2 Pack / قطعتان" (`carousel_06-03`). «نقشة ذهبية» over a red pattern (`feed_05`).
- **Line broken across the black band:** «غترة العطار كلاسيك تحافظ على | أناقتك طوال اليوم» (`realprod` type-led) splits the verb phrase.
- **Deck:**
  - ««من بيت العطار»: حملة 14 يوماً جاهزة للنشر.» (p17) should read «حملة من 14 يوماً، جاهزة للنشر».
  - Full stops end display headlines on p14 to p24.
  - Amiri leading collides on p24.
- **Transliterated English** where Arabic exists: «كومفورت» and «بريميوم» in descriptive copy. They are acceptable only where they are the store's product name. Use «مريح» and «فاخر» in sentences.

### 3.3 Price format and RTL
- **Price format:** see G3. «ر.س» is everywhere, «ريال» appears in `realprod`, decimals are mixed («330» vs «330.00»), and prices are probably ex-VAT.
- **Size ranges flip in RTL.** «مقاس 54-62» renders visually as **«62-54»** (`crops/feed04_num.png`), so it reads as "62 to 54". The same happens on every catalogue poster («62-55», «60-55», «62-54»), and `product_pages_11` drops the word «مقاس» entirely. Rule: write «مقاس من 54 إلى 62», or wrap the range in an LTR isolate (U+2066…U+2069) and test-render it.
- **Comma in display type.** In Cairo, the Arabic comma «،» looks like a Latin comma («بيت العطار،», `feed_01`). Do not put commas in display lines; break the line instead.
- **The English URL** «SIRAJATTARBROS.COM» is set in Inter capitals tracked 0.12 em on every Arabic poster. That is fine, but keep it isolated and at a fixed position (the inline end of the paper column).
- **RTL mirroring in the deck is incomplete.** On p16, the "before" tiles are right-aligned in columns of unequal width, and the before/after pairs are not mirrored as units. Mirror whole components, not just text alignment.
- **The PDF Arabic text layer is broken.** See G4.

### 3.4 Register lint list (automatic check for v3; a hit means a human reviews the line, not an automatic rejection)
- **Must NOT appear in the فصحى version:** «اللي، الحين، ما (as negation before a verb), شوف/وشوف، كمّل، تستاهل، الراس، لرجلينك، شتاك، يتكسر (meaning wrinkle), البايو، إحنا، وش».
- **Must NOT appear in the سعودي version:** «الآن، الذي/التي، لا (as negation, where the Saudi form is used), إلى (in slogans), القدم (in the head-to-toe phrase), لترى، أكمِل».
- **Neutral, allowed in both:** product names, materials, origin, sizes, «بيت العطار», «من بيت واحد», «قطن 100%».

---

## 4. What worked, and how to push it further

### 4.1 Positioning line: "80+ years of craft. Every post should show it."
- **Why it works:** it is short, it states the gap, and it ties product to heritage. The Arabic «إتقان أكثر من ثمانين عاماً يستحق أن يُرى» (p14) is good MSA.
- **Push it:**
  - Make it the spine of the deck. It opens the problem section, gives every section its proof, and closes the deck.
  - Turn "show it" into a rule. **Every v3 asset carries at least one visible craft proof**, chosen from:
    - a macro of the weave or fringe,
    - the gold-foil box logo,
    - the woven corner monogram,
    - a hand finishing a fold,
    - a heritage cue: majlis, dallah or 1940s-to-now archival tone.
  - Give the line a poster form in both registers, used as the campaign sign-off:
    - **MSA:** «ثمانون عاماً من الإتقان… في كل تفصيلة».
    - **Saudi:** «أكثر من ثمانين سنة نتقنها… وتبان في كل تفصيلة».

### 4.2 Catalogue poster structure
- **Why it works:** a clean information order of kicker → product name → spec line → price pill → struck old price → URL, a fixed logo corner, and a brand-green base rule. The client called it "good and polished".
- **Push it:**
  1. **One grid for every category.** Shemagh, ghutra, fabric, perfume, underwear and socks share one frame. The product photo zone is **≥ 55 % of the canvas** and the product fills **60–70 % of the zone's width** (±5 % across the set).
  2. **Grounds.** Replace the grey-panel/white-card seam with a brand ground per category: deep green, sand or cream. White products always sit on a mid-tone or coloured ground (contrast gate in 7.B).
  3. **Prices.** Riyal symbol, VAT-inclusive price, a discount badge when there is a compare-at price, and the struck price at ≥ 4.5:1.
  4. **Names and specs.** Names stay on one line, or break at a semantic boundary (never «… 25 / الذهبي»). Sizes are written «من 55 إلى 62».
  5. **Two registers, one layout:** the kicker and CTA change, everything else stays.
  6. **Native resolution:** 1080×1350 feed, 1080×1920 story/Snap/TikTok, 1080×1080 carousel.

### 4.3 Scenario imagery (the product in different scenes)
- **Why it works:** it answers "catalogue shots aren't scroll-stoppers" with the client's own product in a setting.
- **Push it:**
  - **Saudi scenes with a story**, each tied to a selling moment:
    - the red shemagh at a winter desert camp (كشتة) at dusk, for the season switch from white ghutra to red shemagh (late October to November);
    - the white ghutra on an Eid or Friday-morning majlis table with dallah and finjan;
    - the perfume set on a wedding-evening dresser;
    - the formal socks with polished shoes in a Riyadh office lobby;
    - the undershirt as part of the folded "under the thobe" morning ritual;
    - the fabric bolt on a tailor's cutting table with chalk and shears.
  - **One light recipe for the series:** one key-light direction (e.g., upper-left 45°), one colour temperature (±200 K), the same camera height per category, and a **contact shadow under every resting object**.
  - **Physically plausible scenes only:**
    - no garment stands upright without a body, hanger or form;
    - no box overhangs a ledge;
    - the product's camera angle is within ±10° of the scene's floor plane.
  - **Product truth is locked.** The pattern, the foil logo, the box lid, the label text and the pack quantity match the store photo. The branded lid is always visible when the box is part of the product.
  - **Worn scenarios use the store's real model photos** (`storephotos.jpg` has five strong ones), extended into scenes. Crops never fall at wrists, hands or ankles.
  - **Finish standard:** an image only ships after the 7.B checklist. Show fewer, finished images rather than more unfinished ones.

### 4.4 Also worth keeping
- **The campaign name** «من بيت العطار» / *From the House of Attar*: warm and ownable.
- **The head-to-toe carousel idea**, spanning shemagh to socks in one swipe. It failed on copy and finish, not on concept.
- **The bilingual edition** (but Arabic first).
- **The logo in the top inline-start corner** of every RTL poster.
- **The "by the numbers" page** (123 products, 308 photos, 0 photoshoots). Reframe it around v3's 40 assets and the media plan.

---

## 5. The missing HOW

v3 frames this as **our creative and media-buying method**. It never shows or names a platform.

### 5.1 Three alternative one-line hooks (EN / MSA)
1. **"Your product stays real. Only the scene changes. Then the numbers choose the winner."**
   «منتجكم يبقى كما هو، والمشهد وحده يتغيّر… ثم تختار الأرقام الإعلان الرابح.»
2. **"One store photo in. A finished, tested campaign out."**
   «صورة واحدة من متجركم… وحملة مكتملة ومختبرة.»
3. **"We direct the scene like a photoshoot and buy the media like an investor, without a single new shoot."**
   «نُخرج المشهد كجلسة تصوير، ونشتري الإعلان كمستثمر، دون جلسة تصوير واحدة.»

Recommendation: hook 1 on the "How" divider page, with hook 2 as its sub-line.

### 5.2 The 4-step visual explanation (one page, four equal panels, one product: the زفير shemagh in its box)
| Step | Title (EN / AR) | What the panel shows | One line under it |
|---|---|---|---|
| 1 | **Your photo** / «صورتكم» | The untouched store packshot, exactly as on sirajattarbros.com. | "We start from the photo you already have." |
| 2 | **The product, locked** / «المنتج كما هو» | The same shemagh cut out on a neutral ground, with 3 or 4 small callouts: *pattern ✓, gold-foil logo ✓, box lid ✓, colour ✓*. | "Every thread, logo and colour is checked against your product." |
| 3 | **The scene, directed** / «المشهد مُخرَج» | The same product in a Saudi scene (winter majlis at dusk), with a thin light-direction arrow and a "contact shadow" tick. | "We art-direct a new setting around it: Saudi places, Saudi seasons, one light." |
| 4 | **The ad, live and measured** / «إعلان يُقاس» | The finished 4:5 poster (riyal symbol, فصحى and سعودي versions side by side as small thumbnails) next to a mini bar chart: 3 variants, budget shifting to the winner. | "Two tones, three formats, tested; budget follows what sells." |

Layout rules for this page:
- The four panels are **equal width** (each ≥ 20 % of the page width).
- The same product sits at the **same scale and position** in panels 1 to 3, so only one thing changes per step.
- Numbers are ≥ 24 pt and titles ≥ 14 pt. Arrows sit between panels and point in reading direction (right to left on the Arabic page).
- Under the row, one line answers the client's question in their words: "From a store photo to this result: we keep the product, design the scene, finish it by hand, and let the campaign data pick the winners."

The media-buying half of the "how" belongs in the deck immediately after this page:
- **Platform mix for KSA:** Snapchat, Instagram, TikTok and X.
- **Test → learn → scale cadence:** 3 hooks per hero product; after 72 h the budget moves to the winner.
- **Calendar anchors:**
  - the shemagh-season switch (late October to November 2026),
  - White Friday on 27 November 2026,
  - Founding Day on 22 February 2027,
  - Ramadan and Eid gifting (expected February–March 2027).

### 5.3 Before/after that reads in 2 seconds
1. **Side by side, never stacked.** Both panels are the **same size, aspect ratio, crop and height**, with a gap of ≤ 2 % of page width. On the English page, "before" is on the left. On the Arabic page, «قبل» is on the right, so the eye reads before → after either way.
2. **One pair per hero slide.** Each panel is **≥ 40 % of the slide width**. A supporting slide may show up to 3 pairs, and each pair is still side by side and equal.
3. **Same product scale and position** in both panels (±10 % of bounding box). The only change the eye should register is the world around the product.
4. **The "after" must be different at thumbnail size:** a different ground value or colour (≥ 30 % luminance difference from the "before" ground), a visible setting and visible light. If the after is just "grey → darker grey" (p3), redo it.
5. **Labels are large and identical:**
   - «قبل» / «بعد» and BEFORE / AFTER at **≥ 14 pt** (≥ 2.5 % of the page height), in the **same corner of each panel**.
   - Light-on-dark tags at ≥ 4.5:1.
   - The "after" tag can carry the brand green to signal the result.
6. **Optional third panel,** the finished poster, joined by a single arrow and slightly smaller (≥ 70 % of panel height). Never add a fourth element.
7. **One caption line** naming the change: *"Same box, same shemagh. New majlis, new light. Zero photoshoot."* / «العلبة نفسها والشماغ نفسه… مجلس جديد وضوء جديد، دون جلسة تصوير.»
8. **2-second test:** show the slide to someone outside the project for 2 s. They must be able to say "the store photo became an ad". If they can't, enlarge the panels or increase the scene contrast.

---

## 6. Fonts used inside the old poster images

Source: `everyside/backend/app/services/images/template_composer.py`, opened read-only (`_FONT_FACES`, `_CAIRO_BLACK`, `_run_attrs`, and the per-layout CSS). The Arabic poster face was confirmed visually by rendering specimens (`research/old_renders/fontcheck/specimens.png`) and comparing them with `crops/feed01_text.png`.

| Role in the poster | Face | Weight(s) |
|---|---|---|
| **All Arabic text: headline, kicker, product name, spec line, CTA, price** | **Cairo** (Google Fonts, SIL OFL; Kufi-modern with Titillium-derived Latin and digits) | Regular 400, SemiBold 600, Bold 700, Black 900 |
| Full-bleed and type-led display headlines («بيت العطار…», «لشتاك», «للمناسبات اللي تستاهل») | Cairo | Black 900 (the `h1` is weight 900) |
| Split-panel headline («من الراس للقدم», «كمّل طلّتك») | Cairo | Bold 700 |
| Catalogue product name, first line / second line | Cairo | 700 / 400 |
| Kicker («كلاسيك ما يغيب») | Cairo | 700 |
| Price pill («157.82 ر.س»), with Cairo's own Western digits | Cairo | 800 requested, rendered as Black 900 (no 800 face is loaded) |
| Struck old price and spec line | Cairo | 400 |
| CTA («اطلبه الحين») | Cairo | 600 (700 when boxed) |
| Latin runs: the URL «SIRAJATTARBROS.COM», uppercase and tracked 0.12 em | **Inter** | Regular 400 (Bold, ExtraBold and Black 700/800/900 are loaded for Latin headlines) |
| Fallback renderer only, if the render service is down (not visible in the delivered assets) | Noto Naskh Arabic, DejaVu Sans, and the display face "Guesswhat-Exceptional.otf" | n/a |

Notes:
- The client logo in the posters is the raster `mark.png`, not type.
- The «اسبيشل» gold print and the box foil are the product's own artwork, not our typography.
- The deck PDF embeds Playfair Display, Manrope, Amiri Bold, IBM Plex Sans Arabic, Arial and Segoe UI. Those are the presentation fonts the client asked us to reconsider (see G4).
- **For v3:**
  - Keep **Cairo** for every Arabic line in the images.
  - Use Cairo again for the Arabic presentation, so the deck and the posters share one voice.
  - Pair it with **Inter** for Latin.
  - Font files are available on Google Fonts. The old render service's copies are at `everyside/apps/render/assets/fonts/Cairo-*.ttf` and `Inter-*.ttf` (read-only reference; `fonts/` in this project is still empty).

---

## 7. v3 gates (consolidated, measurable)

### A. Brand and cover
- [ ] Client logo ≥ 18 % of page width on the cover, on its own field, with clear space ≥ 50 % of the logo height. Vector or a ≥ 2000 px transparent file.
- [ ] Reversed gold-on-green lockup on dark grounds. Logo contrast ≥ 3:1 everywhere.
- [ ] "Made specifically for M. Siraj Attar & Bros" / «صُمِّم خصيصاً لمحمد سراج عطار وأخويه» at ≥ 16 pt on the cover.
- [ ] Everyside mark ≤ 1/3 of the client logo width. No platform screenshots or names anywhere.

### B. Every image
- [ ] Native size: 1080×1350 / 1080×1920 / 1080×1080. Deck images placed at ≥ 2 px per pt (cover hero ≥ 3 px per pt).
- [ ] The product bounding box is ≥ 4 % from every frame edge. A deliberate macro crop may cut through fabric only, never through a box, logo, label, head or hands.
- [ ] Contact shadow under every resting product. One light direction and white balance (±200 K) per series. Product camera angle within ±10° of the scene plane.
- [ ] Product-to-ground luminance contrast ≥ 1.6:1 in the 20 px band around the silhouette. White products never sit on a ground lighter than about #BEBEBE unless the ground is coloured.
- [ ] No halo: the 2 px edge fringe is within 10 % of the local ground luminance. No stray threads or mask remnants (zoom-check at 200 %).
- [ ] Product truth: pattern, foil logo, lid, label text, product type and pack quantity match the store listing.
- [ ] No text over the product or over shemagh pattern. Clearance between the text block and the product is ≥ 3 % of canvas width.
- [ ] Stories: text and logo stay out of the top 14 % and bottom 20 %.
- [ ] Model crops avoid joints. No hands cut by a frame edge.
- [ ] No plastic skin, no melted labels, no hallucinated objects such as the line-art lamp.

### C. Every line of Arabic
- [ ] Two complete versions per poster (فصحى and سعودي) with an identical layout. The 3.4 lint list passes.
- [ ] Product names are verbatim from the store and never broken mid-name. Sizes are written «من … إلى …».
- [ ] No commas or full stops in display lines. Line-height ≥ 1.35 for display text and ≥ 1.6 for body text.
- [ ] The final PDF passes the Arabic text round-trip test (G4.4).

### D. Every price
- [ ] Riyal symbol SVG only, at lining-figure height, the same colour as the figures, left of the number with a 0.2–0.25 em gap, set as an LTR-isolated unit.
- [ ] VAT-inclusive price confirmed on the live product page. Whole riyals have no decimals.
- [ ] Discount badge when there is a compare-at price. Struck price ≥ 45 % of the new price's size and ≥ 4.5:1 contrast.
