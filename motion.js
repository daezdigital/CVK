/**
 * CVK Landscape — motion.js
 * Awwwards-level Motion Design: Lenis, GSAP ScrollTrigger, Custom Cursor, Magnetic Buttons
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Initialize Lenis (Smooth Scroll)
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
    mouseMultiplier: 1,
    smoothTouch: false,
    touchMultiplier: 2,
    infinite: false,
  });

  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  // Sync GSAP ScrollTrigger with Lenis
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
    
    lenis.on('scroll', ScrollTrigger.update);
    
    gsap.ticker.add((time) => {
      lenis.raf(time * 1000);
    });
    
    gsap.ticker.lagSmoothing(0);
  }

  // 2. Custom Cursor
  const cursor = document.getElementById('custom-cursor');
  if (cursor && typeof gsap !== 'undefined') {
    // Hide default cursor globally on desktop
    document.body.classList.add('has-custom-cursor');

    // Use GSAP quickTo for performant follow with lerp
    let xTo = gsap.quickTo(cursor, "x", { duration: 0.2, ease: "power3" });
    let yTo = gsap.quickTo(cursor, "y", { duration: 0.2, ease: "power3" });

    window.addEventListener("mousemove", (e) => {
      xTo(e.clientX);
      yTo(e.clientY);
      
      // Ensure cursor is visible once mouse moves
      if (cursor.style.opacity === '0' || cursor.style.opacity === '') {
        gsap.to(cursor, { opacity: 1, duration: 0.3 });
      }
    });

    // Hover effects for links, buttons, and interactive elements
    const hoverables = document.querySelectorAll('a, button, .hacc-panel, .portfolio-item-large, .service-card');
    
    hoverables.forEach(el => {
      el.addEventListener('mouseenter', () => {
        cursor.classList.add('cursor-hover');
      });
      el.addEventListener('mouseleave', () => {
        cursor.classList.remove('cursor-hover');
      });
    });
  }

  // 3. Magnetic Buttons (Emil Kowalski style)
  const magneticButtons = document.querySelectorAll('.btn');
  
  magneticButtons.forEach(btn => {
    // Only apply on non-touch devices
    if(window.matchMedia("(hover: hover)").matches && typeof gsap !== 'undefined') {
      btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;
        
        // Calculate distance from center
        const distX = e.clientX - centerX;
        const distY = e.clientY - centerY;
        
        // Move button towards cursor (subtle magnetic pull)
        gsap.to(btn, {
          x: distX * 0.2,
          y: distY * 0.2,
          duration: 0.6,
          ease: "power3.out"
        });
      });
      
      btn.addEventListener('mouseleave', () => {
        // Snap back to original position
        gsap.to(btn, {
          x: 0,
          y: 0,
          duration: 1,
          ease: "elastic.out(1, 0.3)" // Spring effect on release
        });
      });
    }
  });

  // 4. Parallax Images
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    const parallaxImages = document.querySelectorAll('.parallax-img, .service-detail-image img, .about-image-frame img, .hero-bg-image');
    
    parallaxImages.forEach(img => {
      // Ensure parent has overflow hidden
      if (img.parentElement) {
        img.parentElement.style.overflow = 'hidden';
      }
      
      // Initial scale
      gsap.set(img, { scale: 1.15 });
      
      gsap.to(img, {
        yPercent: 15,
        ease: "none",
        scrollTrigger: {
          trigger: img.parentElement,
          start: "top bottom", // when top of element hits bottom of viewport
          end: "bottom top",   // when bottom of element hits top of viewport
          scrub: true
        }
      });
    });

    // 5. Scroll-driven Text Reveals (Staggered)
    const revealElements = document.querySelectorAll('.reveal-clip-up, .reveal-fade, .service-card, .approach-item, .approach-stats, .about-image-frame');
    
    revealElements.forEach(el => {
      // Reset CSS properties that might conflict
      el.style.opacity = '0';
      el.style.animation = 'none';
      
      let startX = 0;
      let startY = 40;
      
      if (el.classList.contains('reveal-clip-left')) startX = -40;
      if (el.classList.contains('reveal-clip-right')) startX = 40;
      if (startX !== 0) startY = 0;
      
      gsap.fromTo(el, 
        { opacity: 0, y: startY, x: startX },
        {
          opacity: 1, 
          y: 0,
          x: 0,
          duration: 1,
          ease: "power3.out",
          scrollTrigger: {
            trigger: el,
            start: "top 85%", // Trigger slightly before it comes into view
            toggleActions: "play none none reverse"
          }
        }
      );
    });
  }

  // 6. Contact Form Handling
  const leadForm = document.getElementById('cvk-lead-form');
  const statusMsg = document.getElementById('form-status-message');

  if (leadForm && statusMsg) {
    leadForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const submitBtn = leadForm.querySelector('#submit-btn');
      const originalBtnText = submitBtn.textContent;
      
      // Visual feedback
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending...';
      
      // Simulate API Call
      setTimeout(() => {
        statusMsg.textContent = 'Thank you! Your request has been sent. We will contact you shortly.';
        statusMsg.className = 'success'; // See CSS for styling
        statusMsg.classList.remove('hidden');
        
        // Reset form
        leadForm.reset();
        submitBtn.disabled = false;
        submitBtn.textContent = originalBtnText;
        
        // Hide message after 5 seconds
        setTimeout(() => {
          statusMsg.classList.add('hidden');
        }, 5000);
      }, 1500);
    });
  }
});
