old_section = """  <!-- Latest Blog Section -->
  <section class="section">
    <div class="container">
      <div class="text-center anim-fade-up">
        <h2 class="section-title">Latest Adventure News</h2>
      </div>
      <div class="blog-grid">
        <div class="blog-card anim-fade-right">
          <img src="images/blog/winter_gear.jpg" alt="Blog post thumbnail">
          <span style="color: var(--accent-color); font-weight: 600; font-size: 0.9rem;">July 10, 2026</span>
          <h3 style="margin: 10px 0;">Essential Gear for Winter Treks</h3>
          <p style="color: var(--text-light); margin-bottom: 15px;">Don't let the cold stop you. Here is the ultimate packing list to stay warm and safe during your snowy expeditions.</p>
          <a href="#" style="color: var(--primary-color); font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
        </div>
        <div class="blog-card anim-fade-left">
          <img src="images/blog/hiking_boots.jpg" alt="Blog post thumbnail">
          <span style="color: var(--accent-color); font-weight: 600; font-size: 0.9rem;">July 02, 2026</span>
          <h3 style="margin: 10px 0;">The Best Hiking Boots of 2026</h3>
          <p style="color: var(--text-light); margin-bottom: 15px;">We tested over 50 pairs of boots across various terrains. Find out which ones offer the best comfort and durability.</p>
          <a href="#" style="color: var(--primary-color); font-weight: 600;">Read More <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
    </div>
  </section>"""

new_section = """  <!-- Testimonials Section -->
  <section class="section">
    <div class="container">
      <div class="text-center anim-fade-up">
        <h2 class="section-title">What Our Trekkers Say</h2>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
        <div class="premium-card anim-fade-right" style="padding: 30px; text-align: left;">
          <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <img src="https://i.pinimg.com/236x/8b/1e/8f/8b1e8f2378f8c7e937d57076a08990d0.jpg" alt="Emma Stone" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
            <div>
              <h3 style="margin: 0; font-size: 1.1rem;">Emma Stone</h3>
              <div style="color: #FFD700; font-size: 0.9rem; margin-top: 5px;">
                <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
              </div>
            </div>
          </div>
          <p style="color: var(--text-light); font-style: italic; line-height: 1.6;">"The Swiss Alps trek was truly life-changing. The guides were incredibly knowledgeable, the accommodations were top-notch, and the views were out of this world. Highly recommend TrekX!"</p>
        </div>
        <div class="premium-card anim-fade-left" style="padding: 30px; text-align: left;">
          <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <img src="https://i.pinimg.com/236x/a2/e8/cf/a2e8cf38c1142e05b63bc3a65249fc2d.jpg" alt="Michael Chen" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
            <div>
              <h3 style="margin: 0; font-size: 1.1rem;">Michael Chen</h3>
              <div style="color: #FFD700; font-size: 0.9rem; margin-top: 5px;">
                <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
              </div>
            </div>
          </div>
          <p style="color: var(--text-light); font-style: italic; line-height: 1.6;">"From the equipment provided to the meals on the mountain, everything was premium. They made climbing Everest Base Camp feel incredibly safe and surprisingly luxurious."</p>
        </div>
      </div>
    </div>
  </section>"""

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

if old_section in content:
    content = content.replace(old_section, new_section)
    with open('home2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Testimonials section successfully added to home2.html")
else:
    print("Could not find the old section in home2.html.")
