# Siraj Attar store scrape report

Live scrape of https://sirajattarbros.com/ar on **2026-10-04** (Salla store id 946211295). Machine-readable data: `data/catalogue.json` (137 products), `data/categories.json`, `data/photo_classes.json`, `data/compare_2026-09-28_vs_2026-10-04.json`; images in `data/images/` (`<productid>_<n>`, n = 1 is the main photo).

## How it was scraped

- The live site did **not** block us. The Salla storefront API (`api.salla.dev/store/v1/products`, header `Store-Identifier: 946211295`) answered 200 without a session, both for the full product index (`source=product.index`, 10 pages) and for every menu category (`source=categories`).
- All 137 product pages were fetched (3 workers, 0.8 to 1.4 s pauses). Prices were cross-checked against the schema.org Product JSON-LD on each page: 136 of 137 match exactly. The exception is the gift bundle `1381142749` (type `group_products`), whose JSON-LD price is 0. The page shows 307.25.
- Gallery images come from the product-page lightbox links. They are already originals: cdn.salla.sa thumbnails (`<uuid>-WxH-name.jpg`) and the Cloudflare `/cdn-cgi/image/` proxy were stripped. On cdn.files.salla.network the `_600x900`-style suffix is part of the stored original file name. Removing it returns 404, and the API `original_image` points to the suffixed file, so those files were kept. 348 images, 0 failures, 198 MB.
- A rendered DOM check of category pages (Edge, Playwright) shows only the first 15 cards before lazy loading, so category membership comes from the API, not the DOM.
- **Price basis:** the displayed price equals Salla `product:pretax_price`. About half of the regular prices become whole riyals when multiplied by 1.15, so the store likely shows prices before VAT and adds 15% at checkout. This was not verified, because we did not go through checkout. `price` = displayed price; `price_incl_vat_est` = x1.15.

## Headline numbers

- **137 products** in the store index; **124** sit in at least one menu category; **13 are in no menu category** and can be reached only by search or a direct URL.
- 30 menu categories (11 top level + 19 sub-categories). 3 are empty: الشالات الفاخرة, شالات البيداء نص ترمه, أصواف متنوعه. The home-page banner link `c755154187` ("ويترك أثر مميز") is dead. It redirects home and the API returns 422.
- In stock: 117; out of stock: 20.
- **On sale now: 109** products. 97 are in the National Day campaign, which runs from 2026-09-01 and **ends 2026-10-06 02:59 (+03), i.e. the night of 5 Oct**. The product page shows a live countdown, and the site banner still reads "الآن عروض اليوم الوطني تبدأ من 15%". The other 12 are uncategorised items with an open-ended discount.
- Main photographs: fabric_closeup 63, packshot_plain 35, packshot_in_box 34, lifestyle 5. **No main photograph shows the product worn.** 16 model shots exist, all deeper in the galleries of headwear products, and all are on the same white studio sweep.

## Products and prices per category

Prices in SAR as displayed (pre-VAT). "Current" = what the customer pays now; "Regular" = struck price, or the price when the item is not discounted.

| Category | Products | In stock | On sale | Current min-max | Median current | Regular min-max | Discount range |
|---|---:|---:|---:|---|---:|---|---|
| المجموعة الكلاسيكية | 12 | 11 | 9 | 110.86 - 240.21 | 213.04 | 130.4 - 282.6 | 13.6% - 50% |
| أشمغة حمراء | 20 | 16 | 20 | 139.13 - 272 | 204.37 | 169.5 - 330 | 2.2% - 52.2% |
| الغتر | 8 | 7 | 5 | 92 - 208.6 | 122.81 | 130.4 - 208.6 | 10% - 44.2% |
| أشمغة بيضاء | 5 | 4 | 4 | 123.91 - 218.04 | 181.05 | 169.5 - 260.8 | 15% - 50% |
| مجموعة حفاوة | 3 | 3 | 3 | 144.08 - 144.08 | 144.08 | 169.5 - 169.5 | 15% - 15% |
| مجموعة الأصالة | 9 | 9 | 9 | 92 - 207 | 181.05 | 143.4 - 252.17 | 15% - 44.2% |
| وثير للملابس الداخلية | 7 | 6 | 2 | 17.39 - 44.34 | 20 | 17.39 - 60 | 15% - 26.1% |
| الأقمشة | 39 | 34 | 32 | 49 - 732 | 121.74 | 70 - 732 | 20% - 43.5% |
| الأقمشة › سمير اميس | 1 | 1 | 1 | 136.5 - 136.5 | 136.5 | 241.5 - 241.5 | 43.5% - 43.5% |
| الأقمشة › الاقمشه الاوروبيه | 2 | 2 | 2 | 276.96 - 276.96 | 276.96 | 426.09 - 426.09 | 35% - 35% |
| الأقمشة › تترونات | 14 | 13 | 9 | 70 - 396.2 | 117.39 | 70 - 396.2 | 30% - 35% |
| الأقمشة › الأقمشة اليابانية | 24 | 22 | 20 | 97.5 - 396.2 | 117.39 | 150 - 396.2 | 20% - 43.5% |
| الأقمشة › أقطان طبيعية | 4 | 2 | 3 | 125.12 - 732 | 269.29 | 192.5 - 732 | 35% - 43.5% |
| الأقمشة › الأقمشة السويسرية | 2 | 0 | 1 | 364 - 732 | 548 | 560 - 732 | 35% - 35% |
| الأقمشة › الأقمشة الإيطالية | 2 | 1 | 2 | 303.33 - 385.61 | 344.47 | 466.66 - 593.25 | 35% - 35% |
| الأقمشة › مخلوط | 3 | 2 | 2 | 125.12 - 174.58 | 163.4 | 163.4 - 309 | 35% - 43.5% |
| الأقمشة › الأقمشة الكورية | 5 | 5 | 5 | 49 - 49 | 49 | 70 - 70 | 30% - 30% |
| المنتجات الشتوية | 19 | 17 | 18 | 133.04 - 967.75 | 340 | 156.52 - 1,382.5 | 15% - 48.8% |
| المنتجات الشتوية › الشالات الفاخرة | 0 | - | - | - | - | - | - |
| المنتجات الشتوية › شالات البيداء نص ترمه | 0 | - | - | - | - | - | - |
| الأصواف | 36 | 28 | 28 | 133.04 - 1200 | 886.96 | 156.52 - 1,382.5 | 15% - 30% |
| الأصواف › الشالات | 28 | 21 | 20 | 133.04 - 1200 | 886.96 | 156.52 - 1200 | 15% - 15% |
| الأصواف › الأصواف الإنجليزية | 4 | 4 | 4 | 894.25 - 943.25 | 894.25 | 1,277.5 - 1,347.5 | 30% - 30% |
| الأصواف › الأصواف الإيطالية | 4 | 3 | 4 | 710 - 967.75 | 710 | 1015 - 1,382.5 | 30% - 30% |
| الأصواف › أصواف متنوعه | 0 | - | - | - | - | - | - |
| اخرى | 14 | 10 | 11 | 53 - 595 | 150.64 | 82.61 - 595 | 2.2% - 56.5% |
| اخرى › اكسسوارات | 3 | 3 | 2 | 53 - 82.61 | 53 | 82.61 - 86.96 | 39.1% - 39.1% |
| اخرى › المنتجات المخفضة | 6 | 2 | 6 | 139.13 - 272 | 195.86 | 252.17 - 330 | 2.2% - 52.2% |
| اخرى › العطور | 4 | 4 | 3 | 119.55 - 595 | 143.46 | 275 - 595 | 47.8% - 56.5% |
| اخرى › هدايا | 2 | 2 | 0 | 307.25 - 595 | 451.12 | 307.25 - 595 | - |
| غير مصنف (خارج القائمة) | 13 | 13 | 12 | 98.92 - 886.96 | 303.33 | 152.18 - 1,043.47 | 15% - 35.1% |
| ويترك أثر مميز (رابط بانر) | 0 | - | - | - | - | - | - |

Products sit in several categories (e.g. a red shemagh can be in المجموعة الكلاسيكية, أشمغة حمراء and المنتجات المخفضة), so the rows do not add up to 137.

## Changes since the 2026-09-28 scrape

- **No products removed** (all 123 still live). **No offer has ended yet**: all 97 discounts seen on 09-28 are still running at the same price, with one exception below. They all end on the night of 5 Oct.
- **One price change:** شماغ الوسام 26 الأحمر (1546150268) went from 195.50 to **207.00**. The struck price stays 243.48, so the discount is now 15% (was 19.7%).
- **Two items went out of stock:** شماغ العطار الذهبي (333921099) and شماغ برنيني ذهبي (1842109012).
- **New in a menu category:** غترة زفير (196810152, الغتر, 152.17; Salla sync 2026-09-30). الغتر grew from 7 to 8 products.
- **13 products found that the 09-28 run missed.** They are in the store index but in no menu category, and the 09-28 run walked categories only. Salla sync dates for 8 of them fall between 2026-09-08 and 09-22, and 4 have no sync record, so they are most likely older hidden or uncategorised listings rather than launches. `910` (987219575) synced on 2026-09-30 and may be genuinely new. They are 10 thobe fabrics (قماش999, 9426, ارزونا, 933, تيستا بوارنو, تيستا بالميرول, رومنسي, قماش العطار 404, 910, 906) and 3 shawls (Q2S55, Q6S55, البيداء m7s60). 12 of the 13 carry a discount with no end date.
- 8 title edits are whitespace-only clean-ups (double spaces removed). Category membership and gallery images are otherwise unchanged.
- Discount oddities in the running campaign: شماغ نقش العطار 25 الاحمر (437508308) is "on sale" at 272.00, down from 278.26 (2.2%, and out of stock). غترة العطار العصرية is 10% off and شماغ العطار كلاسيك عنبر is 13.6% off. Both are below the "from 15%" promise on the banner.

## Products on sale now

Sorted by discount. "Ends" is the scheduled end of the discount; "open" = no end date set.

| ID | Product | Category | Now | Was | Off | Ends | Stock |
|---|---|---|---:|---:|---:|---|---|
| 189452492 | Attar 3 _ العطار 3 | اخرى | 119.55 | 275 | 56.5% | 2026-10-06 | in |
| 2024205944 | شماغ كلاسيك زفير | أشمغة حمراء | 157.82 | 330 | 52.2% | 2026-10-06 | **OUT** |
| 333921099 | شماغ العطار الذهبي | المجموعة الكلاسيكية | 123.91 | 247.8 | 50% | 2026-10-06 | **OUT** |
| 470478398 | شماغ نقش العطار 25 الذهبي | أشمغة حمراء | 139.13 | 272 | 48.8% | 2026-10-06 | in |
| 14237135 | ِAttar 1 _ العطار 1 | اخرى | 143.46 | 275 | 47.8% | 2026-10-06 | in |
| 1696071629 | Attar2 _العطار 2 | اخرى | 143.46 | 275 | 47.8% | 2026-10-06 | in |
| 1176249105 | غترة العطار سوبر | الغتر | 92 | 165 | 44.2% | 2026-10-06 | in |
| 1526727261 | قماش العطار 096 | الأقمشة | 136.5 | 241.5 | 43.5% | 2026-10-06 | in |
| 512779702 | قماش العطار اسباني قطن 23 | الأقمشة | 174.58 | 309 | 43.5% | 2026-10-06 | in |
| 1316325476 | غترة العطار إسبيشل | الغتر | 92 | 152.1 | 39.5% | 2026-10-06 | in |
| 1842109012 | شماغ برنيني ذهبي | أشمغة حمراء | 194.78 | 320 | 39.1% | 2026-10-06 | **OUT** |
| 2125369422 | شماغ برنيني أحمر | أشمغة حمراء | 196.93 | 323.5 | 39.1% | 2026-10-06 | **OUT** |
| 265256366 | كبك فضي (خيارات متعددة) | اخرى | 53 | 86.96 | 39.1% | 2026-10-06 | in |
| 1610956716 | كبك أزرق (خيارات متعددة) | اخرى | 53 | 86.96 | 39.1% | 2026-10-06 | in |
| 1782560358 | غترة العطار بريميوم | الغتر | 92 | 143.4 | 35.8% | 2026-10-06 | in |
| 2134309440 | قماش ارزونا | غير مصنف | 276 | 425 | 35.1% | 2026-10-06 | in |
| 1124224097 | قماش 933 | غير مصنف | 193.13 | 297.4 | 35.1% | 2026-10-06 | in |
| 708681311 | قماش العطار برو | الأقمشة | 276.96 | 426.09 | 35% | 2026-10-06 | in |
| 1117574161 | قماش العطار ريو | الأقمشة | 276.96 | 426.09 | 35% | 2026-10-06 | in |
| 2029457986 | العطار 913 | الأقمشة | 125.12 | 192.5 | 35% | 2026-10-06 | in |
| 17848842 | قماش العطار 265 | الأقمشة | 113.04 | 173.91 | 35% | 2026-10-06 | in |
| 927677193 | قماش العطار 263 | الأقمشة | 113.04 | 173.91 | 35% | 2026-10-06 | in |
| 502435852 | قماش العطار 292 | الأقمشة | 113.04 | 173.88 | 35% | 2026-10-06 | in |
| 1075081475 | قماش العطار اسبيشل | الأقمشة | 102.37 | 157.5 | 35% | 2026-10-06 | in |
| 1984909826 | قماش العطار 270 | الأقمشة | 113.04 | 173.88 | 35% | 2026-10-06 | in |
| 2025387271 | قماش العطار الابداع | الأقمشة | 102.37 | 157.5 | 35% | 2026-10-06 | in |
| 785634822 | قماش العطار الحلم | الأقمشة | 102.37 | 157.5 | 35% | 2026-10-06 | in |
| 362367801 | قماش العطار 300 | الأقمشة | 97.5 | 150 | 35% | 2026-10-06 | in |
| 1002187832 | قماش العطار 2110 | الأقمشة | 97.5 | 150 | 35% | 2026-10-06 | in |
| 1775701311 | قماش العطار 2206 | الأقمشة | 97.5 | 150 | 35% | 2026-10-06 | in |
| 347923824 | قماش 918 | الأقمشة | 249.93 | 384.5 | 35% | 2026-10-06 | in |
| 1937398379 | قماش 990 | الأقمشة | 249.93 | 384.5 | 35% | open | in |
| 563952490 | قماش إيطالي بوسل-D955082 | الأقمشة | 385.61 | 593.25 | 35% | 2026-10-06 | in |
| 1265128194 | العطار بوبلين لورد أسباني | الأقمشة | 125.12 | 192.5 | 35% | 2026-10-06 | in |
| 1292393513 | العطار 909 | الأقمشة | 249.93 | 384.5 | 35% | 2026-10-06 | in |
| 152164309 | قماش ايطالي تيستا دايمونتي | الأقمشة | 303.33 | 466.66 | 35% | 2026-10-06 | **OUT** |
| 1150351142 | العطار سويسري S- 2920 | الأقمشة | 364 | 560 | 35% | 2026-10-06 | **OUT** |
| 1302660631 | قماش999 | غير مصنف | 135.32 | 208.18 | 35% | 2026-10-06 | in |
| 1147628411 | قماش 9426 | غير مصنف | 98.92 | 152.18 | 35% | 2026-10-06 | in |
| 1369622053 | قماش ايطالي تيستا بوارنو | غير مصنف | 303.33 | 466.66 | 35% | 2026-10-06 | in |
| 1393879881 | قماش ايطالي تيستا بالميرول 25،%مشروك | غير مصنف | 303.33 | 466.66 | 35% | 2026-10-06 | in |
| 1935723405 | قماش العطار 404 | غير مصنف | 178.75 | 275 | 35% | 2026-10-06 | in |
| 987219575 | 910 | غير مصنف | 308.75 | 475 | 35% | 2026-10-06 | in |
| 1762305910 | قماش 906 | غير مصنف | 201.6 | 309.33 | 34.8% | 2026-10-06 | in |
| 972290889 | العطار 404 | الأقمشة | 122.5 | 175 | 30% | 2026-10-06 | in |
| 967106062 | قماش العطار 267 | الأقمشة | 121.74 | 173.91 | 30% | 2026-10-06 | in |
| 1559672581 | قماش القمة | الأقمشة | 110.25 | 157.5 | 30% | 2026-10-06 | in |
| 827099451 | قماش العطار سهيل | الأقمشة | 110.25 | 157.5 | 30% | 2026-10-06 | in |
| 1668806182 | قماش العطار 974 | الأقمشة | 49 | 70 | 30% | 2026-10-06 | in |
| 296408869 | قماش العطار 978 | الأقمشة | 49 | 70 | 30% | 2026-10-06 | in |
| 1204668452 | قماش العطار 975 | الأقمشة | 49 | 70 | 30% | 2026-10-06 | in |
| 1977657819 | قماش العطار 977 | الأقمشة | 49 | 70 | 30% | 2026-10-06 | in |
| 1312648153 | قماش العطار 976 | الأقمشة | 49 | 70 | 30% | 2026-10-06 | in |
| 1852126853 | صوف بيور إيطالي كاروه | المنتجات الشتوية | 710 | 1015 | 30% | 2026-10-06 | in |
| 1449104353 | صوف ايطالي انجليكو سوبر 140 مقلم | المنتجات الشتوية | 710 | 1015 | 30% | 2026-10-06 | in |
| 1489975014 | صوف إيطالي دولفينو سوبر 140 مقلم | المنتجات الشتوية | 967.75 | 1,382.5 | 30% | 2026-10-06 | in |
| 74544352 | صوف ايطالي انجليكو سوبر 140 سادة | المنتجات الشتوية | 710 | 1015 | 30% | 2026-10-06 | **OUT** |
| 1419600434 | صوف omc سوبر 150 مقلم | الأصواف | 943.25 | 1,347.5 | 30% | 2026-10-06 | in |
| 220325430 | صوف ويليام هليستد سوبر 130 مؤنس | الأصواف | 894.25 | 1,277.5 | 30% | 2026-10-06 | in |
| 1029444903 | صوف ويليام هليستد سوبر 130 ساده | الأصواف | 894.25 | 1,277.5 | 30% | 2026-10-06 | in |
| 1023740132 | صوف ويليام هالستد سوبر 130 مقلم | الأصواف | 894.25 | 1,277.5 | 30% | 2026-10-06 | in |
| 2012800981 | سروال طويل كومفورت | وثير للملابس الداخلية | 44.34 | 60 | 26.1% | 2026-10-06 | in |
| 1604079293 | شماغ أوديمار 4 | أشمغة حمراء | 185.87 | 247.83 | 25% | open | in |
| 337691313 | شماغ العطار كلاسيك مرجان | المجموعة الكلاسيكية | 208.7 | 260.87 | 20% | 2026-10-06 | in |
| 2120850122 | شماغ العطار كلاسيك مرجان صافي | المجموعة الكلاسيكية | 208.7 | 260.87 | 20% | 2026-10-06 | in |
| 1949762576 | شماغ العطار الأوربي | أشمغة حمراء | 201.74 | 252.17 | 20% | open | in |
| 1502977199 | قماش لوفر 95 | الأقمشة | 208.7 | 260.87 | 20% | 2026-10-06 | in |
| 1211546059 | شماغ ياقوت أبيض | المجموعة الكلاسيكية | 218.04 | 260.8 | 16.4% | 2026-10-06 | in |
| 1357196057 | شماغ كلاسيك عنبر صافي | المجموعة الكلاسيكية | 218.04 | 256.52 | 15% | 2026-10-06 | in |
| 1499162789 | غترة العطار مكثل | المجموعة الكلاسيكية | 110.86 | 130.4 | 15% | 2026-10-06 | in |
| 966965063 | شماغ العطار كلاسيك ياقوت | المجموعة الكلاسيكية | 229.07 | 269.5 | 15% | 2026-10-06 | in |
| 1983204219 | شماغ العطار كلاسيك عقيق | المجموعة الكلاسيكية | 240.21 | 282.6 | 15% | 2026-10-06 | in |
| 24078165 | شماغ ختم العطار 26 الاحمر | أشمغة حمراء | 221.73 | 260.86 | 15% | 2026-10-06 | in |
| 160018205 | شماغ الهدا | أشمغة حمراء | 181.08 | 213.04 | 15% | 2026-10-06 | in |
| 1664674203 | نقش العطار 26 الأحمر | أشمغة حمراء | 181.08 | 213.04 | 15% | 2026-10-06 | in |
| 1546150268 | شماغ الوسام 26 الأحمر | أشمغة حمراء | 207 | 243.48 | 15% | 2026-10-06 | in |
| 1471159401 | شماغ حفاوة العطار 1 الاحمر | أشمغة حمراء | 144.08 | 169.5 | 15% | 2026-10-06 | in |
| 99351912 | شماغ حفاوة العطار 2 الاحمر | أشمغة حمراء | 144.08 | 169.5 | 15% | 2026-10-06 | in |
| 1988908934 | شماغ ياقوت شلش أحمر | أشمغة حمراء | 221.73 | 260.87 | 15% | 2026-10-06 | in |
| 290704026 | نقش العطار 26 الأبيض | أشمغة بيضاء | 181.05 | 213 | 15% | 2026-10-06 | in |
| 1721304177 | شماغ حفاوة العطار 1 الأبيض | أشمغة بيضاء | 144.08 | 169.5 | 15% | 2026-10-06 | in |
| 892978768 | قميص داخلي وثير إيطالي (قطعة واحدة) | وثير للملابس الداخلية | 44.34 | 52.17 | 15% | 2026-10-06 | in |
| 1744147328 | شال سادة | المنتجات الشتوية | 133.04 | 156.52 | 15% | 2026-10-06 | in |
| 916844931 | شال باشميناQ1S55 | المنتجات الشتوية | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 1691931266 | شال باشمينا Q1S60 | المنتجات الشتوية | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 957781120 | شال باشمينا Q2S58 | المنتجات الشتوية | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 493049478 | شال باشمينا Q2S60 | المنتجات الشتوية | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 668731835 | شال باشمينا Q3S58 | المنتجات الشتوية | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 285519455 | شال البيداء نص ترمه m16s58 | المنتجات الشتوية | 340 | 400 | 15% | open | in |
| 1053178443 | شال البيداء نص ترمه m2s60 | المنتجات الشتوية | 340 | 400 | 15% | open | in |
| 320666697 | شال البيداء نص ترمهm3s60 | المنتجات الشتوية | 340 | 400 | 15% | open | in |
| 630038350 | شال البيداء نص ترمه m4s60 | المنتجات الشتوية | 340 | 400 | 15% | open | in |
| 4977729 | شال البيداء نص ترمهm6s55 | المنتجات الشتوية | 340 | 400 | 15% | open | in |
| 663088504 | شال البيداء نص ترمه m11s60 | المنتجات الشتوية | 340 | 400 | 15% | open | in |
| 1438174847 | شال البيداء نص ترمهm12s60 | المنتجات الشتوية | 340 | 400 | 15% | open | in |
| 1870697154 | شال باشمينا Q1S55 | الأصواف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 47352825 | شال باشمينا Q3S55 | الأصواف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 821325048 | شال باشمينا Q4S55 | الأصواف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 531874291 | شال باشمينا Q5S55 | الأصواف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 681314293 | شال باشمينا Q6S55 | الأصواف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 1629527017 | شال باشمينا Q7S55 | الأصواف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 1341059308 | شال باشمينا Q9S55 | الأصواف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 1239830174 | شال البيداء نص تورمه M2S55 | الأصواف | 340 | 400 | 15% | open | in |
| 183743361 | شال باشمينا Q2S55 | غير مصنف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 2049055147 | شال باشميناQ6S55 | غير مصنف | 886.96 | 1,043.47 | 15% | 2026-10-06 | in |
| 1129261946 | شال البيداء نص ترمه m7s60 | غير مصنف | 340 | 400 | 15% | open | in |
| 193975872 | شماغ العطار كلاسيك عنبر | المجموعة الكلاسيكية | 221.74 | 256.52 | 13.6% | 2026-10-06 | in |
| 1712185778 | غترة العطار العصرية | الغتر | 148.5 | 165 | 10% | 2026-10-06 | **OUT** |
| 437508308 | شماغ نقش العطار 25 الاحمر | أشمغة حمراء | 272 | 278.26 | 2.2% | 2026-10-06 | **OUT** |

## Photography: main-photo classes per category

Classes: packshot_plain, packshot_in_box, worn_by_model, lifestyle, fabric_closeup. The PIL/OpenCV heuristic agreed with the eye review on 127/137; the eye review is final (see `data/photo_classes.json`).

| Category | Main-photo classes | Median main long edge (px) | Mains < 1200 px | Model shots in galleries |
|---|---|---:|---:|---:|
| المجموعة الكلاسيكية | packshot_in_box 12 | 1635 | 0 | 8 |
| أشمغة حمراء | packshot_in_box 18, lifestyle 2 | 1250 | 5 | 11 |
| الغتر | packshot_in_box 8 | 1125 | 4 | 2 |
| أشمغة بيضاء | packshot_in_box 5 | 1250 | 1 | 3 |
| مجموعة حفاوة | packshot_in_box 3 | 1250 | 1 | 0 |
| مجموعة الأصالة | packshot_in_box 9 | 1000 | 6 | 0 |
| وثير للملابس الداخلية | packshot_plain 7 | 2020 | 3 | 0 |
| الأقمشة | fabric_closeup 39 | 1400 | 18 | 0 |
| الأقمشة › سمير اميس | fabric_closeup 1 | 900 | 1 | 0 |
| الأقمشة › الاقمشه الاوروبيه | fabric_closeup 2 | 900 | 2 | 0 |
| الأقمشة › تترونات | fabric_closeup 14 | 1525 | 6 | 0 |
| الأقمشة › الأقمشة اليابانية | fabric_closeup 24 | 1500 | 9 | 0 |
| الأقمشة › أقطان طبيعية | fabric_closeup 4 | 2034 | 1 | 0 |
| الأقمشة › الأقمشة السويسرية | fabric_closeup 2 | 2048 | 0 | 0 |
| الأقمشة › الأقمشة الإيطالية | fabric_closeup 2 | 1150 | 1 | 0 |
| الأقمشة › مخلوط | fabric_closeup 3 | 2020 | 1 | 0 |
| الأقمشة › الأقمشة الكورية | fabric_closeup 5 | 1000 | 5 | 0 |
| المنتجات الشتوية | packshot_plain 13, fabric_closeup 5, packshot_in_box 1 | 4705 | 3 | 0 |
| الأصواف | packshot_plain 22, fabric_closeup 14 | 2923 | 7 | 0 |
| الأصواف › الشالات | packshot_plain 22, fabric_closeup 6 | 4299 | 2 | 0 |
| الأصواف › الأصواف الإنجليزية | fabric_closeup 4 | 1250 | 2 | 0 |
| الأصواف › الأصواف الإيطالية | fabric_closeup 4 | 1000 | 3 | 0 |
| اخرى | packshot_in_box 7, lifestyle 5, packshot_plain 2 | 1439 | 5 | 5 |
| اخرى › اكسسوارات | packshot_plain 2, packshot_in_box 1 | 2020 | 1 | 0 |
| اخرى › المنتجات المخفضة | packshot_in_box 4, lifestyle 2 | 1275 | 3 | 5 |
| اخرى › العطور | lifestyle 3, packshot_in_box 1 | 2389 | 0 | 0 |
| اخرى › هدايا | packshot_in_box 2 | 2950 | 1 | 0 |
| غير مصنف (خارج القائمة) | fabric_closeup 10, packshot_plain 3 | 1000 | 10 | 0 |

## Best hero candidates per category

Picked by eye from the contact sheets: clean background, sharp, high resolution, product in stock unless marked. Paths are relative to the project root.

**المجموعة الكلاسيكية**

- `data/images/966965063_3.jpg` (1346x2020), شماغ العطار كلاسيك ياقوت: Model, Yaqoot red shemagh, symmetrical front pose, clean white sweep
- `data/images/1983204219_3.jpg` (1494x2020), شماغ العطار كلاسيك عقيق: Model adjusting the Aqeeq shemagh (gesture shot)
- `data/images/502827333_2.jpg` (1246x2020), غترة العطار كلاسيك: Model in the white Classic ghutra
- `data/images/1983204219_1.jpg` (2020x1577), شماغ العطار كلاسيك عقيق: Best green-box packshot of the range (2020 px)

**أشمغة حمراء**

- `data/images/966965063_2.jpg` (1386x2020), شماغ العطار كلاسيك ياقوت: Model, Yaqoot shemagh, three-quarter
- `data/images/1604079293_3.jpg` (1241x2020), شماغ أوديمار 4: Model, Audemar 4 shemagh
- `data/images/24078165_3.jpg` (1138x2020), شماغ ختم العطار 26 الاحمر: Model, Khatm 26 red, shemagh thrown back
- `data/images/1988908934_2.jpg` (3803x3803), شماغ ياقوت شلش أحمر: High-res weave detail (3803 px)

**الغتر**

- `data/images/502827333_2.jpg` (1246x2020), غترة العطار كلاسيك: Model in the Classic ghutra
- `data/images/1740470085_2.jpg` (3859x3859), غتر العطار زمرد: "100% COTTON VOILE BY M.SIRAJ ATTAR" selvedge detail, 3859 px
- `data/images/1740470085_1.jpg` (6000x6000), غتر العطار زمرد: Green-box packshot, 6000 px
- `data/images/1499162789_3.jpg` (6000x4000), غترة العطار مكثل: Fringed edge detail, 6000 px

**أشمغة بيضاء**

- `data/images/2124457749_7.jpg` (1127x2020), شماغ زمرد (نقشة الليزر ): Model in the laser-patterned white Zumurrud shemagh
- `data/images/2124457749_6.jpg` (3456x2304), شماغ زمرد (نقشة الليزر ): Laser pattern detail, 3456 px
- `data/images/1211546059_1.jpg` (2020x1574), شماغ ياقوت أبيض: Green-box packshot, 2020 px

**مجموعة حفاوة**

- `data/images/99351912_2.jpg` (1000x1250), شماغ حفاوة العطار 2 الاحمر: Weave close-up (1250 px; best available)
- `data/images/1471159401_1.jpg` (900x1125), شماغ حفاوة العطار 1 الاحمر: Green-box packshot (1125 px)

**مجموعة الأصالة**

- `data/images/1546150268_4.jpg` (1200x1500), شماغ الوسام 26 الأحمر: Wisam 26 weave close-up (1500 px)
- `data/images/160018205_1.jpg` (1000x1250), شماغ الهدا: Green-box packshot (1250 px)

**وثير للملابس الداخلية**

- `data/images/892978768_2.jpg` (2020x1685), قميص داخلي وثير إيطالي (قطعة واحدة): Wathir gift packaging in raking light (only lifestyle frame)
- `data/images/931289172_1.jpg` (1758x2020), قميص داخلي رجالي كومفورت: Ghost-mannequin undershirt, 2020 px
- `data/images/230109116_1.png` (1080x1080), جوارب وثير الخفيفة (ألوان متعددة): Four-colour sock fan, 1080 px

**الأقمشة**

- `data/images/512779702_1.jpg` (2020x1818), قماش العطار اسباني قطن 23: Pinked swatch fan, cream to white, 2020 px
- `data/images/1292393513_1.jpg` (2048x1365), العطار 909: Lilac-white drape with gold "MADE IN JAPAN 909" selvedge print, 2048 px
- `data/images/2029457986_1.jpg` (2020x1346), العطار 913: Gold-foil "العطار 913" branded fabric, 2020 px
- `data/images/1146743451_1.jpg` (2048x1365), هاي لايف: Soft white drape, 2048 px
- `data/images/795805893_1.jpg` (2048x1365), سويسري S-8916 (لونين) **(out of stock)**: Sharpest fabric texture in the store (taupe Swiss cotton, 2048 px), reference only

**المنتجات الشتوية**

- `data/images/821325048_1.jpg` (4484x2989), شال باشمينا Q4S55: Embroidered pashmina flat-lay, 4484 px (retouch gold pins)
- `data/images/663088504_2.jpg` (5184x3456), شال البيداء نص ترمه m11s60: Navy-embroidered Al-Baidaa shawl, 5184 px
- `data/images/1449104353_4.jpg` (4032x2268), صوف ايطالي انجليكو سوبر 140 مقلم: Italian striped wool, folded, 4032 px

**الأصواف**

- `data/images/1449104353_4.jpg` (4032x2268), صوف ايطالي انجليكو سوبر 140 مقلم: Italian striped wool, folded, 4032 px
- `data/images/47352825_1.jpg` (4660x3107), شال باشمينا Q3S55: Pashmina embroidery fills frame, 4660 px
- `data/images/1449104353_5.jpg` (3566x2674), صوف ايطالي انجليكو سوبر 140 مقلم: Navy pinstripe wool folds, 3566 px

**الأصواف › الشالات**

- `data/images/821325048_1.jpg` (4484x2989), شال باشمينا Q4S55: Embroidered pashmina flat-lay, 4484 px (retouch gold pins)
- `data/images/47352825_1.jpg` (4660x3107), شال باشمينا Q3S55: Embroidery detail, 4660 px
- `data/images/681314293_3.jpg` (5184x3456), شال باشمينا Q6S55: Navy paisley close-up, 5184 px

**الأصواف › الأصواف الإنجليزية**

- `data/images/1029444903_1.jpg` (1500x1000), صوف ويليام هليستد سوبر 130 ساده: Solid navy wool drape (1500 px; one photo per product)
- `data/images/1419600434_1.jpg` (1500x1000), صوف omc سوبر 150 مقلم: Wool bolt with selvedge (1500 px)

**الأصواف › الأصواف الإيطالية**

- `data/images/1449104353_4.jpg` (4032x2268), صوف ايطالي انجليكو سوبر 140 مقلم: Striped wool folds, 4032 px
- `data/images/1449104353_1.jpg` (3670x2752), صوف ايطالي انجليكو سوبر 140 مقلم: Main photo, 3670 px

**اخرى › اكسسوارات**

- `data/images/265256366_2.jpg` (2020x1572), كبك فضي (خيارات متعددة): Silver cufflinks on white plinths, 2020 px
- `data/images/1610956716_1.jpg` (2020x1317), كبك أزرق (خيارات متعددة): Blue cufflinks, 2020 px

**اخرى › المنتجات المخفضة**

- `data/images/2125369422_4.jpg` (1434x2020), شماغ برنيني أحمر **(out of stock)**: Close portrait, Bernini red (product OUT OF STOCK)
- `data/images/1842109012_3.jpg` (1325x2020), شماغ برنيني ذهبي **(out of stock)**: Model, Bernini gold (OUT OF STOCK)

**اخرى › العطور**

- `data/images/189452492_1.jpg` (2595x3450), Attar 3 _ العطار 3: Attar 3 bottle on wood with flowers, 3450 px
- `data/images/14237135_2.jpg` (1000x1329), ِAttar 1 _ العطار 1: Hand holding Attar 1 against thobe and shemagh (1329 px)
- `data/images/672063087_1.jpg` (5000x5000), مجموعة عطور العطار: Three-bottle set in the green box, 5000 px

**اخرى › هدايا**

- `data/images/672063087_1.jpg` (5000x5000), مجموعة عطور العطار: Perfume trio in the green box, 5000 px
- `data/images/1381142749_3.webp` (900x900), صندوق الإهداء الخاص: Gift box: shemagh + perfume + cufflinks (900 px only)

Notes for hero use:
- The best model shots of the Bernini, Zafeer and Golden shemaghs (2125369422, 1842109012, 2024205944, 333921099) and the Asriya ghutra (1712185778) are **out of stock**. Avoid them for campaigns, or check stock first.
- In-stock products with model shots: 966965063, 1983204219, 502827333, 2124457749, 1604079293, 24078165.
- Location and lifestyle imagery with people exists only in the home-page banners (`brand/site_banners/`): a falconer in the dunes, and an elderly man with younger men in front of a lantern-lit mud-brick wall under the "تميّز متوارث" campaign. No product page has it.

## Categories with weak photography

- **مجموعة حفاوة**: No model shot; max 1250 px; 3 near-identical green-box shots; two of three products have no description.
- **مجموعة الأصالة**: 6 of 9 main photos under 1200 px; no model shot; all box packshots.
- **الأقمشة الكورية**: All 5 products: one 1000 px gold-foil text shot + one plain white drape; layouts identical, nothing shows the cloth made up.
- **الاقمشه الاوروبيه / سمير اميس**: One or four 900 px WebP images per product; soft (lowest sharpness in the store).
- **الأقمشة الإيطالية**: Main photos 900 to 1400 px; 1 of 2 products out of stock.
- **الأصواف الإنجليزية**: One photo per product, 999 to 1500 px, plain drapes only.
- **الشالات / المنتجات الشتوية**: High resolution (up to 5184 px) but every shot is the same white flat-lay; gold push-pins and black hang-tags are visible in many frames; no shawl is shown worn (over a bisht or thobe).
- **اكسسوارات (عقال)**: Agal: main 1000 px, gallery shots 370 px.
- **هدايا (صندوق الإهداء)**: Gift box only 900 px WebP.
- **الأقمشة (all)**: No photograph links a fabric to a finished thobe; 18 of 39 main photos under 1200 px.
- **غير مصنف**: 10 of 13 main photos at 900 to 1000 px.

Store-wide gaps: no main image shows the product worn; no thobe-fabric image shows a finished thobe; shawls are never shown draped; perfume is the only range with styled lifestyle sets. Fabric main photos are mostly gold-foil branded swatches. They are consistent, but they all look alike across 39 products.

## Out of stock (20)

- 333921099 شماغ العطار الذهبي (المجموعة الكلاسيكية, أشمغة بيضاء)
- 437508308 شماغ نقش العطار 25 الاحمر (أشمغة حمراء, اخرى)
- 1842109012 شماغ برنيني ذهبي (أشمغة حمراء, اخرى)
- 2125369422 شماغ برنيني أحمر (أشمغة حمراء, اخرى)
- 2024205944 شماغ كلاسيك زفير (أشمغة حمراء, اخرى)
- 1712185778 غترة العطار العصرية (الغتر)
- 870973619 جوارب وثير الرسمية (ألوان متعددة) (وثير للملابس الداخلية)
- 152164309 قماش ايطالي تيستا دايمونتي (الأقمشة, الأقمشة الإيطالية)
- 553719979 قماش العطار 35 (الأقمشة, الأقمشة اليابانية)
- 139738121 قماش العطار 333 (الأقمشة, تترونات)
- 1150351142 العطار سويسري S- 2920 (الأقمشة, أقطان طبيعية)
- 795805893 سويسري S-8916 (لونين) (الأقمشة, أقطان طبيعية)
- 74544352 صوف ايطالي انجليكو سوبر 140 سادة (المنتجات الشتوية, الأصواف)
- 144922964 شال البيداء نص ترمه m1s60 (المنتجات الشتوية, الأصواف)
- 579546591 شال باشمينا N11S60 (الأصواف, الشالات)
- 1353584350 شال باشمينا N12S60 (الأصواف, الشالات)
- 113373149 شال باشمينا N13S60 (الأصواف, الشالات)
- 1062495185 شال البيداء نص تورمه N6S60 (الأصواف, الشالات)
- 1838105808 شال البيداء نص تورمه N26S58 (الأصواف, الشالات)
- 329393623 شال البيداء نص تورمه N25S58 (الأصواف, الشالات)

