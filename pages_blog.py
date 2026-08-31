from build import page

drafts = [
    ("What political stability actually means for a country's energy transition", "Sustainable finance"),
    ("Notes from four years on a bank branch floor", "Career"),
    ("Teaching primary school while finishing a Master's thesis", "Education"),
    ("Reading the World Governance Indicators for the first time", "Research methods"),
    ("Moving from Swat to Depok for graduate school", "Travel"),
    ("What green finance means outside the headlines", "Sustainable finance"),
]

cards = "\n".join(f"""            <div class="card">
              <span class="tag-draft">Draft &mdash; sample title</span>
              <h3 style="margin-top:0.6rem;">{title}</h3>
              <p>{cat}</p>
            </div>""" for title, cat in drafts)

body = f"""
    <div class="wrap">
      <section class="ledger">
        <div class="ledger-meta"><span class="label">Blog</span></div>
        <div class="ledger-body">
          <h1>Blog</h1>
          <p class="lede">Future writing on sustainable finance, renewable energy, education, career development, entrepreneurship, digital skills, personal development, travel, and technology.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Sample titles</span></div>
        <div class="ledger-body">
          <p>The titles below are placeholders to show how the blog will be organized once real articles are published &mdash; none of these are live posts yet.</p>
          <div class="grid-3">
{cards}
          </div>
        </div>
      </section>
    </div>
"""

page(
    "blog.html",
    "Blog",
    "Jamil Ahmad's blog on sustainable finance, renewable energy, education, and career development — coming soon.",
    "blog.html",
    body,
)
print("blog built")
