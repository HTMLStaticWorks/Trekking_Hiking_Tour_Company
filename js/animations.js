document.addEventListener('DOMContentLoaded', () => {
  /* --- Scroll Reveal Animations (AOS-like) --- */
  const animationElements = document.querySelectorAll('.anim-fade-up, .anim-fade-left, .anim-fade-right, .anim-zoom-in');

  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const animationObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('anim-active');
        // Optional: Stop observing once animated if we only want it to animate once
        // observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  animationElements.forEach(el => {
    animationObserver.observe(el);
  });

  /* --- Animated Counters --- */
  const counters = document.querySelectorAll('.counter-num');
  
  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = +entry.target.getAttribute('data-target');
        const duration = 2000; // ms
        const increment = target / (duration / 16); // 60fps
        let current = 0;

        const updateCounter = () => {
          current += increment;
          if (current < target) {
            entry.target.innerText = Math.ceil(current);
            requestAnimationFrame(updateCounter);
          } else {
            entry.target.innerText = target;
          }
        };

        updateCounter();
        observer.unobserve(entry.target); // Animate only once
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => {
    counterObserver.observe(counter);
  });

  /* --- Parallax Effect Helper --- */
  const parallaxElements = document.querySelectorAll('.parallax');
  window.addEventListener('scroll', () => {
    let scrollY = window.scrollY;
    parallaxElements.forEach(el => {
      let speed = el.getAttribute('data-speed') || 0.4;
      el.style.backgroundPosition = `center ${scrollY * speed}px`;
    });
  });
});
