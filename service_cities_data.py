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

]
