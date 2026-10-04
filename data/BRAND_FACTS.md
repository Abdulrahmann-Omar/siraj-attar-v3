# Siraj Attar brand facts

Source: the live store https://sirajattarbros.com/ar, scraped 2026-10-04. Raw pages are in `data/raw/site/` and screenshots in `data/raw/screens/`.
Verbatim client text is in Arabic. Our notes are in English.

## Identity

| Item | Value | Source |
|---|---|---|
| Arabic name | محمد سراج عطار وأخويه | og:title, logo, footer |
| English name | M. SIRAJ ATTAR & BROS (logo spelling: "M.SIRAJ ATTAR & BROS") | logo |
| Short/house names used in copy | العطار، سراج العطار، غتر العطار | product titles and descriptions |
| Commercial registration (السجل التجاري) | 7018064480 | footer |
| VAT number | 300189681700003 | footer |
| Store platform | Salla, store id 946211295, username `mhmd-srag-aatar-oakhoyh`; theme "Selia" by Selia Tech (theme 581928698 v1.220.0) | page source |
| Languages | Arabic primary (`/ar`), English alternate (en_US) | og:locale |
| Price display | The site already shows prices with the **new Saudi Riyal symbol** glyph, not "ر.س" (see `data/raw/screens/product_1983204219.png`) | product page |

## Logo

- **`brand/logo_original.png`**: 2024 x 1507 px, RGBA, transparent background, 175 KB. This is the original upload behind the header logo, favicon, apple-touch-icon and og:image. All of them point to `https://cdn.salla.sa/ydOvDq/stores/logos/FKoUAvj1NOqowiCUswiPMHYD5baOCKzbwX8PowSU.png`. The header serves the same file through Cloudflare resizing at 400 px.
- **No SVG logo exists on the site.** We checked the header markup, every `.svg` reference in the rendered home page, the favicon set and the og/twitter images. The PNG above is the highest resolution available. A vector version would have to be traced or requested from the client.
- Construction (top to bottom):
  1. A deep-green roundel with a dashed "stitched" inner ring. Inside it, the name سراج عطار in gold Arabic calligraphy, scattered with small gold diacritic ornaments.
  2. The Arabic wordmark محمد سراج عطار وأخويه in green, in a clean geometric sans.
  3. The English wordmark M.SIRAJ ATTAR & BROS in gold classical serif capitals.
- The roundel alone works as the brand mark. It is foil-stamped on the green gift boxes, printed in gold on the branded fabric selvedges ("العطار 263", "100% COTTON VOILE BY M.SIRAJ ATTAR") and woven into the shemagh/ghutra corners.

## Brand colours (hex)

| Role | Hex | Where it was measured |
|---|---|---|
| **Primary green** | **#004738** | Logo roundel and Arabic wordmark (exact pixel mode); site CSS `--color-primary`; buttons; wishlist icon |
| Primary green, dark | #002112 | site CSS `--color-primary-dark` |
| Primary green, light | #266D5E | site CSS `--color-primary-light` |
| **Gold / sand** | **#C3A278** | Logo calligraphy and English wordmark (exact pixel mode) |
| Light gold (highlight) | #E9C9A4 | Logo ornaments |
| Announcement-bar sand | #E8D6B0 (text #0E3B02) | Top bar ("الآن عروض اليوم الوطني...") |
| Footer grey | #EDEDED (text #004838) | Footer |
| Page background | #FFFFFF | Body |
| Body text | #111827 / #000000 | Menu and body text |
| Sale price red | #DC2626 | Struck/sale price on cards and product page |
| Out-of-stock label | #EA5C5C | Product cards |
| Green gift box, as photographed | #224C38 to #4F7865 | Product packshots. This is the brand green under studio light; use #004738 as the base |

Other recurring palette in the product photography: shemagh red and white, cream/off-white thobe fabrics, and the gold foil of fabric labels. Perfume and lifestyle shots use warm sand/wood tones. Wathir underwear packaging is a teal-green pouch with a white "WB" monogram roundel; its gift box is kraft brown with botanical line art.

## Typography seen on the site

- UI font: **alfont_com29LTAzer** (29LT Azer), with a system fallback. It is used for everything in the theme.
- Banner lettering: the campaign word-mark "تميّز متوارث" is hand-lettered calligraphy. Its taglines are set in a light geometric Arabic sans.

## Taglines and recurring copy (verbatim)

- About page heading: **"أصالة وأناقة... تليق بك"**
- Campaign banner (home slider and footer banner): **"تميّز متوارث"** with **"منتجات تتوارثها الأجيال بفخر وأناقة"**
- Home hero video caption: "وتكمّل الحاضر"
- Announcement bar (live 2026-10-04): "الآن عروض اليوم الوطني تبدأ من 15% , أطلب الآن وأغتنم الفرصة"
- Product copy: "غترة العطار الأصلية تشارككم الأفراح لأكثر من 80 عاماً" and "افضل الاقمشة والغتر والمستلزمات الرجالية حصريا لدى متجر سراج العطار"
- Meta description: "متجر العطار للأصالة عنوان للأقمشة الرجالية أفضل الغتر والأشمغة الأصلية غتر العطار لجميع المناسبات بضائع مخفضه منتجات شتوية فاخرة شماغ ابيض و احمر الاصلي"

## History (About page: عن محمد سراج عطار واخويه)

Key facts:
- **80+ years.** The page says both "منذ 80 سنة" and "منذ أكثر من 80 عاماً". **No founding year is stated.** 80 years before 2026 points to about 1946, but that is an inference.
- **Founder:** the father, **عبد السلام صالح عطار** (رحمه الله). He began trading young in **Makkah**, dealt with pilgrims and imported goods from **Turkey, Aden and Egypt**.
- After his death **his sons founded the company** (hence "وأخويه", "and his brothers").
- **Jeddah branch, شارع قابل: 1377 AH** (about 1957-58 CE). **Riyadh branch, أسواق الديرة بالثميري: 1389 AH** (about 1969-70 CE). Their ghutras and fabrics then became known across KSA and the GCC for high quality at moderate prices.
- They say they are still the choice of "الأمراء والوجهاء" (princes and dignitaries).
- **Today:** the founders' grandchildren run the company through a board of directors, and the page ties its future to **Vision 2030**.
- Product lines named on the page: الأصواف، الغتر، الأشمغة الرجالية.

Full text, verbatim and reflowed into paragraphs:

> أصالة وأناقة... تليق بك
>
> منذ 80 سنة، يجسد هذا التاريخ عراقة وأصالة منتجات محمد سراج عطار وأخويه، ريادة بمجال الأصواف والغتر والأشمغة الرجالية، بمنتجات عالية الجودة والصناعة، وبتنوع يواكب التغير في الموضة
>
> تاريخ من التميز
>
> نستمدُّ أصالتنا من الماضي، ليسطع نجم حاضرنا، ويشرق معه مستقبلنا –بمشيئة الله-. منذ أكثر من 80 عاماً صنعت عائلة العطار من شغفها ومهنيتها في مجال التجارة على أساسٍ متين وكفاءاتٍ مهنيةٍ عريقة ما جعلها في مصافّ روَّاد التميُّز، أظهرت الشركة عصاميتها منذ عهد المؤسس الأب/ عبد السلام صالح عطار -رحمه الله-حين امتهن التجارة في سن مبكرة في مكة المكرمة. ومكّنته حذاقته وقدراته من التواصل والحجاج ومعرفة ثقافات الشعوب، وفهم احتياجاتهم من سلع ومنتجات والتي كان يستوردها من تركيا وعدن ومصر. وبعد وفاة الشيخ عبد السلام، أسس الأبناء الشركة وفق رؤية تطويرية، وفي عام 1377هـ تم افتتاح فرع جدة في شارع قابل، ثم فرع الرياض في أسواق الديرة بالثميري عام 1389هـ، ومنها انتشر بعدها اسم محمد سراج عطار وأخويه بمجال الغتر والأقمشة والتي اشتهرت بجودتها العالية وقيمتها المعتدلة على مستوى المملكة ودول الخليج.
>
> من وحي ماضينا وتميزنا حاضرنا وما زلنا وجهة للأمراء والوجهاء والباحثين عن الجودة والأناقة.
>
> وفي السنوات الأخيرة، وبعصامية أحفاد عائلة العَطَّار ومهنيتهم وترابطهم تولى مجلس الإدارة مهمة الإشراف على أعمال الشركة وتطويرها، للسير على خطى المؤسسين ومبادئهم وقيمهم المهنية، وذلك لتستمر الشركة -بمشيئة الله-كأحد أشهر وأعرق الشركات الوطنية التي تستعين بكفاءات إدارية وخبرات متراكمة تتمتع بالثقة والمصداقية وخدمة الوطن بما يحقق رؤية المملكة 2030 -بمشيئة الله وتوفيقه-مُتنقلةً من جيلٍ إلى جيل بنجاح.

## Branches (فروعنا page): 9 showrooms in 4 cities

All branches share the unified number **920007805** plus an extension.

| City | Branch | Ext. |
|---|---|---|
| الرياض | الديرة، شارع الثميري (the original 1389 AH Riyadh branch) | 205 |
| الرياض | شارع العليا، عمائر السيركون | 206 |
| الرياض | شارع أنس بن مالك، حي الملقا | 209 |
| الرياض | حي الروضة، شارع الحسن بن علي | (not given) |
| جدة | البلد، سوق الندى، خلف عمارة الملكة | 202 |
| جدة | شارع الأمير محمد بن عبدالعزيز (التحلية)، الرياض بلازا | 203 |
| جدة | شارع حائل، الأمل بلازا | 207 |
| مكة المكرمة | العزيزية، طريق المسجد الحرام، مقابل مطعم الطازج | 204 |
| الخبر | الخبر الشمالية، طريق الملك عبدالعزيز، بين شارع 19 وشارع 20 | 208 |

(The page breaks the Makkah landmark across two lines as "الطاز / ج". It reads "الطازج".)

## Contact

- Unified number / WhatsApp: **920007805** (tel: and https://wa.me/920007805). Hours: 10:00 to 17:00, per the returns policy.
- Email: **care@sirajattarbros.com**. The returns policy promises a reply within 3 working days. On the site the address is Cloudflare-obfuscated; we decoded it.
- Contact page text: "للتواصل معنا و خدمتك. رقم الواتس اب : 920007805".
- A floating WhatsApp button appears on every page.

## Social links (store config and footer)

| Platform | URL / handle |
|---|---|
| Instagram | https://www.instagram.com/SirajAttarBros (@SirajAttarBros) |
| X (Twitter) | https://x.com/SirajAttarBros (@SirajAttarBros) |
| Snapchat | https://www.snapchat.com/add/sirajattarbros |
| TikTok | https://www.tiktok.com/@m.sirajattar (note: a different handle from the others) |

The returns policy gives "@SIRAJATTARBROS" as the handle on all platforms. No Facebook, YouTube or LinkedIn link is published. The store has Snapchat and TikTok pixel slots configured (IDs not set in the public config).

## Payments (footer badges and product page)

- **mada**, **credit card** (Visa/Mastercard), **STC Pay**, **Apple Pay**, **cash on delivery (COD)**.
- **Tabby**: the product page widget reads "ابتداءً من 23.48/شهر على ما يصل إلى 12 دفعة شهرية. متوافق مع أحكام الشريعة" (shown on a 240.21 item; the riyal glyph is omitted here).
- **Tamara**: "80.07 شهريًا حتى 3 أشهر، متوافق مع الشريعة الإسلامية!" (240.21 / 3).
- Both BNPL widgets present themselves as Sharia-compliant, which is a useful trust line for ads.
- Customer accounts log in by email (mobile and WhatsApp login are off; allowed country list: SA).
- Prices are shown **before VAT**: displayed price = Salla `product:pretax_price`. VAT (15%) is presumably added at checkout. Not verified.

## Shipping (from the returns page, section 2)

- Inside Saudi Arabia: **2 to 5 working days**.
- GCC: **3 to 7 working days**.
- Outside urban areas the parcel is collected from the courier's nearest office.
- **No shipping fee or free-shipping threshold is published** on any public page. It is only visible at checkout, which we did not open.

## Returns and exchanges (الاستبدال والاسترجاع), summary

- **Exchange within 14 days**, counted from purchase in showrooms or from delivery online. **Return/refund within 7 days.**
- Conditions: the item is completely original, unused, unwashed, unironed and unaltered, in its original packaging with all labels and tags, and the customer has the invoice or order number. **The customer pays return shipping.**
- **Not returnable or exchangeable:** underwear, kufiyas (الكوافي), all accessories, perfumes, and items damaged by misuse. **Fabrics cannot be exchanged or returned.**
- **Sale items:** no refunds (unless the item has a manufacturing defect or is the wrong item). Exchange within **3 days** only.
- Refund to the original payment method within **7 to 14 working days** after inspection.
- Manufacturing defects: report within 7 days with the order or invoice number, clear photos and a short description. The customer chooses an exchange or a refund, and **the company pays shipping**.
- Replacements and refunds are issued after the original item is received and checked.

## Sub-brands and lines seen in the catalogue

- **وثير (Wathir)**: underwear and socks (Egyptian-cotton "كومفورت" basics; Italian-made "وثير إيطالي" pieces). Teal pouch with "WB" monogram; kraft gift box.
- **Bernini (برنيني)**: shemaghs with a "B" monogram and a black box. Both are currently out of stock.
- **Attar 1 / 2 / 3**: eau de parfum, 100 ml, plus a three-bottle gift set in the green box.
- House collections: المجموعة الكلاسيكية (gem names: ياقوت، عقيق، مرجان، عنبر، زمرد، زفير), مجموعة حفاوة, مجموعة الأصالة, نقش العطار / ختم العطار / الوسام (season "25"/"26" designs).
- Origins claimed in descriptions:
  - Japan: most thobe fabrics.
  - Switzerland: ghutras and Swiss cotton.
  - England: shemaghs, and the William Halstead / OMC wools.
  - Italy: Biella wools, Testa fabrics, Wathir pieces.
  - Also Korea, Taiwan, Spain, and the Czech Republic (نقش العطار 26, Rio/Pro fabrics).
  - The agal is "صناعة وطنية" (Saudi-made) from German mohair yarn (صوف مرعز ألماني).

## Home page assets (for reference only, `brand/site_banners/`)

15 banner images (up to 1440 px wide), saved with `_index.json`. They include:
- the "تميّز متوارث" campaign: an elderly man with younger men in front of a lantern-lit mud-brick (Najdi-style) wall;
- a falconer in a white shemagh in the dunes;
- Attar perfume lifestyle shots (hand holding a bottle against a thobe and shemagh);
- Wathir packaging, and white and red shemagh macro shots.

The hero is a video hosted on asas-tools.com (`reel2.mp4`, `vvvv.mp4`). It shows a young man in a white shemagh against a city skyline at dusk (apparently Riyadh), with the caption "وتكمّل الحاضر".
