# -*- coding: utf-8 -*-
# SKNLAB (Cartessa) six-handpiece facial platform — Barboursville only (Sept 2026, from the Cartessa SKNLAB kit).
# This file lives only in the Barboursville repo; Hudson does not have the device. Priced the same as HydraFacial.
def _steps(a,b,c,d): return [("Consultation",a),("Treatment",b),("Results",c),("Maintenance",d)]

_SKN_HTML = '''<section class="tint-mint" id="sknlab-handpieces">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Six Handpieces, One Facial</div><h2>Where Energy Meets Hydration</h2><p>A HydraFacial-style aqua-dermabrasion is only one of SKNLAB&rsquo;s six steps. The other five add energy &mdash; ultrasound, hot &amp; cold, electroporation, microcurrent, and lymphatic massage &mdash; so your provider builds the facial around your skin instead of following one fixed recipe.</p></div>
    <div class="grid">
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Sonic</h3><p>Ultrasonic vibration preps the skin, loosens debris, and boosts circulation so every later step absorbs better.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Aquis</h3><p>Aqua-delivery cleanses, exfoliates, and extracts with gentle suction while infusing three professional solutions &mdash; the hydrating heart of the treatment.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Kelsius</h3><p>Hot and cold settings calm inflammation, promote circulation, and stimulate collagen. Cold is a favorite for redness-prone and post-laser skin.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>N-Fuse</h3><p>Electroporation opens temporary micro-channels so exosomes, growth-factor serums, and other topicals get deeper than they ever could by hand.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Level</h3><p>Microcurrent re-educates and tones facial muscles for a lifted, awake look &mdash; no needles, no downtime.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Balance</h3><p>Enhanced lymphatic massage to de-puff, drain, and finish the facial with an even, rested glow.</p></div>
    </div>
    <div class="results-note reveal" style="text-align:center;margin-top:26px"><img loading="lazy" src="/img/sknlab-handpieces.webp" alt="The six SKNLAB handpieces: Sonic, Aquis, Kelsius, N-Fuse, Level and Balance" width="1200" height="776" style="max-width:640px;width:100%;height:auto;border-radius:16px"></div>
  </div>
</section>
<section class="results" id="sknlab-results">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Before &amp; After</div><h2>SKNLAB Results After One Session</h2><p>Each of these is a single SKNLAB facial. Photos courtesy of Cartessa Aesthetics and the treating practices; individual results vary.</p></div>
    <div class="res-grid" style="grid-template-columns:repeat(3,1fr)">
      <figure class="res reveal"><img loading="lazy" src="/img/sknlab-ba-01.webp" alt="SKNLAB before and after: congested, blemish-prone skin after 1 session" width="1000" height="1000"><figcaption><b>Congestion &amp; Breakouts</b><span>After 1 session</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/sknlab-ba-02.webp" alt="SKNLAB before and after: dull, uneven skin tone after 1 session" width="1000" height="1000"><figcaption><b>Dull, Uneven Tone</b><span>After 1 session</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/sknlab-ba-03.webp" alt="SKNLAB before and after: forehead texture and pores after 1 session" width="1000" height="1000"><figcaption><b>Texture &amp; Pores</b><span>After 1 session</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/sknlab-ba-04.webp" alt="SKNLAB before and after: cheek redness and texture after 1 session" width="1000" height="1000"><figcaption><b>Redness &amp; Texture</b><span>After 1 session</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/sknlab-ba-21.webp" alt="SKNLAB before and after: hydration and glow after 1 session" width="800" height="1000"><figcaption><b>Hydration &amp; Glow</b><span>After 1 session</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/sknlab-man.webp" alt="SKNLAB facial treatment for men at Serene Med Spa Barboursville" width="900" height="600"><figcaption><b>For Him, Too</b><span>Same facial, customized</span></figcaption></figure>
    </div>
  </div>
</section>
<section class="tint-blush" id="sknlab-pricing">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Pricing</div><h2>SKNLAB Facial &mdash; $150</h2><p>Same price as our HydraFacial, and it can be added to the front or back of a laser or microneedling visit. Ask about monthly facial packages at your consultation.</p><p style="margin-top:14px"><a class="btn btn-outline" href="/pricing/#cat-hair-face-body">See the full price list</a></p></div>
  </div>
</section>'''

PAGES6 += [
{
 "slug":"sknlab","crumb":"SKNLAB Facial","area_kw":"SKNLAB facial",
 "title":"SKNLAB Facial in Barboursville, WV | Serene Med Spa",
 "desc":"SKNLAB facial in Barboursville, WV: aqua-dermabrasion plus five energy handpieces, customized to your skin. 30-40 minutes, no downtime, $150. Book today.",
 "ogtitle":"SKNLAB Facial in Barboursville, WV","ogdesc":"Six handpieces, one customized facial: aqua-dermabrasion plus five energy steps for acne, congestion, dullness and early aging. No downtime. $150.",
 "proc_name":"SKNLAB Facial","proc_alt":"SKNLAB Six-Handpiece Aqua-Dermabrasion and Energy Facial (Cartessa Aesthetics)",
 "how":"SKNLAB combines aqua-dermabrasion (cleansing, exfoliation, extraction and solution infusion) with five energy handpieces &mdash; ultrasonic, hot/cold, electroporation, microcurrent and lymphatic massage &mdash; that the provider sequences into a 30&ndash;40 minute facial customized to the patient's skin concerns.","body":"Face, Neck, D&eacute;colletage",
 "eyebrow":"SKNLAB &middot; Barboursville, WV","h1":"SKNLAB Facial in Barboursville, West Virginia",
 "hero":"Where energy meets hydration. SKNLAB takes everything you love about a HydraFacial &mdash; cleanse, exfoliate, extract, infuse &mdash; and adds five energy handpieces so every facial is built for your skin. 30&ndash;40 minutes, zero downtime.",
 "trust":["Six Handpieces","Instant Glow","No Downtime","All Skin Types"],
 "introh2":"A facial that adapts to your skin",
 "introlead":"SKNLAB, by Cartessa Aesthetics, is a six-handpiece facial platform. Its Aquis aqua-delivery handpiece does what a HydraFacial does &mdash; deep-cleans, exfoliates, extracts and infuses hydrating solutions &mdash; and the other five bring proven energies into the same visit: ultrasonic prep, hot and cold therapy, electroporation for serum delivery, microcurrent toning, and lymphatic massage.",
 "intropara":"At Serene Med Spa in Barboursville, our providers start with a quick skin assessment (we also have VISIA imaging on site) and then sequence the handpieces around what your skin needs that day: more extraction and cold therapy for congested, breakout-prone skin; more electroporation and microcurrent for dull or early-aging skin; more hydration and lymphatic drainage before an event. A full SKNLAB facial takes 30&ndash;40 minutes and feels like a hydrating facial with light suction and a few new sensations from the energy handpieces &mdash; nothing painful, and you leave with makeup-ready skin. It is also an excellent hydrating step between Alma Hybrid, Opus Plasma or laser sessions. Individual results vary.",
 "treyebrow":"What It Treats","treh2":"Top Concerns We Treat With SKNLAB",
 "cards":[
   ("Acne &amp; Breakouts","Deep extraction plus cold therapy to calm inflammation. We avoid areas of severe active acne."),
   ("Congested Skin","Blackheads, clogged pores and buildup cleared with aqua-dermabrasion and ultrasonic prep."),
   ("Dull or Dry Skin","Exfoliation and infused hydrating solutions for an immediate, lasting glow."),
   ("Early Signs of Aging","Microcurrent toning and electroporated serums for fine lines and a lifted look."),
   ("Pre-Event Glow","Hydration, drainage and radiance with no downtime &mdash; book it the day before."),
   ("Between Laser Sessions","A gentle hydrating step that supports skin between Hybrid, Opus Plasma or Bio-Boost treatments."),
 ],
 "steps":_steps(
   "A short skin assessment to pick your goals and the handpiece sequence, and to confirm SKNLAB is right for you (we pause for active rashes, cold sores, sunburn, or recent resurfacing).",
   "Sonic prep, Aquis cleanse-exfoliate-extract-infuse, then the energy handpieces your provider selected. 30&ndash;40 minutes, relaxing, no numbing needed.",
   "Immediately brighter, smoother, more hydrated skin, with pores that look smaller and a toned feel. Makeup can go on right away.",
   "Monthly SKNLAB facials keep results building. Many patients rotate SKNLAB with chemical peels or add it around their laser series."),
 "whyh2":"Why choose Serene for SKNLAB in Barboursville",
 "whypara":"Serene is a physician-led practice, so your facial sits inside a real skin plan. Our providers pair SKNLAB with medical-grade skincare, VISIA skin analysis, and our laser and injectable menu &mdash; and if what you need is a peel, a laser, or a prescription, we will tell you.",
 "faqh2":"SKNLAB FAQ",
 "faqs":[
   ("What is SKNLAB?","SKNLAB is a six-handpiece facial device from Cartessa Aesthetics that combines aqua-dermabrasion with five energy-based handpieces (ultrasonic, hot/cold, electroporation, microcurrent and lymphatic massage), so each facial can be customized to your skin."),
   ("How is SKNLAB different from a HydraFacial?","The Aquis handpiece performs the same cleanse-exfoliate-extract-hydrate steps as a HydraFacial. SKNLAB then adds the energy handpieces, so your provider can also calm inflammation, push serums deeper, tone muscles, and drain puffiness in the same visit. Both are $150 at Serene Barboursville."),
   ("How long does a SKNLAB treatment take?","A comprehensive SKNLAB facial takes about 30 to 40 minutes."),
   ("What does it feel like?","Aqua-delivery feels hydrating with some gentle suction that should never pull the skin. The energy handpieces add warmth, cooling, light vibration or a mild tingle &mdash; your provider explains each step before it starts."),
   ("When will I see results?","Right away. The cleansing and infusion leave skin hydrated and more radiant immediately; smaller-looking pores and a toned feel are common. Other benefits build over a series."),
   ("How often should I have it?","A custom facial once a month is the usual recommendation. Your provider will tailor frequency to your skin and any laser or peel series you are doing."),
   ("Who should not have SKNLAB?","We postpone treatment for pregnancy or nursing, active skin conditions in the area (rash, eczema, sunburn, cold sores, active rosacea or severe acne), current or past skin cancer in the area, and recent resurfacing. Under 18 needs parental consent."),
 ],
 "related":["hydrafacial","medical-facials","harmony-bio-boost"],
 "pricing_html":_SKN_HTML,
 "ctah2":"Ready for your SKNLAB facial?",
 "ctapara":"Book a SKNLAB facial or a skin consultation at Serene Med Spa Barboursville.",
},
]
