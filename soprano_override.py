# -*- coding: utf-8 -*-
# soprano_override.py — Barboursville laser-hair-removal page rewrite around the Alma Soprano ICE Platinum.
# Imported by bv_localize.py.

_SOPRANO_HTML = '''<section class="tint-mint" id="soprano">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Our Technology</div><h2>Soprano ICE Platinum: Virtually Painless Laser Hair Removal</h2><p>Barboursville treats with the Alma Soprano ICE Platinum &mdash; three laser wavelengths in a single applicator, delivered with a sweeping in-motion technique and a contact-cooled tip. It&rsquo;s the reason our patients describe treatment as a warm massage rather than the snapping they remember from older lasers.</p></div>
    <div class="grid">
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Three Wavelengths, One Pass</h3><p>Alexandrite (755&nbsp;nm), diode (810&nbsp;nm), and Nd:YAG (1064&nbsp;nm) fire together, so fine, coarse, light-brown, and deep-follicle hair are all treated in the same session.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>In-Motion SHR Heating</h3><p>Instead of one hot pulse per spot, the applicator sweeps continuously and warms the follicle gradually &mdash; effective on the hair, gentle on the skin, and fast: upper and lower legs in about 10 minutes.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>ICE Contact Cooling</h3><p>A sapphire tip chills the surface while the laser works underneath, protecting the skin and keeping the sensation comfortable without numbing cream.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>All Skin Tones, Even Tanned</h3><p>Safe for Fitzpatrick types I&ndash;VI and cleared for tanned skin, so you can treat year-round instead of hiding from the sun for months.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>No Downtime</h3><p>Mild pinkness for an hour or two at most. Go straight back to work, the gym, or the pool.</p></div>
      <div class="card reveal"><div class="ico">&#10022;</div><h3>Any Area</h3><p>Small applicators reach ears, nostrils, and the bikini line; the large tip covers backs and legs quickly.</p></div>
    </div>
  </div>
</section>
<section class="results" id="soprano-results">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Before &amp; After</div><h2>Soprano Laser Hair Removal Results</h2><p>Photographed six weeks after the treatment noted. Hair grows in cycles, so a series of 5&ndash;8 sessions gives the smoothest, longest-lasting result.</p></div>
    <div class="res-grid" style="grid-template-columns:repeat(3,1fr)">
      <figure class="res reveal"><img loading="lazy" src="/img/soprano-chest-2.webp" alt="Soprano laser hair removal before and after: chest, 6 weeks after 5th treatment" width="1762" height="870"><figcaption><b>Chest</b><span>6 weeks after 5th treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/soprano-back.webp" alt="Soprano laser hair removal before and after: back, 6 weeks after 1st treatment" width="1411" height="870"><figcaption><b>Back</b><span>6 weeks after 1st treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/soprano-face.webp" alt="Soprano laser hair removal before and after: facial hair, 6 weeks after 3rd treatment" width="1464" height="870"><figcaption><b>Facial Hair</b><span>6 weeks after 3rd treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/soprano-arms.webp" alt="Soprano laser hair removal before and after: fine vellus arm hair, 6 weeks after 5th treatment" width="1702" height="870"><figcaption><b>Arms (fine vellus hair)</b><span>6 weeks after 5th treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/soprano-chest-3.webp" alt="Soprano laser hair removal before and after: dense chest hair, 6 weeks after 5th treatment" width="1743" height="870"><figcaption><b>Chest (dense hair)</b><span>6 weeks after 5th treatment</span></figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/soprano-chest.webp" alt="Soprano laser hair removal before and after: chest, 6 weeks after 4th treatment" width="2045" height="870"><figcaption><b>Chest</b><span>6 weeks after 4th treatment</span></figcaption></figure>
    </div>
    <p class="rev-note">Individual results may vary. Photos courtesy of Alma, Inc. &mdash; not Serene patients.</p>
    <p style="text-align:center;margin-top:22px"><a class="btn btn-outline" href="/pricing/#cat-hair-face-body">See Laser Hair Removal Pricing &amp; Packages</a></p>
  </div>
</section>'''

def laser_hair_removal(p):
    p["title"] = "Soprano Laser Hair Removal in Barboursville, WV | Serene"
    p["desc"] = "Virtually painless laser hair removal in Barboursville, WV on the Alma Soprano ICE Platinum. Safe for all skin tones, even tanned. Sessions from $49."
    p["ogtitle"] = "Soprano ICE Laser Hair Removal in Barboursville, WV"
    p["ogdesc"] = "Virtually painless, safe for all skin tones, no downtime. Alma Soprano ICE Platinum laser hair removal at Serene Med Spa Barboursville. Sessions from $49."
    p["proc_alt"] = "Soprano ICE Platinum Diode Laser Hair Removal"
    p["how"] = "The Alma Soprano ICE Platinum sweeps three laser wavelengths across the skin in motion, gradually heating hair follicles to stop regrowth while a cooled sapphire tip keeps the skin comfortable, over a series of sessions spaced 6 to 8 weeks apart."
    p["hero"] = "Drop the razor. The Alma Soprano ICE Platinum removes hair on any area &mdash; virtually painlessly, on every skin tone, even tanned &mdash; with zero downtime. Sessions start at $49."
    p["trust"] = ["Virtually Painless", "All Skin Tones, Even Tanned", "No Downtime", "Sessions From $49"]
    p["introh2"] = "This is not your mother&rsquo;s laser hair removal"
    p["introlead"] = "Older hair-removal lasers fired one hot pulse at a time and were off-limits for dark or tanned skin. The Soprano ICE Platinum warms the follicle gradually while chilling the surface, so treatment feels like a warm massage, works on every skin tone, and can be done any month of the year."
    p["intropara"] = ("At Serene Med Spa in Barboursville, our Alma Soprano ICE Platinum treats everything from the upper lip to full legs and backs &mdash; a full set of legs takes about 10 minutes. "
        "Because hair grows in cycles, most people need 5&ndash;8 sessions spaced 6&ndash;8 weeks apart for the smoothest, longest-lasting result. Sessions start at $49, and every 6-session package includes the sixth session free. "
        "Diolaze XL and Alma Harmony are also available for specific areas. Your plan is physician-guided and matched to your skin and hair; individual results vary.")
    p["steps"] = [
        ("Consultation", "We check your skin type and hair, confirm the Soprano is the right fit (it almost always is), and map out your series and package."),
        ("Treatment", "The cooled applicator glides over the area in a sweeping motion. Most people feel gentle warmth &mdash; no numbing cream needed. Small areas take minutes; legs about 10."),
        ("Between Sessions", "Shave as directed, skip waxing and plucking, and come back every 6&ndash;8 weeks so each hair cycle is caught in its growth phase."),
        ("Results", "Hair returns finer and sparser after each visit; by the end of your series most areas need only an occasional touch-up. Results vary."),
    ]
    p["whyh2"] = "Why choose Serene for laser hair removal in Barboursville"
    p["whypara"] = "The right wavelength and settings for your skin are what make laser hair removal both safe and effective. At Serene, treatments run on the Alma Soprano ICE Platinum under the supervision of our board-certified physicians, so you get comfortable, consistent results whether your skin is fair, deep, or freshly tanned."
    p["faqs"] = [
        ("Does Soprano laser hair removal hurt?", "Virtually not. The applicator sweeps continuously and its ICE tip cools the skin, so most patients describe a warm, massage-like feeling rather than the rubber-band snap of older lasers. No numbing cream is needed."),
        ("Is it safe for dark or tanned skin?", "Yes. Soprano ICE Platinum is cleared for all Fitzpatrick skin types (I&ndash;VI) and for tanned skin, which is why we can treat year-round. Settings are adjusted to your skin tone at every visit."),
        ("How many sessions will I need?", "Typically 5&ndash;8 sessions spaced 6&ndash;8 weeks apart, because hair grows in cycles and the laser only affects follicles in their growth phase. We&rsquo;ll give you a personal estimate at your consultation."),
        ("How long does a session take?", "Upper lip or underarms: a few minutes. Upper and lower legs: about 10 minutes. Back or full legs plus bikini: roughly 30 minutes."),
        ("What does it cost?", "Sessions start at $49, and every 6-session package includes the sixth session free. See the full area-by-area list on our pricing page."),
        ("Is there any downtime?", "No. You may notice mild pinkness for an hour or two. You can go back to work, the gym, or the pool right away."),
        ("What areas can be treated?", "Anywhere with unwanted hair: face, upper lip, chin, neck, underarms, arms, chest, back, abdomen, bikini and Brazilian, legs, feet, even ears and nostrils."),
        ("How should I prepare?", "Shave the area 12&ndash;24 hours before, skip waxing, plucking, or threading for 4 weeks beforehand, and avoid self-tanner on the area. Tanned skin is fine; we adjust settings."),
    ]
    p["pricing_html"] = _SOPRANO_HTML + p.get("pricing_html", "")
    return p
