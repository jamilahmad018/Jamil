from build import page

body = """
    <section class="hero">
      <div class="wrap">
        <p class="eyebrow">Swat, Pakistan &rarr; Depok, Indonesia</p>
        <h1>Jamil Ahmad</h1>
        <p class="role-line">Educator, researcher, and sustainable finance professional.</p>
        <p class="lede">I teach at a government primary school in Pakistan, and I study how political stability shapes the renewable energy transition across ASEAN. Before either of those, I spent four years on a bank floor learning how institutions actually work.</p>
        <div class="hero-facts">
          <span class="fact"><strong>2015</strong> &mdash; BBA, University of Swat</span>
          <span class="fact"><strong>2020&ndash;present</strong> &mdash; Primary school teacher</span>
          <span class="fact"><strong>MSF</strong> &mdash; Sustainable Finance, UIII</span>
        </div>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="about.html">About me</a>
          <a class="btn" href="research.html">Explore my research</a>
          <a class="btn btn-quiet" href="experience.html">View my journey &rarr;</a>
        </div>
      </div>
    </section>

    <div class="wrap">
      <section class="ledger" aria-labelledby="who-heading">
        <div class="ledger-meta"><span class="label">Profile</span></div>
        <div class="ledger-body">
          <h2 id="who-heading">A career built one classroom, one branch, and one research question at a time</h2>
          <p>My background sits across three fields that don't usually share a page: primary education, retail banking, and sustainable finance research. I started in a bank, moved into a classroom, and am now finishing a master's degree that asks why some countries manage to grow their renewable energy use even when politics gets shaky. This site is where those threads meet.</p>
          <p><a href="about.html">Read the full story &rarr;</a></p>
        </div>
      </section>

      <section class="ledger" aria-labelledby="snapshot-heading">
        <div class="ledger-meta"><span class="label">Snapshot</span></div>
        <div class="ledger-body">
          <div class="section-title-row">
            <h2 id="snapshot-heading">Where things stand</h2>
          </div>
          <div class="grid-3">
            <div class="card">
              <h3>Education</h3>
              <p>BBA in Human Resource Management from the University of Swat (2015), followed by a Master's in Sustainable Finance at UIII, Indonesia.</p>
              <a href="education.html">See education &rarr;</a>
            </div>
            <div class="card">
              <h3>Experience</h3>
              <p>Government primary school teacher since 2020, four years at Meezan Bank Limited, and an internship at the National Bank of Pakistan.</p>
              <a href="experience.html">See experience &rarr;</a>
            </div>
            <div class="card">
              <h3>Research</h3>
              <p>My thesis studies how political stability affects renewable energy consumption across nine ASEAN countries, 2000&ndash;2023.</p>
              <a href="research.html">See research &rarr;</a>
            </div>
          </div>
        </div>
      </section>

      <section class="ledger" aria-labelledby="research-feature-heading">
        <div class="ledger-meta"><span class="label">Featured</span></div>
        <div class="ledger-body">
          <h2 id="research-feature-heading">Impact of Political Stability on Renewable Energy Consumption</h2>
          <p class="lede">Evidence from ASEAN Countries &mdash; a panel data study covering nine ASEAN economies from 2000 to 2023, examining whether political stability helps or hinders the shift toward renewable energy.</p>
          <p><a class="btn" href="research.html">Read the research overview</a></p>
        </div>
      </section>

      <section class="ledger" aria-labelledby="contact-cta-heading">
        <div class="ledger-meta"><span class="label">Get in touch</span></div>
        <div class="ledger-body">
          <h2 id="contact-cta-heading">Let's connect</h2>
          <p>I'm always glad to hear from other researchers, educators, and people working in sustainable finance.</p>
          <p><a class="btn btn-primary" href="contact.html">Contact me</a></p>
        </div>
      </section>
    </div>
"""

page(
    "index.html",
    "Jamil Ahmad — Educator, Researcher & Sustainable Finance Professional",
    "Jamil Ahmad is a Pakistani educator, researcher, and sustainable finance professional studying political stability and renewable energy across ASEAN.",
    "index.html",
    body,
    og_type="profile",
)
print("home built")
