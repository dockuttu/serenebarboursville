#!/usr/bin/env bash
# build.sh — regenerate the Barboursville site into bundle/site/ (pure Python 3 stdlib; idempotent)
set -euo pipefail
cd "$(dirname "$0")"
echo "==> Homepage";            python3 build_home.py
echo "==> Service pages";       python3 gen_pages.py
python3 build_cities.py
python3 build_aftercare.py        # /aftercare/ hub + 25 per-treatment post-care pages
python3 build_service_cities.py   # service+region landing pages (WV state-level + Huntington gaps)
echo "==> Hand-built pages";    python3 build_static.py
echo "==> Pricing";             python3 build_pricing.py
# blog moved to blog.serenemedspas.com (repo sereneblog); old /blog/ URLs 301 via bundle/nginx.conf
rm -rf bundle/site/blog 2>/dev/null || true
python3 fix_blog_links.py
echo "==> Ultherapy";           python3 build_ultherapy.py
echo "==> Xperience+ rewards";  python3 build_rewards.py
echo "==> Before & After";      python3 build_gallery.py
echo "==> Easy Pay";            python3 build_easypay.py
python3 build_labs.py        # /labs/ test guide pages
python3 build_obagi_shop.py   # Obagi store: /shop/, /shop/<product>/, /cart/, /obagi/, shop.js
echo "==> SEO trim";            python3 seo_trim.py
echo "==> Sitemap";             python3 build_thankyou.py
python3 patch_static_consult.py   # hand-built pages + popup.js -> Zoho form
python3 build_sitemap.py
python3 complimentary_pass.py bundle/site   # "free consultation" -> "complimentary, no-commitment consultation"
echo "==> Cache-bust";          python3 cachebust.py
if [ ! -s bundle/site/index.html ] || [ "$(wc -c < bundle/site/index.html)" -lt 2000 ]; then
  echo "!!! sanity check FAILED" >&2; exit 1; fi
echo "==> Build complete: $(find bundle/site -type f | wc -l) files in bundle/site/"

echo "==> Google Ads tag"
python3 build_wl_ads.py bundle/site   # ads-only /medical-weight-loss/ (noindex, no drug names)
python3 build_ads_pages.py bundle/site   # ads-only /lp/* pages (noindex, no drug names) for Google Ads
python3 inject_gtag.py bundle/site
python3 inject_meta_pixel.py bundle/site   # Meta pixel 475660982946848

echo "==> Page guard (nav <-> built pages <-> deep links)"
python3 easypay_inject.py bundle/site   # Easy Pay band + nav/footer links on every page
python3 shop_inject.py bundle/site      # cart button (shop.js) + Shop nav/footer links on every page
python3 home_badges.py bundle/site      # Biote badge on the homepage
python3 tattoo_pricing.py bundle/site   # tattoo size guide + prices + 5+1 offer on /laser-tattoo-removal/
python3 home_obagi.py bundle/site       # Obagi authorized-provider logo + skincare band on the homepage
python3 home_merz.py bundle/site        # Merz Aesthetics ELITE+ provider status on the homepage
python3 complimentary_pass.py bundle/site   # again, for pages injected after cache-bust
python3 fix_charset.py bundle/site      # <meta charset> must be in the first 1024 bytes
python3 nav_gallery.py bundle/site     # Gallery link in nav + footer (skips /lp/ ads pages)
python3 nav_longevity.py bundle/site   # Longevity link in static pages' mega-menu (skips /lp/ ads pages)
python3 seo_polish.py bundle/site
python3 seo_tech.py bundle/site      # schema cleanup + founder entities, default og:image, branded 404
python3 form_guard_inject.py bundle/site   # spam screening on lead forms + popup source tag
python3 local_sections.py bundle/site     # location-specific block on the top treatment pages
python3 bv_unique_static.py bundle/site   # Barboursville-only wording on the hand-built pages
python3 review_cta_inject.py bundle/site   # Google review ask at the end of every aftercare block
python3 ultherapy_results.py bundle/site   # Ultherapy PRIME before/after (Merz photos)
python3 seo_targeting.py bundle/site # final titles/descriptions for search targeting (Huntington)
python3 check_pages.py
