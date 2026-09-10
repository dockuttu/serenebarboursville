# -*- coding: utf-8 -*-
# Alma Hybrid (CO2 + 1570 nm) — Barboursville only (Sept 2026, from Alma's Hybrid launch kit).
# This file lives only in the Barboursville repo; Hudson does not have the device.
def _steps(a,b,c,d): return [("Consultation",a),("Treatment",b),("Results",c),("Maintenance",d)]

_HY_RESULTS = '''<section class="results" id="hybrid-results">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Before &amp; After</div><h2>Alma Hybrid Results</h2><p>Real Alma Hybrid patients after one or two treatments &mdash; sun damage, acne scarring, fine lines, texture, and a surgical scar.</p></div>
    <div class="res-grid" style="grid-template-columns:repeat(3,1fr)">
      <figure class="res reveal"><img loading="lazy" src="/img/hybrid-sun-damage-2tx.webp" alt="Alma Hybrid before and after: sun damage and pigment, after 2 treatments" width="991" height="704"><figcaption><b>Sun Damage</b><span>After 2 treatments</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/hybrid-wrinkles-1tx.webp" alt="Alma Hybrid before and after: wrinkles and crepey skin, after 1 treatment" width="781" height="548"><figcaption><b>Wrinkles &amp; Crepey Skin</b><span>After 1 treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/hybrid-acne-scars-1tx.webp" alt="Alma Hybrid before and after: acne scars and active acne, after 1 treatment" width="991" height="668"><figcaption><b>Acne &amp; Acne Scars</b><span>After 1 treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/hybrid-texture-2tx.webp" alt="Alma Hybrid before and after: texture and pores, after 2 treatments" width="991" height="662"><figcaption><b>Texture &amp; Pores</b><span>After 2 treatments</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/hybrid-forehead-2tx.webp" alt="Alma Hybrid before and after: forehead redness and scarring, after 2 treatments" width="991" height="403"><figcaption><b>Redness &amp; Scarring</b><span>After 2 treatments</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/hybrid-scar-2tx.webp" alt="Alma Hybrid before and after: surgical scar on the abdomen, after 2 treatments" width="991" height="253"><figcaption><b>Surgical Scar</b><span>After 2 treatments</span></figcaption></figure>
    </div>
    <p class="rev-note">Individual results may vary. Photos courtesy of Alma, Inc. and the treating physicians (Drs. Desai, Vaidya, Rivera, Panchal, Hsu, Steele, Fedok) &mdash; not Serene patients.</p>
  </div>
</section>
<section class="tint-mint" id="hybrid-levels">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Pick Your Downtime</div><h2>Three Ways to Do Alma Hybrid</h2><p>Because the CO2 and 1570&nbsp;nm energies are adjustable, the same device delivers anything from a lunchtime glow to a true resurfacing. Your physician dials it to your goals and your calendar.</p></div>
    <div class="grid">
      <div class="card reveal"><div class="ico">&#10022;</div><h3>SoftLift</h3><p>The lunchtime option. Mostly 1570&nbsp;nm with a light CO2 touch for glow, pores, and early lines. Expect a day or two of pinkness and swelling &mdash; makeup the next morning.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Hybrid Lift</h3><p>Balanced CO2 and 1570&nbsp;nm for sun damage, texture, acne scars, and moderate wrinkles. Plan on a long weekend: redness and light peeling for 3&ndash;5 days.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Deep Resurfacing</h3><p>CO2-forward for deep lines, etched scars, and heavily sun-damaged skin. About a week of crusting and redness, then the most dramatic change a single laser session can give.</p></div>
    </div>
  </div>
</section>'''

PAGES6 = [
{
 "slug":"alma-hybrid","crumb":"Alma Hybrid","area_kw":"Alma Hybrid laser resurfacing",
 "title":"Alma Hybrid Laser Resurfacing in Barboursville, WV | Serene",
 "desc":"Alma Hybrid in Barboursville, WV: CO2 + 1570 nm lasers in one session for wrinkles, sun damage, acne scars and texture, with half the downtime. Book today.",
 "ogtitle":"Alma Hybrid Laser Resurfacing in Barboursville, WV","ogdesc":"Dual-laser resurfacing (CO2 + 1570 nm) for wrinkles, sun damage, acne scars and texture — with about half the downtime of traditional CO2.",
 "proc_name":"Alma Hybrid Laser Resurfacing","proc_alt":"Hybrid Fractional CO2 and 1570 nm Non-Ablative Laser Resurfacing",
 "how":"Alma Hybrid delivers ablative fractional CO2 and non-ablative 1570 nm laser energy from a single handpiece, resurfacing the skin's surface while remodeling collagen in the deeper dermis, so results build faster with less downtime than traditional CO2.","body":"Face, Neck, Chest, Hands, Body Scars",
 "eyebrow":"Alma Hybrid &middot; Barboursville, WV","h1":"Alma Hybrid Laser Resurfacing in Barboursville, West Virginia",
 "hero":"Two gold-standard lasers, one session. Alma Hybrid pairs fractional CO2 with a 1570&nbsp;nm laser to erase sun damage, wrinkles, and scars &mdash; with about half the downtime of a traditional CO2 peel.",
 "trust":["CO2 + 1570 nm in One Pass","Half the Downtime","Scars, Wrinkles &amp; Sun Damage","Physician-Performed"],
 "introh2":"Resurfacing, reinvented",
 "introlead":"Alma Hybrid is the first laser to fire ablative CO2 and non-ablative 1570&nbsp;nm energy from the same handpiece, in a randomized pattern. The CO2 resurfaces the top layers where lines, sun damage, and scars live; the 1570&nbsp;nm reaches the deeper dermis to trigger collagen remodeling without breaking the surface.",
 "intropara":"At Serene Med Spa in Barboursville, that combination lets your physician use gentler CO2 settings than a traditional resurfacing laser while still getting deep dermal repair &mdash; so treatments take about 15 minutes, healing runs roughly half as long, and results show after a single visit. Because both energies are adjustable, the same device does a lunchtime SoftLift, a long-weekend Hybrid Lift, or a full CO2 resurfacing. Settings are matched to your Fitzpatrick skin type, and individual results vary.",
 "treyebrow":"What It Treats","treh2":"Concerns Alma Hybrid Targets",
 "cards":[
   ("Fine Lines &amp; Wrinkles","Soften etched lines around the eyes, mouth, and cheeks and firm crepey skin."),
   ("Sun Damage &amp; Pigment","Lift years of sun spots and mottled tone for a clearer, more even complexion."),
   ("Acne &amp; Acne Scars","Smooth pitted scars, and calm active acne &mdash; 1570&nbsp;nm shrinks overactive oil glands."),
   ("Surgical &amp; Trauma Scars","Flatten, soften, and blend scars on the face and body, including C-section scars."),
   ("Texture &amp; Pores","Refine rough texture and enlarged pores for smoother, tighter-looking skin."),
   ("Skin Laxity","Thicken thin, lax skin as new collagen rebuilds over the following months."),
 ],
 "steps":_steps(
   "We review your concerns, skin type, and how much downtime you can take, then choose SoftLift, Hybrid Lift, or deep resurfacing.",
   "Topical numbing goes on for about 45 minutes; the laser itself takes roughly 15 minutes for a full face, with cooling for comfort.",
   "Expect redness, swelling, and light peeling for a few days (longer for deep resurfacing). Fresh, smoother skin appears within 2&ndash;5 days and keeps improving for several months as collagen rebuilds.",
   "One session makes a visible difference; a series of three spaced about a month apart delivers the best results, then a yearly maintenance treatment."),
 "whyh2":"Why choose Serene for Alma Hybrid in Barboursville",
 "whypara":"Resurfacing lasers reward experience. At Serene, Alma Hybrid treatments are performed by physicians, planned from your VISIA skin analysis and Fitzpatrick skin type, and dialed to your downtime &mdash; not a preset.",
 "faqh2":"Alma Hybrid FAQ",
 "faqs":[
   ("What is Alma Hybrid?","It&rsquo;s a resurfacing laser that combines fractional CO2 (ablative) and 1570&nbsp;nm (non-ablative) energy in one handpiece. The two together treat scarring, acne, sun damage, wrinkles, texture, and laxity with better results and less downtime than either laser alone."),
   ("How is it different from a traditional CO2 laser?","Traditional CO2 relies on aggressive ablation, so full-face treatments take 1.5&ndash;2 hours and redness can linger for weeks or months. Hybrid adds the 1570&nbsp;nm wavelength for deep dermal repair, so we can use gentler CO2 settings, finish in about 15 minutes, and cut healing time roughly in half."),
   ("Does it hurt?","All resurfacing involves some heat. We apply a strong topical numbing cream first and use cooling during treatment; most patients describe warmth and tingling. Deeper resurfacing may include additional comfort measures."),
   ("What is the downtime?","It depends on the level you choose. SoftLift: a day or two of pinkness and swelling. Hybrid Lift: redness and light peeling for 3&ndash;5 days. Deep resurfacing: about 5 days of crusting, then a week or so of fading redness."),
   ("How many treatments will I need?","You&rsquo;ll see improvement after one session. Best results typically come from a series of three, about a month apart, followed by a yearly maintenance treatment."),
   ("Is it safe for darker skin tones?","Hybrid is used on Fitzpatrick types I&ndash;V with adjusted settings, and the 1570&nbsp;nm component is especially useful for deeper skin tones. Take the skin-type quiz on this page and we&rsquo;ll confirm the safest plan at your consultation."),
   ("Can it treat scars on the body?","Yes &mdash; surgical scars, C-section scars, stretch marks, and trauma scars respond well, usually over two or three sessions."),
   ("Who is a good candidate?","Adults from their 20s to their 90s with sun damage, scarring, acne, wrinkles, or texture concerns. It is not performed on active infections, recent isotretinoin use, or during pregnancy; we&rsquo;ll review your history at your consult."),
 ],
 "related":["harmony-bio-boost","morpheus8","botox"],
 "pricing_html":_HY_RESULTS,
 "ctah2":"Ready to resurface?",
 "ctapara":"Book an Alma Hybrid consultation at Serene Med Spa in Barboursville and we&rsquo;ll match the treatment to your skin and your calendar.",
},
]
