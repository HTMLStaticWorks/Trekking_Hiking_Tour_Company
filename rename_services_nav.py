import glob

files = glob.glob('*.html')
for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    changed = False
    
    for line in lines:
        if 'href="services.html"' in line and 'nav-link' in line and '>Services</a>' in line:
            new_lines.append(line.replace('>Services</a>', '>Expeditions</a>'))
            changed = True
        else:
            new_lines.append(line)
            
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f"Updated header navigation in {file_path}")
