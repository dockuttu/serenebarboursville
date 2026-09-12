# -*- coding: utf-8 -*-
# Builds the four hand-authored pages (botox, fillers, morpheus8, weight-loss) for Barboursville
# from the shared templates in templates/, swapping in Barboursville nav/footer/location/contact
# and Mangomint deep links. Pure stdlib.
import re, os
exec(open("common.py").read())
from bv_localize import _s
SITE="bundle/site"

def block(s, start_pat, end_pat, repl):
    """Replace the first start..end (inclusive) block with repl."""
    a=s.find(start_pat)
    if a<0: return s
    b=s.find(end_pat,a)
    if b<0: return s
    return s[:a]+repl+s[b+len(end_pat):]

LOC_SECTION_RE=re.compile(r'<section class="location" id="location">.*?</section>', re.S)
BV_LOCATION='''<section class="location" id="location">
  <div class="wrap loc-grid">
    <div class="loc-info reveal">
      <div class="eyebrow" style="-webkit-text-fill-color:initial;color:var(--gold);background:none">Visit Us</div>
      <h2 style="font-size:clamp(2.1rem,4.4vw,3rem);margin-bottom:20px">Serene Med Spa &mdash; Barboursville</h2>
      <div class="row"><strong>Address</strong><span>1 Chateau Grove Ln<br>Barboursville, WV 25504</span></div>
      <div class="row"><strong>Call</strong><span><a href="%s">%s</a></span></div>
      <div class="row"><strong>Hours</strong><span>Mon&ndash;Fri: 9 AM &ndash; 5 PM<br>Sat&ndash;Sun: By appointment</span></div>
      <div style="margin-top:28px"><a class="btn" href="%%BOOK%%" target="_blank" rel="noopener">Book Online</a></div>
    </div>
    <iframe class="map reveal" loading="lazy" title="Map to Serene Med Spa Barboursville" src="https://www.google.com/maps?q=1+Chateau+Grove+Ln+Barboursville+WV+25504&output=embed"></iframe>
  </div>
</section>''' % (PHONE_TEL, PHONE_DISPLAY)

for slug in ["botox","fillers","morpheus8","weight-loss"]:
    s=open("templates/%s.html"%slug, encoding="utf-8").read()
    book=book_for(slug)
    # structural swaps
    s=block(s,"<header>","</header>",NAV)
    s=block(s,"<footer>","</footer>",FOOTER)
    s=block(s,'<section class="stats">',"</section>",STATS_BRANDS)
    if slug in PM_SLUGS: s=s.replace(STATS_BRANDS, STATS_BRANDS+"\n"+PRICE_MATCH_BAND, 1)
    s=block(s,'<section class="tint-blush" id="reviews">',"</section>",REVIEWS_SECTION)
    s=block(s,'<section class="results" id="results">',"</section>",RESULTS_SECTION)
    s=block(s,'<section class="areas">',"</section>","%AREAS%")
    s=block(s,'<section class="consult" id="consult">',"</section>",CONSULT_SECTION)
    s=block(s,'<div class="finance">',"</div></div>",FINANCE_BAND)
    s=LOC_SECTION_RE.sub(BV_LOCATION,s,count=1)
    s=block(s,'<div class="mbar">',"</div>",STICKY_BAR)
    # Allergan Platinum badge under the hero copy (botox / fillers)
    _bd=device_badge(slug,{"botox":["botox-cosmetic","app-platinum"],"fillers":["juvederm","app-platinum"]})
    _seal=hero_seal(slug,{"botox":["app-platinum"],"fillers":["app-platinum"]})
    if _seal and "hero-seal" not in s: s=s.replace('<div class="svc-hero-media">', '<div class="svc-hero-media">'+_seal,1)
    if _bd and "device-badge" not in s:
        _i=s.index('<div class="svc-hero-txt">'); _j=s.index("</p>",_i)+4; s=s[:_j]+"\n    "+_bd+s[_j:]
    # scripts: everything after the sticky bar up to </body>
    tail=s.rfind("</body>")
    head_end=s.find(STICKY_BAR)+len(STICKY_BAR)
    s=s[:head_end]+"\n"+SCRIPTS+"\n"+s[tail:]
    # remove any leftover inline faq/reveal script above the mbar (now in SCRIPTS)
    s=re.sub(r"<script>\s*document\.querySelectorAll\('\.faq button'\).*?</script>\s*","",s,flags=re.S)
    # geo + booking + text
    s=s.replace('<meta name="geo.region" content="US-OH">','<meta name="geo.region" content="US-WV">')
    s=re.sub(r'content="41\.2401;-81\.4409"','content="38.4109;-82.2926"',s); s=re.sub(r'content="41\.2401, -81\.4409"','content="38.4109, -82.2926"',s)
    s=s.replace("https://booking.mangomint.com/585660",book).replace("%BOOK%",book)
    s=_s(s)
    # area keyword per page
    kw={"botox":"Botox &amp; wrinkle relaxers","fillers":"dermal fillers","morpheus8":"Morpheus8","weight-loss":"medical weight loss"}[slug]
    s=s.replace("%AREAS%",areas_section(kw))
    # schema: provider address
    s=s.replace('"addressLocality": "Barboursville", "addressRegion": "WV", "postalCode": "25504"','"addressLocality": "Barboursville", "addressRegion": "WV", "postalCode": "25504"')
    os.makedirs(os.path.join(SITE,slug),exist_ok=True)
    open(os.path.join(SITE,slug,"index.html"),"w",encoding="utf-8").write(s)
    print("static:",slug,len(s),"bytes")
