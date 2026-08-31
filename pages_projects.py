from build import page

body = """
    <div class="wrap">
      <section class="ledger">
        <div class="ledger-meta"><span class="label">Projects</span></div>
        <div class="ledger-body">
          <h1>Projects</h1>
          <p class="lede">A home for business, research, digital, and creative projects as they come together. This section is intentionally open right now &mdash; it will fill in over time.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Categories</span></div>
        <div class="ledger-body">
          <div class="grid-2">
            <div class="card"><h3>Business projects</h3><p>Entrepreneurial ventures and business initiatives.</p><span class="placeholder">to be added</span></div>
            <div class="card"><h3>Digital projects</h3><p>Digital skills, tools, and online work.</p><span class="placeholder">to be added</span></div>
            <div class="card"><h3>Research projects</h3><p>Work connected to sustainable finance and energy research beyond the thesis.</p><span class="placeholder">to be added</span></div>
            <div class="card"><h3>Content &amp; creative projects</h3><p>Video, music, and other creative work.</p><span class="placeholder">to be added</span></div>
          </div>
        </div>
      </section>
    </div>
"""

page(
    "projects.html",
    "Projects",
    "An evolving collection of business, research, digital, and creative projects by Jamil Ahmad.",
    "projects.html",
    body,
)
print("projects built")
