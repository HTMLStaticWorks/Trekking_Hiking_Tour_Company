with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

cta_block = """  <!-- CTA -->
  <section class="section" style="background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)); color: #FFF; text-align: center;">
    <div class="container anim-zoom-in">
      <h2>Ready For Your Next Adventure?</h2>
      <p style="margin: 20px 0 40px;">Contact us today and let's plan the trip of a lifetime.</p>
      <a href="contact.html" class="btn btn-primary glass-effect">Get In Touch</a>
    </div>
  </section>

"""

if cta_block in content:
    content = content.replace(cta_block, '')
    content = content.replace('  <!-- Footer -->', cta_block + '  <!-- Footer -->')
    with open('home2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Moved CTA block successfully.")
else:
    print("CTA block not found.")
