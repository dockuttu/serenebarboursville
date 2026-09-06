#!/usr/bin/env bash
# build.sh — regenerate the Barboursville site (lean: static homepage + blog + service pages)
set -euo pipefail
cd "$(dirname "$0")"
echo "==> Building blog"
python3 build_blog.py
echo "==> Building Ultherapy service page"
python3 build_ultherapy.py
echo "==> Building Xperience+ rewards page"
python3 build_rewards.py
echo "==> Generating sitemap.xml"
python3 build_sitemap.py
echo "==> Cache-bust styles.css"
python3 cachebust.py
if [ ! -s bundle/site/index.html ] || [ "$(wc -c < bundle/site/index.html)" -lt 2000 ]; then
  echo "!!! sanity check FAILED" >&2; exit 1; fi
echo "==> Build complete: $(find bundle/site -type f | wc -l) files in bundle/site/"
