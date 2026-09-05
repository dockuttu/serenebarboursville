# -*- coding: utf-8 -*-
import os, json, html as _html
exec(open("common.py").read())  # NAV, FOOTER, SCRIPTS, LOGO, BOOK, CONSULT_SECTION
SITE="https://barboursville.serenemedspas.com"

# ---------- posts registry ----------
POSTS = [{
  "slug":"hormone-optimization-barboursville-wv",
  "title":"Hormone Imbalance in Barboursville &amp; Huntington: The Signs",
  "seo_title":"Hormone Optimization &amp; BHRT in Barboursville, WV",
  "h1":"Hormone Imbalance in Barboursville &amp; Huntington: Signs &amp; How BHRT Can Help",
  "desc":"Serving Barboursville, Huntington &amp; the Tri-State: the signs of hormone imbalance in men &amp; women and how physician-supervised BHRT and Bi&ouml;te pellets may help.",
  "date":"2026-09-05","date_h":"September 5, 2026",
  "cat":"Hormone Optimization","cat_link":"/#services",
  "img":"/img/serene-front-desk.jpg",
  "img_alt":"Reception area at Serene Med Spa, a Certified Bi&ouml;te Provider serving Barboursville and Huntington, WV",
  "excerpt":"Tired, foggy, or gaining weight around the middle that won&rsquo;t budge? Those changes often trace back to shifting hormones. Here are the signs to watch for &mdash; and how physician-supervised hormone optimization may help in the Tri-State.",
  "body":'''
<p>Between work, family, and everything in between, it&rsquo;s easy to explain away feeling run-down. But when the fatigue, the stubborn weight, the restless sleep, and the mental fog all pile up at once, there&rsquo;s often a medical reason underneath &mdash; your hormones. At <strong>Serene Med Spa in Barboursville</strong>, we help men and women across the Tri-State &mdash; Huntington, Cabell County, and the surrounding West Virginia, West Virginia, and Kentucky communities &mdash; understand what&rsquo;s really going on and, when it&rsquo;s appropriate, restore balance through <strong>physician-supervised hormone optimization</strong>. As a <strong>Certified Bi&ouml;te Provider</strong>, we start with a simple lab test, not guesswork.</p>
<h2>Why so many adults feel &ldquo;off&rdquo;</h2>
<p>Hormones are chemical messengers that quietly run your energy, sleep, mood, metabolism, focus, and libido. As we age &mdash; and with the everyday stress of busy Tri-State life &mdash; those levels can drift out of their healthy range. The result is a cluster of symptoms that are easy to dismiss one at a time, but add up to a real quality-of-life problem. The good news: it&rsquo;s measurable, and often manageable.</p>
<h2>Signs your hormones may be out of balance</h2>
<p>Many patients tell us they&rsquo;re dealing with several of these at once. <strong>In women</strong> &mdash; often tied to perimenopause and menopause:</p>
<ul><li>Persistent tiredness and low energy</li><li>Trouble staying asleep through the night</li><li>Weight gain around the midsection that resists diet and exercise</li><li>Mood swings, irritability, or feeling constantly &ldquo;on edge&rdquo;</li><li>Brain fog &mdash; trouble with focus and memory</li><li>Low libido and changes in intimate wellness</li></ul>
<p><strong>In men</strong> &mdash; often related to a gradual decline in testosterone:</p>
<ul><li>Fatigue and less day-to-day stamina</li><li>Loss of muscle strength</li><li>Harder time losing weight, with more fat around the middle</li><li>Low or flat mood and a shorter temper</li><li>Reduced mental sharpness</li><li>Lower sex drive and performance changes</li></ul>
<p>Having a few of these doesn&rsquo;t automatically mean your hormones are to blame &mdash; but it&rsquo;s a solid reason to get tested and talk with a provider who can look at the whole picture.</p>
<h2>What hormone optimization (BHRT) actually is</h2>
<p><strong>Bioidentical hormone replacement therapy (BHRT)</strong> is a physician-supervised way of bringing your hormones back toward healthy, balanced levels using <strong>bioidentical hormones</strong> &mdash; hormones that are structurally identical to the ones your body makes on its own. The aim isn&rsquo;t to &ldquo;cure&rdquo; anything; it&rsquo;s to help you feel more like yourself by easing the symptoms that come with hormonal change &mdash; always under medical supervision and tailored to your labs and goals.</p>
<h2>Bi&ouml;te pellet therapy at our Barboursville office</h2>
<p>As a Certified Bi&ouml;te Provider, one of the options we offer is <strong>hormone pellet therapy</strong>. Bi&ouml;te pellets are tiny, bioidentical hormone pellets placed just under the skin during a quick in-office visit. They release a steady, low dose of hormones over several months &mdash; so there&rsquo;s no daily cream or pill to keep track of. Because everyone&rsquo;s body is different, your provider may recommend pellets or another physician-supervised approach that fits your needs, and monitors your progress with follow-up labs.</p>
<h2>What your first visit looks like</h2>
<ol><li><strong>A simple lab test.</strong> We check where your hormone levels actually are.</li><li><strong>A consultation.</strong> We review your results, symptoms, and goals together.</li><li><strong>A personalized plan.</strong> If hormone optimization is right for you, we build a plan around your labs and lifestyle.</li><li><strong>Ongoing support.</strong> We track your progress with follow-up visits and labs.</li></ol>
<h2>Ready to feel more like yourself?</h2>
<p>If several of these signs sound familiar, the next step is simple: get tested and talk with our physician-led team. Call our Barboursville office at <strong><a href="tel:+13045200461">(304)&nbsp;520-0461</a></strong> to book a consultation.</p>
<p><em>This information is for general educational purposes only and is not medical advice. These statements have not been evaluated by the Food and Drug Administration. Individual results vary and are not guaranteed. Hormone therapy is provided only after consultation and evaluation by a licensed provider, and is not intended to diagnose, treat, cure, or prevent any disease.</em></p>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is hormone optimization only for menopause?","acceptedAnswer":{"@type":"Answer","text":"No. Many women pursue it during perimenopause and menopause, but men with symptoms of low testosterone can also benefit. Both start with a simple lab test."}},{"@type":"Question","name":"What are bioidentical hormones?","acceptedAnswer":{"@type":"Answer","text":"They are hormones structurally identical to the ones your body makes naturally. Your provider will explain the options during your consultation."}},{"@type":"Question","name":"Where in West Virginia are you located?","acceptedAnswer":{"@type":"Answer","text":"Our office is in Barboursville, WV and serves Huntington, Cabell County, and the greater Tri-State area."}}]}
</script>
''',
  "author_bio":"Dr. Robin Arora, MD is board-certified in aesthetic medicine by the American Academy of Aesthetic Medicine (AAAM). He completed an internal medicine residency through an NYU-affiliated program in the Bronx and a nephrology fellowship at Tulane University."
}]

HEAD_FONTS='''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

# ---------- individual post pages ----------
for p in POSTS:
    url=f"{SITE}/blog/{p['slug']}/"
    crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
      {"@type":"ListItem","position":2,"name":"Blog","item":SITE+"/blog/"},
      {"@type":"ListItem","position":3,"name":p["cat"],"item":url}]}
    art={"@context":"https://schema.org","@type":"BlogPosting","headline":_html.unescape(p["h1"]),
      "description":_html.unescape(p["desc"]),"image":SITE+p["img"],"datePublished":p["date"],"dateModified":p["date"],
      "author":{"@type":"Person","name":"Dr. Robin Arora, MD"},
      "publisher":{"@type":"MedicalBusiness","name":"Serene Med Spa","logo":{"@type":"ImageObject","url":LOGO}},
      "mainEntityOfPage":url,"articleSection":p["cat"]}
    HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p.get("seo_title", p["title"]+" | Serene Med Spa")}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-WV"><meta name="geo.placename" content="Barboursville, West Virginia">
<meta property="og:type" content="article">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{p['img']}">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(crumb)}
</script>
<script type="application/ld+json">
{json.dumps(art)}
</script>
</head>
<body>

{NAV}

<article class="post">
  <div class="wrap post-wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; <a href="/blog/">Blog</a> &nbsp;&#8250;&nbsp; {p["cat"]}</div>
    <a class="post-cat" href="{p['cat_link']}">{p["cat"]}</a>
    <h1>{p["h1"]}</h1>
    <div class="post-meta">By <strong>Dr. Robin Arora, MD</strong> &middot; {p["date_h"]}</div>
    <img class="post-hero" src="{p['img']}" alt="{p.get('img_alt', p['cat']+' before and after at Serene Med Spa')}" width="1148" height="790">
    <div class="post-body">
{p["body"]}
    </div>
    <div class="post-bio"><p>{p["author_bio"]}</p></div>
    <div class="post-cta">
      <a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a Consultation</a>
      <a class="btn btn-outline" href="/before-after/">See More Results</a>
    </div>
  </div>
</article>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}
</body>
</html>
'''
    d=f"bundle/site/blog/{p['slug']}"
    os.makedirs(d,exist_ok=True)
    open(d+"/index.html","w").write(HTML)
    print("post written:", p["slug"], len(HTML), "bytes")

# ---------- blog index ----------
POSTS_SORTED=sorted(POSTS,key=lambda x:x["date"],reverse=True)
cards="\n".join(f'''      <a class="blog-card reveal" href="/blog/{p['slug']}/">
        <div class="blog-thumb"><img loading="lazy" src="{p['img']}" alt="{p['title']}"></div>
        <div class="blog-txt"><span class="blog-tag">{p['cat']}</span><h3>{p['title']}</h3><p>{p['excerpt']}</p><span class="blog-date">{p['date_h']}</span></div>
      </a>''' for p in POSTS_SORTED)

idx_url=f"{SITE}/blog/"
idx_crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
  {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
  {"@type":"ListItem","position":2,"name":"Blog","item":idx_url}]}
blog_schema={"@context":"https://schema.org","@type":"Blog","name":"Serene Med Spa Blog","url":idx_url,
  "blogPost":[{"@type":"BlogPosting","headline":_html.unescape(p["title"]),"url":f"{SITE}/blog/{p['slug']}/","datePublished":p["date"]} for p in POSTS]}

IDX=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Blog &mdash; Serene Med Spa, Barboursville WV</title>
<meta name="description" content="Aesthetic insights, treatment techniques, and patient case studies from the physician-led team at Serene Med Spa in Barboursville and Huntington, WV.">
<link rel="canonical" href="{idx_url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-WV"><meta name="geo.placename" content="Barboursville, West Virginia">
<meta property="og:type" content="website">
<meta property="og:title" content="Blog &mdash; Serene Med Spa, Barboursville WV">
<meta property="og:description" content="Aesthetic insights &amp; case studies from our physician-led team.">
<meta property="og:url" content="{idx_url}">
<meta property="og:image" content="{LOGO}">
{HEAD_FONTS}
<script type="application/ld+json">
{json.dumps(idx_crumb)}
</script>
<script type="application/ld+json">
{json.dumps(blog_schema)}
</script>
</head>
<body>

<div class="promo">&#10024; <strong>From Our Team</strong> &mdash; techniques, results &amp; aesthetic insights. <a href="{BOOK}" target="_blank" rel="noopener">Book a consultation</a> &#10024;</div>

{NAV}

<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs"><a href="/">Home</a> &nbsp;&#8250;&nbsp; Blog</div>
    <div class="svc-hero-txt" style="max-width:720px">
      <div class="eyebrow">Aesthetic Insights</div>
      <h1>The Serene Blog</h1>
      <p>Technique breakdowns, patient case studies, and honest guidance from our physician-led team &mdash; serving Barboursville, West Virginia and Barboursville, West Virginia.</p>
    </div>
  </div>
</section>

<section class="tint-blush">
  <div class="wrap">
    <div class="blog-grid">
{cards}
    </div>
  </div>
</section>

{CONSULT_SECTION}

{FOOTER}

{SCRIPTS}
</body>
</html>
'''
os.makedirs("bundle/site/blog",exist_ok=True)
open("bundle/site/blog/index.html","w").write(IDX)
print("blog index written:", len(IDX), "bytes;", len(POSTS), "posts")

# ---------- RSS feed (for Metricool blog auto-share) ----------
import email.utils as _eut, datetime as _dt
def _rfc822(d):
    return _eut.format_datetime(_dt.datetime.strptime(d,"%Y-%m-%d").replace(tzinfo=_dt.timezone.utc))
def _x(s):
    return _html.escape(_html.unescape(s), quote=False)
_items=[]
for _p in sorted(POSTS, key=lambda x:x["date"], reverse=True):
    _u=f"{SITE}/blog/{_p['slug']}/"
    _items.append(
      "  <item>\n"
      f"    <title>{_x(_p['title'])}</title>\n"
      f"    <link>{_u}</link>\n"
      f"    <guid isPermaLink=\"true\">{_u}</guid>\n"
      f"    <pubDate>{_rfc822(_p['date'])}</pubDate>\n"
      f"    <description>{_x(_p['excerpt'])}</description>\n"
      "  </item>")
_feed=(
  '<?xml version="1.0" encoding="UTF-8"?>\n'
  '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n<channel>\n'
  f"  <title>Serene Med Spa &#8212; Barboursville Blog</title>\n"
  f"  <link>{SITE}/blog/</link>\n"
  "  <description>Physician-led aesthetics, wellness and hormone insights from Serene Med Spa.</description>\n"
  "  <language>en-us</language>\n"
  f"  <atom:link href=\"{SITE}/blog/feed.xml\" rel=\"self\" type=\"application/rss+xml\"/>\n"
  + "\n".join(_items) + "\n</channel>\n</rss>\n")
open("bundle/site/blog/feed.xml","w",encoding="utf-8").write(_feed)
print("feed.xml written:", len(POSTS), "items")
