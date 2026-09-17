# nav_gallery.py — idempotent: add a "Gallery" link (/before-after/) to the main nav and the
# footer Treatments column on every built page (hand-built pages carry their own nav copy).
# Skips the noindex Google Ads landing pages under /lp/.
import os, sys, glob
BASE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
NAV_OLD  = '<li><a href="/pricing/">Pricing</a></li>'
NAV_NEW  = NAV_OLD + '\n      <li><a href="/before-after/">Gallery</a></li>'
FOOT_OLD = '<li><a href="/pricing/">Pricing &amp; Menu</a></li>'
FOOT_NEW = FOOT_OLD + '\n          <li><a href="/before-after/">Before &amp; After Gallery</a></li>'
n = 0
for p in glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True):
    if os.sep + "lp" + os.sep in p:
        continue
    s = open(p, encoding="utf-8").read()
    t = s
    if 'href="/before-after/">Gallery</a>' not in t:
        t = t.replace(NAV_OLD, NAV_NEW, 1)
    if 'href="/before-after/">Before &amp; After Gallery</a>' not in t:
        t = t.replace(FOOT_OLD, FOOT_NEW, 1)
    if t != s:
        open(p, "w", encoding="utf-8").write(t); n += 1
print("nav_gallery: updated", n, "page(s)")
