# -*- coding: utf-8 -*-
# Generates the Ultherapy service page for the Barboursville site. Pure stdlib.
import json, os
ns={}
exec(open("common.py",encoding="utf-8").read(), ns)
LOGO=ns["LOGO"]; BOOK=ns["BOOK"]; NAV=ns["NAV"]; FOOTER=ns["FOOTER"]; SCRIPTS=ns["SCRIPTS"]
CONSULT=ns["CONSULT_SECTION"]; STICKY=ns.get("STICKY_BAR",""); areas_section=ns["areas_section"]
AREA_SERVED=ns.get("AREA_SERVED", [])
SITE="https://barboursville.serenemedspas.com"; URL=SITE+"/ultherapy/"

CARDS=[("Brow","A subtle lift that opens and refreshes the eyes."),
 ("Under the Chin","Tighten and define a softening jawline and submental area."),
 ("Neck","Firm loose, crepey skin for a smoother, more lifted neck."),
 ("Décolleté","Soften lines and wrinkles on the chest.")]
STEPS=[("Consultation","We assess your skin laxity and goals to confirm Ultherapy is right for you and map your treatment areas."),
 ("Ultrasound Imaging","Real-time imaging lets your provider see beneath the skin and target the ideal depth precisely."),
 ("Treatment","Focused ultrasound is delivered to stimulate collagen. Most sessions take 30&ndash;90 minutes depending on the area."),
 ("Results","Skin lifts and tightens gradually over two to three months as new collagen forms &mdash; and can last a year or more.")]
PRICES=[("Full Face + Neck","$2,900","Our signature full lift"),("Full Face","$2,200",""),
 ("Lower Face + Neck","$2,400",""),("Lower Face &middot; Jowls","$1,650",""),
 ("Neck / Under-Chin","$1,400",""),("Brow Lift","$850",""),("Décolleté","$500","add-on")]
FAQS=[("Is Ultherapy surgery?","No. Ultherapy is completely non-invasive &mdash; no incisions and no downtime. It uses focused ultrasound to lift and tighten from within by stimulating your own collagen."),
 ("Who is a good candidate?","Ultherapy works best for people with mild to moderate skin laxity who want a natural lift without surgery. At your consultation in Barboursville we&rsquo;ll assess your skin and tell you honestly whether it&rsquo;s right for you; more advanced laxity may need more than one session or a different approach."),
 ("Does it hurt?","You may feel brief warmth or tingling as the energy is delivered &mdash; a sign that collagen-building has begun. Comfort is improved on the Ultherapy PRIME platform, and we take steps to keep you comfortable throughout."),
 ("When will I see results?","Some lifting can appear early, but the full effect develops gradually over two to three months as your body builds new collagen. Results can last a year or more."),
 ("How many treatments will I need?","Most people achieve their result in a single session. Depending on your skin we may suggest a touch-up, and an annual maintenance treatment helps preserve your lift."),
 ("Is there any downtime?","No. Most people return to their day right away. You may have mild redness or slight swelling that settles quickly.")]

proc={"@context":"https://schema.org","@type":"MedicalProcedure","name":"Ultherapy",
 "alternateName":"Micro-Focused Ultrasound Skin Lifting","procedureType":"https://schema.org/NoninvasiveProcedure",
 "howPerformed":"Ultherapy uses micro-focused ultrasound energy to stimulate collagen deep in the skin, lifting and tightening the brow, chin, and neck and improving lines on the décolleté, guided by real-time ultrasound imaging.",
 "bodyLocation":"Brow, Chin, Neck, Décolleté","url":URL,
 "provider":{"@type":"MedicalBusiness","name":"Serene Med Spa — Barboursville","telephone":"+1-304-520-0461",
  "address":{"@type":"PostalAddress","streetAddress":"1 Chateau Grove Ln","addressLocality":"Barboursville","addressRegion":"WV","postalCode":"25504","addressCountry":"US"},
  "areaServed":AREA_SERVED}}
crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"Ultherapy","item":URL}]}
faqjson={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQS]}

def cards_html(cs): return "\n".join('      <div class="card reveal"><div class="ico">&#10022;</div><h3>%s</h3><p>%s</p></div>'%(h,p) for h,p in cs)
def steps_html(ss): return "\n".join('      <div class="step reveal"><div class="num"></div><div><h3>%s</h3><p>%s</p></div></div>'%(h,p) for h,p in ss)
def faq_html(fs): return "\n".join('      <div class="faq reveal"><button>%s<span class="plus">+</span></button><div class="ans"><p>%s</p></div></div>'%(q,a) for q,a in fs)
def price_html(ps): return "\n".join('      <div class="card reveal"><div class="ico">&#10022;</div><h3>%s</h3><p><strong>%s</strong>%s</p></div>'%(n,pr,("<br>"+note if note else "")) for n,pr,note in ps)

HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ultherapy in Barboursville, WV | Serene Med Spa</title>
<meta name="description" content="Ultherapy PRIME in Barboursville, WV — non-invasive ultrasound that lifts the brow, chin & neck and smooths the décolleté. No downtime. Book today.">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-WV"><meta name="geo.placename" content="Barboursville, West Virginia"><meta name="geo.position" content="38.4109;-82.2926"><meta name="ICBM" content="38.4109, -82.2926">
<meta property="og:type" content="website"><meta property="og:title" content="Ultherapy in Barboursville, WV"><meta property="og:description" content="Non-invasive ultrasound lifting of the brow, chin & neck in Barboursville, WV. No surgery, no downtime. Book today."><meta property="og:url" content="{URL}"><meta property="og:image" content="{LOGO}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">
{json.dumps(proc, ensure_ascii=False)}
</script>
<script type="application/ld+json">
{json.dumps(crumb, ensure_ascii=False)}
</script>
<script type="application/ld+json">
{json.dumps(faqjson, ensure_ascii=False)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>Now at Serene Barboursville:</strong> Ultherapy PRIME &mdash; the lift you can see. <a href="{BOOK}">Book a consultation</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Ultherapy</div>
    <div class="svc-hero-grid">
      <div class="svc-hero-txt">
        <div class="eyebrow">Ultherapy PRIME &middot; Barboursville, WV</div>
        <h1>Ultherapy in Barboursville, West Virginia</h1>
        <p>The FDA-cleared treatment that lifts and tightens the brow, chin, and neck using ultrasound &mdash; no surgery, no downtime, and results that build naturally over time.</p>
        <a class="btn" href="{BOOK}">Book Your Consultation</a>
        <a class="btn btn-outline" href="tel:+13045200461">Call (304) 520-0461</a>
      </div>
      <div class="svc-hero-media"><img src="/img/morpheus8.jpg" alt="Ultherapy skin lifting at Serene Med Spa in Barboursville, West Virginia" width="800" height="800"></div>
    </div>
  </div>
</section>

<div class="trust"><div class="wrap">
  <div class="item"><b>&#10022;</b> FDA-Cleared Lifting</div>
  <div class="item"><b>&#10022;</b> No Surgery, No Downtime</div>
  <div class="item"><b>&#10022;</b> Builds Your Own Collagen</div>
  <div class="item"><b>&#10022;</b> Physician-Led</div>
</div></div>

<section><div class="wrap prose reveal">
  <h2>Lift and tighten &mdash; without surgery</h2>
  <p class="lead">Ultherapy is the gold standard in non-invasive lifting. Using micro-focused ultrasound, it stimulates your body&rsquo;s own collagen deep beneath the surface to lift the brow, chin, and neck and smooth the décolleté.</p>
  <p>Now available at our Barboursville office serving Huntington and the Tri-State, Ultherapy uses ultrasound imaging so your provider can actually see the layers of tissue being treated &mdash; delivering energy precisely where it does the most good. Most people need just one session, with no downtime, and results that develop gradually over two to three months and can last a year or more.</p>
</div></section>

<section class="tint-blush"><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">Where It Works</div><h2>What Ultherapy Lifts</h2></div>
  <div class="grid">
{cards_html(CARDS)}
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">The Experience</div><h2>What to Expect</h2></div>
  <div class="steps">
{steps_html(STEPS)}
  </div>
</div></section>

<section class="tint-mint"><div class="wrap prose reveal" style="text-align:center">
  <div class="eyebrow" style="justify-content:center">Physician-Led</div>
  <h2>Why choose Serene for Ultherapy in the Tri-State</h2>
  <p>Ultherapy at Serene is physician-led, performed by our medical team on the advanced Ultherapy PRIME platform &mdash; the newest evolution of the gold standard in non-invasive lifting. We take the time to confirm you&rsquo;re a good candidate, set honest expectations, and deliver a natural-looking lift tailored to your face.</p>
  <a class="btn" href="{BOOK}">Book a Consultation</a>
</div></section>

<section id="pricing" class="tint-blush"><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">Investment</div><h2>Ultherapy Pricing &mdash; Barboursville</h2><p>One session, priced by the area you want to lift. Financing is available, and your consultation is always complimentary.</p></div>
  <div class="grid">
{price_html(PRICES)}
  </div>
  <div class="prose reveal" style="text-align:center;max-width:680px;margin:32px auto 0">
    <p>&#10024; <strong>Founding Patient offer:</strong> Full Face + Neck for <strong>$2,299</strong> for our first 20 Ultherapy patients &mdash; limited time. Ask about monthly financing to spread the cost.</p>
  </div>
</div></section>

<section id="faq"><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">Good to Know</div><h2>Ultherapy FAQ</h2></div>
  <div class="faq-list">
{faq_html(FAQS)}
  </div>
</div></section>

{areas_section("non-surgical skin lifting")}

<section class="location" id="location"><div class="wrap loc-grid">
  <div class="loc-info reveal">
    <div class="eyebrow" style="-webkit-text-fill-color:initial;color:var(--gold);background:none">Visit Us</div>
    <h2 style="font-size:clamp(2.1rem,4.4vw,3rem);margin-bottom:20px">Serene Med Spa &mdash; Barboursville</h2>
    <div class="row"><strong>Address</strong><span>1 Chateau Grove Ln<br>Barboursville, WV 25504</span></div>
    <div class="row"><strong>Call</strong><span><a href="tel:+13045200461">(304) 520-0461</a></span></div>
    <div class="row"><strong>Hours</strong><span>Mon&ndash;Fri: 9 AM &ndash; 5 PM<br>Sat&ndash;Sun: By appointment</span></div>
    <div style="margin-top:28px"><a class="btn" href="{BOOK}">Book Now</a></div>
  </div>
  <iframe class="map reveal" loading="lazy" title="Map to Serene Med Spa Barboursville" src="https://www.google.com/maps?q=1+Chateau+Grove+Ln+Barboursville+WV+25504&output=embed"></iframe>
</div></section>

<section class="cta"><div class="wrap reveal">
  <h2>Ready to lift and tighten &mdash; without surgery?</h2>
  <p>Book an Ultherapy consultation with our Barboursville team and see if the gold standard in non-invasive lifting is right for you.</p>
  <a class="btn" href="{BOOK}">Book Your Visit</a>
</div></section>

{CONSULT}

{FOOTER}

{STICKY}

{SCRIPTS}
</body>
</html>
'''
os.makedirs("bundle/site/ultherapy", exist_ok=True)
open("bundle/site/ultherapy/index.html","w",encoding="utf-8").write(HTML)
print("build_ultherapy: wrote ultherapy/index.html (%d bytes)"%len(HTML))
