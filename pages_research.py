from build import page
import json

thesis_schema = {
    "@context": "https://schema.org",
    "@type": "ScholarlyArticle",
    "headline": "Impact of Political Stability on Renewable Energy Consumption: Evidence from ASEAN Countries",
    "author": {"@type": "Person", "name": "Jamil Ahmad"},
    "about": ["Sustainable Finance", "Renewable Energy", "Political Stability", "ASEAN"],
    "isPartOf": {
        "@type": "CollegeOrUniversity",
        "name": "Universitas Islam Internasional Indonesia (UIII)"
    }
}

body = """
    <div class="wrap">
      <section class="ledger">
        <div class="ledger-meta"><span class="label">Research</span></div>
        <div class="ledger-body">
          <h1>Impact of Political Stability on Renewable Energy Consumption</h1>
          <p class="lede">Evidence from ASEAN Countries &mdash; my Master's thesis at Universitas Islam Internasional Indonesia (UIII), studying whether political stability helps or hinders the shift toward renewable energy in Southeast Asia.</p>
          <div class="stat-strip">
            <div class="stat"><span class="value mono">9</span><span class="label">ASEAN countries</span></div>
            <div class="stat"><span class="value mono">2000&ndash;2023</span><span class="label">Study period</span></div>
            <div class="stat"><span class="value mono">RE&nbsp;GLS</span><span class="label">Estimation method</span></div>
            <div class="stat"><span class="value mono">&minus;3.799</span><span class="label">Political stability coefficient</span></div>
          </div>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Question</span></div>
        <div class="ledger-body">
          <h2>Research question</h2>
          <p>Does political stability increase or decrease the share of renewable energy in a country's total final energy consumption? The thesis tests this across nine ASEAN countries (ASEAN-9) over 2000&ndash;2023, alongside a set of economic control variables.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Framework</span></div>
        <div class="ledger-body">
          <h2>Theoretical grounding</h2>
          <p>The study is grounded in Institutional Theory, Sustainable Development Theory, and Energy Transition Theory &mdash; three lenses for understanding how governance quality interacts with a country's energy choices.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="num mono">01</span><span class="label">Method</span></div>
        <div class="ledger-body">
          <h2>Methodology</h2>
          <div class="timeline-item">
            <h3>Variables</h3>
            <p><strong>Dependent variable:</strong> Renewable Energy Consumption (REC), measured as renewable energy's share of total final energy consumption.<br>
            <strong>Focal independent variable:</strong> Political Stability (PS), drawn from the World Governance Indicators (WGI).<br>
            <strong>Control variables:</strong> log-transformed GDP per capita (with a quadratic term to capture a possible U-shaped relationship), foreign direct investment (FDI), trade openness, and inflation.</p>
          </div>
          <div class="timeline-item">
            <h3>Sample &amp; data</h3>
            <p>Panel data for nine ASEAN countries (ASEAN-9) from 2000 to 2023.</p>
          </div>
          <div class="timeline-item">
            <h3>Estimation</h3>
            <p>Random Effects GLS regression with cluster-robust standard errors, estimated in Stata. A Hausman test (&chi;&sup2; = 2.12, p = 0.833) supported the choice of the Random Effects model over Fixed Effects.</p>
          </div>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Findings</span></div>
        <div class="ledger-body">
          <h2>Results &amp; findings</h2>
          <p>Political stability showed a statistically significant <strong>negative</strong> relationship with renewable energy consumption (&beta; = &minus;3.799). FDI, trade openness, and inflation were not statistically significant in the model. The added quadratic GDP-per-capita term points to a U-shaped relationship between income and renewable energy consumption, with an estimated turning point around USD&nbsp;39,500 per capita.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Implications</span></div>
        <div class="ledger-body">
          <h2>Implications</h2>
          <p>A negative relationship between political stability and renewable energy consumption is counter-intuitive at first glance, and the thesis discusses possible explanations rooted in institutional theory &mdash; for instance, how stable governments may prioritize established energy infrastructure over transition investment in the short term. A fuller discussion, along with policy implications, will be added here as the thesis is finalized.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Materials</span></div>
        <div class="ledger-body">
          <h2>Downloadable materials</h2>
          <div class="grid-3">
            <div class="card"><h3>Abstract</h3><p>500-word abstract.</p><span class="placeholder">add abstract</span></div>
            <div class="card"><h3>Full thesis (PDF)</h3><p>Complete thesis document.</p><span class="placeholder">add thesis PDF</span></div>
            <div class="card"><h3>Dataset</h3><p>Panel data and Stata outputs.</p><span class="placeholder">add data</span></div>
          </div>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Interests</span></div>
        <div class="ledger-body">
          <h2>Research interests</h2>
          <p>Sustainable finance, renewable energy, green finance, energy transition, sustainable development, political economy, and financial sustainability &mdash; with a sustained interest in how governance and political economy intersect with Southeast Asia's energy transition.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">What's next</span></div>
        <div class="ledger-body">
          <h2>Future research</h2>
          <p>I'm interested in extending this line of work to other regions and to firm-level sustainable finance questions. More specific plans and citation details will be added here as the thesis is finalized and published.</p>
        </div>
      </section>
    </div>
"""

page(
    "research.html",
    "Research",
    "Jamil Ahmad's Master's thesis: Impact of Political Stability on Renewable Energy Consumption — Evidence from ASEAN Countries, a panel data study of nine ASEAN economies, 2000–2023.",
    "research.html",
    body,
    extra_schema=thesis_schema,
    og_type="article",
)
print("research built")
