# -*- coding: utf-8 -*-
# bv_unique_static.py — post-build, idempotent. Barboursville-only wording for the four hand-built
# pages (botox, fillers, morpheus8, weight-loss) so they are not city-swapped copies of Hudson.
# Exact-string swaps; prints a warning if a source sentence has changed and no longer matches.
import os, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else "bundle/site"
R = {
 "botox": [
  ("Soften fine lines and expression wrinkles for a naturally refreshed look — administered by board-certified physicians who believe less is more.",
   "Relax frown lines, forehead lines and crow&rsquo;s feet with Botox, Dysport, Xeomin or Daxxify, backed by our Tri-State price-match promise."),
  ("At Serene Med Spa in Barboursville, every treatment is planned and performed by our board-certified physicians. We take a conservative, tailored approach: enhancing your features and refreshing your appearance while keeping your expressions natural. We offer Botox&reg; along with Dysport&reg; and Xeomin&reg;, and we'll help you choose the neurotoxin that best fits your goals. Whether it's your first time or part of your ongoing routine, we start with a conversation about your goals.",
   "Barboursville patients can choose Botox&reg;, Dysport&reg;, Xeomin&reg; or Daxxify&reg;, and we&rsquo;ll explain how they differ before you decide. Treatment is planned by our physician-led team with a conservative approach, so your expressions stay natural. Whether it&rsquo;s your first time or you&rsquo;re switching from another practice, we start with a short conversation about your goals."),
  ("Injectables are as much art as science. Placement, dosing, and an understanding of how your face moves make the difference between \"refreshed\" and \"overdone.\" At Serene, your treatment is always performed by board-certified physicians — Dr. Robin Arora and Dr. Shweta Arora — in a calm, welcoming setting right here in Barboursville.",
   "Good results depend more on placement and dose than on the brand name. At Serene Barboursville, your injector studies how your face moves before treating, prices are published up front, and we&rsquo;ll match a lower published price on the same product from a licensed provider within 30 miles."),
 ],
 "fillers": [
  ("Restore lost volume, define your features, and smooth deeper folds with hyaluronic-acid fillers — artfully placed by board-certified physicians.",
   "Replace lost volume in the cheeks, lips and jawline, and soften folds around the mouth, with hyaluronic-acid fillers placed by our physician-led team."),
  ("At Serene Med Spa in Barboursville, filler is an art form. Our board-certified physicians study proportion and balance to create results that look like a better-rested version of you — never overfilled. Every plan starts with a consultation to understand what you like and what you'd like to refine.",
   "In Barboursville we treat lips, cheeks, jawline, chin and under-eyes, and we plan each syringe around your whole face rather than one feature. Your first visit is a consultation about what you like, what you&rsquo;d change and how much product it realistically takes, so there are no surprises on price."),
  ("Beautiful filler results come down to injector skill and an eye for proportion. At Serene, your treatment is always performed by board-certified physicians — Dr. Robin Arora and Dr. Shweta Arora — who prioritize safety, symmetry, and a look that's unmistakably yours.",
   "Filler results come down to anatomy and restraint. Our Barboursville team, led by Dr. Robin Arora and Dr. Shweta Arora, favors gradual, balanced changes and welcomes you back if anything needs refining. Hyaluronic-acid fillers can also be dissolved if ever needed."),
 ],
 "morpheus8": [
  ("Tighten, smooth, and resurface your skin from within — RF microneedling that remodels collagen for firmer, fresher-looking skin, guided by board-certified physicians.",
   "Tighten mild laxity, refine pores and soften acne scars with Morpheus8 radiofrequency microneedling at our Barboursville office."),
  ("At Serene Med Spa in Barboursville, Morpheus8 treatments are customized and physician-supervised. We tailor the depth and energy to your skin and goals, whether you're targeting early signs of aging, acne scarring, enlarged pores, or mild laxity along the jawline and neck.",
   "Barboursville patients use Morpheus8 for the lower face and neck, acne scarring, enlarged pores and body areas such as the abdomen and arms. Because we also offer SecretRF and classic microneedling here, your provider can tell you honestly whether Morpheus8 is the right depth of treatment for your skin."),
  ("Energy-based treatments deliver the best results — and stay safest — in experienced hands. At Serene, Morpheus8 is guided by board-certified physicians, Dr. Robin Arora and Dr. Shweta Arora, who tailor every session to your skin type and goals right here in Barboursville.",
   "Radiofrequency microneedling is safest when the settings match your skin type. At Serene Barboursville, every Morpheus8 plan is physician-supervised, with depth and energy chosen for you and a typical series of about three sessions mapped out before you start."),
 ],
 "weight-loss": [
  ("A physician-supervised, personalized path to your goals — combining medical expertise, real support, and modern options like GLP-1 medications when appropriate.",
   "Medical weight loss in Barboursville with physician oversight, regular check-ins, and GLP-1 medications when they&rsquo;re appropriate for you."),
  ("Lasting weight loss isn't about willpower alone — it's about the right plan, medical guidance, and support along the way. At Serene Med Spa in Barboursville, our board-certified physicians build a program around your health history, lifestyle, and goals.",
   "Weight loss that lasts usually takes more than willpower. At Serene Barboursville, your program starts with your health history, lifestyle and goals, and is built and supervised by our physician-led team."),
  ("Weight management is medicine — and it's safest and most effective under a physician's care. At Serene, your program is designed and supervised by board-certified physicians, Dr. Robin Arora and Dr. Shweta Arora, who take the time to understand your health and support you throughout your journey.",
   "Weight management is medical care. In Barboursville, your plan is designed and monitored by Dr. Robin Arora and Dr. Shweta Arora, with check-ins to track progress and adjust your plan over time. Medicare patients can also ask about our <a href=\"https://blog.serenemedspas.com/medicare-glp-1-bridge-program-barboursville-huntington-wv/?loc=barboursville\">GLP-1 bridge program</a>."),
 ],
}
n = miss = 0
for slug, pairs in R.items():
    p = os.path.join(BASE, slug, "index.html")
    if not os.path.exists(p): continue
    s = open(p, encoding="utf-8").read(); t = s
    for old, new in pairs:
        if old in t: t = t.replace(old, new)
        elif new not in t:
            miss += 1; print("  !! bv_unique_static: source text changed on /%s/: %s..." % (slug, old[:60]))
    if t != s:
        open(p, "w", encoding="utf-8").write(t); n += 1
print("bv_unique_static: %d page(s) rewritten, %d unmatched" % (n, miss))
