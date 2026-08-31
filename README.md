# Jamil Ahmad — personal website

A static, no-build personal brand site: plain HTML, CSS, and a few lines of
JavaScript. No paid services required, no server needed. Every page is a
self-contained `.html` file, so you can open any one of them, edit the text,
and save — no build step required to make a content change.

## What's in this folder

```
index.html         Home
about.html          About
education.html      Education
experience.html     Experience
research.html       Research (your thesis)
projects.html       Projects
content.html        Content & Media (YouTube, TikTok, Instagram links)
blog.html           Blog (sample/draft titles only — no real posts yet)
contact.html        Contact form + direct links
css/style.css        All styling
js/main.js           Mobile menu toggle — the only JS on the site
assets/              Put your photo, thesis PDF, and social preview image here
sitemap.xml           For search engines
robots.txt             For search engines
build.py, pages_*.py   The generator scripts that produced the HTML (optional — see below)
```

Every page includes SEO metadata (title, description, canonical URL, Open
Graph tags, Twitter card tags) and Schema.org structured data (`Person`,
`WebSite`, `BreadcrumbList`, and a `ScholarlyArticle` on the research page)
so search engines can understand who you are and connect all the pages to
the same identity.

Every placeholder — missing links, your photo, your thesis PDF, unfinished
sections — is marked with a small dashed tag that says things like
`add link` or `add thesis PDF`, so you can find them by searching the files
for the word `placeholder`.

## Two ways to edit content

**Easiest: edit the HTML directly.** Open any `.html` file in a text editor,
find the text you want to change, and edit it. The header, footer, and
navigation are duplicated at the top/bottom of every file — if you change
one (e.g. adding a real LinkedIn link), repeat that same change in the
other eight files, or use your editor's "find in all files" feature.

**Optional: regenerate from the Python scripts.** `build.py` holds the
shared header/footer/SEO template, and each `pages_*.py` file holds one
page's content. If you're comfortable with a little Python, edit the
relevant `pages_*.py` file and run it (e.g. `python3 pages_about.py`) to
regenerate that one HTML file — this keeps the header/footer/SEO tags
consistent everywhere automatically. This is entirely optional; you never
need Python to run or host the site.

## Step-by-step: publish it for free with GitHub Pages

You don't need to know how to code to do this part.

1. **Create a GitHub account** at github.com if you don't have one.
2. **Create a new repository.** Click the "+" in the top right → "New
   repository". Name it `jamil-ahmad-website` (or anything you like). Set
   it to Public. Don't add a README, .gitignore, or license — you already
   have these files.
3. **Upload your files.** On the new repository's page, click
   "uploading an existing file" and drag in every file and folder from
   this project (`index.html`, `about.html`, `css/`, `js/`, `assets/`,
   `sitemap.xml`, `robots.txt`, everything). Commit the changes.
4. **Turn on GitHub Pages.** In your repository, go to Settings → Pages.
   Under "Build and deployment", set Source to "Deploy from a branch",
   choose the `main` branch and the `/ (root)` folder, then click Save.
5. **Wait a minute or two.** GitHub will give you a live URL that looks
   like `https://your-username.github.io/jamil-ahmad-website/`. Visit it
   to confirm the site works.
6. **Fill in the placeholders.** Add your real email, LinkedIn, YouTube,
   and other links by editing the relevant HTML files (search for
   `placeholder`), then upload the updated files again (GitHub will let
   you overwrite them, or you can use GitHub Desktop for easier repeat
   uploads).

That's it — the site is live and free, with no hosting bill, ever.

### Making the contact form actually send you email

The contact form in `contact.html` currently points to a placeholder
(`https://formspree.io/f/YOUR_FORM_ID`). Formspree has a free tier that
works with static sites like this one:

1. Go to formspree.io and create a free account.
2. Create a new form and copy the form ID it gives you.
3. In `contact.html`, replace `YOUR_FORM_ID` in the `<form action="...">`
   line with your real ID.

## Connecting a custom domain later (e.g. jamilahmad.com)

Nothing about the site's structure needs to change to add a custom domain
— GitHub Pages supports this directly, for free:

1. Buy the domain from any registrar (Namecheap, GoDaddy, Google Domains,
   etc. — this is the only part of this whole project that typically
   costs money).
2. In your registrar's DNS settings, add the four GitHub Pages A records
   pointing `jamilahmad.com` to GitHub's IP addresses, and a CNAME record
   pointing `www.jamilahmad.com` to `your-username.github.io`. GitHub's
   own Pages documentation lists the current IP addresses to use.
3. In your repository, go to Settings → Pages → Custom domain, and enter
   `jamilahmad.com`. GitHub will create a `CNAME` file in your repo
   automatically and issue a free HTTPS certificate for you.
4. **Update the placeholder URLs.** Every canonical link, Open Graph tag,
   and the `sitemap.xml` / `robots.txt` files currently use a placeholder
   address: `https://jamilahmad.example`. Once your real domain is live,
   do a find-and-replace of `https://jamilahmad.example` with
   `https://jamilahmad.com` across every `.html` file and in
   `sitemap.xml` / `robots.txt` (or, if using the Python scripts, update
   the `SITE_URL` variable at the top of `build.py` and re-run each
   `pages_*.py` file).
5. Resubmit your sitemap in Google Search Console under the new domain so
   Google recrawls it correctly.

## SEO next steps once the site is live

- Submit the site to **Google Search Console** and **Bing Webmaster
  Tools**, and submit `sitemap.xml` in both.
- Add your real photo and a 1200×630px social preview image at
  `assets/profile-photo.jpg` and `assets/og-image.jpg` (see
  `assets/README-assets.txt`).
- As you add real LinkedIn, Google Scholar, YouTube, etc. links, also add
  them to the `sameAs` array in the `Person` schema inside `build.py` (or
  directly in each HTML file's `<script type="application/ld+json">`
  block) — this is one of the strongest signals for Google to associate
  all your profiles with the same person.
- Once your thesis is finished, add the real abstract and PDF on
  `research.html` in place of the placeholders.

## What was deliberately left out

Per the brief, nothing on this site invents job titles, dates, awards,
publications, or credentials beyond what was provided. Anywhere
information wasn't available, you'll find a clearly marked placeholder
instead of a guess.
