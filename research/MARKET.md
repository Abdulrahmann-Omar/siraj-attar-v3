# Market research: M. Siraj Attar & Bros (محمد سراج عطار وأخويه)

Research for the Creative Director + Media Buyer proposal. Compiled 2026-10-04 (Riyadh time), which is 23 Rabi' al-Thani 1448 (the Ministry of Finance site shows that Hijri date the same day).

How to read the tags:
- **[Official]** comes from a government body or the brand's own site or store.
- **[Verified]** was checked directly in this session (live page, file, font or Unicode data).
- **[Secondary]** comes from press, agency blogs or aggregators. Treat it as directional.
- **[Estimate]** is our own calculation or judgement, and the reasoning is shown.

Evidence files are in `research/evidence/`. The official SAMA documents and the official riyal SVG are in `data/sama/`.

---

## 0. Key findings (read this first)

1. **The heritage claim holds up, and the number is inconsistent.** The family business goes back to founder Abdulsalam Saleh Attar trading in Makkah. The sons founded the company, opened Jeddah (Qabel Street) in 1377H (≈1957/58) and Riyadh (Deira, al-Thumairi) in 1389H (≈1969). The website says "80 years". Instagram and TikTok say "85 years". D&B lists the company as established in 1945. **The proposal should use one number. Use "80+" (أكثر من 80 عامًا), because the client already approved that line.**
2. **The house is strong in the shop and weak on social.** It has 9 branches (Riyadh 4, Jeddah 3, Makkah 1, Khobar 1) and about 16K Instagram followers. TikTok (@m.sirajattar) has only **728 followers and 65 videos**, against Ajlan & Bros at **138.7K followers and 1.6M likes**. Current content is mostly static Fusha posters: perfume offers and National Day greetings.
3. **The store already uses the new riyal symbol, and its prices are shown before VAT.** The Salla setting `use_sar_symbol: true` puts ⃁ to the left of the number, which is correct. The displayed figures, however, are pre-VAT (`product:pretax_price` = displayed price). For example, ⃁ 221.74 × 1.15 = ⃁ 255.00, and ⃁ 1,020.00 for a pashmina shawl. **Posters must show the price the customer actually pays at checkout. Confirm this with the client before typesetting any price.**
4. **The official SAMA guideline gives 10 usage rules (Feb 2026 edition).** The symbol always goes to the LEFT of the number, in Arabic and in Latin text, with a space between them. It must be the same height as the numerals and have enough contrast. **No colour is mandated.** The official SVG has been downloaded to `data/sama/Saudi_Riyal_Symbol-2.svg`, so `brand/riyal.png` does not need to be vectorised. Unicode is U+20C1 (Unicode 17.0, Sep 2025). Font support is still patchy, so posters should use the SVG and not a font glyph.
5. **The calendar decides the plan.** Ramadan 1448 is expected to begin Mon 8 Feb 2027 and Eid al-Fitr on Tue 9 Mar 2027. Tailors stop taking Eid orders around mid-Ramadan, so **the thobe-fabric peak falls in Rajab–Sha'ban (10 Dec 2026 – 7 Feb 2027), before Ramadan**. Founding Day (Mon 22 Feb 2027) falls on about 15 Ramadan. White Friday (27 Nov) comes one day after the November salary (Thu 26 Nov) and inside the school autumn break.
6. **Snapchat is the lead platform for Saudi men.** Ad reach is 25.3M (89% of adults 18+) and Snap claims 90% of 13–34s in KSA. TikTok, YouTube, Instagram, X and Google Search (95% share) make up the rest of the mix. Salla has native integrations for Snap Pixel + CAPI, the TikTok Events API, Meta CAPI with daily catalogue sync, and Google Merchant Center.
7. **There are gaps the house can own.** (a) The oldest Makkah-rooted merchant story in the category. (b) Specialism in the white Swiss ghutra while competitors fight over the red shemagh. (c) It is the only house selling head to toe: shemagh, ghutra, Japanese/Korean/European fabrics, English/Italian wool, pashmina shawls, perfume, the وثير underwear line, agal and cufflinks. (d) "HOW" content that teaches the craft (the مرزام crease, ironing at 110 °C, fabric choice). (e) Short video.
8. **The current copy already mixes registers and has errors.** Examples: the site banner "أطلب الآن وأغتنم" should be "اطلب الآن واغتنم", and the product page's "اشتريها معًا" is colloquial next to Fusha copy. Section 7 gives the rules and 30 phrase pairs.

---

## 1. The brand

### 1.1 History and identity

| Item | Finding | Source |
|---|---|---|
| Legal / trade name | محمد سراج عطار وأخويه, "M. Siraj Attar & Bros" (also "Mohammed Siraj Attar Brothers Co.") | [Official] store footer; [Secondary] D&B |
| Founder lineage | The father, Sheikh Abdulsalam Saleh Attar (عبد السلام صالح عطار), started trading young in **Makkah**, dealing with pilgrims and importing goods from Turkey, Aden and Egypt. After his death the sons founded the company. | [Official] [About page](https://sirajattarbros.com/ar/عن-محمد-سراج-عطار-واخوية/page-1340146930) |
| First branches | **Jeddah, Qabel Street (شارع قابل), 1377H (≈1957/58)**, then **Riyadh, Deira souqs, al-Thumairi, 1389H (≈1969/70)** | [Official] About page |
| "Founded" year | D&B lists it as established **1945** in Jeddah. HQ is on Hail Street, Jeddah, with 51–200 employees (ZoomInfo). | [Secondary] [D&B](https://www.dnb.com/business-directory/company-profiles.mohammed_siraj_attar_brothers_company.7eb7fdca0944a7e23f2c50b325575997.html), [ZoomInfo](https://www.zoominfo.com/c/m-siraj-attar--bros/1318247299) |
| Heritage claim | Site: "منذ 80 سنة" and "أكثر من 80 عاماً". Instagram/TikTok bios: "لأكثر من 85 عاماً". | [Verified] site, IG, TikTok on 2026-10-04 |
| Reputation line (own words) | "وجهة للأمراء والوجهاء والباحثين عن الجودة والأناقة"; known for "جودة عالية وقيمة معتدلة" across KSA and the Gulf; now run by a board of the founders' grandchildren | [Official] About page |
| Signature product | **غترة العطار**: white, **Swiss-made, 100% cotton**, sizes 50–62, "تشارككم الأفراح لأكثر من 80 عاماً". Also sold by multi-brand retailers in KSA and Kuwait (e.g. [Al Rawassi](https://alrawassi.com.sa/%D8%BA%D8%AA%D8%B1%D8%A9-%D8%A7%D9%84%D8%B9%D8%B7%D8%A7%D8%B1-%D8%A5%D9%84%D9%8A%D8%AC%D9%86%D8%AA/p1312977412), [Hsate](https://hsate.com.sa/en/%D9%85%D8%AD%D9%85%D8%AF-%D8%B3%D8%B1%D8%A7%D8%AC-%D8%A7%D9%84%D8%B9%D8%B7%D8%A7%D8%B1-%D8%A7%D8%AE%D9%88%D9%8A%D9%87/brand-1870715699), [Al Faisal](https://alfaisal1-sa.com/%D9%85%D8%AD%D9%85%D8%AF-%D8%B3%D8%B1%D8%A7%D8%AC-%D8%B9%D8%B7%D8%A7%D8%B1-%D9%88-%D8%A3%D8%AE%D9%88%D9%8A%D9%87/brand-1714003804), [Shumaghy](https://shumaghy.com/en/%D9%85%D8%AD%D9%85%D8%AF-%D8%B3%D8%B1%D8%A7%D8%AC-%D8%B9%D8%B7%D8%A7%D8%B1-%D9%88%D8%A3%D8%AE%D9%88%D9%8A%D9%87/brand-625136840), [Al Mubarkiya, Kuwait](https://almubarkiya.com/almubarkiya_store/%D9%85%D8%AD%D9%85%D8%AF-%D8%B3%D8%B1%D8%A7%D8%AC-%D8%B9%D8%B7%D8%A7%D8%B1-%D9%88%D8%A3%D8%AE%D9%88%D9%8A%D9%87/)) | [Verified] product page; [Secondary] retailers |
| Visual identity | Deep green (store `theme-color` **#004738**) with a gold calligraphic "سراج عطار" roundel. Green gift box with gold foil. | [Verified] store HTML, `research/evidence/store_price_display_2026-10-04.png` |

**Implication.** The founder-to-grandchildren line (Makkah → Jeddah → Riyadh) is a real, three-generation story that no competitor can match. Ajlan & Bros dates from 1979, Lomar from 2002 and Desar from about 2000. Lead with "80+ years" and use the dated milestones (1377H, 1389H) as proof points. Do not use "85".

### 1.2 Branches (store page "فروعنا") [Official]

All branches share one unified number, 920007805, with extensions. WhatsApp uses the same number. Source: [فروعنا](https://sirajattarbros.com/ar/فروعنا/page-91100985).

| City | Branch | Ext. |
|---|---|---|
| Riyadh | Deira, al-Thumairi Street (the historic 1389H branch) | 205 |
| Riyadh | Olaya Street, Sircon buildings (عمائر السيركون) | 206 |
| Riyadh | Anas bin Malik Street, al-Malqa | 209 |
| Riyadh | al-Rawdah, al-Hasan bin Ali Street | n/a |
| Jeddah | al-Balad, Souq al-Nada, behind al-Malika building | 202 |
| Jeddah | Prince Mohammed bin Abdulaziz St (Tahlia), Riyadh Plaza | 203 |
| Jeddah | Hail Street, al-Amal Plaza | 207 |
| Makkah | al-Aziziyah, Masjid al-Haram Road | 204 |
| Khobar | al-Khobar al-Shamaliyah, King Abdulaziz Road (between St 19 and 20) | 208 |

There are 9 branches. That makes geo-targeting realistic for Riyadh, Jeddah, Makkah and the Eastern Province, along with "visit the branch" CTAs. The **al-Balad branch in historic Jeddah** is a natural heritage shoot location.

### 1.3 Online store facts [Verified 2026-10-04]

- **Platform:** Salla (assets on `cdn.salla.sa`). Arabic and English are enabled. The catalogue holds 123 products in 20 categories (scrape of 2026-09-28).
- **Payments offered:** `mada`, `credit_card`, `stc_pay`, `apple_pay`, `tabby_installment`, `tamara_installment`, `cod`. The product page shows Tamara ("44.92 ⃁ شهريًا حتى 3 أشهر") and Tabby ("13.17 ⃁/شهر على 12 دفعة") widgets, plus an Apple Pay button.
- **Currency display:** `use_sar_symbol: true`. The symbol renders to the **left** of the number (⃁ 134.76), as SAMA requires. `arabic_numbers_enabled: false`, so the store uses Western digits.
- **Tracking:** a Google Tag Manager container (`GTM-TGFC6FV`) is present, and Hotjar is listed in the cookie configuration. No Snap/TikTok/Meta pixel code appears in the raw HTML, so pixels are probably injected through GTM or Salla's native integrations. **This needs an audit before launch to avoid double-firing or missing CAPI** (see 5.5).
- **Prices are shown before VAT.** The page meta has `product:pretax_price:amount` equal to the displayed price. Multiplying by 1.15 gives clean figures in most cases:

| Product | Displayed now | × 1.15 (likely checkout total) |
|---|---|---|
| شماغ العطار كلاسيك عنبر | 221.74 (was 256.52) | **255.00** (was 295.00) |
| شماغ العطار كلاسيك مرجان | 208.70 | **240.00** |
| قماش العطار 265 (Japanese) | 113.04 | **130.00** |
| شال باشمينا Q1S55 | 886.96 | **1,020.00** |
| جوارب وثير | 17.39 | **20.00** |
| شماغ العطار كلاسيك عقيق | 240.21 (was 282.60) | 276.24 (was 325.00; the 15% National Day discount is applied to the pre-VAT price) |

Rule for the poster team: **check one item in the cart before typesetting.** Under Saudi VAT practice, a price shown without a VAT note is presumed to include VAT ([Secondary] [ClearTax KSA VAT](https://www.cleartax.com/sa/vat-rates-saudi-arabia)), so an ad price below the checkout total is a compliance and trust risk.

### 1.4 Social accounts

| Platform | Handle | Size (checked 2026-10-04) | Activity | Source |
|---|---|---|---|---|
| Instagram | @sirajattarbros | **≈16K followers** (15.6K in the logged-out UI), 1,009 posts, follows 0 | Posted 3 Oct 2026, 22 Sep (×3, National Day), Aug 4–6 (perfume reels), June | [Verified] [profile](https://www.instagram.com/sirajattarbros/); `research/evidence/instagram_sirajattarbros_2026-10-04.png` |
| Snapchat | @sirajattarbros (public business profile, "Retail company") | Subscriber count **not public** | 1 public Story snap on 3 Oct 2026; 14 saved highlights; 8 Spotlight posts (Nov 2025 – Jun 2026) | [Verified] [profile](https://www.snapchat.com/add/sirajattarbros) |
| TikTok | **@m.sirajattar** (note: not @sirajattarbros) | **728 followers, 2,076 likes, 65 videos** | Low | [Verified] [profile](https://www.tiktok.com/@m.sirajattar) |
| X | @SirajAttarBros | **≈9.7K followers** | Collection launches, Ramadan fabric exhibition, family-heritage posts | [Secondary] search snapshot; [X](https://x.com/SirajAttarBros) |
| Facebook | two pages (`sirajattarbross`, `SirajAttarBros`) | n/a | Not checked (login wall); low priority | [Secondary] search results |
| Linktree | linktr.ee/msirajattar | n/a | Hub for all bios | [Verified] |

A TikTok handle **@sirajattarbros** exists with 1 follower and no videos. Ask the client whether they own it. Moving to one handle everywhere would help search and recall.

### 1.5 What the current content looks like

- **Format.** Mostly static posters in the brand's deep green with gold, plus some product photography and a few perfume reels. There is very little video of people wearing the product, very little styling or "how to" content, and almost no creator or UGC content.
- **Themes (last 4 months).** Perfume launch ("Attar 1/2/3 Eau de Parfum", "احصل عليه الآن بخصم 20%") in early August. National Day 96 ("عزنا بطبعنا", extended offers "لأن الوطن غالٍ مددنا عروضنا"). A Hijri New Year greeting. Classic-collection gemstone names on X (عنبر صافي، ياقوت، مرجان صافي، عقيق).
- **Register.** Mostly Fusha headlines, with orthographic slips and dialect forms creeping in. Examples: "أطلب الآن وأغتنم الفرصة" (should be اطلب… واغتنم) and "اشتريها معًا" (colloquial imperative; Fusha would be "اشترِها معًا").
- **Instagram highlights** are utility-led: طريقة الطلب، الفروع، الأقمشة، الأشمغة، الغتر، التواصل.
- **Diagnosis.** The feed shows that the house has heritage but not how it makes the product. That matches the client feedback ("80+ years of craft. Every post should show it" and "HOW?").

---

## 2. Competitors in KSA and how they advertise

### 2.1 Landscape

| Segment | Player | What they are | How they advertise / what stands out | Source |
|---|---|---|---|---|
| Headwear house | **Ajlan & Bros (عجلان وإخوانه)** | Founded 1979 in Riyadh's Deira souq by four brothers. Brands: **Brouge (بروجيه)**, السامي, Drosh (دروش), **Maybach (ميباج)**, plus licensed-luxury shemaghs (Versace, Lamborghini, Ferrari, Maserati, Aston Martin, Cavalli, Missoni, Kenzo, Iceberg). Forbes Top 100 Arab Family Businesses 2025. | Heaviest social spender in the category. **TikTok 138.7K followers / 1.6M likes / 299 videos**, Instagram ≈42K, **verified Snapchat** with 5.1K public subscribers and weekly Spotlight posts (Mar–May 2026). Teaser launches ("شماغ ميباج.. هيبة حضور"), giveaways (iPhone and shemagh prizes), licensed brand names. Own e-store ajstore.com. | [Verified] TikTok/Snap; [Secondary] [Wikipedia AR](https://ar.wikipedia.org/wiki/%D8%B9%D8%AC%D9%84%D8%A7%D9%86_%D9%88%D8%A7%D8%AE%D9%88%D8%A7%D9%86%D9%87_(%D8%B4%D8%B1%D9%83%D8%A9)), [Forbes ME](https://www.forbesmiddleeast.com/ar/lists/top-100-arab-family-businesses-2025/ajlan-bros-holding/), [Maaal](https://maaal.com/archives/202203/%D8%B4%D9%85%D8%A7%D8%BA-%D9%85%D9%8A%D8%A8%D8%A7%D8%AC-%D9%87%D9%8A%D8%A8%D8%A9-%D8%AD%D8%B6%D9%88%D8%B1-%D9%88-%D8%A8%D8%B5%D9%85%D8%A9-%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9-%D9%81%D9%8A-%D8%B9%D8%A7/) |
| Headwear brand | **Al Bassam (شماغ البسام)** | From Mohammed Al-Saad Al-Ajlan Sons (أبناء محمد السعد العجلان). English-made. Positioned as "international quality at an attractive price". One of the best-selling red shemaghs. | Sold mostly through multi-brand stores and Gulf retailers; little direct social presence (the TikTok handle is empty) | [Secondary] [Al Ajlan Online](https://alajlanonline.com/), [Oqily](https://oqily.com/en/blog/shemagh-albassam/a-648320302) |
| Headwear brand | **Desar (دسار)** | Local premium red shemagh, about 25 years old | Instagram ≈12K. **Year-numbered and limited editions** (e.g. "كلاسيكي فينتج 2025/58", Royal, الشيوخ, Winter edition, 25th-anniversary edition), "أيقونة الزي الوطني". Sold on Amazon.sa. | [Secondary] [Instagram](https://www.instagram.com/desar.shemagh/), [Amazon.sa](https://www.amazon.sa/-/en/Fashion-Desar/s?rh=n%3A12463219031%2Cp_4%3ADesar) |
| Licensed luxury shemagh | Dunhill, Givenchy, Valentino, Pierre Cardin, Bentley, Ferrari, Tessuti | The aspirational tier (often Swiss, English or Italian-made) | Price signal and brand halo; sold through multi-brand stores | [Secondary] [Luxury AV](https://luxuryav.net/Saudi-men's-shemagh), [Al Rawassi blog](https://alrawassi.com.sa/blog/%D9%85%D8%A7%D8%B1%D9%83%D8%A7%D8%AA-%D8%A7%D9%84%D8%B4%D9%85%D8%A7%D8%BA-%D8%A7%D9%84%D9%85%D8%AD%D9%84%D9%8A%D8%A9/a-2037591590) |
| Local value shemagh | Rasem (رسم), Castle (كاستل, Madinah factory), Shahin, Kahraman, Sayar | Value and mid-market | Price-led | [Secondary] same |
| Thobe brand | **Lomar (لومار)** | Jeddah, 2002, design-led modern thobes; one of the Fashion Commission's "100 Saudi Brands" (2022); sponsored the Italian Super Cup in Jeddah (2019) | Fashion-press PR, sponsorships, X ≈31.6K, Facebook ≈57K; small TikTok (924) | [Secondary] [Arab News](https://www.arabnews.com/node/2397841/lifestyle), [MBSC case](https://www.mbsc.edu.sa/wp-content/uploads/2023/10/Case-Study-Lomar-Final.pdf); [Verified] TikTok |
| Thobe brands | Al Dafah (الدفة), Al Aseel (الأصيل), Al Shiaka (الشياكة), Toby | Ready-made thobes | Seasonal Eid and gifting pushes | [Secondary] [Hia mag](https://www.hiamag.com/%D9%87%D9%88/%D9%85%D9%88%D8%B6%D8%A9/1380976-%D8%AE%D9%85%D8%B3-%D9%85%D8%A7%D8%B1%D9%83%D8%A7%D8%AA-%D8%AB%D9%8A%D8%A7%D8%A8-%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9-%D9%84%D8%A7%D8%AE%D8%AA%D9%8A%D8%A7%D8%B1-%D9%87%D8%AF%D9%8A%D8%A9-%D9%8A%D9%88%D9%85-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85%D9%8A) |
| Fabric houses | Mills: **Toyobo, Shikibo, Ichimura Sangyo, Richie** (Japanese). Retailers: Al Sultan, Al Tamimi, Al Rammah, Emtex and many Salla stores | Thobe fabric by the metre | SEO blogs ("أفضل قماش ياباني"), price promotions, Ramadan pushes | [Secondary] [Mansuj](https://mansuj.com/blog/%D8%A3%D9%81%D8%B6%D9%84-%D9%85%D8%A7%D8%B1%D9%83%D8%A7%D8%AA-%D8%A7%D9%84%D8%A3%D9%82%D9%85%D8%B4%D8%A9-%D8%A7%D9%84%D9%8A%D8%A7%D8%A8%D8%A7%D9%86%D9%8A%D8%A9/a-1046115959), [Emtex](https://emtex.com.sa/%D8%A3%D9%82%D9%85%D8%B4%D8%A9-%D8%B1%D8%AC%D8%A7%D9%84%D9%8A%D8%A9-%D9%84%D9%84%D8%AB%D9%8A%D8%A7%D8%A8-%D9%85%D8%B5%D8%A7%D8%AF%D8%B1-%D9%88%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA/) |
| Multi-brand e-stores (also resellers of Siraj Attar) | Al Rawassi, Hsate (فخامة رجل), Al Faisal, Shumaghy, Shemagh Shop, Oqily, Al Mutameez | Compete on range, delivery and content | Heavy SEO content: "best shemagh 2026" lists and ترسيمة tutorials | [Secondary] links above, [Shemagh Shop](https://shemaghshop.sa/ar/blog/tarsimet-al-cobra-thabat-al-shmagh/a-1984957567) |

### 2.2 Market size and price bands

- Saudis spend about **⃁ 4.5bn on thobes during Ramadan alone**. Shemagh and ghutra sales exceed **⃁ 1.5bn a year**. About **15M metres** of fabric are used in the Ramadan/Eid season. The average buyer gets about 4 thobes a year. There are about 13,000 licensed men's tailors. Japanese fabric prices have risen more than 100% in five years, and lower-cost Chinese, Korean, Thai and Indonesian fabrics have gained share. Only about 10% of shemaghs are made locally. Source: [Secondary] [Asharq Al-Awsat, Apr 2024](https://aawsat.com/%D9%8A%D9%88%D9%85%D9%8A%D8%A7%D8%AA-%D8%A7%D9%84%D8%B4%D8%B1%D9%82/4950836-%D8%A7%D9%84%D8%AB%D9%88%D8%A8-%D8%A7%D9%84%D8%B1%D8%AC%D8%A7%D9%84%D9%8A-%D9%8A%D9%83%D9%84%D9%81-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%8A%D9%86-45-%D9%85%D9%84%D9%8A%D8%A7%D8%B1-%D8%B1%D9%8A%D8%A7%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%B9%D8%A7%D9%85).
- **Shemagh price bands** [Secondary] [Luxury AV](https://luxuryav.net/Saudi-men's-shemagh):

  | Band | Brands | Price range (⃁) |
  |---|---|---|
  | Value | Kahraman | 94–180 |
  | Local mid | Shahin; Rasem | 165–220; 220+ |
  | Licensed luxury | Pierre Cardin; Ferrari; Bentley; Valentino; Tessuti | 323–370; 310–690; 414–439; 423–565; 498–586 |

  Siraj Attar's shemaghs come to about **⃁ 240–295 including VAT**, which is the upper-local band. That leaves room to argue **"heritage-house quality at local-premium prices"** against the licensed tier.

### 2.3 Advertising patterns in the category [Secondary + Verified]

1. **Annual numbered editions and gemstone or collection names.** Desar uses "2025/58" and Siraj Attar already uses "نقش العطار 26" and "ختم العطار 26". This yearly "new season" ritual is the category's main lever.
2. **Licensed foreign luxury names** (Ajlan) as a shortcut to prestige.
3. **Giveaways and teaser launches** on Snapchat, TikTok and X (Ajlan's Maybach launch).
4. **Styling tutorials** (ترسيمة الكوبرا، الصقر) are made mostly by multi-brand stores as blog and TikTok SEO content, not by the houses themselves.
5. **National moments** (National Day, Founding Day, Ramadan/Eid) using heritage visuals. The rules on national symbols apply (section 6).

### 2.4 Gaps Siraj Attar can own

| Gap | Why it is open | Proposal angle |
|---|---|---|
| **The oldest living merchant story** | Ajlan dates from 1979 and Lomar from 2002. Only Siraj Attar has Makkah trading roots, a Jeddah branch from 1377H and a Riyadh branch from 1389H. | "80+ years of craft. Every post should show it." Heritage series: three generations, the Deira and al-Balad shops, the old ledger. |
| **The white ghutra specialist** | Competitor noise is about the red shemagh. The Swiss-made Attar ghutra is the house's signature and is also stocked by Gulf retailers. | Own the white season and occasions: Eid morning, weddings, summer, formal business. Use the line "غترة العطار" as the hero. |
| **Head to toe from one house** | Headwear, thobe fabric, wool, shawls, perfume and underwear usually come from different brands. Siraj Attar sells all of them. | A "complete look" bundle or gift box: Eid kit, groom kit, winter kit. Raise AOV with Tabby or Tamara instalments. |
| **The HOW (client feedback)** | No house explains its craft. Only resellers post tutorials. | Short "how" videos: the مرزام crease, ironing at 110 °C (from the product care notes), Japanese vs Korean fabric, Super 130 vs 150 wool, how many metres a thobe takes. A clear before/after in 2 seconds. |
| **Short-form video** | TikTok 728 followers vs Ajlan's 138.7K. Snapchat Spotlight posts are rare. | A weekly 9:16 "ترسيمة اليوم" series, Spark Ads, creator collaborations (licensed under Mawthooq; section 6). |
| **Winter wear** | English (William Halstead) and Italian (Dolfino, Angelico) wools and pashmina shawls are rare in the category. | Sequence content with the traditional seasons: الوسم, then المربعانية, then الشبط (section 4). |
| **Register discipline** | Category copy is a mix of Fusha and dialect. | Two clean registers, A/B-tested (sections 5.7 and 7). |

---

## 3. The Saudi riyal symbol: official guidance and typesetting rules

### 3.1 Official facts

- **Approved** by King Salman on **21/08/1446H = 20 Feb 2025** and announced by SAMA. It reads "ريال" in calligraphy-inspired letters (lam, alif, raa, yaa). [Official] [SAMA](https://www.sama.gov.sa/en-US/Currency/SRS/Pages/default.aspx)
- **Official documents** are downloaded into `data/sama/` [Official, Verified]:
  - `Guidelines_ar.pdf`: "الدليل الإرشادي لرمز الريال السعودي / Saudi Riyal Symbol Guidelines", 22 pp, **creation date 2026-02-10**. [link](https://www.sama.gov.sa/ar-sa/Currency/SRS/Documents/Guidelines.pdf)
  - `Font_Designers_Guidelines.pdf`: "إرشادات مصممي الخطوط", 33 pp, dated 2026-01-13. [link](https://www.sama.gov.sa/ar-sa/Currency/SRS/Documents/Font_Designers_Guidelines.pdf)
  - `Saudi_Riyal_Symbol-2.svg`: the **official vector** (viewBox 1124.14 × 1256.39, two paths, fill #231f20). [link](https://www.sama.gov.sa/ar-sa/Currency/Documents/Saudi_Riyal_Symbol-2.svg). PNG and EPS are also on the [guideline page](https://www.sama.gov.sa/en-US/Currency/SRS/Pages/Guideline.aspx).
  - The SVG has the same geometry as `brand/riyal.png`. **Use the SVG directly; do not trace the PNG.**

### 3.2 SAMA's 10 usage rules (Guidelines PDF pp. 16–17)

Screenshots are in `research/evidence/sama_usage_rules_ar.png` and `sama_usage_rules_en.png`. Note that press articles from 2025 list "8 rules". The 2026 guideline adds Written Value and Negative Value.

| # | Arabic heading | English | Rule |
|---|---|---|---|
| 1 | الموقع | Position | "يكون الرمز دائمًا يسار القيمة العددية لجميع اللغات". **Always LEFT of the number, in every language.** "123 ⃁" is marked wrong. |
| 2 | المسافة | Spacing | "ترك مسافة بين الرمز والقيم العددية". **There must be a space.** "⃁123" (touching) is marked wrong. |
| 3 | القيمة المكتوبة | Written value | The symbol goes to the left of the whole written value. Arabic: **"123 مليون ⃁"** (symbol last, at the far left). Latin: "⃁ 123 million". Putting the symbol between the number and the word is wrong. |
| 4 | القيمة السالبة | Negative value | The symbol goes to the left of both the minus sign and the number. Arabic shows "⃁ 123-"; Latin shows "⃁ -123". |
| 5 | التناسب | Proportions | Keep the shape's proportions. No stretching. |
| 6 | البنية الهندسية | Geometry | Keep the geometric structure. No redrawing or mirroring of strokes. |
| 7 | المحاذاة | Alignment | "مطابقة ارتفاع الرمز مع ارتفاع النص": **the same height as the text.** A symbol shown smaller than the numerals is marked wrong. |
| 8 | الاتجاه | Direction | The symbol's direction must follow the text. Never flip it horizontally. |
| 9 | المساحة الخالية | Negative space | Keep clear space equal to **one third of the symbol's height** around it when it sits inside a shape, such as a badge or circle. |
| 10 | تباين الألوان | Contrast | There must be **sufficient contrast** with the background. A low-contrast tint is marked wrong. |

**Colour:** SAMA sets no colour. The examples use the guideline's grey-green and white-on-dark. The only requirement is contrast. [Official, Verified]

### 3.3 Size, alignment and spacing in detail (Font Designers' Guidelines) [Official]

- **Vertical alignment.** "The top of the Lam should align with the top of Latin numerals. The bottom of the Lam sits on the baseline." The yaa's dots (the lowest slanted stroke) **fall below the baseline**. If Arabic-Indic digits sit higher than the baseline, the alif can be aligned with the top of the numerals instead.
- **Spacing.** The symbol needs ample white space. In a normal-weight font, its side bearing should be at least **1.5 × the gap between the alif and the lam**. Lighter weights need less and heavier weights need more.
- **What may be adapted.** Weight, width (within limits), stroke contrast (thin verticals, thick slants, "as is typical in Arabic"), terminal style (rounded or sharp) and effects (outline, texture, brush), as long as the construction and proportions stay the same. Extreme compression or contrast that "no longer feels Arabic" is discouraged.
- The symbol must work with **both Arabic and Latin numerals** and sit comfortably alongside $, £ and €.

### 3.4 Arabic and Latin contexts: the RTL trap [Verified]

- U+20C1 has Unicode bidi class **ET (European Terminator)** and general category Sc. Verified against [UnicodeData.txt 17.0](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt): `20C1;SAUDI RIYAL SIGN;Sc;0;ET`.
- In an **Arabic (RTL) paragraph**, typing "⃁ 150" in logical order makes the symbol appear on the **right**, which is wrong. Typing "150 ⃁" in logical order makes it appear on the left, which is correct. In an **English (LTR)** paragraph, type "⃁ 150".
- **Robust rule for HTML and PDF:** wrap every price in an LTR isolate, `<span dir="ltr">⃁ 150</span>` (or LRI U+2066 … PDI U+2069), whichever language surrounds it. For **posters**, place the SVG yourself, always on the visual left.
- The SAMA examples, including the Arabic page, use **Western digits** ("123"), and the client store has Arabic-Indic digits switched off. Use **Western digits in both registers.**

### 3.5 Unicode and font support (as of Oct 2026)

| Item | Status | Source |
|---|---|---|
| Code point | **U+20C1 SAUDI RIYAL SIGN**, Currency Symbols block | [Official] Unicode |
| Encoded in | **Unicode 17.0, released 9 Sep 2025** | [Secondary] [Wikipedia](https://en.wikipedia.org/wiki/Saudi_riyal_sign) |
| CLDR | CLDR 48 (Oct 2025) lists ⃁ as an **alternate** symbol, not the default, because font support is limited. Software may still output "ر.س" or "SAR" by default. | [Secondary] [Wikipedia](https://en.wikipedia.org/wiki/Saudi_riyal_sign), [h-haboubi](https://h-haboubi.com/blog/others/new-saudi-riyal-symbol-guide/) |
| Windows 11 | Arabic keyboard support since Dec 2025 (AltGr+S, reported). **Checked on this machine:** Arial, Segoe UI, Tahoma, Times New Roman, Calibri, Courier New, Consolas, Microsoft Sans Serif, Traditional Arabic, Arabic Typesetting, Sakkal Majalla, Simplified Arabic, Andalus and Aldhabi include U+20C1. | [Verified] font scan; [Secondary] [UltraTextGen](https://ultratextgen.com/updates/uae-dirham-symbol-unicode-18/) |
| iOS | On the iPhone keyboard since March 2026 (user reports) | [Secondary] same |
| Android / Google Noto | The request to add it to Noto Arabic was **still open** at last report | [Secondary] same |
| Web fonts | Community fonts: [Saudi-Riyal-Font](https://github.com/emran-alhaddad/Saudi-Riyal-Font) (U+20C1 plus legacy PUA U+E900) and [riyal.js](https://riyal.js.org/) | [Secondary] |
| Project `fonts/` folder | Empty at the time of writing. Most Arabic display fonts (IBM Plex Sans Arabic, Noto) **cannot be assumed** to include the glyph. | [Verified] |

### 3.6 House rules for prices in this project

1. **Symbol:** the official SVG, always on the **visual left** of the number, in both the Fusha and Saudi versions and in the English deck.
2. **Gap:** one word space of the numeral font, about **0.25–0.30 em**. Never zero and never a wide gap. When the symbol sits inside a badge or circle, keep clear space of at least ⅓ of the symbol's height.
3. **Height:** the lam's top lines up with the **top of the Western numerals** and its foot sits on the numerals' baseline. The yaa's dots drop slightly below the baseline. Never make the symbol a superscript or smaller than the numerals.
4. **Colour and weight:** the same colour as the numerals (gold on green, or green or black on ivory) with WCAG-level contrast. Match the visual weight of bold numerals; a hairline stroke in the same colour is acceptable. No gradients that reduce contrast and no outline-only symbol at small sizes.
5. **Never** write "ر.س", "SAR" or "ريال" next to the symbol. Never put the symbol to the right of the number. Never flip it.
6. **Old and new prices:** the new price is the larger figure. The old price is smaller, struck through **including its symbol**, and placed after the new price in reading order. In Arabic posters that means to its left, or underneath.
7. **Value:** show the **VAT-inclusive price the customer pays** (section 1.3) and copy it exactly, halalas included, unless the store price is round. Do not round.
8. **Instalments:** "أو 4 دفعات ⃁ 63.75 مع تابي" is fine as a secondary line. Apply the same symbol rules.

---

## 4. Saudi seasonal calendar, October 2026 – April 2027

### 4.1 Hijri month map 1448H (Umm al-Qura; Ramadan, Shawwal and Dhu al-Hijjah depend on moon sighting ±1 day)

[Secondary] [MakkahLive](https://makkahlive.net/en/tools/islamic-calendar), cross-checked against the MoF site (Sun 4 Oct 2026 = 23/04/1448) and the MoE school calendar (Founding Day = 15 Ramadan).

| Month | Starts | Month | Starts |
|---|---|---|---|
| Jumada I | Mon 12 Oct 2026 | Sha'ban | Sat 9 Jan 2027 |
| Jumada II | Wed 11 Nov 2026 | **Ramadan** | **Mon 8 Feb 2027** |
| Rajab | Thu 10 Dec 2026 | **Shawwal (Eid al-Fitr)** | **Tue 9 Mar 2027** |
| | | Dhu al-Qa'dah | Thu 8 Apr 2027 |

### 4.2 Dated calendar

| Date (2026–27) | Moment | Type | Notes | Source |
|---|---|---|---|---|
| Fri 16 Oct → Sun 6 Dec | **الوسم** (52 days: العواء 16 Oct, السماك 29 Oct, الغفر 11 Nov, الزبانا 24 Nov) | Traditional season | The first cool nights, called "عواء البرد" in Najdi lore. **Shemagh season opener.** | [Secondary] [Sabq (al-Musnad)](https://sabq.org/saudia/9tpnralqns), [SPA](https://www.spa.gov.sa/1039469) |
| **Wed 21 Oct** | **Riyadh Season 2026 opens** (7th edition, "Big Time", 10 weeks, so about the end of Dec; earlier editions ran into Q1) | Event | Evening outings in Riyadh (4 branches). Boxing, UFC, Six Kings Slam, Boulevard. | [Official] [SPA](https://www.spa.gov.sa/en/N2686677); [Secondary] [Gulf News](https://gulfnews.com/world/gulf/saudi/riyadh-season-2026-to-begin-on-october-21-with-10-weeks-of-entertainment-1.500689955) |
| **Tue 27 Oct** | Government salary day | Pay | | [Official] [MoF 2026](https://www.mof.gov.sa/mediacenter/Payroll/Pages/2026.aspx) |
| Wed 11 Nov | 11.11 sales | Retail | Teaser for White Friday | [Secondary] |
| **Fri 20 – Sat 28 Nov** | **School autumn break** (9 days) | School | Family trips and gatherings | [Secondary, citing MoE] [Wego](https://rahhal.wego.com/blog/%D8%A7%D9%84%D8%AA%D9%82%D9%88%D9%8A%D9%85-%D8%A7%D9%84%D8%AF%D8%B1%D8%A7%D8%B3%D9%8A-1448-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9-%D8%A7%D9%84%D8%A7%D8%AC%D8%A7%D8%B2%D8%A7%D8%AA/) |
| ≈Fri 20 – Mon 30 Nov | **White Friday** (Amazon.sa) / Yellow Friday (noon) | Retail | Amazon early access from 20 Nov | [Secondary] [GetWafarna](https://www.getwafarna.com/en/article/black-friday-2026-date) |
| **Thu 26 Nov** | Government salary day (the 27th is a Friday, so it moves to the Thursday) | Pay | **Salary, then White Friday the next day, inside the school break: the strongest discount window** | [Official] MoF |
| **Fri 27 Nov** | Black / White Friday | Retail | Cyber Monday is 30 Nov | [Secondary] |
| **Mon 7 Dec → Fri 15 Jan** | **المربعانية** (40 days, the coldest stretch) | Traditional season | Wool, shawls, heavy shemagh, darker winter thobes | [Secondary] [Saudi Calendars](https://saudicalendars.com/events/%D9%81%D8%B5%D9%84-%D8%A7%D9%84%D8%B4%D8%AA%D8%A7%D8%A1-2026/), [SaudiSalary](https://saudisalary.com/season/marba) |
| Thu 10 Dec | 1 Rajab | Hijri | **Eid-thobe preparation starts (Rajab to mid-Ramadan)** | [Secondary] Asharq Al-Awsat (above) |
| Mon 21 Dec | Winter solstice | Astronomical | | [Secondary] |
| **Sun 27 Dec** | Government salary day | Pay | | [Official] MoF |
| **Fri 8 – Sat 16 Jan 2027** | **School mid-year break** | School | Desert camping (كشتات), family gatherings, weddings | [Secondary, MoE] Wego |
| ≈16 Jan → ≈10 Feb | **الشبط** (26 days) | Traditional season | Still cold | [Secondary] |
| **Wed 27 Jan** | Salary day (by MoF rule; the 2027 list is not yet published) | Pay | **Main fabric-buying salary before Ramadan** | [Estimate] from MoF rule |
| **Mon 8 Feb** | **1 Ramadan 1448** (expected) | Religious | Shopping moves to after iftar, about 8 pm – 2 am | [Secondary] [Arab News](https://www.arabnews.com/node/2636507), [Gulf Business](https://gulfbusiness.com/ramadan-2025-snap-menas-georges-odeimi-on-trends/) |
| ≈10/11 Feb → ≈20 Mar | **العقارب** (39 days) | Traditional season | End of winter | [Secondary] |
| Fri 19 – Mon 22 Feb | School Founding Day long weekend | School | | [Secondary, MoE] Wego |
| **Mon 22 Feb (≈15 Ramadan)** | **Founding Day (يوم التأسيس)** | National | **Falls in mid-Ramadan in 2027**, so the tone must suit Ramadan. Heritage dress is the theme. | [Official] annual date 22 Feb |
| ≈22 Feb | Tailors stop taking new Eid orders (around mid-Ramadan; in some cities as early as the first quarter of Ramadan) | Trade | **Fabric sales collapse after this point; ready-made, headwear, perfume and gifts take over** | [Secondary] [Al Watan](https://www.alwatan.com.sa/article/1074646), Asharq Al-Awsat |
| Fri 26 Feb → Sat 13 Mar | School Eid al-Fitr break (19 Ramadan – 5 Shawwal) | School | The longest family window (19 Feb – 13 Mar, with only 3 school days between breaks) | [Secondary, MoE] Wego |
| **Sun 28 Feb** | Salary day (the 27th is a Saturday, so it moves to Sunday; may be brought forward before Eid by directive) | Pay | Last-10-nights shopping | [Estimate] MoF rule |
| ≈Fri 5 – Sat 6 Mar | Last orders for delivery before Eid (allow 2–3 days) | Ops | Use a **countdown creative** | [Estimate] |
| **Tue 9 Mar** | **Eid al-Fitr 1448** (expected) | Religious | Private sector about 9–12 Mar; government longer | [Secondary] [Time and Date](https://www.timeanddate.com/holidays/saudi-arabia/eid-al-fitr), [Officeholidays](https://www.officeholidays.com/holidays/saudi-arabia/eid-al-fitr) |
| 9 Mar → 7 Apr | **Shawwal: wedding season** | Social | Weddings cluster after Ramadan, in school breaks and on Thursday nights. Wedding halls report summer and spring as the busiest periods. | [Secondary] [Zafaf](https://saudi-arabia.zafaf.net/wedding-venues/ideas/choose-wedding-hall-saudi-arabia-2026-guide-1836); [Estimate] Shawwal peak |
| **Sun 28 Mar** | Salary day (the 27th is a Saturday) | Pay | | [Estimate] MoF rule |
| **Tue 27 Apr** | Salary day | Pay | | [Estimate] MoF rule |

**Salary rule [Official]:** government salaries are paid on the 27th of each Gregorian month. If the 27th is a Friday, they are paid the Thursday before. If it is a Saturday, they are paid the Sunday after ([MoF](https://www.mof.gov.sa/mediacenter/Payroll/Pages/2026.aspx)). Private-sector pay dates vary, typically between the 25th and the 1st.

### 4.3 Which moments matter most for this category, and why

1. **The Eid al-Fitr run-up (Sha'ban to Ramadan, 9 Jan – 8 Mar 2027). This is the biggest moment.** Eid means new clothes from head to toe. The order of demand matters: **fabric first** (Rajab–Sha'ban, before tailors close around 15 Ramadan), then **shemagh, ghutra, agal, perfume and gift boxes** through the last ten nights. Ramadan CPMs run about 68% higher ([Secondary] [BIMO](https://www.bimogroup.co/blog/meta-ads-benchmarks-gulf.html)), so build audiences in January, when Q1 is the cheapest window.
2. **Winter onset (الوسم, 16 Oct, to المربعانية, 7 Dec – 15 Jan): the shemagh season.** The red shemagh dominates winter and the white ghutra summer and formal occasions ([Secondary] [Ashabelia](https://ashabelia.ae/shemagh/), [Saudipedia](https://saudipedia.com/en/what-is-the-difference-between-shemagh-and-ghutra)). This is the natural launch for new-season shemaghs (نقش العطار 26). In December, add wool and pashmina. The traditional season names make native, dialect-friendly hooks: "دخل الوسم", "دخلت المربعانية".
3. **26–30 November: salary, then White Friday, inside the autumn break.** This is the most price-sensitive window, and CPMs rise 30–50%. Use bundles (shemagh, perfume and وثير) and Tabby/Tamara messaging. **Do not discount the heritage hero lines heavily.** Bundle instead.
4. **The 27th of each month.** Plan bursts on 26–29 Oct, 26–30 Nov, 27–31 Dec, 27–31 Jan and 28 Feb – 6 Mar.
5. **Founding Day (22 Feb, in mid-Ramadan).** This is the best brand fit of the year: heritage, traditional dress, "since before most brands existed". It must look like Ramadan (night, majlis, family) and must not use the flag, emblem or images of leaders (section 6).
6. **Riyadh Season (21 Oct – about end Dec).** Outfit occasions for Riyadh, where the house has 4 branches. Use geo-targeting and evening dayparts.
7. **Mid-year break (8–16 Jan) and the Shawwal wedding season (Mar–Apr).** Camping and winter-wear content in January. Groom kits (white ghutra, fabric, perfume, gift box) and guest gifting from Shawwal onward.

---

## 5. Media buying in KSA, 2025–2026

### 5.1 Reach (DataReportal *Digital 2026: Saudi Arabia*, ad-audience data, early 2026)

[Secondary] [DataReportal](https://datareportal.com/reports/digital-2026-saudi-arabia). Population is 34.7M, internet penetration 99%, and there are 38.6M social media user identities.

| Platform | Ad reach | % of adults 18+ | % male | ≈ male ad reach [Estimate] | Role for this brand |
|---|---|---|---|---|---|
| **Snapchat** | 25.3M | **89.0%** | 55.5% | 14.0M | **Lead** platform: reach, Stories, Spotlight, catalogue/DPA. Snap: "reach 90% of 13–34s in KSA" and users "open the app nearly 50 times a day" ([Snap × Salla](https://forbusiness.snapchat.com/resources/salla)). |
| **TikTok** | 38.6M* | 154%* | 60.9% | (23.5M*) | Video discovery, tutorials, Spark Ads. *The figure exceeds the population; DataReportal publishes it "as is". |
| **YouTube** | 27.5M | n/a | 59.0% | 16.2M | Ramadan and long-form heritage film; reached through PMax/Demand Gen |
| **Instagram** | 18.2M | 71.0% | 58.9% | 10.7M | Brand home, catalogue, Reels, retargeting |
| **Facebook** | 17.7M | 70.0% | 75.7% | 13.4M | Mostly through Meta's Advantage+ placements |
| **X** | 15.0M | 57.2% | 61.4% | 9.2M | Older and opinion-led Saudi men, news and sports. Test for Founding Day and launches. |
| **Google Search** | n/a | n/a | n/a | n/a | **95.44% search share** (StatCounter, Apr 2026). Captures demand for "شماغ", "غترة سويسري", "قماش ياباني". [Secondary] [StatCounter](https://gs.statcounter.com/search-engine-market-share/all/saudi-arabia) |

**Caveat [Estimate]:** these audiences include non-Saudis, who are 44.4% of the population and mostly male. Saudi nationals number 19.6M (GASTAT 2024, [Argaam](https://www.argaam.com/en/article/articledetail/id/1827144)), so the core audience of **Saudi men aged 18–55 is roughly 5 million people**. Ad platforms cannot target by nationality. Use Arabic-language audiences, interests (traditional wear, Saudi culture), lookalikes of buyers and geo-targeting around the branches. Let the creative (Saudi dress, Saudi dialect) do the self-selection.

### 5.2 Cost benchmarks (planning ranges; SAR at the 3.75 peg)

These come from agency blogs, not audited data. Treat them as **hypotheses to validate in weeks 1–2**.

| Platform | CPM | CPC | CPA (fashion / e-com) | Other | Source |
|---|---|---|---|---|---|
| Snapchat | ⃁ 6–18 (one source) up to US$8–15 ≈ ⃁ 30–56 (another) | US$0.15–0.60 ≈ **⃁ 0.55–2.25** | **⃁ 22–60** (optimistic) | ROAS 3–4× | [Ekoinnovations](https://ekoinnovations.com/blog/snapchat-ads-cost-saudi-arabia-2026), [Hovi](https://thehovi.com/blog/agency-insights/performance-marketing-ksa-uae-strategies-roi-2026) |
| TikTok | US$5–12 ≈ **⃁ 19–45** | US$0.20–0.80 ≈ **⃁ 0.75–3.0** | CPL ⃁ 30–94 | ROAS 3–5× | [AdManage](https://admanage.ai/blog/tiktok-ads-cost), Hovi |
| Meta (IG/FB) | US$8–15 ≈ **⃁ 30–56** standard; **US$18–28 in Ramadan**. FB KSA average US$12.01. | Fashion US$0.45–1.20 ≈ **⃁ 1.7–4.5** | IG fashion **⃁ 45–130**; e-com ⃁ 35–110 | IG fashion CTR 1.0–1.8%, CVR 1.8–4.5%; ROAS 3.5–7× | [BIMO](https://www.bimogroup.co/blog/meta-ads-benchmarks-gulf.html), [Lebesgue](https://lebesgue.io/facebook-ads/facebook-cpm-by-country), [Hikmah AI](https://www.hikmahaiagency.com/blog/instagram-ads-benchmarks-saudi-arabia-2026) |
| Google Search | n/a | US$0.80–2.50 ≈ **⃁ 3–9.4** (generic; brand terms are much cheaper) | CPL ⃁ 56–188 | ROAS 4–7× | Hovi |

**Seasonality [Secondary, BIMO]:** Ramadan CPM about +68%. National Day +30–50%. White Friday +30–50%. **January–February is the cheapest acquisition window.** **Language [Secondary, Hovi]:** Arabic creative outperforms English by about 15–25% in KSA. One study cited by the press found 85% of Saudi consumers prefer the non-regional "white" dialect in product marketing ([Thmanyah](https://thmanyah.com/24043/)).

### 5.3 Creative specs and safe zones

| Placement | Ratio / size | Key specs | Safe zone (1080 × 1920 canvas) | Source |
|---|---|---|---|---|
| Snapchat Single Image/Video, Story, Collection | 9:16, 1080×1920 (min 720×1280) | Image ≤5 MB jpg/png. Video mp4/mov H.264 ≤1 GB, 3 s+ (6–10 s recommended; under 3 s loops). Audio required (stereo, about −16 LUFS). Brand name ≤25–32 chars, **headline ≤34 chars**. Collection thumbnails 160×160. | Keep text and logos out of the **top 150 px** and the **bottom 150 px** per Snap's guide. Some guides say bottom 330 px or 15%. Use the stricter value. | [Stackmatix](https://www.stackmatix.com/blog/snapchat-ad-specs), [AdNabu](https://blog.adnabu.com/snapchat/snapchat-ad-specs/) |
| TikTok In-Feed / Spark | 9:16, 1080×1920 (min 540×960) | mp4/mov ≤500 MB, bitrate ≥516 kbps, up to 10 min allowed. Test cuts of 6–15 s [Estimate]. | Varies with caption length and add-ons. **TikTok publishes a right-to-left (Arabic) template; use it.** Typical LTR insets: top about 130, bottom 300–440, right about 120–140, left about 60. | [Recharm](https://www.recharm.com/blog/tiktok-video-ad-specs), [Coinis](https://coinis.com/how-to/design-tiktok-feed-ad) |
| Meta Reels / Stories | 9:16, 1080×1920 | | **Top 14% (≈270 px), bottom 35% (≈670 px), sides 6% (≈65 px).** Design to the Reels bottom margin even for Stories. | [Lucid Media](https://www.lucidmedia.co.nz/blog/instagram-facebook-ad-safe-zones-2026/), [AdsUploader](https://adsuploader.com/blog/meta-ads-safe-zones) |
| Instagram / FB feed | **4:5, 1080×1350** (carousel 1:1 or 4:5) | | The profile grid previews at **3:4** (since Jan 2025), so keep key content in the central 3:4 area | [Oktopost](https://www.oktopost.com/blog/instagram-grid-size-guide/) |
| Google PMax / Demand Gen | 1.91:1 1200×628; 1:1 1200×1200; 4:5 960×1200; logo 1:1 1200×1200 and 4:1 1200×300 | jpg/png ≤5 MB | Keep content in the **central 80%** | [Google Ads Help](https://support.google.com/google-ads/answer/14530211?hl=en) |
| YouTube | 16:9 1920×1080; Shorts 9:16 | | | |

**One master frame for every 9:16 placement [Estimate]:** keep headline, price and logo inside **x 140–940, y 270–1250** on a 1080×1920 canvas. Leave 140 px on **both** sides, because Arabic phone interfaces can mirror the engagement rail to the left. The lower third is for imagery only.

### 5.4 Salla tracking setup (do this before spending)

| Platform | How on Salla | Notes |
|---|---|---|
| **Snapchat** | Dashboard: Marketing → Tracking tools → Snapchat → "link your account". The Snap Business Extension creates or connects the **Snap Pixel and Conversions API**. Verify with Events Manager → Test Events. | [Official] [Snap × Salla](https://forbusiness.snapchat.com/resources/salla) |
| **TikTok** | The Salla app "TikTok Conversion API": paste the Pixel ID and an Access Token. Separate integration for "TikTok Pixel – Catalog". | [Official] [Salla help: TikTok CAPI](https://help.salla.sa/article/%D8%A7%D9%84%D8%B1%D8%A8%D8%B7-%D9%85%D8%B9-tiktok-conversion-api/zd0j9rru0h3cgbi593roxpmn), [Pixel/Catalog](https://help.salla.sa/article/%D8%A7%D9%84%D8%B1%D8%A8%D8%B7-%D9%85%D8%B9-%D8%AA%D9%8A%D9%83-%D8%AA%D9%88%D9%83-%D8%A8%D9%83%D8%B3%D9%84-%D9%83%D8%A7%D8%AA%D8%A7%D9%84%D9%88%D8%AC-tiktok-pixel-catalog/ayv1nzj44b0gildja7mg36e7) |
| **Meta** | Salla Ads → Connection tools: Business Manager, ad account, **pixel**, Instagram. **The pixel, CAPI and catalogue connect automatically, and the catalogue syncs daily.** A Facebook CAPI article also exists. | [Official] [Salla help: Meta](https://help.salla.sa/en/article/meta-ads-integration-salla/pib4qsgp5ipywrqlfg4p3sna), [FB CAPI](https://help.salla.sa/article/%D8%A7%D9%84%D8%B1%D8%A8%D8%B7-%D9%85%D8%B9-facebook-conversion-api/wwclnwgqaq4eg04ali1eepaf) |
| **Google** | Link Google Merchant Center (free listings plus Shopping/PMax). GA4 and Ads conversions through the existing GTM container. Server-side GTM via Stape is an option. | [Official] [Salla help: GMC](https://help.salla.sa/article/1983067357); [Secondary] [Stape](https://stape.io/blog/meta-capi-for-salla-via-server-gtm) |

**Checklist [Estimate]:**
1. Audit GTM-TGFC6FV for pixels that are also installed natively, and remove duplicates.
2. Confirm event deduplication between pixel and CAPI (shared `event_id`).
3. Test ViewContent, AddToCart, InitiateCheckout and Purchase on mobile, including Apple Pay, Tabby and Tamara flows, which redirect off-site.
4. Check that catalogue feeds carry **VAT-inclusive prices** and that size variants (50–62) map correctly.
5. Build seed audiences: past buyers, WhatsApp/branch customers (hashed, with consent) and video viewers.
6. UTM naming per platform, concept and register (e.g. `utm_content=heritage_fusha_9x16`).

### 5.5 Payment options shoppers expect

- **The store already offers all the key methods:** mada, Visa/Mastercard, Apple Pay, STC Pay, Tabby, Tamara and cash on delivery. [Verified]
- **Context:** e-payments were **85% of retail payments in 2025**, up from 79% in 2024 ([Official] [SAMA via SPA](https://www.spa.gov.sa/en/N2558262)). Survey data puts Apple Pay at about 36% and mada at about 22% of preferred online payment. Cash on delivery has fallen to about 10% of online transactions ([Secondary] [Bycom](https://bycomsolutions.com/blog/ecommerce-saudi-arabia-complete-guide/)).
- **In ads:** mention instalments on high-ticket items (wool ⃁ 1,000+, pashmina ⃁ 1,020–1,380). For example, Fusha "قسّطها على 4 دفعات" and Saudi "تقدر تقسّطها على 4". Mention Apple Pay or mada as a frictionless checkout cue in retargeting. Tabby and Tamara both say "متوافق مع الشريعة", which reassures this audience.

### 5.6 A 90-day test plan for a heritage menswear store [Estimate: recommendation]

**Window:** Sun 18 Oct 2026 → Sat 16 Jan 2027 (13 weeks). It covers the shemagh-season launch, three salary days, White Friday, المربعانية and the mid-year break. It ends **before** the Ramadan/Eid flight (17 Jan – 8 Mar), which the test results will shape.

**Budget tiers:** "Core" is ⃁ 60,000 (about ⃁ 4,600/week). "Growth" is ⃁ 120,000. This brackets published agency guidance of ⃁ 15–30K a month for KSA e-commerce ([Hovi](https://thehovi.com/blog/agency-insights/performance-marketing-ksa-uae-strategies-roi-2026)) and ⃁ 5–10K a month for a first Snapchat test ([Sedra Media](https://sedramedia.com/snapchat-ads-for-b2c-brands-in-saudi-arabia/), [Eko](https://ekoinnovations.com/blog/snapchat-ads-saudi-arabia-2026)).

| Channel | Share (Core) | ⃁ (Core) | Job | Formats |
|---|---|---|---|---|
| Snapchat | 35% | 21,000 | Reach Saudi men; prospecting; catalogue | Single video/image, Collection, DPA once the catalogue is live; Story Ads for winter collections |
| Google (Search + PMax/Shopping) | 20% | 12,000 | Capture demand: brand terms, "غترة سويسري", "شماغ أحمر", "قماش ياباني", "صوف إنجليزي", "شال باشمينا" | Search, PMax with the Merchant feed |
| Meta (IG/FB) | 20% | 12,000 | Retargeting, catalogue, Reels; brand home for new followers | Advantage+ catalogue, Reels, 4:5 carousels |
| TikTok | 20% | 12,000 | "How" content and tutorials; follower growth | Spark Ads from the brand account, in-feed 9:16 |
| Reserve / X test | 5% | 3,000 | X test around launches; top-up for winners | Promoted posts |

**Phasing:**

| Weeks | Dates | Focus | Budget weighting |
|---|---|---|---|
| 1–2 | 18–31 Oct | **Learn.** Tracking QA (5.4). 4 creative concepts × **2 registers (Fusha vs Saudi)** × 2 formats, so the brief's two-tone deliverable becomes a live A/B test. Salary burst 26–29 Oct. | 15% |
| 3–6 | 1–28 Nov | **Optimise.** Cut the bottom half of the creative. Build retargeting pools (video viewers, ATC). 11.11 teaser. **26–30 Nov peak** (salary, White Friday, school break) with bundles. | 40% |
| 7–13 | 29 Nov – 16 Jan | **Winter scale.** المربعانية from 7 Dec: wool, pashmina, heavy shemagh, winter thobe fabrics, gift boxes. Salary 27 Dec. Mid-year break 8–16 Jan. **From 10 Dec (Rajab), start "order your Eid fabric early" messaging.** | 45% |

**Creative concepts to test:**
1. **Heritage / HOW:** a 6–10 s craft close-up, such as pressing the مرزام, with the line "80+ years".
2. **Product hero:** catalogue poster with price.
3. **Scenario:** majlis, Riyadh Season night, desert camp in winter.
4. **Offer or bundle:** White Friday or a gift box.

**Measurement and guardrails:**
- **Primary KPI:** new-customer CPA against break-even. Break-even CPA = AOV × gross margin. For example, at an AOV of ⃁ 300 and a 50% margin, break-even is ⃁ 150, so target ≤ ⃁ 100. Secondary KPIs are ROAS (target ≥3×), ATC rate and CTR.
- **Optimisation event:** optimise for AddToCart or InitiateCheckout until each platform records enough weekly purchases, then switch to Purchase.
- **Kill or scale:** after about 3–5K impressions per creative, pause anything in the bottom quartile on CTR or hook rate. Scale winners by no more than 20–30% every 2–3 days.
- **Register test read-out:** compare CTR, CVR and CPA for the Fusha and Saudi versions of the same design, per platform. The hypothesis is that Saudi wins on Snapchat and TikTok and Fusha holds up on Google Display and X.

**Then the Ramadan/Eid flight (17 Jan – 8 Mar):**
- Fabric push from 17 Jan to about 20 Feb, with "اطلب قماش العيد قبل زحمة الخياطين" in Fusha or Saudi.
- Headwear, perfume and gift boxes from 8 Feb to 6 Mar.
- Founding Day heritage film on 19–22 Feb.
- Last-order countdown on 3–6 Mar.
- Budget about 1.5–2× the monthly test run-rate, because CPMs are about 68% higher in Ramadan. Schedule mostly 8 pm – 2 am.

---

## 6. Cultural accuracy notes for imagery

### 6.1 Shemagh vs ghutra

- **Shemagh (شماغ):** red-on-white check, cotton, folded into a **triangle**. It has been the dominant Saudi head covering since the mid-1970s and dominates **winter**. [Secondary] [Saudipedia](https://saudipedia.com/en/what-is-the-difference-between-shemagh-and-ghutra)
- **Ghutra (غترة):** plain **white**, lightweight cotton (the Attar ghutra is Swiss voile). Worn more in **summer and at formal or business occasions**. Some patterned white ghutras exist. [Secondary] Saudipedia, [Ashabelia](https://ashabelia.ae/ghutra/)
- **The Saudi shemagh has no fringe or tassels.** A fringed or knotted edge (مهدّب) and wearing it with a suit read as **Jordanian**. Black-and-white check reads as the Palestinian **keffiyeh**. Neither is right for this brand. [Secondary] [Arrajol](https://www.arrajol.com/content/40491/%D8%A3%D8%B2%D9%8A%D8%A7%D8%A1/6-%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA-%D9%85%D8%AB%D9%8A%D8%B1%D8%A9-%D8%B9%D9%86-%D8%A7%D9%84%D8%B4%D9%85%D8%A7%D8%BA-%D9%88%D8%A7%D9%84%D8%BA%D8%AA%D8%B1%D8%A9), [Wikipedia AR: كوفية](https://ar.wikipedia.org/wiki/%D9%83%D9%88%D9%81%D9%8A%D8%A9)
- In Saudi Arabia the shemagh and ghutra are worn **only with the thobe**, never with Western suits. [Secondary] Arrajol

### 6.2 How it is worn (folding, crease and named styles)

- **المرزام (al-mirzam)** is the **centre crease** ironed into the front of the folded shemagh or ghutra. It sits exactly at the middle of the forehead and is the hallmark of a well-dressed Saudi man. The agal is lowered slightly forward over it to "lock" the crease. [Secondary] [Shemagh Shop](https://shemaghshop.sa/ar/blog/tarsimet-al-cobra-thabat-al-shmagh/a-1984957567)
- **الترسيمة (al-tarsima)** is the overall shaping or "set" of the headdress. Named sets include:
  - **الكوبرا (cobra):** both front edges raised into a hood-like peak. Popular with younger men and confident and formal in feel. Use little or no starch, because heavy starch makes it flare. The very stiff, highly starched upright "cobra" is strongly associated with **Qatar**; for a Saudi read, keep it soft and pressed.
  - **الصقر (falcon).**
  - **ثلاث مرازيم (three creases).**
  - **The traditional drop:** sides hanging naturally, no folds.
  - **The casual back-throw:** ends flipped back over the shoulders or crown.

  [Secondary] [Shemagh Shop](https://shemaghshop.sa/blog/how-to-wear-shemagh/a-1306801504), [Wikipedia: Qatari clothing](https://en.wikipedia.org/wiki/Qatari_clothing), [StriveME](https://striveme.com/article/%D9%84%D8%A7%D9%8A%D9%81-%D8%B3%D8%AA%D8%A7%D9%8A%D9%84/%D9%85%D9%88%D8%B6%D8%A9/%D8%B7%D8%B1%D9%8A%D9%82%D8%A9-%D9%84%D8%A8%D8%B3-%D8%A7%D9%84%D8%B4%D9%85%D8%A7%D8%BA-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A), [Arab News](https://www.arabnews.com/news/460492)
- **Without the agal:** common for casual wear, work and some religious men. A skullcap (طاقية) underneath holds it, and the ends are folded up on the head. [Secondary] [Bin Afif](https://binafiff.com/blog/%D8%B7%D8%B1%D9%8A%D9%82%D8%A9-%D9%84%D8%A8%D8%B3-%D8%A7%D9%84%D8%B4%D9%85%D8%A7%D8%BA-%D8%A8%D8%AF%D9%88%D9%86-%D8%B9%D9%82%D8%A7%D9%84/a-1840539087)
- **Image QA:** the check must be **symmetrical left to right** and the crease centred. The triangle point hangs down the back. Fabric edges should be clean and hemmed. The forehead edge should be crisp. **Use the house's own care line as HOW content:** "يجب تسخين المكواة على درجة 110 مئوية" (from the product description).

### 6.3 Agal (عقال)

- The Saudi standard is a **plain black** double ring of wool cord, worn level and slightly forward. Gold-thread (مقصّب) agals are ceremonial; avoid them for everyday customers. [Secondary] [Laabis](https://laabis.com/pages/Types-of-Saudi-Oqal), [Saudipedia: agal-making](https://saudipedia.com/article/15176/%D9%85%D8%AC%D8%AA%D9%85%D8%B9/%D8%B5%D9%86%D8%A7%D8%B9%D8%A9-%D8%A7%D9%84%D8%B9%D9%82%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9)
- **Avoid:** the **Qatari كركوشة**, four cords with tassels hanging down the back, which is thick and stiff, and long decorative tails generally. [Secondary] [Al Araby](https://www.alaraby.co.uk/%D8%A7%D9%84%D8%B9%D9%82%D8%A7%D9%84-%D8%A7%D9%84%D9%82%D8%B7%D8%B1%D9%8A-%D9%88%D8%A8%D8%B1-%D9%88%D8%B5%D9%88%D9%81-%D9%88%D8%AD%D8%B1%D9%8A%D8%B1-%D9%88%22%D9%83%D8%B1%D9%83%D9%88%D8%B4%D8%A9%22-0)

### 6.4 Thobe: Saudi vs neighbouring countries

| Country | Collar | Chest / front | Other cues | Use? |
|---|---|---|---|---|
| **Saudi** | Stiffened (حشوة) collar in one of three main shapes: **قلابي** (two-point shirt collar, fastened by buttons), **صيني** (band/mandarin) or **round/plain**. Some young men wear embroidered collars. | Stiffened chest pocket and placket (جبزور) | Sleeves end in a cuff, **plain (سادة) or French cuff with cufflinks (كبك)**. Three pockets (two hidden at the hips, one on the left chest). White most of the year; **grey, beige or navy in winter**. | **Yes** |
| Kuwaiti | Short round collar without stiffening | Rounded, unstiffened pocket and placket | A pressed **crease from below the buttons to the hem** and two back pleats | No |
| Qatari | Saudi-like stiff pointed collar | Saudi-like | Kuwaiti-like side pockets and front crease. **كركوشة agal**, very stiff starched ghutra | No |
| Emirati | **Collarless** kandura | Embroidered V neckline | A **long tassel (طربوشة)** hanging from the neckline. Ghutra often white or tied as a حمدانية. | No |
| Omani | Collarless dishdasha with a tassel | n/a | **Kumma cap or massar turban** instead of a shemagh | No |

Sources: [Secondary] [Saudipedia: Saudi thobe](https://saudipedia.com/en/saudi-thobe), [Al Khayal](https://store.alkhayalksa.net/en/blog/saudi-qatar-kuwait-thobe/a-236789199), [Almrsal: collar types](https://www.almrsal.com/post/498640), [Penley Perspective](https://penleyperspective.com/traditional-arab-mens-clothing/), [Khaleejesque](https://khaleejesque.me/2009/09/19/the-anatomy-of-the-dishdasha/). Siraj Attar sells cufflinks (كبك فضي/أزرق), so **show French cuffs with the house's cufflinks** in fabric and thobe shots.

### 6.5 Bisht (بشت / مشلح)

- A **loose, open-front outer cloak** worn over the thobe with gold or silver zari edging. Colours are black, brown, beige, cream, white and maroon. [Secondary] [Saudipedia: Mishlah](https://saudipedia.com/en/mishlah)
- **When it is worn:** weddings (especially the groom and the groom's father), Eid, official ceremonies, national events and graduations. Demand peaks around Eid and weddings.
- **Official weekday colour protocol** (state occasions): white on Friday, brown on Saturday, cream/yellow on Sunday, burgundy on Monday, black on Tuesday, light brown on Wednesday, beige on Thursday.
- Winter bishts use coarse wool; summer ones are light. The **Hasawi bisht** (al-Ahsa) is the prestige craft.
- **Siraj Attar does not sell bishts.** If one appears, for example in a groom scene, it is styling, not product. Keep the bisht's colour harmonious with the shemagh or ghutra and never let it hide the hero product.

### 6.6 Winter wear

- **الفروة (farwa):** a long, sleeved winter coat lined with fleece or fur (natural or synthetic), worn over the thobe in black, brown or grey, especially for desert camps and evening majlis. [Secondary] [Ashpel](https://ashpel.com/blog/%D8%A8%D8%B4%D8%AA-%D9%81%D8%B1%D9%88%D8%A9-%D8%B1%D8%AC%D8%A7%D9%84%D9%8A/a-1321649851), [New Arabia](https://newarabia.co.uk/blogs/news/the-farwa-why-this-ancient-arabian-winter-coat-is-making-a-comeback)
- **Winter shemagh:** heavier cotton, red dominant. Siraj Attar has a "المنتجات الشتوية" category with "شماغ نقش العطار 25 الذهبي".
- **Shawl (شال):** pashmina or a "نص ترمه" shawl worn over the shoulders or under the agal-less shemagh in cold weather. Siraj Attar's range runs from about ⃁ 390 to ⃁ 1,380 including VAT.
- **Winter thobes:** wool and darker colours (grey, navy, brown, olive), using Siraj Attar's English (William Halstead Super 130, OMC Super 150) and Italian (Dolfino and Angelico Super 140) wools. [Secondary] [Sarmadi](https://sarmadii.com/blog/%D9%82%D9%85%D8%A7%D8%B4-%D8%A7%D9%84%D9%83%D8%B4%D9%85%D9%8A%D8%B1/a-1644393316)
- **Settings:** desert camp (كشتة) with a fire and dallah, a winter majlis, a Riyadh Season evening, Jeddah al-Balad (رواشين).

### 6.7 What NOT to show

1. **Mixed-gender intimacy.** No couples, no physical contact, no women modelling menswear. The safest grammar for this category is **men only or across generations** (grandfather, father, son). Show gifting through hands and the gift box. GAMR (formerly GCAM) media rules ban "immodesty" and flaunting luxury and require consent to film children. [Secondary] [Mimeta](https://www.mimeta.org/mimeta-news-on-censorship-in-art/2025/10/21/arab-states-intensify-digital-content-controls), [Arab News](https://www.arabnews.com/node/2176661)
2. **National symbols on commerce.** Never use the **Saudi flag** (it carries the Shahada), the **state emblem (palm and swords)**, or **images or names of the leadership** on products, prints or ads, **including on National and Founding Day**. The Ministry of Commerce inspects stores and e-stores. Use heritage patterns, Najdi or Hijazi architecture and the brand's own green and gold instead. [Official] [Ministry of Commerce](https://mc.gov.sa/ar/mediacenter/News/Pages/16-09-22-01.aspx), [Argaam](https://www.argaam.com/ar/article/articledetail/id/1588472)
3. **Sacred imagery as a backdrop.** Do not use the Ka'bah, the Haram interior or Qur'an pages as product backgrounds, despite the house's Makkah origin. Refer to Makkah through the old souq, the trading story and the Aziziyah branch. [Estimate: best practice]
4. **Wrong-country dress:** Emirati collarless kandura with tassel; Qatari كركوشة or rigid cobra; Kuwaiti creased thobe; Omani kumma or massar; Jordanian fringed shemagh with a suit; Palestinian black-and-white keffiyeh; Levantine or Egyptian galabiya.
5. **Etiquette errors** [Estimate: etiquette convention]. Serving or receiving coffee with the left hand (the dallah is held in the left hand and the cup offered with the right). Shoe soles pointing at people in a majlis. Shoes on majlis carpets. A ghutra or shemagh worn loose and uncreased in a "premium" shot.
6. **AI artefacts** (most common in generated images): asymmetric or warped check; a merged agal and shemagh; extra fingers on hands holding the fabric; Latin-style or garbled Arabic text in the scene; Western-style collar plackets on the thobe; sunglasses pushed onto the shemagh in formal shots.
7. **Influencers:** any paid Saudi creator must hold a **Mawthooq licence**, and partnerships must be labelled. [Secondary] [Arab News](https://www.arabnews.com/node/2176661), [Catchers](https://catchers.agency/blog/influencer-marketing-regulations-in-saudi-arabia/)

---

## 7. Arabic copy registers: Fusha vs Saudi

### 7.1 Why both, and what "Saudi" means here

- Saudi brand content swings between Fusha, the "white" dialect (اللهجة البيضاء) and local dialect. Video leans colloquial for authenticity; written and official content leans Fusha. [Secondary] [Al Majalla, 2020](https://www.majalla.com/node/101306/%D9%84%D9%85%D8%A7%D8%B0%D8%A7-%D9%8A%D8%AA%D8%A3%D8%B1%D8%AC%D8%AD-%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89-%D8%A7%D9%84%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A-%D8%A8%D9%8A%D9%86-%D8%A7%D9%84%D9%81%D8%B5%D8%AD%D9%89-%D9%88%C2%AB%D8%A7%D9%84%D8%A8%D9%8A%D8%B6%D8%A7%D8%A1%C2%BB-%D9%88%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D9%8A%D8%A9%D8%9F), [Thmanyah](https://thmanyah.com/24043/)
- **"سعودي" in this project means white Saudi dialect with a Najdi lean.** It is understood from Jeddah to Dammam. It is not heavy Bedouin vocabulary, Hijazi-only words or other Gulf dialects.

### 7.2 Rules for keeping the registers separate

1. **One register per piece, end to end.** Headline, subline, CTA, offer badge, price label, instalment line and caption must all use the same register. The client's example "رأس … لرجلينك" fails because a Fusha noun with hamza sits next to a colloquial dual.
2. **These elements are neutral and appear unchanged in both versions:** product names exactly as in the store (e.g. "شماغ العطار كلاسيك عنبر", "نقش العطار 26"), the brand name, sizes, the ⃁ price, and the tagline "من بيت العطار", which works in both.
3. **Strong Fusha markers must not appear in the Saudi version:** الآن، سوف، لن، لم، ليس، لدينا/لديك، إنّ، الذي/التي/الذين، ماذا، لماذا، أيّ، accusative tanween (عاماً، شماغاً), and passive forms such as يُرجى or تُطلب.
4. **Strong Saudi markers must not appear in the Fusha version:** الحين، وش، ليش، اللي، تبي/أبي، ودّك، ترى، مرّة (meaning "very"), كذا، لين (meaning "until"), حنّا، ما راح، يطوفك، كشخة، راس/فاس (without hamza), the dialect dual (رجلينك، عيونك), and verbs with dropped hamza (يبدي، يجي).
5. **Keep it Saudi, not "Gulf" or pan-Arab.** Avoid وايد and شلون (Kuwaiti/Emirati), چ (Kuwaiti/Iraqi spelling), كتير، هيك، بدّك، هلّأ (Levantine), and دلوقتي، عايز، إزاي، يتكرمش (Egyptian). In Saudi, a creased thobe "يتكسّر"; it does not "يتكرمش".
6. **Spelling in the Saudi version** follows standard orthography for every word that is not a dialect marker. Keep ة, the correct hamzat wasl (اطلب not أطلب) and no phonetic spellings beyond the accepted ones (الحين، وش، راس، دفا، الشتا).
7. **Address and gender.** Address the man as singular masculine. Gift copy addresses the buyer ("أهدِه", "هديته"). Make verbs and pronouns agree with the product noun (7.4).
8. **Digits** are Western in both versions. Punctuation is Arabic: the comma ،, the question mark ؟ and guillemets « ».
9. **Lint before export.** Scan each version against the marker lists in rules 3–5. A hit sends the line back for human review.

### 7.3 Thirty phrase pairs for menswear ads

| # | فصحى (MSA) | سعودي (Saudi white dialect) | Marker |
|---|---|---|---|
| 1 | اطلبه الآن | اطلبه الحين | الآن / الحين |
| 2 | من الرأس حتى القدمين | من راسك لين رجلينك | hamza, لين, dual |
| 3 | ماذا تنتظر؟ | وش تنتظر؟ | ماذا / وش |
| 4 | لماذا العطار؟ | ليش العطار؟ | لماذا / ليش |
| 5 | أناقتك تبدأ من هنا | كشختك تبدي من هنا | كشخة, dropped hamza |
| 6 | يليق بك | لايق عليك | |
| 7 | خصمٌ يصل إلى 30% | خصم لين 30% | لين |
| 8 | العرض لفترة محدودة | العرض ما يطوّل | |
| 9 | لا تفوّت العرض | لا يطوفك العرض | يطوفك |
| 10 | الكمية محدودة | الكمية على قدّها | idiom |
| 11 | قبل نفاد الكمية | قبل لا تخلص الكمية | قبل لا |
| 12 | سارِع بالطلب | الحق اطلب | |
| 13 | لن تجد مثله | ما راح تلقى مثله | لن / ما راح |
| 14 | جودةٌ تثق بها منذ أكثر من 80 عامًا | جودة تعرفها من أكثر من 80 سنة | tanween, عام/سنة |
| 15 | هذا ما يميّزنا | هذا اللي يميّزنا | ما / اللي |
| 16 | نحن هنا لخدمتك | حنّا هنا لخدمتك | نحن / حنّا |
| 17 | أيّ شماغ يناسبك؟ | وش الشماغ اللي يناسبك؟ | |
| 18 | دفءٌ يرافقك طوال الشتاء | دفا يكفيك الشتا كله | |
| 19 | حلّ البرد | دخل البرد | |
| 20 | استعدّ لإطلالة العيد | جهّز كشخة العيد | |
| 21 | أهدِه شماغًا يليق به | أهده شماغ يليق فيه | tanween, به/فيه |
| 22 | هديةٌ تُسعده | هدية تبيّض الوجه | idiom |
| 23 | يصلك إلى باب منزلك | يوصلك لين باب بيتك | |
| 24 | الدفع عند الاستلام متاح | تقدر تدفع عند الاستلام | |
| 25 | قسّط مشترياتك على 4 دفعات دون فوائد | قسّطها على 4 دفعات بدون فوائد | |
| 26 | قماشٌ لا يتجعّد | قماش ما يتكسّر | لا / ما; يتكسّر (not يتكرمش) |
| 27 | ارتدِه بثقة | البسه وأنت واثق | |
| 28 | تعرّف على أقمشتنا اليابانية | شوف أقمشتنا اليابانية | |
| 29 | كل ما تحتاجه في مكانٍ واحد | كل اللي تحتاجه في مكان واحد | ما / اللي |
| 30 | اطلب قماش العيد قبل ازدحام الخيّاطين | اطلب قماش العيد قبل زحمة الخيّاطين | |

Notes:
- Pair 5: "كشخة" is pan-Saudi and safe.
- Pair 7: "لين" (meaning "until") is Najdi and understood nationwide. A softer option is "خصم يوصل 30%".
- Pair 26: "يتكسّر" is how Saudis describe creases in a thobe. Avoid the Egyptian "يتكرمش".

### 7.4 Gender agreement by product (both registers)

| Noun | Gender | Fusha CTA | Saudi CTA |
|---|---|---|---|
| شماغ، عقال، قماش، صوف، شال، عطر، كبك | m. | اطلبه الآن | اطلبه الحين |
| غترة، فروة، هدية، علبة الإهداء | f. | اطلبها الآن | اطلبها الحين |
| صندوق الإهداء | m. | اطلبه الآن | اطلبه الحين |
| جوارب وثير، ملابس داخلية | pl. (non-human, so feminine singular agreement) | اطلبها الآن | اطلبها الحين |

### 7.5 Errors in the client's existing copy (fix these and do not copy them)

| Current | Problem | Fusha fix | Saudi fix |
|---|---|---|---|
| الآن عروض اليوم الوطني تبدأ من 15% , أطلب الآن وأغتنم الفرصة | "أطلب" and "أغتنم" have wrong hamzas (both take hamzat wasl); Latin comma with a space before it; "الآن" repeated | عروض اليوم الوطني تبدأ من 15%، اطلب الآن واغتنم الفرصة | عروض اليوم الوطني تبدأ من 15%، اطلب الحين ولا يطوفك العرض |
| اشتريها معًا بـ … | A colloquial imperative inside Fusha UI copy | اشترِها معًا بـ ⃁ … | خذها كلها مع بعض بـ ⃁ … |
| احصل عليه الآن بخصم 20 | Fine as Fusha; keep it in the Fusha version only | n/a | خذه الحين بخصم 20% |

---

## Sources (main)

**Official:**
- SAMA riyal symbol: [page](https://www.sama.gov.sa/en-US/Currency/SRS/Pages/default.aspx), [guidelines page](https://www.sama.gov.sa/en-US/Currency/SRS/Pages/Guideline.aspx), [Guidelines PDF](https://www.sama.gov.sa/ar-sa/Currency/SRS/Documents/Guidelines.pdf), [Font Designers' PDF](https://www.sama.gov.sa/ar-sa/Currency/SRS/Documents/Font_Designers_Guidelines.pdf), [SVG](https://www.sama.gov.sa/ar-sa/Currency/Documents/Saudi_Riyal_Symbol-2.svg)
- Unicode: [UnicodeData 17.0](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt)
- MoF: [salary dates 2026](https://www.mof.gov.sa/mediacenter/Payroll/Pages/2026.aspx)
- SPA: [Riyadh Season 2026](https://www.spa.gov.sa/en/N2686677), [SAMA e-payments 2025](https://www.spa.gov.sa/en/N2558262)
- Ministry of Commerce: [national-symbol ban](https://mc.gov.sa/ar/mediacenter/News/Pages/16-09-22-01.aspx)
- Brand: [store](https://sirajattarbros.com/ar), [About](https://sirajattarbros.com/ar/عن-محمد-سراج-عطار-واخوية/page-1340146930), [Branches](https://sirajattarbros.com/ar/فروعنا/page-91100985), [Instagram](https://www.instagram.com/sirajattarbros/), [TikTok](https://www.tiktok.com/@m.sirajattar), [Snapchat](https://www.snapchat.com/add/sirajattarbros), [X](https://x.com/SirajAttarBros)
- Salla help: [Meta](https://help.salla.sa/en/article/meta-ads-integration-salla/pib4qsgp5ipywrqlfg4p3sna), [TikTok CAPI](https://help.salla.sa/article/%D8%A7%D9%84%D8%B1%D8%A8%D8%B7-%D9%85%D8%B9-tiktok-conversion-api/zd0j9rru0h3cgbi593roxpmn), [GMC](https://help.salla.sa/article/1983067357)
- Snap: [Snap × Salla](https://forbusiness.snapchat.com/resources/salla)
- Google: [PMax image specs](https://support.google.com/google-ads/answer/14530211?hl=en)

**Data and press:**
- [DataReportal Digital 2026 KSA](https://datareportal.com/reports/digital-2026-saudi-arabia)
- [StatCounter KSA search](https://gs.statcounter.com/search-engine-market-share/all/saudi-arabia)
- [GASTAT via Argaam](https://www.argaam.com/en/article/articledetail/id/1827144)
- [Asharq Al-Awsat: thobe market](https://aawsat.com/%D9%8A%D9%88%D9%85%D9%8A%D8%A7%D8%AA-%D8%A7%D9%84%D8%B4%D8%B1%D9%82/4950836-%D8%A7%D9%84%D8%AB%D9%88%D8%A8-%D8%A7%D9%84%D8%B1%D8%AC%D8%A7%D9%84%D9%8A-%D9%8A%D9%83%D9%84%D9%81-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%8A%D9%86-45-%D9%85%D9%84%D9%8A%D8%A7%D8%B1-%D8%B1%D9%8A%D8%A7%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%B9%D8%A7%D9%85)
- [Al Watan: tailors](https://www.alwatan.com.sa/article/1074646)
- [Gulf News: Riyadh Season](https://gulfnews.com/world/gulf/saudi/riyadh-season-2026-to-begin-on-october-21-with-10-weeks-of-entertainment-1.500689955)
- [Wego: MoE calendar 1448](https://rahhal.wego.com/blog/%D8%A7%D9%84%D8%AA%D9%82%D9%88%D9%8A%D9%85-%D8%A7%D9%84%D8%AF%D8%B1%D8%A7%D8%B3%D9%8A-1448-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9-%D8%A7%D9%84%D8%A7%D8%AC%D8%A7%D8%B2%D8%A7%D8%AA/)
- [MakkahLive Hijri 1448](https://makkahlive.net/en/tools/islamic-calendar)
- [Sabq: الوسم](https://sabq.org/saudia/9tpnralqns)
- [Arab News: Ramadan nights](https://www.arabnews.com/node/2636507)
- [Saudipedia: shemagh/ghutra](https://saudipedia.com/en/what-is-the-difference-between-shemagh-and-ghutra), [Saudipedia: thobe](https://saudipedia.com/en/saudi-thobe), [Saudipedia: mishlah](https://saudipedia.com/en/mishlah)
- [Al Majalla: ad registers](https://www.majalla.com/node/101306/%D9%84%D9%85%D8%A7%D8%B0%D8%A7-%D9%8A%D8%AA%D8%A3%D8%B1%D8%AC%D8%AD-%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89-%D8%A7%D9%84%D8%A5%D8%B9%D9%84%D8%A7%D9%86%D9%8A-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A-%D8%A8%D9%8A%D9%86-%D8%A7%D9%84%D9%81%D8%B5%D8%AD%D9%89-%D9%88%C2%AB%D8%A7%D9%84%D8%A8%D9%8A%D8%B6%D8%A7%D8%A1%C2%BB-%D9%88%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D9%8A%D8%A9%D8%9F)

**Agency benchmarks (directional):** [Hovi](https://thehovi.com/blog/agency-insights/performance-marketing-ksa-uae-strategies-roi-2026), [BIMO](https://www.bimogroup.co/blog/meta-ads-benchmarks-gulf.html), [Hikmah AI](https://www.hikmahaiagency.com/blog/instagram-ads-benchmarks-saudi-arabia-2026), [Ekoinnovations](https://ekoinnovations.com/blog/snapchat-ads-cost-saudi-arabia-2026), [Lebesgue](https://lebesgue.io/facebook-ads/facebook-cpm-by-country), [AdManage](https://admanage.ai/blog/tiktok-ads-cost), [Stackmatix](https://www.stackmatix.com/blog/snapchat-ad-specs), [Recharm](https://www.recharm.com/blog/tiktok-video-ad-specs), [Lucid Media](https://www.lucidmedia.co.nz/blog/instagram-facebook-ad-safe-zones-2026/)
