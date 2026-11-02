document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a[href^="http"]').forEach(function (link) {
    if (!link.href.startsWith(window.location.origin)) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });
});

// Header tabs: arrows to scroll the tab bar when not every tab fits.
document.addEventListener('DOMContentLoaded', function () {
  var list = document.querySelector('.md-tabs__list');
  if (!list) return;
  var bar = list.parentElement;

  function arrow(dir, label, symbol) {
    var b = document.createElement('button');
    b.className = 'tabs-arrow tabs-arrow--' + dir;
    b.type = 'button';
    b.setAttribute('aria-label', label);
    b.textContent = symbol;
    b.addEventListener('click', function () {
      var step = list.clientWidth * 0.7;
      list.scrollBy({ left: dir === 'left' ? -step : step, behavior: 'smooth' });
    });
    bar.appendChild(b);
    return b;
  }
  var left = arrow('left', 'Show previous tabs', '‹');
  var right = arrow('right', 'Show more tabs', '›');

  function update() {
    var max = list.scrollWidth - list.clientWidth;
    left.classList.toggle('is-visible', list.scrollLeft > 2);
    right.classList.toggle('is-visible', list.scrollLeft < max - 2);
  }

  // Bring the current page's tab into view.
  var active = list.querySelector('.md-tabs__item--active');
  if (active) {
    var offset = active.getBoundingClientRect().left - list.getBoundingClientRect().left;
    list.scrollLeft += offset - (list.clientWidth - active.offsetWidth) / 2;
  }

  list.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
});

// Screenshots: click to see them at nearly full screen size; click again or press Esc to close.
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.md-typeset img.screenshot').forEach(function (img) {
    img.addEventListener('click', function () {
      var overlay = document.createElement('div');
      overlay.className = 'img-zoom';
      var big = document.createElement('img');
      big.src = img.currentSrc || img.src;
      big.alt = img.alt;
      overlay.appendChild(big);
      function close() {
        overlay.remove();
        document.removeEventListener('keydown', onKey);
      }
      function onKey(e) { if (e.key === 'Escape') close(); }
      overlay.addEventListener('click', close);
      document.addEventListener('keydown', onKey);
      document.body.appendChild(overlay);
    });
  });
});
