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
  const themeToggle = document.getElementById('theme-toggle');
  const body = document.body;
  const currentTheme = localStorage.getItem('theme');

  if (currentTheme) {
    body.classList.add(currentTheme);
    if (themeToggle && currentTheme === 'dark-mode') {
      themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      body.classList.toggle('dark-mode');
      
      let theme = 'light';
      if (body.classList.contains('dark-mode')) {
        theme = 'dark-mode';
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
      } else {
        themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
      }
      
      localStorage.setItem('theme', theme);
    });
  }

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
  const rtlToggle = document.getElementById('rtl-toggle');
  const htmlEl = document.documentElement;
  const currentDir = localStorage.getItem('direction');

  if (currentDir === 'rtl') {
    htmlEl.setAttribute('dir', 'rtl');
    if (rtlToggle) rtlToggle.innerText = 'LTR';
  } else {
    htmlEl.setAttribute('dir', 'ltr');
    if (rtlToggle) rtlToggle.innerText = 'RTL';
  }

  if (rtlToggle) {
    rtlToggle.addEventListener('click', () => {
      const dir = htmlEl.getAttribute('dir');
      if (dir === 'ltr' || !dir) {
        htmlEl.setAttribute('dir', 'rtl');
        localStorage.setItem('direction', 'rtl');
        rtlToggle.innerText = 'LTR';
      } else {
        htmlEl.setAttribute('dir', 'ltr');
        localStorage.setItem('direction', 'ltr');
        rtlToggle.innerText = 'RTL';
      }
    });
  }

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
