import os, glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the two variations
    new_content = content.replace(
        '<a href="signup.html" class="nav-link">Sign Up</a>',
        '<a href="signup.html" class="btn btn-primary">Sign Up</a>'
    )
    new_content = new_content.replace(
        '<a href="signup.html" class="nav-link" style="color: var(--text-color);">Sign Up</a>',
        '<a href="signup.html" class="btn btn-primary">Sign Up</a>'
    )
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
