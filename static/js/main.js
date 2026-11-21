document.addEventListener('DOMContentLoaded', () => {
  const root = document.documentElement;
  const themeToggle = document.getElementById('themeToggle');
  const storedTheme = localStorage.getItem('lishu-theme');
  if (storedTheme) root.dataset.theme = storedTheme;
  updateThemeIcon();

  themeToggle?.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('lishu-theme', root.dataset.theme);
    updateThemeIcon();
  });

  function updateThemeIcon() {
    const icon = themeToggle?.querySelector('i');
    if (icon) icon.className = root.dataset.theme === 'dark' ? 'bi bi-sun' : 'bi bi-moon-stars';
  }

  const nav = document.getElementById('mainNav');
  const backToTop = document.getElementById('backToTop');
  const onScroll = () => {
    nav?.classList.toggle('scrolled', window.scrollY > 30);
    backToTop?.classList.toggle('visible', window.scrollY > 500);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  document.querySelectorAll('.category-pill').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.category-pill').forEach(item => item.classList.remove('active'));
      button.classList.add('active');
      const filter = button.dataset.filter;
      document.querySelectorAll('.product-item').forEach(item => {
        item.style.display = filter === 'all' || item.classList.contains(filter) ? '' : 'none';
      });
    });
  });

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('revealed');
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.section, .product-card, .benefit-card, .testimonial-card').forEach(el => observer.observe(el));
});
