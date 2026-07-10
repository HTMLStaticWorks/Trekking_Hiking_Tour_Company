old_gallery = """      <div class="gallery-grid">
        <div class="gallery-item anim-zoom-in"><img src="images/gallery/gallery_1.png" alt="Gallery"></div>
        <div class="gallery-item anim-zoom-in" style="transition-delay: 0.1s"><img src="images/gallery/gallery_2.png" alt="Gallery"></div>
        <div class="gallery-item anim-zoom-in" style="transition-delay: 0.2s"><img src="images/treks/rocky.png" alt="Gallery"></div>
        <div class="gallery-item anim-zoom-in" style="transition-delay: 0.3s"><img src="images/blog/swiss_alps.png" alt="Gallery"></div>
        <div class="gallery-item anim-zoom-in" style="transition-delay: 0.4s"><img src="images/treks/everest.png" alt="Gallery"></div>
      </div>"""

new_gallery = """      <div class="gallery-grid">
        <div class="gallery-item anim-zoom-in"><img src="images/gallery/gallery_large.png" alt="Hikers above clouds at sunrise"></div>
        <div class="gallery-item anim-zoom-in" style="transition-delay: 0.1s"><img src="images/gallery/gallery_bridge.png" alt="Hiker on suspension bridge in misty forest"></div>
        <div class="gallery-item anim-zoom-in" style="transition-delay: 0.2s"><img src="images/gallery/gallery_tents.png" alt="Glowing tents by glacial lake at night"></div>
        <div class="gallery-item anim-zoom-in" style="transition-delay: 0.3s"><img src="images/gallery/gallery_valley.png" alt="Alpine valley with Matterhorn mountain"></div>
        <div class="gallery-item anim-zoom-in" style="transition-delay: 0.4s"><img src="images/gallery/gallery_snow.png" alt="Mountaineers trekking up snowy glacier"></div>
      </div>"""

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

if old_gallery in content:
    content = content.replace(old_gallery, new_gallery)
    with open('home2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Gallery successfully updated in home2.html")
else:
    print("Could not find the old gallery section in home2.html.")
