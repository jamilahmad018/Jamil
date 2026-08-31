from build import page

body = """
    <div class="wrap">
      <section class="ledger">
        <div class="ledger-meta"><span class="label">Education</span></div>
        <div class="ledger-body">
          <h1>Education</h1>
          <p class="lede">Two degrees, five years apart, that trace a path from human resource management to sustainable finance.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="num mono">01</span><span class="label">2015</span></div>
        <div class="ledger-body">
          <div class="timeline-item">
            <span class="period mono">Graduated 2015</span>
            <h3>Bachelor of Business Administration</h3>
            <span class="org">University of Swat &mdash; Major: Human Resource Management &mdash; CGPA 3.50/4.00</span>
            <p>My undergraduate degree focused on human resource management, giving me a foundation in organizational behavior and management that carried through into my banking and teaching work.</p>
          </div>

          <div class="timeline-item">
            <span class="period mono">In progress</span>
            <h3>Master of Sustainable Finance</h3>
            <span class="org">Universitas Islam Internasional Indonesia (UIII)</span>
            <p>My graduate studies focus on sustainable finance, with a thesis examining the impact of political stability on renewable energy consumption across ASEAN countries. Full details are on the <a href="research.html">research page</a>.</p>
            <div class="placeholder-block">Placeholders: degree certificate, transcript highlights, course list, and thesis PDF will be added here once available.</div>
          </div>
        </div>
      </section>
    </div>
"""

page(
    "education.html",
    "Education",
    "Jamil Ahmad's education: a BBA in Human Resource Management from the University of Swat and a Master's in Sustainable Finance from UIII.",
    "education.html",
    body,
)
print("education built")
