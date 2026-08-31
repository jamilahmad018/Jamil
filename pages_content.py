from build import page

body = """
    <div class="wrap">
      <section class="ledger">
        <div class="ledger-meta"><span class="label">Content &amp; Media</span></div>
        <div class="ledger-body">
          <h1>Content &amp; Media</h1>
          <p class="lede">I create digital content around short-form video, travel, music production, and educational topics. This page will link out to that work as channels go live.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Channels</span></div>
        <div class="ledger-body">
          <h2>Channels &amp; profiles</h2>
          <ul class="link-list">
            <li id="youtube"><span>YouTube</span><span class="placeholder">add link</span></li>
            <li><span>TikTok</span><span class="placeholder">add link</span></li>
            <li><span>Instagram</span><span class="placeholder">add link</span></li>
          </ul>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Focus areas</span></div>
        <div class="ledger-body">
          <h2>What I make content about</h2>
          <div class="grid-2">
            <div class="card"><h3>Educational &amp; informational</h3><p>Short explainers connected to my teaching and research background.</p></div>
            <div class="card"><h3>Travel</h3><p>Content from my travels, including my move to Indonesia for graduate school.</p></div>
            <div class="card"><h3>Music production</h3><p>An ongoing personal interest I'm developing alongside everything else.</p></div>
            <div class="card"><h3>Short-form video</h3><p>Quick-format content across platforms as channels come online.</p></div>
          </div>
        </div>
      </section>
    </div>
"""

page(
    "content.html",
    "Content & Media",
    "Jamil Ahmad's digital content: short-form video, travel, music production, and educational content, with links to his channels as they launch.",
    "content.html",
    body,
)
print("content built")
