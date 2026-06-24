import os
import glob

def update_logos():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Define replacements
        # Normal logo in header
        content = content.replace('>Trek<span>X</span></a>', '><img src="images/favicon.svg" alt="TrekX Logo" class="brand-icon">Trek<span>X</span></a>')
        
        # Logo in div (login/signup)
        content = content.replace('>Trek<span style="color: var(--accent-color);">X</span></div>', '><img src="images/favicon.svg" alt="TrekX Logo" class="brand-icon">Trek<span style="color: var(--accent-color);">X</span></div>')

        # Since the replace might match already replaced content if we run it twice, we should be careful,
        # but since we're only running it once, it's fine.

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    update_logos()
    print("Logos updated in HTML files.")
