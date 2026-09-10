# -*- coding: utf-8 -*-
# Turns the shared (Hudson-authored) page copy into Barboursville copy, and applies
# Barboursville-specific rewrites for pages whose devices / offerings differ.
import re

# services Barboursville does not offer (Hudson-only devices) or that stay hidden
BV_SKIP = {"body-contouring", "emsculpt-neo", "lipomelt", "diamondglow", "peptide-therapy", "peptides", "house-calls"}

_SUBS = [
 ("Northeast Ohio", "the Tri-State"),
 ("Hudson, Ohio", "Barboursville, West Virginia"),
 ("Hudson, OH", "Barboursville, WV"),
 ("Hudson", "Barboursville"),
 ("Ohio", "West Virginia"),
 ("Akron", "Huntington"), ("Cleveland", "Charleston"),
 ("Summit, Portage, Cuyahoga, and Geauga counties", "Cabell, Wayne, Putnam and Lincoln counties"),
 ("Summit, Portage, Cuyahoga &amp; Geauga counties", "Cabell, Wayne, Putnam &amp; Lincoln counties"),
 ("(330) 460-5915", "(304) 520-0461"), ("(330)&nbsp;460-5915", "(304)&nbsp;520-0461"), ("330-460-5915", "304-520-0461"), ("+13304605915", "+13045200461"),
 ("50 W Streetsboro St, Suite 2", "1 Chateau Grove Ln"), ("44236", "25504"),
 ("hudson.serenemedspas.com", "barboursville.serenemedspas.com"),
 ("/hydration-bar/", "/iv-therapy/"),   # Hudson-only page
]
_OH = re.compile(r"\bOH\b")

def _s(x):
    for a, b in _SUBS: x = x.replace(a, b)
    return _OH.sub("WV", x)

def localize(o):
    """Deep-copy o (dict/list/tuple/str) with all strings localized."""
    if isinstance(o, str): return _s(o)
    if isinstance(o, dict): return {k: localize(v) for k, v in o.items()}
    if isinstance(o, list): return [localize(v) for v in o]
    if isinstance(o, tuple): return tuple(localize(v) for v in o)
    return o

# ---------------- Barboursville-specific rewrites ----------------
def _related(p, keep):
    p["related"] = [k for k in p["related"] if k not in BV_SKIP][:3] or keep
    return p

def laser_skin(p):
    p["title"] = "Laser Skin Resurfacing in Barboursville, WV | Alma Hybrid, Opus &amp; PICO"
    p["desc"] = "Laser skin resurfacing in Barboursville, WV — Alma Hybrid CO2, Opus Plasma, PICO fractional &amp; Moxi. Smooth texture, fine lines &amp; sun damage. Book today."
    p["ogdesc"] = "Smooth texture, fine lines & sun damage with Alma Hybrid CO2, Opus Plasma, PICO & Moxi resurfacing in Barboursville, WV."
    p["intropara"] = ("At Serene Med Spa in Barboursville, we offer a full range of resurfacing options &mdash; from gentle, no-downtime treatments like MOXI "
        "to the Alma Hybrid, which combines fractional CO2 with a non-ablative 1570&nbsp;nm laser in a single session, plus Opus Plasma and PICO fractional resurfacing. "
        "Your physician will match the depth of treatment to your skin, your goals and the downtime you can afford.")
    for i,(q,a) in enumerate(p["faqs"]):
        if "MOXI, Cool Peel" in a or "Cool Peel" in a:
            p["faqs"][i] = (q, a.replace("(MOXI, Cool Peel)", "(MOXI, Hybrid 1570)").replace("MOXI and Cool Peel", "MOXI and the Hybrid's non-ablative mode")
                               .replace("(CO2, Opus Plasma, PICO Fractional)", "(Alma Hybrid CO2, Opus Plasma, PICO Fractional)").replace("Fractional CO2", "Alma Hybrid CO2"))
    p["intropara"] = p["intropara"].replace("Cool Peel", "Hybrid")
    return p

def photofacial(p):
    p["intropara"] = p["intropara"] + (" In Barboursville we treat with Sciton BBL, Lumecca and Alma Harmony IPL, choosing the platform that best fits your skin tone and concern.")
    return p

def laser_hair_removal(p):
    p["intropara"] = p["intropara"] + (" Our Barboursville location uses the Alma Soprano &mdash; a virtually painless diode laser safe for all skin types &mdash; with Diolaze XL and Alma Harmony available for specific areas. Sessions start at $49, and every 6-session package includes the sixth session free.")
    return p

def laser_nail_fungus(p):
    p["intropara"] = p["intropara"] + " Treatments in Barboursville are performed on the Alma Harmony platform."
    return p

def laser_tattoo(p):
    p["intropara"] = p["intropara"].replace("PICO laser", "Discovery Pico Plus laser").replace("PICO", "Discovery Pico Plus", 1) if "PICO" in p["intropara"] else p["intropara"] + " Barboursville tattoo removal is performed on the Discovery Pico Plus."
    return p

def microneedling(p):
    p["intropara"] = p["intropara"] + " For deeper remodeling we also offer SecretRF radio-frequency microneedling and Morpheus8 at our Barboursville location."
    return p

def medical_facials(p):
    p["title"] = "Medical Facials &amp; Microdermabrasion in Barboursville, WV | Serene"
    p["h1"] = "Medical Facials &amp; Microdermabrasion in Barboursville, WV"
    p["crumb"] = "Medical Facials"
    p["intropara"] = p["intropara"] + " Barboursville also offers true microdermabrasion (including the Wet Diamond tip) alongside our classic, acne, pumpkin-enzyme and dermaplane facials."
    return p

def hydrafacial(p):
    p["intropara"] = p["intropara"].replace("DiamondGlow", "microdermabrasion")
    p["faqs"] = [(q, a.replace("DiamondGlow", "microdermabrasion")) for q,a in p["faqs"]]
    return p

def body_generic(p):
    # strip EMSCULPT / Lipomelt / DiamondGlow mentions that don't apply at Barboursville
    def fix(t):
        return (t.replace("EMSCULPT NEO, ", "").replace("EMSCULPT NEO and ", "").replace(", EMSCULPT NEO", "").replace("EMSCULPT NEO", "EvolveX")
                 .replace("Lipomelt, ", "").replace(", Lipomelt", "").replace("Lipomelt", "EvolveX")
                 .replace("DiamondGlow, ", "").replace(", DiamondGlow", "").replace("DiamondGlow", "HydraFacial"))
    for k in ("desc","ogdesc","hero","introlead","intropara","whypara","ctapara"):
        if k in p: p[k] = fix(p[k])
    p["cards"] = [(fix(h), fix(d)) for h,d in p["cards"]]
    p["faqs"] = [(fix(q), fix(a)) for q,a in p["faqs"]]
    return p

def harmony_bio_boost(p):
    # Barboursville maps skin with VISIA (no Alma IQ there)
    def fix(t): return t.replace("Alma IQ skin analysis","VISIA skin analysis").replace("Alma IQ","VISIA")
    for k in ("desc","ogdesc","hero","introlead","intropara","whypara","ctapara","pricing_html","how"):
        if k in p: p[k]=fix(p[k])
    p["cards"]=[(fix(h),fix(d)) for h,d in p["cards"]]
    p["steps"]=[(fix(h),fix(d)) for h,d in p["steps"]]
    p["faqs"]=[(fix(q),fix(a)) for q,a in p["faqs"]]
    return p

BV_OVERRIDES = {
 "harmony-bio-boost": lambda p: _related(harmony_bio_boost(body_generic(p)), ["alma-hybrid","morpheus8","photofacial"]),
 "laser-skin": lambda p: _related(laser_skin(body_generic(p)), ["alma-hybrid","harmony-bio-boost","morpheus8"]),
 "photofacial": lambda p: _related(photofacial(body_generic(p)), ["harmony-bio-boost","laser-skin","hyperpigmentation"]),
 "laser-hair-removal": lambda p: _related(laser_hair_removal(body_generic(p)), ["photofacial","botox","fillers"]),
 "laser-nail-fungus": lambda p: _related(laser_nail_fungus(body_generic(p)), ["laser-hair-removal","botox","fillers"]),
 "laser-tattoo-removal": lambda p: _related(laser_tattoo(body_generic(p)), ["laser-skin","botox","fillers"]),
 "microneedling": lambda p: _related(microneedling(body_generic(p)), ["morpheus8","fillers","botox"]),
 "medical-facials": lambda p: _related(medical_facials(body_generic(p)), ["hydrafacial","chemical-peels","botox"]),
 "hydrafacial": lambda p: _related(hydrafacial(body_generic(p)), ["medical-facials","botox","fillers"]),
}
# every other page still gets the generic clean-up + related-list filter
def _default(p): return _related(body_generic(p), ["botox","fillers","morpheus8"])
class _Overrides(dict):
    def __contains__(self, k): return True
    def __getitem__(self, k): return dict.get(self, k, _default)
BV_OVERRIDES = _Overrides(BV_OVERRIDES)
