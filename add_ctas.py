import re

with open('packages.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the price paragraph: <p class="trek-price">$299</p>
# and replace it with a flex container holding the price and a Book Now button.
# Since the price varies, we use a regex.

pattern = re.compile(r'<p class="trek-price">(\$[0-9,]+)</p>')

replacement = r'''<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
              <p class="trek-price" style="margin: 0;">\1</p>
              <a href="contact.html" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.9rem; border-radius: 30px;">Book Now</a>
            </div>'''

new_content = pattern.sub(replacement, content)

if new_content != content:
    with open('packages.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully added 'Book Now' CTAs to packages.html")
else:
    print("No changes made. Price tags might not match the pattern.")
