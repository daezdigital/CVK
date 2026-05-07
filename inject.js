const fs = require('fs');
const files = ['index.html', 'services.html', 'portfolio.html', 'about.html', 'contact.html'];

const injection = `
  <!-- Custom Cursor -->
  <div id="custom-cursor"></div>
  
  <!-- Awwwards Motion Dependencies -->
  <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.19/bundled/lenis.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="motion.js"></script>
</body>`;

files.forEach(file => {
  if (fs.existsSync(file)) {
    let content = fs.readFileSync(file, 'utf8');
    if (!content.includes('custom-cursor')) {
      content = content.replace('</body>', injection);
      fs.writeFileSync(file, content);
      console.log('Injected into ' + file);
    }
  }
});
