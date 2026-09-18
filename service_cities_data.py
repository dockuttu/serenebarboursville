# -*- coding: utf-8 -*-
# service_cities_data.py — Barboursville: service + region landing pages.
#
# Built from Search Console (90 days to Sept 2026, sc-domain:serenemedspas.com), filtered to
# WV/Tri-State geography. Two clusters stood out:
#   * STATE-LEVEL "<service> west virginia" / "<service> wv" — 1,171 impressions, 5 clicks (0.4%).
#     Twenty distinct queries and nothing on the site targeting any of them. Biggest single gap.
#   * HUNTINGTON service queries — 1,243 impressions, 45 clicks (3.6%). Partly working;
#     tattoo removal is already the best performer and deserves its own page.
# Deliberately NOT built: massage (Serene does not offer it), EMSCULPT (not a device we have —
# Barboursville does body contouring on EvolveX/BodyTite), Paintsville KY (closed location),
# Lexington KY (out of area). Prices must match build_pricing.py — Barboursville prices differ
# from Hudson's (Botox $10 vs $11, Sculptra $600 vs $750, 3 Juvederm $1,300 vs $1,400).

_WV_VISIT = "What to expect on your first visit"
_WV_DIR   = "Getting to Serene from around West Virginia"

SC_PAGES = [

# ---------- MED SPA — WEST VIRGINIA (hub, ~550 impressions, near-zero clicks) ----------
{
 "slug":"med-spa-west-virginia", "service":"Med Spa", "service_url":"/pricing/",
 "city":"West Virginia", "city_state":"West Virginia", "also":["Huntington, WV","Charleston, WV","Teays Valley, WV","Hurricane, WV","Milton, WV"],
 "title":"Med Spa in West Virginia | Physician-Led | Serene Med Spa",
 "desc":"Physician-owned medical spa in West Virginia &mdash; Botox from $10 a unit, filler $500 a syringe, lasers and weight loss, in Barboursville off I-64 exit 20.",
 "eyebrow":"Medical Spa &middot; West Virginia",
 "h1":"A Physician-Led Med Spa in West Virginia",
 "hero":"Botox from $10 a unit. Filler at $500 a syringe. Every treatment performed or supervised by board-certified physicians, at 1 Chateau Grove Ln in Barboursville &mdash; right off I-64 exit 20.",
 "drive":"Off I-64 exit 20 in Barboursville",
 "dir_h2":_WV_DIR, "visit_h2":_WV_VISIT, "cta_h2":"The med spa West Virginia drives to",
 "introh2":"What makes a med spa a medical practice",
 "introlead":"West Virginia has plenty of places offering injectables. The distinction worth caring about is whether a physician is actually in the building &mdash; and whether the prices are published before you walk in.",
 "intro":"<p>Serene is owned and run by physicians. Dr. Shweta Arora is board-certified in anesthesiology with certification in aesthetic medicine; Dr. Robin Arora is board-certified in internal medicine, nephrology and hypertension. Stephanie Welker, FNP-BC rounds out the clinical team. Your consultation, your treatment and your follow-up happen with the same people.</p><p>Our full menu is published on the <a href=\"/pricing/\">pricing page</a>: Botox at <strong>$10 per unit</strong>, dermal filler at <strong>$500 a syringe</strong> (three Juv&eacute;derm syringes $1,300), Sculptra at <strong>$600 a vial</strong>, HydraFacial and SKNLAB facials at <strong>$150</strong>, laser hair removal from <strong>$49</strong> a session, and medical weight loss. We also run a <strong>Tri-State Price Match</strong> on injectables.</p><p>On the device side we are an Alma practice &mdash; Alma Hybrid CO&sup2; resurfacing, Soprano ICE Platinum hair removal, Harmony IPL, Alma TED and Alma Duo &mdash; plus Morpheus8, Ultherapy PRIME and Bi&ouml;te hormone pellets. We are an Allergan Platinum partner, so All&#275; points work here.</p><p>Patients come from Huntington, Charleston, Teays Valley, Hurricane and Milton, and from Ashland and Ironton across the river.</p>",
 "price_rows":[("Botox, Xeomin or Daxxify","$10 /unit"),("Dysport","$3.99 /unit"),("Dermal Filler","$500 /syringe"),("3 Juv&eacute;derm Syringes","$1,300"),("Sculptra","$600 /vial"),("HydraFacial or SKNLAB Facial","$150"),("Laser Hair Removal","From $49"),("Alma Hybrid CO&sup2; Resurfacing","$600&ndash;$1,000"),("Consultation","No charge")],
 "directions":"<p>We are at <strong>1 Chateau Grove Ln, Barboursville, WV 25504</strong> &mdash; just off <strong>I-64 exit 20</strong> (Barboursville / Huntington Mall) on the US-60 side, with free parking outside the door.</p><p><strong>From Huntington:</strong> I-64 East to exit 20, about 15 minutes. <strong>From Charleston:</strong> I-64 West to exit 20, about 45 minutes. <strong>From Teays Valley or Hurricane:</strong> I-64 West, 20 to 25 minutes. <strong>From Ashland, KY or Ironton, OH:</strong> US-60 or I-64, about 30 to 40 minutes.</p>",
 "origin_q":"Charleston,+WV",
 "faqs":[
  ("Where is the best med spa in West Virginia?","We would not claim a title, but here is what is verifiable about Serene: it is physician-owned, every price is published on the website, and it holds Allergan Platinum partner status. Serene Med Spa is at 1 Chateau Grove Ln in Barboursville, off I-64 exit 20, and also has an Ohio location in Hudson."),
  ("How much is Botox in West Virginia?","Botox, Xeomin and Daxxify are $10 per unit at our Barboursville office; Dysport is $3.99 per Dysport unit. A typical frown-line treatment is about 20 units, and Baby Botox is $200 for 20 units."),
  ("Do you price match other West Virginia med spas?","Yes, on injectables. Our Tri-State Price Match covers the same product, treatment and quantity at a licensed medical provider within 30 miles of Barboursville, where the price is currently published on a website or printed menu."),
  ("Who performs the treatments?","Board-certified physicians Dr. Shweta Arora and Dr. Robin Arora, and Stephanie Welker, FNP-BC. Physicians are on site, not on call."),
  ("How far is Barboursville from Charleston or Huntington?","Huntington is about 15 minutes east on I-64; Charleston is about 45 minutes west. We are at exit 20, so it is a highway trip with no city driving at either end."),
  ("Do you treat patients from Kentucky and Ohio?","Regularly. Ashland, Catlettsburg and Flatwoods in Kentucky and Ironton, South Point and Proctorville in Ohio are all roughly 30 to 40 minutes away."),
  ("Is there a consultation fee?","No. Consultations are complimentary and carry no commitment."),
 ],
 "related":[("/pricing/","Full Price List"),("/dermal-fillers-west-virginia/","Dermal Fillers in WV"),("/lip-filler-west-virginia/","Lip Filler in WV"),("/laser-hair-removal-west-virginia/","Laser Hair Removal in WV"),("/med-spa-huntington-wv/","Med Spa Near Huntington")],
},

# ---------- DERMAL FILLERS — WEST VIRGINIA (~165 impressions, 0 clicks) ----------
{
 "slug":"dermal-fillers-west-virginia", "service":"Dermal Fillers", "service_url":"/fillers/",
 "city":"West Virginia", "city_state":"West Virginia", "also":["Huntington, WV","Charleston, WV","Teays Valley, WV","Milton, WV"],
 "title":"Dermal Fillers in West Virginia | $500/Syringe | Serene",
 "desc":"Dermal fillers in West Virginia &mdash; Juv&eacute;derm, Restylane and Radiesse at $500 a syringe, injected by physicians in Barboursville off I-64 exit 20.",
 "eyebrow":"Dermal Fillers &middot; West Virginia",
 "h1":"Dermal Fillers in West Virginia",
 "hero":"The full Juv&eacute;derm family plus Restylane and Radiesse, at $500 a syringe &mdash; injected by board-certified physicians, with the price published before you book.",
 "drive":"Off I-64 exit 20 in Barboursville",
 "dir_h2":_WV_DIR, "visit_h2":_WV_VISIT, "cta_h2":"Filler, done by a physician",
 "introh2":"Product matched to anatomy, not to inventory",
 "introlead":"Filler is not one product, and most results that look obviously done come from the wrong gel in the wrong plane rather than from too much of it.",
 "intro":"<p>We carry the full Juv&eacute;derm range alongside Restylane and Radiesse, so the choice follows the anatomy: a soft, flexible gel for lips, something firmer for jawline and chin, a fine particle under the eyes, and Radiesse when the goal is structure plus collagen stimulation.</p><p>Dermal filler is <strong>$500 per syringe</strong>, three Juv&eacute;derm syringes are <strong>$1,300</strong>, and Radiesse is <strong>$500 a syringe</strong>. Those numbers are on the <a href=\"/pricing/\">pricing page</a> and they do not move. Our Tri-State Price Match applies: bring a currently published local price on the same product and quantity and we will match it.</p><p>Hyaluronic acid fillers can be dissolved with hyaluronidase, priced from <strong>$150</strong>. Radiesse and Sculptra cannot &mdash; which is exactly why the product conversation belongs at the consultation, before anyone injects you.</p>",
 "price_rows":[("Dermal Filler &mdash; per syringe","$500"),("3 Juv&eacute;derm Syringes","$1,300"),("Cheek, Jawline, Chin or Under-Eye Filler","$500 /syringe"),("Hand Filler","$500 /syringe"),("Radiesse","$500 /syringe"),("Sculptra","$600 /vial"),("Filler Reversal (hyaluronidase)","$150+"),("Consultation","No charge")],
 "directions":"<p>We are at <strong>1 Chateau Grove Ln, Barboursville, WV 25504</strong>, just off <strong>I-64 exit 20</strong> with free parking at the door.</p><p><strong>From Huntington:</strong> about 15 minutes. <strong>From Charleston:</strong> about 45 minutes west on I-64. <strong>From Teays Valley or Hurricane:</strong> 20 to 25 minutes. <strong>From Ashland, KY or Ironton, OH:</strong> 30 to 40 minutes.</p>",
 "origin_q":"Charleston,+WV",
 "faqs":[
  ("How much do dermal fillers cost in West Virginia?","Filler is $500 per syringe at Serene Med Spa in Barboursville, and three Juv&eacute;derm syringes are $1,300. Radiesse is also $500 a syringe. Consultations are complimentary."),
  ("Which fillers do you carry?","The full Juv&eacute;derm family, Restylane and Radiesse. Sculptra, a collagen stimulator rather than a traditional filler, is $600 a vial."),
  ("Can filler be dissolved?","Hyaluronic acid fillers such as Juv&eacute;derm and Restylane can be reversed with hyaluronidase, from $150. Radiesse and Sculptra cannot be dissolved."),
  ("How long does filler last?","Roughly 6 to 12 months in the lips and 12 to 18 months in the cheeks and jawline. Areas that move constantly break filler down faster. Individual results vary."),
  ("Do you price match filler?","On injectables, yes &mdash; the same product, treatment and quantity, currently published by a licensed medical provider within 30 miles of Barboursville."),
  ("Who injects?","Board-certified physicians Dr. Shweta Arora and Dr. Robin Arora, and Stephanie Welker, FNP-BC."),
 ],
 "related":[("/fillers/","All Dermal Fillers"),("/lip-filler-west-virginia/","Lip Filler in WV"),("/med-spa-west-virginia/","Med Spa in West Virginia"),("/botox-huntington-wv/","Botox in Huntington"),("/pricing/","Full Price List")],
},

# ---------- LIP FILLER — WEST VIRGINIA (~98 impressions, 0 clicks) ----------
{
 "slug":"lip-filler-west-virginia", "service":"Lip Filler", "service_url":"/lip-filler/",
 "city":"West Virginia", "city_state":"West Virginia", "also":["Huntington, WV","Charleston, WV","Milton, WV","Hurricane, WV"],
 "title":"Lip Filler in West Virginia | $500 Full, $300 Half | Serene",
 "desc":"Lip filler and lip injections in West Virginia &mdash; $500 a full syringe, $300 for a half-syringe Mini Pout, $80 lip flip. Physician-injected in Barboursville.",
 "eyebrow":"Lip Filler &middot; West Virginia",
 "h1":"Lip Filler in West Virginia",
 "hero":"Volbella, Juv&eacute;derm Ultra XC and Restylane Kysse, placed by board-certified physicians. $500 a full syringe, $300 for a half-syringe Mini Pout, or an $80 lip flip.",
 "drive":"Off I-64 exit 20 in Barboursville",
 "dir_h2":_WV_DIR, "visit_h2":_WV_VISIT, "cta_h2":"Lips that still look like yours",
 "introh2":"Start smaller than you think",
 "introlead":"The most common regret in lip filler is not the product. It is having placed a full syringe on the first visit when half of one would have done the job.",
 "intro":"<p>We price a half syringe deliberately &mdash; the <strong>Mini Pout at $300</strong> &mdash; because it is the right starting point for most first-time patients. A full syringe is <strong>$500</strong>, and a <strong>lip flip</strong> using about 8 units of Botox is <strong>$80</strong>, which is sometimes all a short upper lip actually needs. You can always add. Removing means dissolving.</p><p>Product choice follows the lip: <strong>Volbella</strong> for subtle definition and fine lip lines, <strong>Juv&eacute;derm Ultra XC</strong> when more structure is wanted, <strong>Restylane Kysse</strong> for flexible movement.</p><p>All three are hyaluronic acid, so all three can be reversed with hyaluronidase from $150. Lips swell more than anywhere else on the face &mdash; expect 24 to 48 hours of real swelling and a settled result at about two weeks, so do not book them the week of an event.</p>",
 "price_rows":[("Lip Filler &mdash; Full Syringe (1 mL)","$500"),("Lip Filler &mdash; Half Syringe (Mini Pout)","$300"),("Lip Flip (about 8 units)","$80"),("Filler Reversal (hyaluronidase)","$150+"),("Consultation","No charge")],
 "directions":"<p><strong>1 Chateau Grove Ln, Barboursville, WV 25504</strong>, off <strong>I-64 exit 20</strong>, free parking at the door.</p><p><strong>From Huntington:</strong> about 15 minutes. <strong>From Charleston:</strong> about 45 minutes. <strong>From Milton or Hurricane:</strong> 15 to 25 minutes. <strong>From Ashland, KY:</strong> about 35 minutes.</p>",
 "origin_q":"Huntington,+WV",
 "faqs":[
  ("How much is lip filler in West Virginia?","A full syringe is $500 and a half-syringe Mini Pout is $300 at Serene Med Spa in Barboursville. A lip flip, which uses about 8 units of Botox rather than filler, is $80."),
  ("What is the difference between a lip flip and lip filler?","A lip flip relaxes the muscle so the upper lip rolls slightly outward &mdash; it adds shape, not volume, and lasts about three months. Filler adds actual volume and lasts 6 to 12 months. Some patients do both."),
  ("Should I start with a half syringe?","Usually, yes. The $300 Mini Pout is the sensible first step. Adding more later is easy; dissolving and starting over is not."),
  ("How much will I swell?","Lips swell more than any other area. Expect substantial swelling for 24 to 48 hours and a final result at about two weeks."),
  ("Can lip filler be dissolved?","Yes. Every lip product we use is hyaluronic acid and can be reversed with hyaluronidase, from $150."),
  ("Do you do lip injections for patients from Charleston?","Regularly &mdash; Charleston is about 45 minutes west on I-64, and we are at exit 20 so there is no city driving at our end."),
 ],
 "related":[("/lip-filler/","About Lip Filler"),("/dermal-fillers-west-virginia/","Dermal Fillers in WV"),("/lip-filler-huntington-wv/","Lip Filler in Huntington"),("/med-spa-west-virginia/","Med Spa in West Virginia"),("/pricing/","Full Price List")],
},


# ---------- LASER HAIR REMOVAL — WEST VIRGINIA (~91 impressions, 1 click) ----------
{
 "slug":"laser-hair-removal-west-virginia", "service":"Laser Hair Removal", "service_url":"/laser-hair-removal/",
 "city":"West Virginia", "city_state":"West Virginia", "also":["Huntington, WV","Charleston, WV","Teays Valley, WV","Milton, WV"],
 "title":"Laser Hair Removal in West Virginia | From $49 | Serene",
 "desc":"Laser hair removal in West Virginia on the Alma Soprano ICE Platinum &mdash; from $49 a session, safe for all skin tones, year-round. Barboursville, I-64 exit 20.",
 "eyebrow":"Laser Hair Removal &middot; West Virginia",
 "h1":"Laser Hair Removal in West Virginia",
 "hero":"Alma Soprano ICE Platinum &mdash; virtually painless, safe for every skin tone, and it works year-round. Underarms $75, bikini line $99, packages of six at five sessions&rsquo; price.",
 "drive":"Off I-64 exit 20 in Barboursville",
 "dir_h2":_WV_DIR, "visit_h2":_WV_VISIT, "cta_h2":"Done with shaving",
 "introh2":"The laser that changed who can be treated",
 "introlead":"Older hair-removal lasers targeted pigment in the hair with a single wavelength, which made them risky on darker skin and useless on fine hair. Soprano ICE Platinum works differently.",
 "intro":"<p>It fires three wavelengths &mdash; 755, 810 and 1064&nbsp;nm &mdash; simultaneously, and heats the follicle gradually with a moving handpiece rather than stacking single high-energy pulses. In practice that means two things: it is <strong>safe across Fitzpatrick skin types I through VI</strong>, and most people describe it as a warm massage rather than the rubber-band snap of older systems.</p><p>It also means you are not restricted to winter. Because the treatment is not pigment-dependent in the old way, we treat through the summer with sensible sun precautions.</p><p>Pricing is per area, and every area has a <strong>package of six priced at five sessions</strong>: underarms <strong>$75</strong> ($375 for six), bikini line <strong>$99</strong> ($495), Brazilian <strong>$129</strong> ($645), full face <strong>$129</strong> ($645), upper lip <strong>$75</strong> ($375), and smaller areas such as sideburns or areola from <strong>$49</strong>. Most people need six to eight sessions spaced four to six weeks apart, because only follicles in the active growth phase respond to any given treatment.</p>",
 "price_rows":[("Sideburns or Areola","$49 (6 for $245)"),("Hands","$50 (6 for $250)"),("Upper Lip or Underarms","$75 (6 for $375)"),("Chin or Ears","$89 (6 for $445)"),("Bikini Line","$99 (6 for $495)"),("Brazilian or Full Face","$129 (6 for $645)"),("Neck or Stomach","$160 (6 for $800)"),("Consultation","No charge")],
 "directions":"<p><strong>1 Chateau Grove Ln, Barboursville, WV 25504</strong>, off <strong>I-64 exit 20</strong>, free parking outside the door.</p><p><strong>From Huntington:</strong> about 15 minutes. <strong>From Charleston:</strong> about 45 minutes west on I-64. <strong>From Teays Valley or Hurricane:</strong> 20 to 25 minutes. <strong>From Ashland, KY or Ironton, OH:</strong> 30 to 40 minutes.</p>",
 "origin_q":"Charleston,+WV",
 "faqs":[
  ("How much is laser hair removal in West Virginia?","It is priced per area at Serene Med Spa in Barboursville, from $49 a session for small areas. Underarms are $75, bikini line $99, Brazilian and full face $129. Every area has a package of six for the price of five."),
  ("How many sessions will I need?","Most people need six to eight, spaced four to six weeks apart. Hair grows in cycles and only follicles in the active growth phase respond to a given session, which is why a series is necessary rather than optional."),
  ("Is it safe for darker skin tones?","Yes. Soprano ICE Platinum is used across Fitzpatrick skin types I through VI, and the 1064 nm wavelength in particular is well suited to deeper skin tones. Your provider confirms settings at your consultation."),
  ("Does it hurt?","Far less than older lasers. The handpiece is cooled and kept moving, gradually heating the follicle rather than delivering single sharp pulses. Most patients describe it as a warm massage."),
  ("Can I have it done in summer?","Yes, with sensible sun precautions. Avoid deliberate tanning and sunburn on the area before and after, and use sunscreen."),
  ("Do I need to shave beforehand?","Yes, shave the area the day before or the morning of. Do not wax, pluck or use depilatory creams for several weeks beforehand, since the laser needs an intact follicle to target."),
 ],
 "related":[("/laser-hair-removal/","About Laser Hair Removal"),("/laser-hair-removal-huntington-wv/","Laser Hair Removal in Huntington"),("/med-spa-west-virginia/","Med Spa in West Virginia"),("/laser-tattoo-removal-huntington-wv/","Tattoo Removal in Huntington"),("/pricing/","Full Price List")],
},

# ---------- MEN'S FACIAL / MEN'S SKIN — WEST VIRGINIA (~116 impressions, 0 clicks) ----------
{
 "slug":"mens-facial-west-virginia", "service":"Men's Facials", "service_url":"/medical-facials/",
 "city":"West Virginia", "city_state":"West Virginia", "also":["Huntington, WV","Charleston, WV","Teays Valley, WV","Ashland, KY"],
 "title":"Men's Facials in West Virginia | $150 | Serene Med Spa",
 "desc":"Facials for men in West Virginia &mdash; HydraFacial and SKNLAB at $150, plus ingrown-hair and beard-line treatment. Physician-led, Barboursville, I-64 exit 20.",
 "eyebrow":"Men's Skin &middot; West Virginia",
 "h1":"Men's Facials in West Virginia",
 "hero":"A 30-minute HydraFacial or SKNLAB facial at $150 &mdash; no fuss, no downtime, no sales pitch. Plus real answers for ingrown hairs, beard-line irritation and sun damage.",
 "drive":"Off I-64 exit 20 in Barboursville",
 "dir_h2":_WV_DIR, "visit_h2":_WV_VISIT, "cta_h2":"Straightforward skin care for men",
 "introh2":"What men actually come in for",
 "introlead":"Most men who book a facial are not chasing a glow. They have a specific problem: ingrown hairs along the jaw, redness that will not settle, blackheads across the nose, or twenty years of sun on the forehead.",
 "intro":"<p>Male skin is thicker, oilier and &mdash; because of daily shaving &mdash; chronically irritated in ways that most facial menus ignore. Our approach starts with the complaint rather than the package.</p><p>The workhorses are the <strong>HydraFacial</strong> and the <strong>SKNLAB facial</strong>, both <strong>$150</strong> and both about 30 minutes: cleanse, exfoliate, extract and hydrate, with no downtime and nothing visible afterward except clearer skin. For ingrown hairs and razor bumps along the neck and beard line, the durable answer is usually <strong>laser hair removal</strong> on the beard line &mdash; neck and beard line is $160 a session, or $800 for six &mdash; which thins the problem at the source.</p><p>For deeper sun damage and texture we have Alma Hybrid CO&sup2; resurfacing, Opus Plasma and Morpheus8. And because Serene is physician-owned, a conversation about skin can extend into hormone optimization, weight loss or men's wellness without a referral across town.</p>",
 "price_rows":[("HydraFacial","$150"),("SKNLAB Facial","$150"),("Facials &amp; Dermaplaning","$100+"),("Laser Facial","$400"),("Laser Hair Removal &mdash; Neck &amp; Beard Line","$160 (6 for $800)"),("Botox (including shoulder slimming)","$10 /unit"),("Consultation","No charge")],
 "directions":"<p><strong>1 Chateau Grove Ln, Barboursville, WV 25504</strong>, off <strong>I-64 exit 20</strong>, free parking at the door and a private treatment room.</p><p><strong>From Huntington:</strong> about 15 minutes. <strong>From Charleston:</strong> about 45 minutes. <strong>From Ashland, KY or Ironton, OH:</strong> 30 to 40 minutes.</p>",
 "origin_q":"Huntington,+WV",
 "faqs":[
  ("Do you do facials for men?","Yes, routinely. HydraFacial and SKNLAB facials are $150 and take about 30 minutes, with no downtime and nothing visible afterward."),
  ("What helps with ingrown hairs and razor bumps?","Laser hair removal along the neck and beard line is usually the durable fix, because it thins the follicles causing the problem. Neck and beard line is $160 a session or $800 for a package of six."),
  ("Is there downtime?","Not from a HydraFacial or SKNLAB facial &mdash; you can go straight back to work. Resurfacing lasers are a different matter and we will tell you exactly what to expect before you book one."),
  ("Do men get Botox here?","Regularly. Botox is $10 a unit, and shoulder slimming Botox is priced the same. Men often start with the frown line between the brows."),
  ("Will I be the only man there?","No. A substantial share of our patients are men, and consultations happen in a private treatment room rather than an open bay."),
  ("What else do you offer men?","Hormone optimization with Bi&ouml;te pellets, medical weight loss, IV therapy, laser hair removal, and men's sexual wellness including Alma Duo. All under one roof with physicians on site."),
 ],
 "related":[("/medical-facials/","Medical Facials"),("/hydrafacial/","HydraFacial"),("/mens-sexual-wellness/","Men's Sexual Wellness"),("/laser-hair-removal-west-virginia/","Laser Hair Removal in WV"),("/med-spa-west-virginia/","Med Spa in West Virginia")],
},


# ---------- BOTOX — HUNTINGTON (~180 impressions, 2 clicks) ----------
{
 "slug":"botox-huntington-wv", "service":"Botox &amp; Fillers", "service_url":"/botox/",
 "city":"Huntington", "city_state":"Huntington, WV", "also":["Barboursville, WV","Ona, WV","Milton, WV","Proctorville, OH","Chesapeake, OH"],
 "title":"Botox in Huntington, WV | $10 a Unit | Serene Med Spa",
 "desc":"Botox at $10 a unit and filler at $500 a syringe for Huntington, WV &mdash; physician-injected, 15 minutes east at I-64 exit 20 in Barboursville. Price match.",
 "eyebrow":"Botox &amp; Fillers &middot; Serving Huntington, WV",
 "h1":"Botox and Fillers for Huntington, West Virginia",
 "hero":"Botox at $10 a unit. Dysport at $3.99. Filler at $500 a syringe. Injected by board-certified physicians 15 minutes east of Huntington, right off I-64 exit 20.",
 "drive":"About 15 minutes from Huntington",
 "cta_h2":"Fifteen minutes east on I-64",
 "introh2":"Ten dollars a unit, and we will match a lower one",
 "introlead":"Huntington patients tend to arrive having already priced Botox somewhere else. So here is ours, plainly: $10 a unit, published on the website, the same for everyone.",
 "intro":"<p>Botox, Xeomin and Daxxify are <strong>$10 per unit</strong>; Dysport is <strong>$3.99 per Dysport unit</strong>. Those scales are not comparable &mdash; Dysport typically needs two to three times the units for the same effect &mdash; so the honest comparison is cost per treated area, which your injector will walk through. Baby Botox is <strong>$200 for 20 units</strong> and a lip flip is <strong>$80</strong>.</p><p>Our <strong>Tri-State Price Match</strong> covers injectables: find a currently published price on the same product and quantity at a licensed medical provider within 30 miles, and we will match it. Dermal filler is <strong>$500 a syringe</strong>, with three Juv&eacute;derm syringes at <strong>$1,300</strong>.</p><p>We are an <strong>Allergan Platinum</strong> partner, so All&#275; members earn and redeem points here. Injections are performed by board-certified physicians and Stephanie Welker, FNP-BC &mdash; and we are at I-64 exit 20, which makes the trip from Huntington a highway run rather than a cross-town crawl.</p>",
 "price_rows":[("Botox, Xeomin or Daxxify","$10 /unit"),("Dysport","$3.99 /unit"),("Baby Botox","$200 / 20 units"),("Lip Flip","$80"),("Shoulder Slimming Botox","$10 /unit"),("Dermal Filler","$500 /syringe"),("3 Juv&eacute;derm Syringes","$1,300"),("Consultation","No charge")],
 "directions":"<p><strong>From Huntington (about 10 miles):</strong> I-64 East to <strong>exit 20</strong> (Barboursville / Huntington Mall), then follow US-60. We are at 1 Chateau Grove Ln with free parking outside the door &mdash; usually about 15 minutes door to door.</p><p><strong>From Proctorville or Chesapeake, OH:</strong> cross at the Robert C. Byrd or 31st Street bridge and pick up I-64 East, about 20 to 25 minutes. <strong>From Ona or Milton:</strong> I-64 West, 10 to 15 minutes.</p>",
 "origin_q":"Huntington,+WV",
 "faqs":[
  ("How much is Botox in Huntington, WV?","Botox, Xeomin and Daxxify are $10 per unit at Serene Med Spa, 15 minutes east in Barboursville. Dysport is $3.99 per Dysport unit. A typical frown-line treatment is about 20 units, and Baby Botox is $200 for 20 units."),
  ("Is there a Serene office in Huntington itself?","Our West Virginia office is at 1 Chateau Grove Ln in Barboursville, off I-64 exit 20 &mdash; about 15 minutes east of Huntington. We also have an Ohio location in Hudson."),
  ("Do you match Botox prices from other Huntington med spas?","Yes. Our Tri-State Price Match covers the same product, treatment and quantity at a licensed medical provider within 30 miles of Barboursville, where the price is currently published on a website or printed menu."),
  ("Botox or Dysport?","They are dosed on different scales, so the per-unit prices are not comparable. Dysport usually needs two to three times the units, which puts the cost per area in a similar range. Your injector will recommend based on how you respond, not on price."),
  ("How long does Botox last?","Most people get three to four months. Dose, the muscles treated and your own metabolism all matter. Individual results vary."),
  ("Can I be treated the same day as my consultation?","Usually yes, if you are a good candidate &mdash; so one trip from Huntington covers both."),
  ("Do you take All&#275; points?","Yes, we are an Allergan Partner Privileges Platinum practice."),
 ],
 "related":[("/botox/","About Botox"),("/lip-filler-huntington-wv/","Lip Filler in Huntington"),("/dermal-fillers-west-virginia/","Dermal Fillers in WV"),("/med-spa-huntington-wv/","Med Spa Near Huntington"),("/pricing/","Full Price List")],
},

# ---------- FACIALS — HUNTINGTON (~134 impressions, 1 click) ----------
{
 "slug":"facials-huntington-wv", "service":"Medical Facials", "service_url":"/medical-facials/",
 "city":"Huntington", "city_state":"Huntington, WV", "also":["Barboursville, WV","Ona, WV","Milton, WV","Proctorville, OH"],
 "title":"Facials in Huntington, WV | HydraFacial $150 | Serene",
 "desc":"Medical facials for Huntington, WV &mdash; HydraFacial and SKNLAB at $150, dermaplaning from $100, VI peels from $250. Physician-led, 15 minutes east at exit 20.",
 "eyebrow":"Medical Facials &middot; Serving Huntington, WV",
 "h1":"Medical Facials for Huntington, West Virginia",
 "hero":"HydraFacial and SKNLAB facials at $150, dermaplaning from $100, medical-grade peels from $250 &mdash; chosen for your skin by a physician-led team, 15 minutes east of Huntington.",
 "drive":"About 15 minutes from Huntington",
 "cta_h2":"Book a facial that was chosen for your skin",
 "introh2":"The difference a medical facial makes",
 "introlead":"A spa facial is designed to feel good. A medical facial is designed to change something &mdash; congestion, pigment, texture, active acne &mdash; and it starts with someone qualified looking at your skin.",
 "intro":"<p>Both are legitimate. They are just not the same purchase, and it is worth knowing which one you are making.</p><p>Our core treatments are the <strong>HydraFacial</strong> and the <strong>SKNLAB facial</strong>, both <strong>$150</strong>. HydraFacial cleanses, extracts and hydrates in about 30 minutes with no downtime. SKNLAB uses six handpieces &mdash; ultrasound, hot and cold, microcurrent and lymphatic drainage alongside the cleanse &mdash; and suits skin that needs more than decongesting. <strong>Facials and dermaplaning</strong> start at <strong>$100</strong>, and the <strong>Laser Facial</strong> is <strong>$400</strong>.</p><p>When the problem runs deeper, we escalate: <strong>VI chemical peels from $250</strong> for tone, acne and melasma, a <strong>depigmentation treatment from $200</strong>, and Alma Hybrid CO&sup2; or Opus Plasma resurfacing for texture and sun damage. Skin is mapped with VISIA at your consultation so the recommendation is based on what is actually in your skin, not on what is being promoted this month.</p>",
 "price_rows":[("HydraFacial","$150"),("SKNLAB Facial","$150"),("Facials &amp; Dermaplaning","$100+"),("Laser Facial","$400"),("VI Chemical Peels","$250+"),("Depigmentation Treatment","$200+"),("Consultation","No charge")],
 "directions":"<p><strong>From Huntington (about 10 miles):</strong> I-64 East to <strong>exit 20</strong>, then US-60 to 1 Chateau Grove Ln &mdash; about 15 minutes, free parking at the door.</p><p><strong>From Proctorville or Chesapeake, OH:</strong> about 20 to 25 minutes. <strong>From Ona or Milton:</strong> 10 to 15 minutes on I-64 West.</p>",
 "origin_q":"Huntington,+WV",
 "faqs":[
  ("How much is a facial near Huntington, WV?","HydraFacial and SKNLAB facials are both $150 at Serene Med Spa in Barboursville, 15 minutes east of Huntington. Facials with dermaplaning start at $100 and the Laser Facial is $400."),
  ("HydraFacial or SKNLAB &mdash; which should I book?","HydraFacial is the efficient 30-minute cleanse, extract and hydrate. SKNLAB adds ultrasound, microcurrent, hot and cold and lymphatic drainage across six handpieces, so it suits skin needing more than decongesting. Both are $150 and we will steer you at the consultation."),
  ("Is there any downtime?","Not from a HydraFacial, SKNLAB facial or dermaplaning &mdash; most people go straight back to work. Chemical peels and resurfacing lasers do have downtime, and we will tell you exactly how much before you book."),
  ("Do you treat active acne?","Yes. Depending on what we find, that can mean facials with extractions, VI peels from $250, or Kenalog injections for individual inflamed cysts. Persistent acne is a medical problem and gets treated as one."),
  ("What about melasma and dark spots?","VI peels from $250 and our depigmentation treatment from $200 are the usual starting points, along with strict sun protection. Melasma is managed rather than cured, and anyone promising a permanent fix is overselling."),
  ("Do you analyze skin first?","Yes, with VISIA imaging at your consultation, which shows sun damage and pigment below the surface that is not yet visible."),
 ],
 "related":[("/medical-facials/","Medical Facials"),("/hydrafacial/","HydraFacial"),("/sknlab/","SKNLAB Facial"),("/mens-facial-west-virginia/","Men's Facials in WV"),("/med-spa-huntington-wv/","Med Spa Near Huntington")],
},

# ---------- LIP FILLER — HUNTINGTON (~68 impressions, 4 clicks) ----------
{
 "slug":"lip-filler-huntington-wv", "service":"Lip Filler", "service_url":"/lip-filler/",
 "city":"Huntington", "city_state":"Huntington, WV", "also":["Barboursville, WV","Ona, WV","Milton, WV","Proctorville, OH"],
 "title":"Lip Filler in Huntington, WV | $500 / $300 | Serene Med Spa",
 "desc":"Lip filler for Huntington, WV &mdash; $500 a full syringe, $300 half-syringe Mini Pout, $80 lip flip. Physician-injected 15 minutes east at I-64 exit 20.",
 "eyebrow":"Lip Filler &middot; Serving Huntington, WV",
 "h1":"Lip Filler for Huntington, West Virginia",
 "hero":"Volbella, Juv&eacute;derm Ultra XC and Restylane Kysse, injected by board-certified physicians. $500 a full syringe, $300 for a half-syringe Mini Pout, $80 for a lip flip.",
 "drive":"About 15 minutes from Huntington",
 "cta_h2":"Fifteen minutes for lips you will still like in a year",
 "introh2":"Three ways to treat a lip, and only one of them is a full syringe",
 "introlead":"Plenty of lips do not need a full syringe. Some need half. Some need no filler at all &mdash; just a lip flip to let a short upper lip roll outward.",
 "intro":"<p>We price all three deliberately: a <strong>full syringe at $500</strong>, a <strong>half-syringe Mini Pout at $300</strong>, and a <strong>lip flip at $80</strong> using about 8 units of Botox. Most first-time patients are best served by the Mini Pout. Adding later is simple; dissolving and restarting is not.</p><p>Product is matched to the lip: <strong>Volbella</strong> for definition and fine lip lines, <strong>Juv&eacute;derm Ultra XC</strong> for more structure, <strong>Restylane Kysse</strong> when flexible movement matters most. All three are hyaluronic acid and all three can be reversed with hyaluronidase from <strong>$150</strong>.</p><p>One practical note for Huntington patients planning around an event: lips swell more than anywhere else. Expect 24 to 48 hours of genuine swelling and a settled result at roughly two weeks, so book with that runway.</p>",
 "price_rows":[("Lip Filler &mdash; Full Syringe (1 mL)","$500"),("Lip Filler &mdash; Half Syringe (Mini Pout)","$300"),("Lip Flip (about 8 units)","$80"),("Filler Reversal (hyaluronidase)","$150+"),("Consultation","No charge")],
 "directions":"<p><strong>From Huntington (about 10 miles):</strong> I-64 East to <strong>exit 20</strong>, then US-60 to 1 Chateau Grove Ln. About 15 minutes, free parking at the door.</p><p><strong>From Proctorville or Chesapeake, OH:</strong> 20 to 25 minutes. <strong>From Ona or Milton:</strong> 10 to 15 minutes.</p>",
 "origin_q":"Huntington,+WV",
 "faqs":[
  ("How much is lip filler in Huntington, WV?","A full syringe is $500 and a half-syringe Mini Pout is $300 at Serene Med Spa in Barboursville, 15 minutes east. A lip flip is $80."),
  ("What is a lip flip?","About 8 units of Botox placed along the upper lip so it rolls slightly outward. It changes shape rather than adding volume, costs $80, and lasts around three months."),
  ("Full syringe or half?","Most first-timers should start with the $300 Mini Pout. You can always add more at a follow-up."),
  ("How long does it last?","Typically 6 to 12 months. Lips move constantly, so they metabolize filler faster than cheeks or jawline."),
  ("How long is the swelling?","Substantial for 24 to 48 hours, settling over about two weeks. Do not schedule lips in the week before an event."),
  ("Can it be dissolved?","Yes &mdash; every lip product we use is hyaluronic acid, reversible with hyaluronidase from $150."),
 ],
 "related":[("/lip-filler/","About Lip Filler"),("/lip-filler-west-virginia/","Lip Filler in WV"),("/botox-huntington-wv/","Botox in Huntington"),("/dermal-fillers-west-virginia/","Dermal Fillers in WV"),("/pricing/","Full Price List")],
},

# ---------- LASER HAIR REMOVAL — HUNTINGTON (~71 impressions, 3 clicks) ----------
{
 "slug":"laser-hair-removal-huntington-wv", "service":"Laser Hair Removal", "service_url":"/laser-hair-removal/",
 "city":"Huntington", "city_state":"Huntington, WV", "also":["Barboursville, WV","Ona, WV","Milton, WV","Proctorville, OH"],
 "title":"Laser Hair Removal in Huntington, WV | From $49 | Serene",
 "desc":"Laser hair removal for Huntington, WV on the Alma Soprano ICE Platinum &mdash; underarms $75, bikini $99, six sessions for the price of five. I-64 exit 20.",
 "eyebrow":"Laser Hair Removal &middot; Serving Huntington, WV",
 "h1":"Laser Hair Removal for Huntington, West Virginia",
 "hero":"Alma Soprano ICE Platinum &mdash; virtually painless, safe for all skin tones, and it works year-round. Underarms $75, bikini line $99, packages of six at five sessions&rsquo; price.",
 "drive":"About 15 minutes from Huntington",
 "cta_h2":"Stop shaving, starting this season",
 "introh2":"Priced per area, packaged at six",
 "introlead":"Laser hair removal is only ever sold honestly as a series, because a single session can only affect the follicles that happen to be in their active growth phase that week.",
 "intro":"<p>That is why every area here carries a <strong>package of six priced at five sessions</strong>, and why we say plainly that most people need six to eight treatments spaced four to six weeks apart.</p><p>Per session: sideburns or areola <strong>$49</strong>, hands <strong>$50</strong>, upper lip or underarms <strong>$75</strong>, chin or ears <strong>$89</strong>, bikini line <strong>$99</strong>, Brazilian or full face <strong>$129</strong>, neck and beard line or stomach <strong>$160</strong>. Package pricing is on the <a href=\"/pricing/\">pricing page</a>.</p><p>We treat on the <strong>Soprano ICE Platinum</strong>, which fires 755, 810 and 1064&nbsp;nm simultaneously through a cooled, moving handpiece. It is safe across Fitzpatrick types I to VI &mdash; including deeper skin tones that older lasers could not treat safely &mdash; and comfortable enough that most patients describe it as a warm massage. For men, the neck and beard line is the most requested area, usually because of ingrown hairs rather than the hair itself.</p>",
 "price_rows":[("Sideburns or Areola","$49 (6 for $245)"),("Hands","$50 (6 for $250)"),("Upper Lip or Underarms","$75 (6 for $375)"),("Chin or Ears","$89 (6 for $445)"),("Bikini Line","$99 (6 for $495)"),("Brazilian or Full Face","$129 (6 for $645)"),("Neck &amp; Beard Line or Stomach","$160 (6 for $800)"),("Consultation","No charge")],
 "directions":"<p><strong>From Huntington (about 10 miles):</strong> I-64 East to <strong>exit 20</strong>, then US-60 to 1 Chateau Grove Ln &mdash; about 15 minutes with free parking at the door.</p><p><strong>From Proctorville or Chesapeake, OH:</strong> 20 to 25 minutes. <strong>From Ona or Milton:</strong> 10 to 15 minutes.</p>",
 "origin_q":"Huntington,+WV",
 "faqs":[
  ("How much is laser hair removal in Huntington, WV?","Pricing is per area at Serene Med Spa in Barboursville, from $49 a session. Underarms are $75, bikini line $99, Brazilian and full face $129. Every area has a package of six for the price of five."),
  ("How many treatments will I need?","Six to eight for most people, spaced four to six weeks apart, because only follicles in the active growth phase respond to any single session."),
  ("Is it safe for darker skin?","Yes. Soprano ICE Platinum treats Fitzpatrick types I through VI, and its 1064 nm wavelength is particularly suited to deeper skin tones."),
  ("Does it hurt?","Much less than older lasers. The handpiece is cooled and kept moving, heating the follicle gradually rather than with sharp single pulses."),
  ("Does it help with ingrown hairs?","Usually yes, and it is the most common reason men book the neck and beard line. Reducing the follicles reduces the ingrowns."),
  ("Do I need to shave first?","Yes &mdash; shave the day before or the morning of. Do not wax, pluck or use depilatory creams for several weeks beforehand, since the laser needs an intact follicle."),
 ],
 "related":[("/laser-hair-removal/","About Laser Hair Removal"),("/laser-hair-removal-west-virginia/","Laser Hair Removal in WV"),("/mens-facial-west-virginia/","Men's Facials in WV"),("/laser-tattoo-removal-huntington-wv/","Tattoo Removal in Huntington"),("/pricing/","Full Price List")],
},

# ---------- LASER TATTOO REMOVAL — HUNTINGTON (132 impressions, 18 clicks — best performer) ----------
{
 "slug":"laser-tattoo-removal-huntington-wv", "service":"Laser Tattoo Removal", "service_url":"/laser-tattoo-removal/",
 "city":"Huntington", "city_state":"Huntington, WV", "also":["Barboursville, WV","Ashland, KY","Ironton, OH","Proctorville, OH"],
 "title":"Tattoo Removal in Huntington, WV | From $125 | Serene",
 "desc":"Laser tattoo removal for Huntington, WV &mdash; priced by size from $125 a session, six-session packages, physician-led. Barboursville, off I-64 exit 20.",
 "eyebrow":"Laser Tattoo Removal &middot; Serving Huntington, WV",
 "h1":"Laser Tattoo Removal for Huntington, West Virginia",
 "hero":"Priced by the size of the tattoo, not by guesswork &mdash; from $125 a session, with packages of six. Physician-led removal 15 minutes east of Huntington at I-64 exit 20.",
 "drive":"About 15 minutes from Huntington",
 "cta_h2":"Start with a complimentary size and colour assessment",
 "introh2":"Priced by size, measured at the consultation",
 "introlead":"Most tattoo removal pricing is deliberately vague. Ours is a table, based on the one thing that actually drives cost: how much surface area has to be treated.",
 "intro":"<p><strong>Micro</strong> (under 1 sq in, fits under a quarter) is <strong>$125</strong> a session or <strong>$625</strong> for six. <strong>Small</strong> (1&ndash;4 sq in) is <strong>$150</strong> or <strong>$750</strong>. <strong>Medium</strong> (5&ndash;9 sq in) is <strong>$250</strong> or <strong>$1,250</strong>. <strong>Large</strong> (10&ndash;16 sq in, up to a dollar bill) is <strong>$400</strong> or <strong>$2,000</strong>. Anything bigger &mdash; sleeves and back pieces &mdash; is quoted at your complimentary consultation, which carries no commitment.</p><p>What the table cannot tell you is how many sessions you will need, and anyone who gives you a firm number before seeing the tattoo is guessing. It depends on ink colour and density, how deep it was placed, how old it is, where it sits on the body and how well you heal. Black and dark blue clear most readily; greens, light blues and some yellows are stubborn. Amateur tattoos usually need fewer sessions than professional work. Sessions are spaced six to eight weeks apart so your body can clear the fragmented pigment.</p><p>We will tell you at the consultation if we think complete clearance is unlikely, and what realistic fading looks like instead &mdash; which is often enough if you are covering up rather than erasing.</p>",
 "price_rows":[("Micro &mdash; under 1 sq in","$125 (6 for $625)"),("Small &mdash; 1&ndash;4 sq in","$150 (6 for $750)"),("Medium &mdash; 5&ndash;9 sq in","$250 (6 for $1,250)"),("Large &mdash; 10&ndash;16 sq in","$400 (6 for $2,000)"),("Sleeves &amp; back pieces","Quoted at consultation"),("Consultation","No charge")],
 "directions":"<p><strong>From Huntington (about 10 miles):</strong> I-64 East to <strong>exit 20</strong>, then US-60 to 1 Chateau Grove Ln &mdash; about 15 minutes, free parking at the door.</p><p><strong>From Ashland, KY:</strong> I-64 East, about 35 minutes. <strong>From Ironton or Proctorville, OH:</strong> 25 to 35 minutes.</p>",
 "origin_q":"Huntington,+WV",
 "faqs":[
  ("How much does tattoo removal cost in Huntington, WV?","It is priced by size at Serene Med Spa in Barboursville: micro $125, small $150, medium $250 and large $400 per session, each with a package of six. Sleeves and back pieces are quoted at a complimentary consultation."),
  ("How many sessions will it take?","It depends on ink colour and density, depth, age, body location and your healing. Anyone quoting a firm number sight unseen is guessing. We give you a realistic range after seeing the tattoo."),
  ("Which colours are hardest to remove?","Black and dark blue respond best. Greens, light blues and some yellows are considerably more stubborn and may need more sessions or may fade rather than clear."),
  ("How far apart are sessions?","Six to eight weeks, so your body has time to clear the fragmented pigment between treatments. Rushing the interval does not speed up the result."),
  ("Does it hurt?","Most people find it sharper than getting the tattoo, but each session is much shorter. We use cooling and can apply topical numbing beforehand."),
  ("Can you fade a tattoo for a cover-up instead of removing it?","Yes, and it is a common request. Fading for a cover-up needs far fewer sessions than full clearance &mdash; tell us at the consultation so we plan for it."),
  ("Will it scar?","Properly performed laser removal rarely scars, though existing scarring from the original tattoo will remain. Following aftercare and not picking the treated area matters."),
 ],
 "related":[("/laser-tattoo-removal/","About Tattoo Removal"),("/laser-hair-removal-huntington-wv/","Laser Hair Removal in Huntington"),("/med-spa-huntington-wv/","Med Spa Near Huntington"),("/med-spa-west-virginia/","Med Spa in West Virginia"),("/pricing/","Full Price List")],
},

]
