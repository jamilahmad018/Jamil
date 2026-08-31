from build import page

body = """
    <div class="wrap">
      <section class="ledger">
        <div class="ledger-meta"><span class="label">Experience</span></div>
        <div class="ledger-body">
          <h1>Experience</h1>
          <p class="lede">Three roles, three very different environments &mdash; a classroom, a bank branch, and now a research desk.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="num mono">01</span><span class="label">Since 2020</span></div>
        <div class="ledger-body">
          <div class="timeline-item">
            <span class="period mono">2020 &mdash; present</span>
            <h3>Government Primary School Teacher</h3>
            <span class="org">Pakistan</span>
            <p>I've been teaching at the primary level in Pakistan's government school system since 2020, working directly with young students on foundational education.</p>
          </div>

          <div class="timeline-item">
            <span class="period mono">Approx. 4 years</span>
            <h3>Branch Service Officer</h3>
            <span class="org">Meezan Bank Limited</span>
            <p>I spent about four years at Meezan Bank Limited as a Branch Service Officer, handling day-to-day branch operations and customer service.</p>
          </div>

          <div class="timeline-item">
            <span class="period mono">6 months</span>
            <h3>Internship</h3>
            <span class="org">National Bank of Pakistan</span>
            <p>A six-month internship at the National Bank of Pakistan gave me my first close look at the banking sector before I moved into a full-time branch role.</p>
          </div>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Entrepreneurial</span></div>
        <div class="ledger-body">
          <h2>Business &amp; entrepreneurial activities</h2>
          <p>Alongside teaching and research, I'm interested in entrepreneurship and business activities, including digital skills and online earning. Details on specific ventures will be added here as they're ready to share.</p>
          <div class="placeholder-block">Placeholder: specific business/entrepreneurial projects to be added.</div>
        </div>
      </section>
    </div>
"""

page(
    "experience.html",
    "Experience",
    "Jamil Ahmad's professional experience: government primary school teacher since 2020, four years at Meezan Bank Limited, and an internship at the National Bank of Pakistan.",
    "experience.html",
    body,
)
print("experience built")
