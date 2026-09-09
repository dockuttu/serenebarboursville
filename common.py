# -*- coding: utf-8 -*-
# Shared components for Serene Med Spa — Barboursville, WV
# Full site: home + service pages (gen_pages.py) + pricing + blog + Ultherapy + Xperience+ rewards.
import json

LOGO = "https://serenemedspas.com/wp-content/uploads/2024/11/Serene_Logo-1024x574.png"
PHONE_TEL = "tel:+13045200461"
PHONE_DISPLAY = "(304) 520-0461"
SITE_URL = "https://barboursville.serenemedspas.com"

# ---- Mangomint online booking (deep links to the right consultation) ----
MM = "https://booking.mangomint.com/serenemedspa?serviceId=%s"
BOOK = MM % 321                      # Free Consultation — the default "Book" everywhere
BOOK_MAP = {                          # slug -> consultation that page should open
 "ultherapy":            MM % 322,   # Ultherapy Consultation
 "medical-facials":      MM % 323,   # Acne Consultation (acne facial / skin)
 "emsculpt-neo":         MM % 324,   # Body Contouring Consultation
 "evolve-x":             MM % 324, "bodytite": MM % 324, "facetite": MM % 324,
 "forma":                MM % 324, "liposuction": MM % 324, "lipomelt": MM % 324,
 "mens-sexual-wellness": MM % 325,   # Sexual Wellness Consultation
 "womens-sexual-wellness": MM % 325,
 "weight-loss":          MM % 326,   # Weight Loss Consultation
 "hormone-optimization": MM % 327,   # Hormone (Biöte) Consultation
 # ---- treatment services (book the treatment directly) ----
 "botox": MM % 328,                  # Wrinkle Relaxer (Botox · Dysport · Xeomin · Daxxify)
 "fillers": MM % 329, "lip-filler": MM % 329, "cheek-filler": MM % 329,
 "under-eye-filler": MM % 329, "jawline-filler": MM % 329, "chin-filler": MM % 329,  # Dermal Filler
 "skinvive": MM % 330,               # Skinvive
 "sculptra": MM % 331,               # Sculptra
 "kybella": MM % 332,                # Kybella (per vial)
 "thread-lift": MM % 337,            # PDO Thread Lift
 "spider-veins": MM % 338, "under-eye-prp": MM % 333, "kenalog": MM % 334, "laser-hair-removal": MM % 339,           # Spider Vein Sclerotherapy
}
def book_for(slug): return BOOK_MAP.get(slug, BOOK)

# ---- Barboursville Price Match Guarantee (site-wide highlight) ----
PM_SLUGS = {"botox","fillers","lip-filler","cheek-filler","under-eye-filler","jawline-filler","chin-filler",
            "skinvive","kybella","sculptra","under-eye-prp","kenalog","thread-lift","spider-veins","sculptra-bbl"}
PRICE_MATCH_RIBBON = '''<div class="promo">&#10022; <strong>Tri-State Price Match:</strong> Botox $10/unit &amp; we&rsquo;ll match any published local price on injectables &mdash; <a href="/#price-match">see the guarantee</a></div>
'''
PRICE_MATCH_BAND = '''<section class="pmatch reveal" id="price-match">
  <div class="wrap">
    <div class="pm-grid">
      <div class="pm-txt">
        <div class="eyebrow">Barboursville Price Match Guarantee</div>
        <h2>We&rsquo;ll match any published Tri-State price on injectables</h2>
        <p>Botox, Dysport, Xeomin &amp; Daxxify from <strong>$10/unit</strong>. Dermal filler from <strong>$500/syringe</strong>. Sculptra <strong>$600/vial</strong>. Every treatment performed by our physician-led team &mdash; and if you find a lower published price on the same treatment anywhere in the Tri-State, bring it in and we&rsquo;ll match it.</p>
        <div class="pm-cta"><a class="btn" href="%s" target="_blank" rel="noopener">Book Botox &mdash; $10/unit</a><a class="btn btn-ghost" href="/pricing/#injectables">See Full Pricing</a></div>
        <p class="pm-fine">Match applies to the same product, treatment and quantity at a licensed medical provider within 30 miles of Barboursville, WV. Price must be currently published (website or printed menu). Not combinable with other offers or rewards.</p>
      </div>
      <div class="pm-stats">
        <div><b>$10</b><span>Botox / unit</span></div>
        <div><b>$500</b><span>Filler / syringe</span></div>
        <div><b>$600</b><span>Sculptra / vial</span></div>
        <div><b>$300</b><span>PDO threads from</span></div>
      </div>
    </div>
  </div>
</section>
''' % (MM % 328)

# ---- Barboursville service catalogue (drives nav, footer, sitemap) ----
CATEGORIES = [
 ("Injectables", [
   ("botox","Botox"), ("fillers","Dermal Fillers"), ("lip-filler","Lip Filler"),
   ("cheek-filler","Cheek Filler"), ("under-eye-filler","Under-Eye Filler"),
   ("jawline-filler","Jawline Filler"), ("chin-filler","Chin Filler"),
   ("skinvive","Skinvive"), ("kybella","Kybella"), ("sculptra","Sculptra"),
   ("under-eye-prp","Under-Eye PRP / PRF"), ("kenalog","Kenalog Injections"),
 ]),
 ("Skin &amp; Facials", [
   ("morpheus8","Morpheus8"), ("ultherapy","Ultherapy"), ("laser-facial","Laser Facial"), ("chemical-peels","Chemical Peels"),
   ("hydrafacial","HydraFacial"), ("medical-facials","Medical Facials &amp; Microdermabrasion"),
   ("hyperpigmentation","Hyperpigmentation &amp; Melasma"),
 ]),
 ("Laser", [
   ("laser-skin","Laser Skin Resurfacing"), ("harmony-bio-boost","Harmony Bio-Boost"), ("photofacial","Photofacial (BBL &amp; IPL)"),
   ("laser-hair-removal","Laser Hair Removal"), ("laser-tattoo-removal","Laser Tattoo Removal"),
   ("laser-nail-fungus","Laser Nail Fungus"),
 ]),
 ("Body &amp; Contouring", [
   ("evolve-x","Evolve X"), ("bodytite","BodyTite"), ("facetite","FaceTite"),
   ("forma","Forma Skin Tightening"), ("liposuction","Liposuction &amp; Fat Transfer"),
   ("weight-loss","Medical Weight Loss"), ("sculptra-bbl","Sculptra BBL"),
 ]),
 ("Regenerative &amp; Hair", [
   ("microneedling","Microneedling &amp; PRP"), ("thread-lift","PDO Thread Lift"),
   ("prp-hair-restoration","Hair Restoration"),
 ]),
 ("Wellness", [
   ("iv-therapy","IV Therapy"), ("hormone-optimization","Hormone Optimization"),
   ("mens-sexual-wellness","Men's Sexual Wellness"), ("womens-sexual-wellness","Women's Sexual Wellness"),
   ("spider-veins","Spider Vein Treatment"), ("xperience-rewards","Xperience+ Rewards"),
 ]),
]
ALL_SLUGS = [s for _,items in CATEGORIES for s,_ in items]

# ---- local SEO: 30-mile radius around 1 Chateau Grove Ln, Barboursville ----
AREA_TOWNS = ["Barboursville", "Proctorville, OH", "Ona", "Salt Rock", "Huntington", "Chesapeake, OH", "Milton", "Culloden", "Burlington, OH", "Ceredo", "Hurricane", "Kenova", "Wayne", "South Point, OH", "Catlettsburg, KY", "Ashland, KY", "Teays Valley", "Coal Grove, OH", "Ironton, OH", "Russell, KY"]
AREA_SERVED = (
  [{"@type":"AdministrativeArea","name":n} for n in ["Cabell County, WV","Wayne County, WV","Lincoln County, WV","Putnam County, WV","Lawrence County, OH","Boyd County, KY","Greenup County, KY"]] +
  [{"@type":"City","name":t} for t in ["Barboursville, WV","Huntington, WV","Milton, WV","Hurricane, WV","Ona, WV","Teays Valley, WV","Proctorville, OH","Chesapeake, OH","South Point, OH","Ironton, OH","Ashland, KY","Catlettsburg, KY"]]
)
COUNTY_LINE = "Cabell, Wayne, Lincoln and Putnam counties in West Virginia, Lawrence County, Ohio, and Boyd &amp; Greenup counties in Kentucky"

def areas_section(treatment="care"):
    tags = "".join('<span>%s</span>' % t for t in AREA_TOWNS)
    return '''<section class="areas">
  <div class="wrap reveal" style="text-align:center">
    <div class="eyebrow" style="justify-content:center">Proudly Serving</div>
    <h2>Barboursville, Huntington &amp; the Tri-State</h2>
    <p style="max-width:720px;margin:0 auto 22px;color:var(--muted)">Located just off I-64 in Barboursville, Serene Med Spa welcomes patients seeking %s from across %s &mdash; including the communities below.</p>
    <div class="area-tags">%s</div>
  </div>
</section>''' % (treatment, COUNTY_LINE, tags)

# ---- navigation ----
def _mega():
    cols=[]
    for cat, items in CATEGORIES:
        links = "".join('<a href="/%s/">%s</a>' % (s,l) for s,l in items)
        cols.append('<div class="mcol"><h5>%s</h5>%s</div>' % (cat, links))
    return '<div class="mega">%s</div>' % "".join(cols)

NAV = PRICE_MATCH_RIBBON + '''<header>
  <div class="wrap nav">
    <a href="/"><img src="%s" alt="Serene Med Spa — Barboursville, WV"></a>
    <ul>
      <li class="has-drop"><a href="/#services">Treatments &#9662;</a>
        %s
      </li>
      <li><a href="/pricing/">Pricing</a></li>
      <li><a href="https://blog.serenemedspas.com/">Blog</a></li>
      <li class="has-drop"><a href="#" onclick="return false">Locations &#9662;</a>
        <div class="mega loc-mini">
          <a href="https://hudson.serenemedspas.com/">Hudson, OH</a>
          <a href="/">Barboursville, WV</a>
        </div>
      </li>
      <li><a href="/#consult">Contact</a></li>
    </ul>
    <a class="btn nav-book" href="%s" target="_blank" rel="noopener">Book Now</a>
    <button class="menu-toggle" aria-label="Menu" onclick="var u=document.querySelector('.nav ul');u.style.display=u.style.display==='flex'?'none':'flex'">&#9776;</button>
  </div>
</header>''' % (LOGO, _mega(), BOOK)

_FOOT_ITEMS = [("botox","Botox"),("fillers","Dermal Fillers"),("lip-filler","Lip Filler"),
  ("morpheus8","Morpheus8"),("ultherapy","Ultherapy"),("hydrafacial","HydraFacial"),
  ("laser-hair-removal","Laser Hair Removal"),("weight-loss","Medical Weight Loss"),("iv-therapy","IV Therapy")]
FOOTER_TREAT = '''      <div>
        <h4>Treatments</h4>
        <ul>
%s
          <li><a href="/pricing/">Pricing &amp; Menu</a></li>
          <li><a href="/#services">All Treatments</a></li>
        </ul>
      </div>''' % "\n".join('          <li><a href="/%s/">%s</a></li>'%(s,l) for s,l in _FOOT_ITEMS)

FOOTER = '''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img src="%s" alt="Serene Med Spa" style="filter:brightness(0) invert(1)">
        <p style="max-width:340px">Physician-led medical spa &amp; wellness in Barboursville, West Virginia, proudly serving Huntington, Cabell County &amp; the greater Tri-State. Natural results, personalized plans, and care you can trust.</p>
      </div>
%s
      <div>
        <h4>Contact</h4>
        <ul>
          <li>1 Chateau Grove Ln</li>
          <li>Barboursville, WV 25504</li>
          <li><a href="%s">%s</a></li>
          <li><a href="%s" target="_blank" rel="noopener">Book Online</a></li>
          <li><a href="/xperience-rewards/">Xperience+ Rewards</a></li>
          <li><a href="https://blog.serenemedspas.com/">Blog</a></li>
          <li style="margin-top:10px;font-weight:600">Also in Hudson, OH</li>
          <li><a href="https://hudson.serenemedspas.com/">Visit our OH location &rsaquo;</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">&copy; 2026 Serene Med Spa, Barboursville WV. All rights reserved.</div>
  </div>
</footer>''' % (LOGO, FOOTER_TREAT, PHONE_TEL, PHONE_DISPLAY, BOOK)

# ---- engagement components ----
STICKY_BAR = '''<div class="mbar">
  <a class="mbar-call" href="%s">&#9742;&nbsp; Call</a>
  <a class="mbar-book" href="%s" target="_blank" rel="noopener">Book Now</a>
</div>''' % (PHONE_TEL, BOOK)

PARTNER_BADGES = '''<div class="partners reveal">
      <a href="/ultherapy/" title="Ultherapy PRIME provider"><img src="/img/badges/ultherapy-prime.png" alt="Ultherapy PRIME provider" class="badge-wide" loading="lazy"></a>
      <span title="Merz Aesthetics Bronze Preferred Partner"><img src="/img/badges/merz-bronze-preferred.png" alt="Merz Aesthetics Bronze Preferred Partner" class="badge-round" loading="lazy"></span>
      <a href="/xperience-rewards/" title="Xperience+ Rewards Program"><img src="/img/badges/xperience-plus.png" alt="Xperience+ Rewards Program by Merz Aesthetics" class="badge-xp" loading="lazy"></a>
    </div>'''

STATS_BRANDS = '''<section class="stats">
  <div class="wrap">
    <div class="stat-row reveal">
      <div class="stat"><b data-count="2">0</b><span>Board-Certified Physicians</span></div>
      <div class="stat"><b>5&#9733;</b><span>Google-Rated Care</span></div>
      <div class="stat"><b data-count="100" data-suffix="%">0</b><span>Physician-Led</span></div>
      <div class="stat"><b data-count="35" data-suffix="+">0</b><span>Treatments Offered</span></div>
    </div>
    <div class="brands reveal">
      <span>Botox</span><span>Juv&eacute;derm</span><span>Sculptra</span><span>Morpheus8</span><span>HydraFacial</span><span>Bi&ouml;te</span>
    </div>
    ''' + PARTNER_BADGES + '''
  </div>
</section>'''

FINANCE_BAND = '''<div class="finance"><div class="wrap reveal">
  <span>&#128179; Flexible financing &amp; membership options available &mdash; ask us about the best fit at your visit.</span>
  <a class="btn btn-outline" href="%s" target="_blank" rel="noopener">Book a Consultation</a>
</div></div>''' % BOOK

REVIEWS_SECTION = '''<section class="tint-blush" id="reviews">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Loved by Barboursville</div><h2>What Our Patients Say</h2></div>
    <div class="rev-grid">
      <div class="rev reveal"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Dr. Shweta Arora is skilled with fillers &amp; Botox. She listens to your concerns and looks at your face to see what is needed! I look and feel 10 yrs younger after the first visit. She starts conservatively which is nice if it&rsquo;s your first time. Love Serene Spa in Barboursville."</p><div class="who">&mdash; Dbeauty Angel</div></div>
      <div class="rev reveal"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Dr Arora is the best! So considerate and patient. Took the time to answer my many questions without trying to rush me out. Extremely thorough and knowledgeable. I recommend emphatically. He does not disappoint."</p><div class="who">&mdash; Roseann Cerrito</div></div>
      <div class="rev reveal"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Great service and great staff. Very helpful with any questions. I always leave feeling taken care of and looking my best."</p><div class="who">&mdash; Christopher Cross</div></div>
    </div>
    <p class="rev-note">&#9733;&#9733;&#9733;&#9733;&#9733; Verified reviews from our patients on Google</p>
  </div>
</section>'''

# ---- aftercare (shared content, WV phone) ----
exec(open("aftercare_data.py").read())  # AFTERCARE, AC_ALIAS
def aftercare_html(slug):
    key = AC_ALIAS.get(slug)
    if not key or key not in AFTERCARE: return ""
    d = AFTERCARE[key]
    cols = "\n".join(
      '      <div class="ac-col reveal"><h3>%s</h3><ul>%s</ul></div>'
      % (h, "".join("<li>%s</li>" % b for b in bl)) for h, bl in d["cols"])
    parts = ['<section class="aftercare" id="aftercare">',
      '  <div class="wrap">',
      '    <div class="section-head reveal"><div class="eyebrow">After Your Visit</div><h2>Aftercare</h2><p>%s</p></div>' % d["intro"],
      '    <div class="ac-grid">', cols, '    </div>']
    if d.get("normal"):
        parts.append('    <div class="ac-strip reveal"><span class="ac-lbl">What&rsquo;s normal</span><div class="ac-tags">%s</div></div>'
                     % "".join("<span>%s</span>" % n for n in d["normal"]))
    if d.get("urgent"):
        parts.append('    <div class="ac-strip ac-alert reveal"><span class="ac-lbl">&#9888; Call your provider if you experience</span><div class="ac-tags">%s</div></div>'
                     % "".join("<span>%s</span>" % u for u in d["urgent"]))
    if d.get("results"):
        parts.append('    <p class="ac-results reveal"><strong>Results:</strong> %s</p>' % d["results"])
    parts.append('    <p class="ac-note">General guidance from Serene Med Spa &mdash; always follow the specific instructions your provider gives you. Questions? Call <a href="%s">%s</a>.</p>' % (PHONE_TEL, PHONE_DISPLAY.replace(" ","&nbsp;")))
    parts += ['  </div>', '</section>']
    return "\n".join(parts)

# ---- hero photo per slug ----
HERO_MAP = {
 "botox":"botox-inject","fillers":"filler-inject","lip-filler":"lip-inject",
 "cheek-filler":"filler-inject","under-eye-filler":"filler-inject","jawline-filler":"filler-inject",
 "chin-filler":"filler-inject","skinvive":"filler-inject","kybella":"filler-inject","sculptra":"filler-inject",
 "morpheus8":"morpheus8","ultherapy":"morpheus8","laser-facial":"laser","chemical-peels":"facial-2","hydrafacial":"hydrafacial",
 "medical-facials":"facial-room","hyperpigmentation":"skin-analysis",
 "laser-skin":"laser","harmony-bio-boost":"skin-analysis","photofacial":"laser","laser-hair-removal":"laser","laser-tattoo-removal":"laser",
 "laser-nail-fungus":"laser","evolve-x":"morpheus8","bodytite":"morpheus8",
 "facetite":"morpheus8","forma":"morpheus8","liposuction":"dr-arora","weight-loss":"dr-arora",
 "microneedling":"morpheus8","thread-lift":"filler-inject","under-eye-prp":"filler-inject","kenalog":"botox-inject","sculptra-bbl":"dr-arora","prp-hair-restoration":"hair-ted",
 "iv-therapy":"facial-room","hormone-optimization":"dr-arora",
 "mens-sexual-wellness":"dr-arora","womens-sexual-wellness":"dr-arora","spider-veins":"laser",
}
def hero_for(slug): return HERO_MAP.get(slug, "facial-3")

RESULTS_SECTION = '''<section class="results" id="results">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Real Patients</div><h2>Real Results</h2></div>
    <div class="res-grid">
      <figure class="res reveal"><img loading="lazy" src="/img/ba-forehead.jpg" alt="Before and after wrinkle-relaxer treatment at Serene Med Spa Barboursville"><figcaption>Wrinkle Relaxer &mdash; Before &amp; After</figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/ba-cheek.jpg" alt="Before and after dermal filler at Serene Med Spa Barboursville"><figcaption>Dermal Filler &mdash; Before &amp; After</figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/ba-lip.jpg" alt="Before and after lip filler at Serene Med Spa Barboursville"><figcaption>Lip Filler &mdash; Before &amp; After</figcaption></figure>
      <figure class="res reveal"><img loading="lazy" src="/img/m8-result.jpg" alt="Before and after Morpheus8 skin resurfacing"><figcaption>Morpheus8 &mdash; Before &amp; After</figcaption></figure>
    </div>
    <p class="rev-note">Individual results may vary. Photos of our own patients, shared with consent.</p>
  </div>
</section>'''

CONSULT_SECTION = '''<section class="consult" id="consult">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Get In Touch</div><h2>Request a Consultation</h2><p>Tell us what you&rsquo;re interested in and our team will reach out &mdash; or <a href="%s" target="_blank" rel="noopener">book online</a> / call <a href="%s">%s</a>.</p></div>
    <div class="consult-card reveal">
      <div class="hs-form-frame" data-region="na2" data-form-id="16625e0e-6a46-4664-98c6-2cbf264da060" data-portal-id="242695075"></div>
    </div>
  </div>
  <script src="https://js-na2.hsforms.net/forms/embed/242695075.js" defer></script>
</section>''' % (BOOK, PHONE_TEL, PHONE_DISPLAY.replace(" ","&nbsp;"))

SCRIPTS = '''<script>
  document.querySelectorAll('.faq button').forEach(function(b){b.addEventListener('click',function(){var f=b.parentElement,ans=f.querySelector('.ans'),open=f.classList.contains('open');document.querySelectorAll('.faq').forEach(function(x){x.classList.remove('open');x.querySelector('.ans').style.maxHeight=null;});if(!open){f.classList.add('open');ans.style.maxHeight=ans.scrollHeight+'px';}});});
  var io=new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
  (function(){var done=false;function run(){if(done)return;var s=document.querySelector('.stats');if(!s)return;var r=s.getBoundingClientRect();if(r.top<innerHeight-40&&r.bottom>0){done=true;document.querySelectorAll('.stat b[data-count]').forEach(function(el){var t=+el.getAttribute('data-count'),suf=el.getAttribute('data-suffix')||'',c=0,step=Math.max(1,Math.ceil(t/45));var iv=setInterval(function(){c+=step;if(c>=t){c=t;clearInterval(iv);}el.textContent=c+suf;},22);});}}
  addEventListener('scroll',run,{passive:true});addEventListener('load',run);run();})();
</script>
<script src="/popup.js" defer></script>
<script>function loadScript(a){var b=document.getElementsByTagName("head")[0],c=document.createElement("script");c.type="text/javascript",c.src="https://tracker.metricool.com/resources/be.js",c.onreadystatechange=a,c.onload=a,b.appendChild(c)}loadScript(function(){beTracker.t({hash:"1b170ac2814a470a9b94ea34c6f6d045"})});</script>'''
print("common loaded (Barboursville):", len(ALL_SLUGS), "services")
