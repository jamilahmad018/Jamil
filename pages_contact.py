from build import page

body = """
    <div class="wrap">
      <section class="ledger">
        <div class="ledger-meta"><span class="label">Contact</span></div>
        <div class="ledger-body">
          <h1>Get in touch</h1>
          <p class="lede">I'm glad to hear from other researchers, educators, and people working in sustainable finance and banking.</p>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Direct</span></div>
        <div class="ledger-body">
          <h2>Direct contact</h2>
          <ul class="link-list">
            <li><span>Email</span><span class="placeholder">add professional email</span></li>
            <li id="linkedin"><span>LinkedIn</span><span class="placeholder">add link</span></li>
            <li id="scholar"><span>Google Scholar</span><span class="placeholder">add link</span></li>
            <li><span>ResearchGate</span><span class="placeholder">add link</span></li>
            <li><span>ORCID</span><span class="placeholder">add link</span></li>
            <li><span>Facebook</span><span class="placeholder">add link</span></li>
          </ul>
        </div>
      </section>

      <section class="ledger">
        <div class="ledger-meta"><span class="label">Message</span></div>
        <div class="ledger-body">
          <h2>Send a message</h2>
          <p class="form-note">This form is a front-end placeholder. To make it work for free, connect it to a service like Formspree or Getform (see the README) &mdash; no backend hosting required.</p>
          <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
            <div class="form-field">
              <label for="name">Name</label>
              <input type="text" id="name" name="name" required>
            </div>
            <div class="form-field">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" required>
            </div>
            <div class="form-field">
              <label for="message">Message</label>
              <textarea id="message" name="message" required></textarea>
            </div>
            <button class="btn btn-primary" type="submit">Send message</button>
          </form>
        </div>
      </section>
    </div>
"""

page(
    "contact.html",
    "Contact",
    "Get in touch with Jamil Ahmad — educator, researcher, and sustainable finance professional.",
    "contact.html",
    body,
)
print("contact built")
