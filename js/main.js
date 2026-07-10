document.addEventListener('DOMContentLoaded', () => {
  /* --- Page Loader --- */
  const loaderWrapper = document.querySelector('.loader-wrapper');
  if (loaderWrapper) {
    setTimeout(() => {
      loaderWrapper.style.opacity = '0';
      setTimeout(() => {
        loaderWrapper.style.display = 'none';
      }, 500);
    }, 800); // Simulated loading time
  }

  /* --- Sticky Header --- */
  const header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('sticky');
      } else {
        header.classList.remove('sticky');
      }
    });
  }

  /* --- Mobile Menu Toggle --- */
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!navMenu.contains(e.target) && !mobileToggle.contains(e.target) && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
      }
    });
  }

  /* --- Theme Toggle (Dark/Light) --- */
  const themeToggles = document.querySelectorAll('.theme-toggle-btn');
  const body = document.body;
  const currentTheme = localStorage.getItem('theme');

  if (currentTheme) {
    body.classList.add(currentTheme);
    if (currentTheme === 'dark-mode') {
      themeToggles.forEach(btn => {
        btn.innerHTML = '<i class="fas fa-sun"></i>';
      });
    }
  }

  themeToggles.forEach(btn => {
    btn.addEventListener('click', () => {
      body.classList.toggle('dark-mode');
      
      let theme = 'light';
      const isDark = body.classList.contains('dark-mode');
      if (isDark) {
        theme = 'dark-mode';
      }
      
      themeToggles.forEach(toggle => {
        toggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
      });
      
      localStorage.setItem('theme', theme);
    });
  });

  /* --- FAQ Accordion --- */
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const header = item.querySelector('h4');
    if (header) {
      header.addEventListener('click', () => {
        // Toggle current item
        item.classList.toggle('active');
        // Optional: Close other items
        // faqItems.forEach(other => { if (other !== item) other.classList.remove('active'); });
      });
    }
  });

  /* --- RTL Toggle --- */
  const rtlToggles = document.querySelectorAll('.rtl-toggle-btn');
  const htmlEl = document.documentElement;
  const currentDir = localStorage.getItem('direction');

  if (currentDir === 'rtl') {
    htmlEl.setAttribute('dir', 'rtl');
    rtlToggles.forEach(btn => {
      btn.innerText = 'LTR';
    });
  } else {
    htmlEl.setAttribute('dir', 'ltr');
    rtlToggles.forEach(btn => {
      btn.innerText = 'RTL';
    });
  }

  rtlToggles.forEach(btn => {
    btn.addEventListener('click', () => {
      const dir = htmlEl.getAttribute('dir');
      const targetDir = (dir === 'ltr' || !dir) ? 'rtl' : 'ltr';
      htmlEl.setAttribute('dir', targetDir);
      localStorage.setItem('direction', targetDir);
      
      rtlToggles.forEach(toggle => {
        toggle.innerText = targetDir === 'rtl' ? 'LTR' : 'RTL';
      });
    });
  });

  /* --- Back To Top Button --- */
  const backToTop = document.getElementById('back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTop.classList.add('show');
      } else {
        backToTop.classList.remove('show');
      }
    });

    backToTop.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});
