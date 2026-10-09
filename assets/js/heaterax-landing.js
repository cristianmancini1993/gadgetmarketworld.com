(function () {
  function endOfToday() {
    var d = new Date();
    d.setHours(23, 59, 59, 999);
    return d.getTime();
  }
  var end = endOfToday();
  function pad(n) {
    return String(n).padStart(2, '0');
  }
  function tick() {
    var diff = Math.max(0, end - Date.now());
    var h = Math.floor(diff / 3600000);
    var m = Math.floor((diff % 3600000) / 60000);
    var s = Math.floor((diff % 60000) / 1000);
    document.querySelectorAll('[data-cd-h]').forEach(function (el) {
      el.textContent = pad(h);
    });
    document.querySelectorAll('[data-cd-m]').forEach(function (el) {
      el.textContent = pad(m);
    });
    document.querySelectorAll('[data-cd-s]').forEach(function (el) {
      el.textContent = pad(s);
    });
    if (diff > 0) setTimeout(tick, 1000);
  }
  tick();
})();

(function () {
  var el = document.getElementById('liveCount');
  if (!el) return;
  var count = 18;
  var tpl = el.getAttribute('data-live') || '<strong>{n} persone</strong> stanno acquistando ora';
  function render() {
    el.innerHTML = tpl.replace('{n}', String(count));
  }
  render();
  setInterval(function () {
    count += Math.random() > 0.5 ? 1 : -1;
    count = Math.min(24, Math.max(14, count));
    render();
  }, 3500);
})();

document.querySelectorAll('.hx-faq .faq-item .faq-q').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var item = btn.closest('.faq-item');
    if (!item) return;
    var open = item.classList.contains('open');
    item.parentElement.querySelectorAll('.faq-item.open').forEach(function (i) {
      i.classList.remove('open');
    });
    if (!open) item.classList.add('open');
  });
});

(function () {
  var btn = document.getElementById('faqShowMore');
  if (!btn) return;
  btn.addEventListener('click', function () {
    document.querySelectorAll('.hx-faq .faq-item.is-hidden').forEach(function (item) {
      item.classList.remove('is-hidden');
    });
    btn.style.display = 'none';
  });
})();
