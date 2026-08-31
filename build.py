import os, re, json

SITE_URL = "https://jamilahmad.example"  # placeholder — replaced at deploy/custom-domain step, see README
SITE_NAME = "Jamil Ahmad"
OUT = "/home/claude/site"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("education.html", "Education"),
    ("experience.html", "Experience"),
    ("research.html", "Research"),
    ("projects.html", "Projects"),
    ("content.html", "Content & Media"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]

PERSON_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Person",
    "@id": SITE_URL + "/#person",
    "name": "Jamil Ahmad",
    "nationality": "Pakistani",
    "jobTitle": ["Primary School Teacher", "Researcher", "Sustainable Finance Professional"],
    "alumniOf": [
        {
            "@type": "CollegeOrUniversity",
            "name": "University of Swat"
        },
        {
            "@type": "CollegeOrUniversity",
            "name": "Universitas Islam Internasional Indonesia (UIII)"
        }
    ],
    "knowsAbout": [
        "Sustainable Finance", "Renewable Energy", "Political Stability and Economic Impact",
        "Sustainable Development", "Green Finance", "Energy Transition", "Financial Sustainability"
    ],
    "url": SITE_URL,
    "sameAs": []  # placeholders — populate once real profile links are added, see contact.html
}

WEBSITE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": SITE_URL + "/#website",
    "url": SITE_URL,
    "name": "Jamil Ahmad",
    "publisher": {"@id": SITE_URL + "/#person"}
}

def breadcrumb_schema(page_title, path):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"}]
    if path != "index.html":
        items.append({"@type": "ListItem", "position": 2, "name": page_title, "item": f"{SITE_URL}/{path}"})
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

def nav_html(current):
    items = []
    for href, label in NAV:
        current_attr = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{current_attr}>{label}</a></li>')
    return "\n        ".join(items)

def header_html(current):
    return f"""  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap">
      <a class="wordmark" href="index.html">Jamil Ahmad</a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
        <span></span>
      </button>
      <nav class="site-nav" id="site-nav" aria-label="Primary">
        <ul>
        {nav_html(current)}
        </ul>
      </nav>
    </div>
  </header>
"""

FOOTER = """  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <h4>Jamil Ahmad</h4>
          <p style="max-width:32ch;">Educator and researcher working on sustainable finance and the political economy of renewable energy.</p>
        </div>
        <div>
          <h4>Navigate</h4>
          <ul>
            <li><a href="about.html">About</a></li>
            <li><a href="research.html">Research</a></li>
            <li><a href="experience.html">Experience</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Elsewhere</h4>
          <ul>
            <li><a href="contact.html#linkedin">LinkedIn — <span class="placeholder">add link</span></a></li>
            <li><a href="content.html#youtube">YouTube — <span class="placeholder">add link</span></a></li>
            <li><a href="contact.html#scholar">Google Scholar — <span class="placeholder">add link</span></a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>Jamil Ahmad — Educator &middot; Researcher &middot; Sustainable Finance &middot; Content Creator</span>
        <span>&copy; 2026 Jamil Ahmad. All rights reserved.</span>
      </div>
    </div>
  </footer>
  <script src="js/main.js"></script>
"""

def page(path, title, description, current, body, extra_schema=None, og_type="website"):
    schemas = [PERSON_SCHEMA, WEBSITE_SCHEMA, breadcrumb_schema(title, path)]
    if extra_schema:
        schemas.append(extra_schema)
    schema_tag = "\n".join(
        f'  <script type="application/ld+json">{json.dumps(s, indent=2)}</script>' for s in schemas
    )
    canonical = f"{SITE_URL}/{path}" if path != "index.html" else f"{SITE_URL}/"
    full_title = title if path == "index.html" else f"{title} | Jamil Ahmad"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full_title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="author" content="Jamil Ahmad">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Jamil Ahmad">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE_URL}/assets/og-image.jpg">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{full_title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{SITE_URL}/assets/og-image.jpg">

  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="css/style.css">
{schema_tag}
</head>
<body>
{header_html(current)}
  <main id="main">
{body}
  </main>
{FOOTER}
</body>
</html>
"""
    with open(os.path.join(OUT, path), "w") as f:
        f.write(html)

print("helpers ready")
