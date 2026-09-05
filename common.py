# -*- coding: utf-8 -*-
# Shared components for Serene Med Spa — Barboursville, WV (lean site: home + blog)
LOGO = "https://serenemedspas.com/wp-content/uploads/2024/11/Serene_Logo-1024x574.png"
BOOK = "tel:+13045200461"
PHONE_DISPLAY = "(304) 520-0461"
AREA_TOWNS = ["Barboursville","Huntington","Milton","Hurricane","Teays Valley","Ona","Ceredo","Kenova","Proctorville, OH","Ashland, KY"]
AREA_SERVED = (
  [{"@type":"AdministrativeArea","name":n} for n in ["Cabell County, WV","Wayne County, WV","Putnam County, WV"]] +
  [{"@type":"City","name":t+", WV"} for t in ["Barboursville","Huntington","Milton","Hurricane","Ona"]]
)
NAV = '''<header>
  <div class="wrap nav">
    <a href="/"><img src="%s" alt="Serene Med Spa — Barboursville, WV"></a>
    <ul>
      <li><a href="/#services">Treatments</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li class="has-drop"><a href="#" onclick="return false">Locations &#9662;</a>
        <div class="mega loc-mini">
          <a href="https://hudson.serenemedspas.com/">Hudson, OH</a>
          <a href="/">Barboursville, WV</a>
        </div>
      </li>
      <li><a href="/#consult">Contact</a></li>
    </ul>
    <a class="btn nav-book" href="%s">Call to Book</a>
    <button class="menu-toggle" aria-label="Menu" onclick="var u=document.querySelector('.nav ul');u.style.display=u.style.display==='flex'?'none':'flex'">&#9776;</button>
  </div>
</header>''' % (LOGO, BOOK)
FOOTER = '''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img src="%s" alt="Serene Med Spa" style="filter:brightness(0) invert(1)">
        <p style="max-width:340px">Physician-led medical spa &amp; wellness in Barboursville, West Virginia, proudly serving Huntington, Cabell County &amp; the greater Tri-State. Natural results, personalized plans, and care you can trust.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/#services">Treatments</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="https://hudson.serenemedspas.com/">Hudson, OH location</a></li>
          <li><a href="/#consult">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li>1 Chateau Grove Ln</li>
          <li>Barboursville, WV 25504</li>
          <li><a href="tel:+13045200461">(304) 520-0461</a></li>
          <li style="margin-top:10px;font-weight:600">Also in Hudson, OH</li>
          <li><a href="https://hudson.serenemedspas.com/">Visit our OH location &rsaquo;</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">&copy; 2026 Serene Med Spa, Barboursville WV. All rights reserved.</div>
  </div>
</footer>''' % LOGO
def areas_section(treatment="care"):
    tags = "".join('<span>%s</span>' % t for t in AREA_TOWNS)
    return '<section class="areas"><div class="wrap reveal" style="text-align:center"><div class="eyebrow" style="justify-content:center">Proudly Serving</div><h2>Barboursville, Huntington &amp; the Tri-State</h2><div class="area-tags">%s</div></div></section>' % tags
STICKY_BAR = '<div class="mbar"><a class="mbar-call" href="tel:+13045200461">&#9742;&nbsp; Call</a><a class="mbar-book" href="tel:+13045200461">Book Now</a></div>'
CONSULT_SECTION = '''<section class="consult" id="consult">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Get In Touch</div><h2>Request a Consultation</h2><p>Tell us what you&rsquo;re interested in and our team will reach out &mdash; or call <a href="tel:+13045200461">(304)&nbsp;520-0461</a>.</p></div>
    <div class="consult-card reveal">
      <div class="hs-form-frame" data-region="na2" data-form-id="16625e0e-6a46-4664-98c6-2cbf264da060" data-portal-id="242695075"></div>
    </div>
  </div>
  <script src="https://js-na2.hsforms.net/forms/embed/242695075.js" defer></script>
</section>'''
SCRIPTS = '''<script>
  var io=new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
</script>
<script src="/popup.js" defer></script>
<script>function loadScript(a){var b=document.getElementsByTagName("head")[0],c=document.createElement("script");c.type="text/javascript",c.src="https://tracker.metricool.com/resources/be.js",c.onreadystatechange=a,c.onload=a,b.appendChild(c)}loadScript(function(){beTracker.t({hash:"1b170ac2814a470a9b94ea34c6f6d045"})});</script>'''
print("common loaded (Barboursville)")
