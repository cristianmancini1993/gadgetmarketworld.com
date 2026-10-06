/**
 * Meta Pixel Purchase on thank-you pages — delegates to tracking.js (retry until fbq ready).
 */
(function () {
  function tryFire() {
    if (window.fireMetaThankYouPurchase && window.fireMetaThankYouPurchase()) return true;
    return false;
  }

  function onReady() {
    if (tryFire()) return;
    var attempts = 0;
    var timer = window.setInterval(function () {
      attempts += 1;
      if (tryFire() || attempts >= 60) window.clearInterval(timer);
    }, 100);
  }

  if (document.readyState === 'complete') {
    onReady();
  } else {
    window.addEventListener('load', onReady);
  }
})();
