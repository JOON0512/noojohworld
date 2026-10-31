(() => {
  const root = document.documentElement;
  const button = document.querySelector('.theme-toggle');
  let saved = null;
  try { saved = localStorage.getItem('hojoon-theme'); } catch (_) { /* Theme remains usable without storage. */ }
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const apply = theme => {
    root.dataset.theme = theme;
    button?.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#171b20' : '#fafaf8');
  };
  apply(saved === 'dark' || saved === 'light' ? saved : system.matches ? 'dark' : 'light');
  if (button) {
    button.hidden = false;
    button.addEventListener('click', () => {
      saved = root.dataset.theme === 'dark' ? 'light' : 'dark';
      apply(saved);
      try { localStorage.setItem('hojoon-theme', saved); } catch (_) { /* Optional preference. */ }
    });
  }
  system.addEventListener('change', e => { if (!saved) apply(e.matches ? 'dark' : 'light'); });
  const videos = document.getElementById('videos');
  if (!videos) return;
  fetch('data/videos.json').then(r => { if (!r.ok) throw new Error('Unavailable'); return r.json(); }).then(items => {
    if (!Array.isArray(items)) return;
    for (const item of items) {
      if (!/^[\w-]{11}$/.test(item.id) || typeof item.title !== 'string') continue;
      const article = document.createElement('article');
      const iframe = document.createElement('iframe');
      iframe.src = `https://www.youtube-nocookie.com/embed/${item.id}?hl=en`;
      iframe.title = item.title;
      iframe.loading = 'lazy';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      iframe.allowFullscreen = true;
      iframe.referrerPolicy = 'strict-origin-when-cross-origin';
      const title = document.createElement('h3');
      title.textContent = item.title;
      const caption = document.createElement('div');
      caption.className = 'video-caption';
      caption.append(title);
      if (typeof item.duration === 'string') {
        const duration = document.createElement('p');
        duration.className = 'video-duration';
        duration.textContent = item.duration;
        caption.append(duration);
      }
      const watch = document.createElement('a');
      watch.className = 'text-link';
      watch.href = `https://www.youtube.com/watch?v=${item.id}`;
      watch.target = '_blank';
      watch.rel = 'noopener noreferrer';
      watch.textContent = 'Watch on YouTube ↗';
      watch.setAttribute('aria-label', `${item.title} — Watch on YouTube`);
      caption.append(watch);
      article.append(iframe, caption);
      videos.append(article);
    }
    if (videos.children.length) {
      const section = document.getElementById('video-section');
      section.hidden = false;
      if (window.location.hash === '#video-section') section.scrollIntoView();
    }
  }).catch(() => { /* No video section until real videos are available. */ });
})();
