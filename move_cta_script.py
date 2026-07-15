import glob, re

files = ['services.html', 'packages.html', 'index.html', 'home2.html', 'gallery.html', 'destinations.html', 'contact.html', 'about.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    cta_pattern = re.compile(r'[ \t]*<a href="signup\.html" class="btn btn-primary">Sign Up</a>\n')
    match = cta_pattern.search(content)
    if not match:
        print(f"CTA not found in {file}")
        continue
        
    cta_str = match.group(0)
    content = content.replace(cta_str, '')
    
    rtl_pattern = re.compile(r'([ \t]*<button class="icon-btn rtl-toggle-btn" id="rtl-toggle".*?>RTL</button>\n)')
    content, n = rtl_pattern.subn(lambda m: m.group(1) + cta_str, content)
    
    if n > 0:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"RTL button not found in {file}")
