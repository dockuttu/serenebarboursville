# Restore original meta descriptions from source data, then trim <title> (<=60)
# and description (<=155) cleanly on word/sentence boundaries (no mid-word or
# dangling-preposition cuts). Idempotent: always trims from the ORIGINAL source,
# so re-running fixes any earlier awkward truncations. Build step.
import glob, re, os
from html import unescape
BASE="bundle/site"

# ---- originals for generated (data-driven) pages, keyed by slug ----
ns={}
exec(open("common.py").read(), ns)
exec(open("pages_data.py").read(), ns)
for _k in ('PAGES2','PAGES3','PAGES4','PAGES5','PAGES6'): ns[_k]=[]
import glob as _glob
for _f in sorted(_glob.glob('pages_data_new*.py')): exec(open(_f).read(), ns)
from bv_localize import localize, BV_OVERRIDES
ORIG_DESC={}
for p in ns['PAGES']+ns['PAGES2']+ns['PAGES3']+ns['PAGES4']+ns['PAGES5']+ns['PAGES6']:
    q=BV_OVERRIDES[p['slug']](localize(p))
    ORIG_DESC[p['slug']]=q['desc']

SPECIAL_TITLES={
 "index.html":"Serene Med Spa &mdash; Barboursville, WV | Botox, Fillers &amp; More",
 "pricing/index.html":"Menu &amp; Pricing &mdash; Serene Med Spa, Barboursville WV",
 "botox/index.html":"Botox in Barboursville, WV | Serene Med Spa",
 "fillers/index.html":"Dermal Fillers in Barboursville, WV | Serene Med Spa",
 "morpheus8/index.html":"Morpheus8 in Barboursville, WV | Serene Med Spa",
 "weight-loss/index.html":"Medical Weight Loss in Barboursville, WV | Serene Med Spa",
 "hyperpigmentation/index.html":"Hyperpigmentation Treatment in Barboursville, WV | Serene",
 "womens-sexual-wellness/index.html":"Women's Sexual Wellness in Barboursville, WV | Serene",
 "mens-sexual-wellness/index.html":"Men's Sexual Wellness in Barboursville, WV | Serene Med Spa",
 "laser-nail-fungus/index.html":"Laser Nail Fungus Treatment in Barboursville, WV | Serene",
 "medical-facials/index.html":"Facials &amp; Microdermabrasion in Barboursville, WV | Serene",
 "laser-skin/index.html":"Laser Skin Resurfacing in Barboursville, WV | Serene Med Spa",
 "photofacial/index.html":"BBL &amp; IPL Photofacial in Barboursville, WV | Serene Med Spa",
}
# Clean, hand-written descriptions for hand-built pages whose original long
# text is not in the data files (so they can't be sourced/re-trimmed).
SPECIAL_DESCS={
 "index.html":"Physician-led medical spa in Barboursville, WV — Botox, fillers, Morpheus8, Ultherapy, laser, HydraFacial, weight loss & IV wellness. Book online today.",
 "botox/index.html":"Botox, Dysport & Xeomin in Barboursville, WV — physician-led wrinkle relaxers for natural, refreshed results. From $10/unit. Book online today.",
 "fillers/index.html":"Physician-injected dermal fillers in Barboursville, WV — lip, cheek, jawline & under-eye filler for natural volume and definition. Book your consultation.",
 "morpheus8/index.html":"Morpheus8 RF microneedling in Barboursville, WV at Serene Med Spa — tighten, smooth, and resurface skin on the face and body. Physician-led. Book today.",
 "weight-loss/index.html":"Physician-supervised medical weight loss in Barboursville, WV — personalized GLP-1 programs guided by board-certified providers. Book a consultation.",
 "pricing/index.html":"Serene Med Spa Barboursville pricing — Botox from $10/unit, fillers, Morpheus8, Ultherapy, laser hair removal packages, HydraFacial, weight loss & IV.",
 "womens-sexual-wellness/index.html":"Physician-led women's sexual wellness in Barboursville, WV — discreet, non-surgical care including the O-Shot (PRP), VTone, FormaV & Morpheus8 V. Book today.",
 "mens-sexual-wellness/index.html":"Physician-led men's sexual wellness in Barboursville, WV — discreet, non-surgical care including Alma Duo acoustic wave therapy & the P-Shot (PRP). Book today.",
}

def dlen(x): return len(unescape(x))

def short_title(raw):
    if dlen(raw)<=60: return raw
    parts=raw.split(" | ")
    if len(parts)>=3 and parts[-1].strip()=="Serene Med Spa":
        return parts[0]+" | "+parts[-1]          # drop middle descriptor
    if len(parts)==2 and "&mdash;" in parts[1]:
        return parts[0]+" | "+parts[1].split("&mdash;")[0].strip()  # drop tagline
    if len(parts)>=2 and dlen(parts[0]+" | Serene")<=60:
        return parts[0]+" | Serene"
    return raw

WEAK={'a','an','the','and','with','for','to','of','in','on','at','without','that','or','your',
 '&','&amp;','&mdash;','&ndash;','—','–','using','over','into','from','by','than'}
def _clean(x): return re.sub(r'[.,;:&—–-]','',x).lower()
def _tidy(s):
    toks=s.split(" "); changed=True
    while changed and toks:
        changed=False
        if _clean(toks[-1]) in WEAK|{''}:
            toks.pop(); changed=True; continue
        if len(toks)>=2 and not toks[-1].endswith('.') and _clean(toks[-2]) in WEAK:
            toks=toks[:-2]; changed=True
    return " ".join(toks).rstrip(" ,;:-&—–")
def short_desc(raw, target=153):
    if dlen(raw)<=155: return raw
    out=""
    for tok in raw.split(" "):
        cand=(out+" "+tok).strip()
        if dlen(cand)>target: break
        out=cand
    lp=out.rfind('.')
    if lp>=90: return out[:lp+1]
    lc=out.rfind(',')
    if lc>=90: return _tidy(out[:lc])
    return _tidy(out)

changed=0
pages=sorted(set(glob.glob(os.path.join(BASE,"**","index.html"),recursive=True))|{os.path.join(BASE,"index.html")})
for p in pages:
    rel=os.path.relpath(p,BASE)
    slug=rel[:-len("/index.html")] if rel.endswith("/index.html") else ""  # "" for homepage
    s=open(p).read(); orig=s
    # ---- title ----
    m=re.search(r'<title>(.*?)</title>',s,re.S)
    if m:
        raw=m.group(1); new=SPECIAL_TITLES.get(rel, short_title(raw))
        if new!=raw: s=s.replace("<title>%s</title>"%raw,"<title>%s</title>"%new,1)
    # ---- description (+ og:description) ----
    md=re.search(r'name="description" content="(.*?)"',s,re.S)
    if md:
        cur=md.group(1)
        source = SPECIAL_DESCS.get(rel) or ORIG_DESC.get(slug) or cur
        new=short_desc(source)
        if new!=cur:
            s=s.replace('name="description" content="%s"'%cur,'name="description" content="%s"'%new,1)
            s=s.replace('property="og:description" content="%s"'%cur,'property="og:description" content="%s"'%new,1)
    if s!=orig:
        open(p,"w").write(s); changed+=1
print("seo_trim: updated",changed,"pages")

# ---- verify ----
over_t=over_d=0
for p in pages:
    s=open(p).read()
    t=(re.search(r'<title>(.*?)</title>',s,re.S) or [None,""])[1]
    d=(re.search(r'name="description" content="(.*?)"',s,re.S) or [None,""])[1]
    if dlen(t)>60: over_t+=1; print("  long title (%d): %s"%(dlen(t),unescape(t)))
    if dlen(d)>155: over_d+=1; print("  long desc (%d): %s"%(dlen(d),unescape(d)[-40:]))
print("remaining over-length -> titles:",over_t," descriptions:",over_d)
