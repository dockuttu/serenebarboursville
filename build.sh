#!/usr/bin/env bash
# build.sh — regenerate the Barboursville site into bundle/site/ (pure Python 3 stdlib; idempotent)
set -euo pipefail
cd "$(dirname "$0")"
echo "==> Homepage";            python3 build_home.py
echo "==> Service pages";       python3 gen_pages.py
python3 build_cities.py
echo "==> Hand-built pages";    python3 build_static.py
echo "==> Pricing";             python3 build_pricing.py
# blog moved to blog.serenemedspas.com (repo sereneblog); old /blog/ URLs 301 via bundle/nginx.conf
rm -rf bundle/site/blog 2>/dev/null || true
python3 fix_blog_links.py
echo "==> Ultherapy";           python3 build_ultherapy.py
echo "==> Xperience+ rewards";  python3 build_rewards.py
echo "==> SEO trim";            python3 seo_trim.py
echo "==> Sitemap";             python3 build_sitemap.py
echo "==> Cache-bust";          python3 cachebust.py
if [ ! -s bundle/site/index.html ] || [ "$(wc -c < bundle/site/index.html)" -lt 2000 ]; then
  echo "!!! sanity check FAILED" >&2; exit 1; fi
echo "==> Build complete: $(find bundle/site -type f | wc -l) files in bundle/site/"

echo "==> Google Ads tag"
python3 build_wl_ads.py bundle/site   # ads-only /medical-weight-loss/ (noindex, no drug names)
python3 inject_gtag.py bundle/site

echo "==> Page guard (nav <-> built pages <-> deep links)"
python3 seo_polish.py bundle/site
python3 check_pages.py
