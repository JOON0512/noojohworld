(() => {
  const root = document.documentElement;
  const button = document.querySelector('.theme-toggle');
  let saved = null;
  try { saved = localStorage.getItem('hojoon-theme'); } catch (_) { /* Theme remains usable without storage. */ }
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const apply = theme => {
    root.dataset.theme = theme;
    button?.setAttribute('aria-label', theme === 'dark' ? '밝은 테마로 전환' : '어두운 테마로 전환');
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#111722' : '#f8f9fc');
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
      iframe.src = `https://www.youtube-nocookie.com/embed/${item.id}`;
      iframe.title = item.title;
      iframe.loading = 'lazy';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      iframe.allowFullscreen = true;
      iframe.referrerPolicy = 'strict-origin-when-cross-origin';
      const title = document.createElement('h4');
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
      watch.textContent = 'YouTube에서 보기 ↗';
      watch.setAttribute('aria-label', `${item.title} — YouTube에서 보기`);
      caption.append(watch);
      article.append(iframe, caption);
      videos.append(article);
    }
    if (videos.children.length) document.getElementById('video-section').hidden = false;
  }).catch(() => { /* No video section until real videos are available. */ });
})();
