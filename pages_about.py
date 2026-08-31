from build import page

body = """
    <div class="wrap">
      <section class="ledger">
        <div class="ledger-meta"><span class="label">About</span></div>
        <div class="ledger-body">
          <h1>About Jamil Ahmad</h1>
          <p class="lede">I'm a Pakistani educator, researcher, and sustainable finance professional. My work sits at the intersection of banking, education, and the economics of the energy transition.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Background</span></div>
        <div class="ledger-body">
          <h2>Background</h2>
          <p>I grew up and studied in Swat, Pakistan, and completed my Bachelor of Business Administration at the University of Swat in 2015, majoring in Human Resource Management with a CGPA of 3.50/4.00. From there my path went through banking, teaching, and now graduate research &mdash; three fields that have each shaped how I think about institutions, people, and long-term development.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Banking</span></div>
        <div class="ledger-body">
          <h2>Banking experience</h2>
          <p>I completed a six-month internship at the National Bank of Pakistan, followed by roughly four years at Meezan Bank Limited as a Branch Service Officer. That time gave me a close-up view of how financial institutions operate day to day, and it's part of why questions about financial and organizational sustainability stayed with me afterward.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Teaching</span></div>
        <div class="ledger-body">
          <h2>Teaching career</h2>
          <p>Since 2020, I've worked as a government primary school teacher in Pakistan. Teaching at the primary level keeps me grounded &mdash; it's a daily reminder that education and development work happen at the level of individual people, not just policy.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Graduate study</span></div>
        <div class="ledger-body">
          <h2>Master's in Sustainable Finance</h2>
          <p>I'm currently completing a Master's degree in Sustainable Finance at Universitas Islam Internasional Indonesia (UIII). My thesis examines the impact of political stability on renewable energy consumption across ASEAN countries &mdash; a question that sits right at the intersection of governance and the energy transition. You can read more about it on the <a href="research.html">research page</a>.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Interests</span></div>
        <div class="ledger-body">
          <h2>Research interests</h2>
          <p>Sustainable finance, renewable energy, political stability and its economic impact, sustainable development, green finance, energy transition, and organizational and financial sustainability.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Beyond work</span></div>
        <div class="ledger-body">
          <h2>Entrepreneurship, content, and personal interests</h2>
          <p>Outside of teaching and research, I'm interested in entrepreneurship, digital skills, online earning, content creation, and music production. I also enjoy travel and am generally curious about personal development. These interests will get their own space on the <a href="content.html">content &amp; media</a> and <a href="projects.html">projects</a> pages as they take shape.</p>
        </div>
      </section>
    </div>
"""

page(
    "about.html",
    "About",
    "About Jamil Ahmad — Pakistani educator, researcher, and sustainable finance professional with a background in banking and primary education.",
    "about.html",
    body,
)
print("about built")
