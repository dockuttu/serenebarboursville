#!/usr/bin/env bash
# build.sh — regenerate the Barboursville site (lean: static homepage + blog)
set -euo pipefail
cd "$(dirname "$0")"
echo "==> Building blog"
python3 build_blog.py
echo "==> Cache-bust styles.css"
python3 cachebust.py
if [ ! -s bundle/site/index.html ] || [ "$(wc -c < bundle/site/index.html)" -lt 2000 ]; then
  echo "!!! sanity check FAILED" >&2; exit 1; fi
echo "==> Build complete: $(find bundle/site -type f | wc -l) files in bundle/site/"
