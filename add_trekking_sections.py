import os

new_sections = """
  <!-- The Art of Trekking -->
  <section class="section">
    <div class="container">
      <div style="display: flex; flex-wrap: wrap; gap: 40px; align-items: center;">
        <div style="flex: 1; min-width: 300px; max-width: 550px;" class="anim-fade-right">
          <img src="images/hero/hero-2.png" alt="The Art of Trekking"
            style="border-radius: 20px; box-shadow: var(--shadow-lg); width: 100%; max-height: 400px; object-fit: cover;">
        </div>
        <div style="flex: 1; min-width: 300px;" class="anim-fade-left">
          <h2 class="section-title">The Art of Trekking</h2>
          <p style="margin-bottom: 20px; color: var(--text-light);">Trekking is more than just walking; it's a profound journey of self-discovery, resilience, and connection with nature. Away from the hustle and bustle of city life, the trails offer a unique opportunity to recharge both mentally and physically.</p>
          <p style="color: var(--text-light); margin-bottom: 30px;">Whether you're traversing a lush forest or conquering a high-altitude peak, every step builds endurance and rewards you with breathtaking panoramas that few get to witness.</p>
          <a href="about.html" class="btn btn-secondary">Learn More</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Trekking Difficulty Levels -->
  <section class="section" style="background: var(--surface-color);">
    <div class="container">
      <div class="text-center anim-fade-up">
        <h2 class="section-title">Trekking Difficulty Levels</h2>
        <p class="section-subtitle">Find the perfect trail that matches your experience and fitness level.</p>
      </div>
      
      <div class="features-grid">
        <!-- Beginner -->
        <div class="feature-item anim-fade-up">
          <i class="fas fa-hiking" style="font-size: 3rem; color: var(--accent-color); margin-bottom: 20px;"></i>
          <h3>Beginner</h3>
          <p style="color: var(--text-light); margin-bottom: 15px;">Ideal for newcomers. Features scenic walks on well-paved trails, typically requiring 2-4 hours of walking per day.</p>
          <span style="font-size: 0.9rem; font-weight: 600; color: var(--primary-color);">Minimal Experience Required</span>
        </div>
        <!-- Intermediate -->
        <div class="feature-item anim-fade-up" style="transition-delay: 0.2s">
          <i class="fas fa-mountain" style="font-size: 3rem; color: var(--accent-color); margin-bottom: 20px;"></i>
          <h3>Intermediate</h3>
          <p style="color: var(--text-light); margin-bottom: 15px;">For the active adventurer. Expect uneven terrain, moderate altitude, and 4-7 hours of hiking daily.</p>
          <span style="font-size: 0.9rem; font-weight: 600; color: var(--primary-color);">Good Fitness Required</span>
        </div>
        <!-- Advanced -->
        <div class="feature-item anim-fade-up" style="transition-delay: 0.4s">
          <i class="fas fa-mountain-sun" style="font-size: 3rem; color: var(--accent-color); margin-bottom: 20px;"></i>
          <h3>Advanced</h3>
          <p style="color: var(--text-light); margin-bottom: 15px;">For experienced trekkers. High altitudes, steep ascents, and multi-day endurance challenges.</p>
          <span style="font-size: 0.9rem; font-weight: 600; color: var(--primary-color);">Excellent Fitness Required</span>
        </div>
      </div>
    </div>
  </section>
"""

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

if "<!-- The Art of Trekking -->" not in index_content:
    index_content = index_content.replace('  <!-- Why Choose Us -->', new_sections + '\n  <!-- Why Choose Us -->')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Updated index.html")

# Update home2.html
with open('home2.html', 'r', encoding='utf-8') as f:
    home2_content = f.read()

if "<!-- The Art of Trekking -->" not in home2_content:
    home2_content = home2_content.replace('  <!-- Featured Destinations -->', new_sections + '\n  <!-- Featured Destinations -->')
    with open('home2.html', 'w', encoding='utf-8') as f:
        f.write(home2_content)
    print("Updated home2.html")
