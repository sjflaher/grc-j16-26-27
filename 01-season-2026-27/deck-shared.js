// GRC deck navigation — arrows/space/click to advance, N = speaker notes, F = fullscreen
(function () {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const progress = document.querySelector('.progress');
  const counter = document.querySelector('.counter');
  const notesEl = document.querySelector('.notes');
  let i = Math.min(parseInt(location.hash.slice(1), 10) || 0, slides.length - 1);

  function show(n) {
    i = Math.max(0, Math.min(n, slides.length - 1));
    slides.forEach((s, j) => s.classList.toggle('active', j === i));
    progress.style.width = ((i + 1) / slides.length * 100) + '%';
    counter.textContent = (i + 1) + ' / ' + slides.length;
    location.hash = i;
    const note = slides[i].getAttribute('data-notes');
    notesEl.innerHTML = note ? '<b>Notes:</b> ' + note : '<b>Notes:</b> —';
    const dark = slides[i].classList.contains('statement');
    counter.style.color = dark ? 'rgba(255,255,255,.55)' : 'rgba(0,0,0,.45)';
    document.querySelector('.brand').style.color = dark ? 'rgba(255,255,255,.45)' : 'rgba(0,0,0,.35)';
  }

  document.addEventListener('keydown', (e) => {
    if (['ArrowRight', ' ', 'PageDown'].includes(e.key)) { e.preventDefault(); show(i + 1); }
    else if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); show(i - 1); }
    else if (e.key === 'Home') show(0);
    else if (e.key === 'End') show(slides.length - 1);
    else if (e.key.toLowerCase() === 'n') notesEl.classList.toggle('show');
    else if (e.key.toLowerCase() === 'f') {
      document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen();
    }
  });
  document.addEventListener('click', (e) => {
    if (e.target.closest('.notes')) return;
    (e.clientX > window.innerWidth / 3) ? show(i + 1) : show(i - 1);
  });
  show(i);
})();
