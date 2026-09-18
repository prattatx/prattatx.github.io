/* ============================================================
   James H. Pratt — site behaviour
   Progressive enhancement only. Everything here is optional;
   the page is fully readable with JavaScript disabled.
   ============================================================ */

(function () {
  'use strict';

  document.documentElement.classList.add('js');

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. The signal rail ----------
     A deterministic trace. Same seed, same waveform, every load.
     Quiet at the edges, active through the middle, the way a real
     recording looks when someone stops talking at the ends. */

  function makeSignal(height, width) {
    var cx = width / 2;
    var step = 2;
    var pts = [];
    // fixed-seed LCG so the trace is identical on every visit
    var seed = 20000617;
    function rnd() {
      seed = (seed * 1103515245 + 12345) % 2147483648;
      return seed / 2147483648;
    }
    var raw = [];
    for (var y = 0; y <= height; y += step) {
      var t = y / height;
      // envelope: quiet at both ends, active through the middle
      var env = Math.pow(Math.sin(Math.PI * t), 0.85);
      var v =
        Math.sin(t * 17.3) * 0.50 +
        Math.sin(t * 39.1 + 1.1) * 0.28 +
        Math.sin(t * 71.7 + 2.4) * 0.13 +
        (rnd() - 0.5) * 0.10;
      raw.push(v * env);
    }
    // 5-tap smoothing so the trace reads as a signal, not static
    for (var i = 0; i < raw.length; i++) {
      var a = raw[Math.max(0, i - 2)], b = raw[Math.max(0, i - 1)];
      var c = raw[i];
      var d2 = raw[Math.min(raw.length - 1, i + 1)];
      var e = raw[Math.min(raw.length - 1, i + 2)];
      var sm = (a + 2 * b + 3 * c + 2 * d2 + e) / 9;
      pts.push([cx + sm * (width * 0.40), i * step]);
    }
    // catmull-rom style: straight segments at 2px are already smooth enough
    return 'M' + pts.map(function (p) {
      return p[0].toFixed(2) + ' ' + p[1].toFixed(1);
    }).join('L');
  }

  /* ---------- 1b. The hero field ----------
     The same signal, given room. The rail is a 1px thread in a gutter nobody
     reads; the hero has roughly 480px of empty paper to the right of a 42ch
     lede. This is not a second motif, it is the first one opened out into a
     multi-channel montage, the shape a real recording takes on paper.

     Deterministic like the rail: one seed, same field every visit. Quiet at
     the left so it emerges out of the text rather than crowding it, and
     settling as it falls toward the buttons. Static on purpose: the stat rail
     is the page's one orchestrated entrance and design.md allows exactly one. */

  function makeChannels(w, h) {
    var n = Math.max(7, Math.min(13, Math.round(h / 48)));
    var gap = h / n;
    var step = 3;
    var seed = 20000617;
    function rnd() {
      seed = (seed * 1103515245 + 12345) % 2147483648;
      return seed / 2147483648;
    }
    var out = [];
    for (var i = 0; i < n; i++) {
      var base = (i + 0.5) * gap;
      // the recording winds down as it falls toward the buttons: the top
      // channels are busy and nearly touch, the last one is almost a flat line
      var fall = 1 - i / (n - 1);
      var act = Math.pow(fall, 0.9);
      var amp = gap * (0.05 + 1.05 * act);
      var op = (0.14 + 0.46 * Math.pow(fall, 0.8)).toFixed(3);
      // each channel gets its own character, or the field reads as ruled paper
      var f1 = 9 + rnd() * 9;
      var f2 = 26 + rnd() * 22;
      var f3 = 55 + rnd() * 40;
      var ph = rnd() * 6.283;
      var noise = 0.10 + rnd() * 0.22;
      var hasBurst = rnd() > 0.45;
      var bx = 0.35 + rnd() * 0.5;
      var bw = 0.05 + rnd() * 0.07;
      var raw = [];
      for (var x = 0; x <= w; x += step) {
        var t = x / w;
        // quiet at the left edge so the field grows out of the lede
        var env = Math.pow(t, 0.65);
        var v =
          Math.sin(t * f1 + ph) * 0.52 +
          Math.sin(t * f2 + ph * 1.4) * 0.26 +
          Math.sin(t * f3 + ph * 0.6) * 0.11 +
          (rnd() - 0.5) * noise;
        if (hasBurst) {
          var g = Math.exp(-Math.pow((t - bx) / bw, 2));
          v += Math.sin(t * 150 + ph) * 0.55 * g;
        }
        raw.push(env * v);
      }
      var pts = [];
      for (var j = 0; j < raw.length; j++) {
        var a = raw[Math.max(0, j - 2)], b = raw[Math.max(0, j - 1)];
        var c = raw[j];
        var d2 = raw[Math.min(raw.length - 1, j + 1)];
        var e = raw[Math.min(raw.length - 1, j + 2)];
        var sm = (a + 2 * b + 3 * c + 2 * d2 + e) / 9;
        pts.push((j * step).toFixed(1) + ' ' + (base + sm * amp).toFixed(2));
      }
      out.push('<path d="M' + pts.join('L') + '" opacity="' + op + '"/>');
    }
    return out.join('');
  }

  var field = document.querySelector('.hero-field');

  function buildField() {
    if (!field) return;
    var w = field.clientWidth;
    var h = field.clientHeight;
    // the CSS hides it below 1100px, where the lede would crowd it
    if (!w || !h || !field.offsetParent) { field.innerHTML = ''; return; }
    field.innerHTML =
      '<svg width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '" ' +
      'aria-hidden="true" focusable="false">' + makeChannels(w, h) + '</svg>';
  }

  var rail = document.querySelector('.rail');
  var railState = null;

  function buildRail() {
    if (!rail) return;
    var w = rail.clientWidth;
    var h = rail.clientHeight;
    if (!w || !h) return;
    var d = makeSignal(h, w);
    rail.innerHTML =
      '<svg width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '" aria-hidden="true" focusable="false">' +
        '<defs><clipPath id="railClip"><rect id="railRect" x="0" y="0" width="' + w + '" height="0"/></clipPath></defs>' +
        '<path class="wave-base" d="' + d + '"/>' +
        '<path class="wave-live" d="' + d + '" clip-path="url(#railClip)"/>' +
        '<circle class="playhead-ring" cx="' + (w / 2) + '" cy="0" r="7"/>' +
        '<circle class="playhead" cx="' + (w / 2) + '" cy="0" r="2.5"/>' +
      '</svg>';
    railState = {
      h: h,
      rect: rail.querySelector('#railRect'),
      dot: rail.querySelector('.playhead'),
      ring: rail.querySelector('.playhead-ring')
    };
    drawRail();
  }

  var topbar = document.querySelector('.rail-top');

  function scrollProgress() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    if (max <= 0) return 0;
    return Math.min(1, Math.max(0, window.scrollY / max));
  }

  function drawRail() {
    var p = scrollProgress();
    if (railState) {
      var y = p * railState.h;
      railState.rect.setAttribute('height', y.toFixed(1));
      railState.dot.setAttribute('cy', y.toFixed(1));
      railState.ring.setAttribute('cy', y.toFixed(1));
    }
    if (topbar) topbar.style.transform = 'scaleX(' + p + ')';
  }

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      drawRail();
      ticking = false;
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });

  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () { buildRail(); buildField(); }, 180);
  });

  buildRail();
  drawRail();
  buildField();

  /* ---------- 2. Reveal on scroll ---------- */

  var revealables = document.querySelectorAll('.reveal');
  if (reduced || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(revealables, function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    Array.prototype.forEach.call(revealables, function (el) {
      io.observe(el);
      /* An element already on screen at load must not depend on the observer.
         The -8% bottom margin lands almost exactly on the stat rail in a 900px
         viewport, which made the site's strongest asset a load-timing coin
         flip: on an unlucky paint it stayed at opacity 0 with no second chance.
         Run its entrance on the next frame instead, so the animation still
         plays but cannot be missed. */
      if (el.getBoundingClientRect().top < window.innerHeight) {
        requestAnimationFrame(function () {
          requestAnimationFrame(function () {
            el.classList.add('in');
            io.unobserve(el);
          });
        });
      }
    });

    /* Safety net. Whatever the observer has not delivered once the page has
       loaded and fonts have settled, paint it if it is on screen. Content is
       never left permanently invisible because a callback did not fire. */
    window.addEventListener('load', function () {
      setTimeout(function () {
        Array.prototype.forEach.call(revealables, function (el) {
          if (!el.classList.contains('in') &&
              el.getBoundingClientRect().top < window.innerHeight) {
            el.classList.add('in');
            io.unobserve(el);
          }
        });
      }, 300);
    });
  }

  /* ---------- 3. Mobile nav ---------- */

  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    var closeNav = function (returnFocus) {
      nav.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.textContent = 'Menu';
      if (returnFocus) toggle.focus();
    };

    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.textContent = open ? 'Close' : 'Menu';
    });

    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') closeNav(false);
    });

    /* Escape closes the panel and returns focus to the control that opened it,
       so a keyboard user is never left inside a dismissed menu. */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) closeNav(true);
    });
  }

  /* ---------- 4. Booking clicks ---------- */

  /* A booked call is the site's only conversion and nothing measured it, so every
     judgement about CTA placement was inference. utm_content on each href
     attributes the click on cal.com's side; this event attributes it here, so
     click share by position becomes observable instead of argued. */
  document.addEventListener('click', function (e) {
    if (!e.target || !e.target.closest) return;
    var a = e.target.closest('a[data-cta]');
    if (a && typeof window.gtag === 'function') {
      window.gtag('event', 'book_click', { cta_location: a.getAttribute('data-cta') });
    }
  });
})();
