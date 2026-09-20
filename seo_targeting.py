# -*- coding: utf-8 -*-
# seo_targeting.py — final SEO pass: sets <title> + meta/OG/Twitter descriptions for the
# highest-value pages so they target the searches patients actually use.
# Runs near the end of build.sh (after seo_trim/seo_tech), so these values win. Idempotent.
import os, re, sys, html
SITE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"

def _set(doc, title, desc):
    n = 0
    if title:
        t = html.escape(title, quote=False)
        doc, k = re.subn(r"<title>.*?</title>", "<title>%s</title>" % t, doc, count=1, flags=re.S); n += k
        for prop in ('property="og:title"', 'name="twitter:title"'):
            doc = re.sub(r'(<meta\s+%s\s+content=")[^"]*(")' % re.escape(prop), lambda m: m.group(1) + html.escape(title) + m.group(2), doc)
    if desc:
        d = html.escape(desc)
        for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
            doc, k = re.subn(r'(<meta\s+%s\s+content=")[^"]*(")' % re.escape(prop), lambda m: m.group(1) + d + m.group(2), doc)
            n += k
    return doc, n

def run(PAGES):
    done = 0
    for path, (title, desc) in PAGES.items():
        f = os.path.join(SITE, path.strip("/"), "index.html") if path.strip("/") else os.path.join(SITE, "index.html")
        if not os.path.exists(f):
            print("seo_targeting: missing", path); continue
        doc = open(f, encoding="utf-8").read()
        new, n = _set(doc, title, desc)
        if new != doc:
            open(f, "w", encoding="utf-8").write(new); done += 1
    print("seo_targeting: updated %d pages" % done)

PAGES = {'/': ('Med Spa in Huntington & Barboursville, WV | Serene', 'Physician-led med spa in Barboursville, WV, 15 minutes from Huntington: Botox $10/unit, fillers, Morpheus8, Ultherapy, laser, weight loss and IV wellness.'),
 '/botox/': ('Botox in Huntington & Barboursville, WV | $10/Unit', 'Botox, Dysport and Xeomin from $10/unit in Barboursville, WV, 15 minutes from Huntington. Physician-led injections for natural, refreshed results.'),
 '/fillers/': ('Dermal Fillers in Huntington & Barboursville, WV', 'Physician-injected lip, cheek, jawline and under-eye filler in Barboursville, WV, near Huntington. Natural volume and definition. Book a consultation.'),
 '/lip-filler/': ('Lip Filler in Huntington & Barboursville, WV | Serene', 'Physician-injected lip filler near Huntington, WV: $500 full syringe or $300 half syringe for subtle volume, shape and hydration that looks natural.'),
 '/under-eye-filler/': ('Under-Eye Filler in Huntington & Barboursville, WV', 'Physician-injected tear trough filler in Barboursville, WV, near Huntington. Softens hollows and dark circles for a rested look. Candidacy checked first.'),
 '/morpheus8/': ('Morpheus8 in Huntington & Barboursville, WV | Serene', 'Morpheus8 RF microneedling near Huntington, WV to tighten, smooth and resurface skin on the face and body. Physician-led care in Barboursville.'),
 '/weight-loss/': ('Medical Weight Loss in Huntington & Barboursville, WV', 'Physician-supervised medical weight loss near Huntington, WV: personalized GLP-1 programs, labs and monthly check-ins in Barboursville.'),
 '/hormone-optimization/': ('Biote Hormone Therapy | Huntington & Barboursville, WV', 'Biote hormone optimization near Huntington, WV, guided by Labcorp panels for hormones, thyroid, vitamins and blood counts. Physician-led, in Barboursville.'),
 '/laser-hair-removal/': ('Laser Hair Removal in Huntington & Barboursville, WV', 'Virtually painless Soprano ICE laser hair removal near Huntington, WV. Safe for all skin tones, even tanned skin. Sessions from $49 in Barboursville.'),
 '/microneedling/': ('Microneedling & PRP in Huntington & Barboursville, WV', 'Microneedling and microneedling with PRP near Huntington, WV for texture, acne scars and fine lines. Physician-led care in Barboursville.'),
 '/photofacial/': ('BBL & IPL Photofacial | Huntington & Barboursville, WV', 'BBL and IPL photofacials near Huntington, WV to clear sun spots, redness and rosacea-prone skin for a brighter, more even complexion.'),
 '/laser-skin/': ('Laser Resurfacing in Huntington & Barboursville, WV', 'CO2, Opus Plasma, PICO fractional and Moxi laser resurfacing near Huntington, WV for texture, fine lines and sun damage. Physician-led.'),
 '/sculptra/': ('Sculptra in Huntington & Barboursville, WV | Serene', 'Sculptra collagen stimulator near Huntington, WV for gradual, natural volume and firmer-looking skin. Physician-injected in Barboursville.'),
 '/ultherapy/': ('Ultherapy in Huntington & Barboursville, WV | Serene', 'Ultherapy PRIME near Huntington, WV: non-invasive ultrasound that lifts the brow, chin and neck with no downtime. Physician-led in Barboursville.'),
 '/iv-therapy/': ('IV Therapy in Huntington & Barboursville, WV | Serene', 'IV hydration, vitamin and NAD+ drips near Huntington, WV. Physician-supervised IV wellness in Barboursville to replenish and recover.'),
 '/laser-tattoo-removal/': ('Laser Tattoo Removal | Huntington & Barboursville, WV', 'PICO laser tattoo removal near Huntington, WV from $125 per session. Buy 5 sessions, get the 6th free. Complimentary, no-commitment consultation.'),
 '/hydrafacial/': ('HydraFacial in Huntington & Barboursville, WV | Serene', 'HydraFacial near Huntington, WV: cleanse, exfoliate, extract and hydrate for an instant glow with no downtime. Book in Barboursville.'),
 '/chemical-peels/': ('Chemical Peels in Huntington & Barboursville, WV', 'VI Peel and The Perfect Derma Peel near Huntington, WV for brighter, clearer, smoother skin. Medical-grade peels chosen for your skin type.'),
 '/thread-lift/': ('PDO Thread Lift in Huntington & Barboursville, WV', 'PDO thread lift near Huntington, WV: a non-surgical way to lift and firm sagging skin with little downtime. Physician-performed in Barboursville.'),
 '/prp-hair-restoration/': ('PRP Hair Restoration | Huntington & Barboursville, WV', 'PRP hair restoration near Huntington, WV, using your own platelet-rich plasma to support thicker, healthier hair. Physician-led in Barboursville.'),
 '/under-eye-prp/': ('Under-Eye PRP & PRF | Huntington & Barboursville, WV', 'Under-eye PRP and PRF near Huntington, WV: your own platelets soften dark circles, crepey skin and hollows without filler.'),
 '/kybella/': ('Kybella in Huntington & Barboursville, WV | Serene', 'Kybella near Huntington, WV: the FDA-approved injectable that permanently reduces double-chin fat without surgery. Physician-led in Barboursville.'),
 '/jawline-filler/': ('Jawline Filler in Huntington & Barboursville, WV', 'Physician-injected jawline filler near Huntington, WV to sculpt a defined, contoured jawline and refresh your profile. Book in Barboursville.'),
 '/cheek-filler/': ('Cheek Filler in Huntington & Barboursville, WV', 'Physician-injected cheek filler near Huntington, WV to restore mid-face volume, lift and definition for a naturally refreshed look.'),
 '/aftercare/botox/': (None, 'Botox aftercare from Serene Med Spa Barboursville: what to do and avoid in the first 24 hours, when results appear and when to call us.'),
 '/aftercare/dermal-filler/': (None, 'Dermal filler aftercare from Serene Med Spa Barboursville: swelling and bruising tips, activities to avoid, and warning signs that need a call.'),
 '/aftercare/o-shot/': (None, 'O-Shot aftercare from Serene Med Spa Barboursville: comfort tips, activity guidance, what is normal after treatment and when to contact us.')}

if __name__ == "__main__":
    run(PAGES)
