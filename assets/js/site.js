/* ============================================================
   James H. Pratt: site behaviour
   Progressive enhancement only. Everything here is optional;
   the page is fully readable with JavaScript disabled, and every
   animated figure ships in its finished state.
   ============================================================ */

(function () {
  'use strict';

  /* The layout sets this inline in <head> so entrance styles never flash.
     Repeated here for any page that does not use the default layout. */
  document.documentElement.classList.add('js');

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canAnimate = !reduced && typeof Element.prototype.animate === 'function';
  var EASE_OUT = 'cubic-bezier(.16, 1, .3, 1)';

  /* Run fn once, the first time el is on screen. Falls back to running at once
     where IntersectionObserver is missing, and a load-time sweep catches
     anything the observer never reported, so no figure can stay hidden. */
  var pending = [];
  function whenSeen(el, fn, threshold) {
    var done = false;
    function run() {
      if (done) return;
      done = true;
      fn();
    }
    if (!('IntersectionObserver' in window)) { run(); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { io.disconnect(); run(); }
      });
    }, { threshold: threshold || 0.25 });
    io.observe(el);
    pending.push({ el: el, run: function () { io.disconnect(); run(); } });
  }
  window.addEventListener('load', function () {
    setTimeout(function () {
      pending.forEach(function (p) {
        var r = p.el.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.85 && r.bottom > 0) p.run();
      });
    }, 400);
  });

  /* Count a figure up from zero to its data-count. The element already holds
     the final text, so this only ever replaces it with itself at the end. */
  function countUp(el, duration, delay) {
    var target = parseFloat(el.getAttribute('data-count'));
    if (isNaN(target)) return;
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    var final = el.textContent;
    var start = null;
    var settled = false;
    function settle() {
      settled = true;
      el.textContent = final;
    }
    el.textContent = prefix + '0' + suffix;
    function frame(now) {
      if (settled) return;
      if (start === null) start = now + (delay || 0);
      var t = Math.min(1, Math.max(0, (now - start) / duration));
      var eased = 1 - Math.pow(1 - t, 4);
      if (t < 1) {
        el.textContent = prefix + Math.round(target * eased) + suffix;
        window.requestAnimationFrame(frame);
      } else {
        settle();
      }
    }
    window.requestAnimationFrame(frame);
    /* Frames stop in a background tab and timers do not. Whatever happens to
       the animation, the figure ends on its real value. */
    setTimeout(settle, (delay || 0) + duration + 400);
  }

  /* ---------- 1. Scroll progress ---------- */

  var topbar = document.querySelector('.rail-top');

  function drawProgress() {
    if (!topbar) return;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var p = max <= 0 ? 0 : Math.min(1, Math.max(0, window.scrollY / max));
    topbar.style.transform = 'scaleX(' + p + ')';
  }

  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      drawProgress();
      ticking = false;
    });
  }, { passive: true });
  drawProgress();

  /* ---------- 2. The sorting figure ----------
     Each task leaves the source at the top of the figure, travels down the
     trunk to the decision point, waits there a beat, then runs along the bar
     and drops into its column. The chips never leave the DOM positions they
     ship in: each one is animated from an offset back to zero, so if anything
     here fails the figure is simply already sorted. */

  var sorter = document.querySelector('[data-sorter]');

  function playSorter() {
    var tree = sorter.querySelector('.sorter-tree');
    var node = sorter.querySelector('.sorter-node');
    var replay = sorter.querySelector('.sorter-replay');
    var chips = Array.prototype.slice.call(sorter.querySelectorAll('.chip'));
    var counters = sorter.querySelectorAll('.sorter-n');
    var timers = [];
    var running = [];

    chips.sort(function (a, b) {
      return a.getAttribute('data-order') - b.getAttribute('data-order');
    });

    function run() {
      running.forEach(function (a) { a.cancel(); });
      timers.forEach(clearTimeout);
      running = [];
      timers = [];
      if (replay) replay.hidden = true;

      var treeBox = tree.getBoundingClientRect();
      var srcX = treeBox.left + treeBox.width / 2;
      var srcY = treeBox.top - 14;            /* just under the source label */
      var nodeY = treeBox.top + 28;           /* the bar, where the node sits */

      /* the connector draws first: trunk down, bar out, drops down */
      [['.st-trunk', 'scaleY(0)', 0],
       ['.st-bar', 'scaleX(0)', 220],
       ['.st-drop--l', 'scaleY(0)', 480],
       ['.st-drop--r', 'scaleY(0)', 480]].forEach(function (step) {
        var el = sorter.querySelector(step[0]);
        running.push(el.animate(
          [{ transform: step[1] }, { transform: 'none' }],
          { duration: 320, delay: step[2], easing: EASE_OUT, fill: 'backwards' }
        ));
      });
      running.push(node.animate(
        [{ transform: 'scale(0)' }, { transform: 'scale(1)' }],
        { duration: 300, delay: 200, easing: EASE_OUT, fill: 'backwards' }
      ));

      Array.prototype.forEach.call(counters, function (c) { c.textContent = '0'; });

      var first = 900;      /* after the connector is drawn */
      var gap = 430;        /* between tasks */
      var travel = 1150;

      chips.forEach(function (chip, i) {
        var box = chip.getBoundingClientRect();
        var cx = box.left + box.width / 2;
        var cy = box.top + box.height / 2;
        var toSrc = 'translate(' + (srcX - cx) + 'px,' + (srcY - cy) + 'px)';
        var toNode = 'translate(' + (srcX - cx) + 'px,' + (nodeY - cy) + 'px)';
        var overCol = 'translate(0px,' + (nodeY - cy) + 'px)';
        var delay = first + i * gap;

        /* Neutral while it travels; it takes its column's colour on landing,
           which is the implicit final keyframe. */
        var plain = {
          backgroundColor: '#fffdf9',
          borderColor: '#948977',
          color: '#26231f'
        };
        function at(offset, transform, extra) {
          var k = { offset: offset, transform: transform, easing: EASE_OUT };
          for (var key in plain) k[key] = plain[key];
          for (var e in extra) k[e] = extra[e];
          return k;
        }
        running.push(chip.animate([
          at(0, toSrc + ' scale(.92)', { opacity: 0 }),
          at(0.12, toSrc, { opacity: 1 }),
          at(0.36, toNode, { opacity: 1 }),
          at(0.48, toNode, { opacity: 1 }),
          at(0.72, overCol, { opacity: 1 }),
          { offset: 1, transform: 'none', opacity: 1 }
        ], { duration: travel, delay: delay, fill: 'backwards' }));
        chip.style.zIndex = String(20 - i);

        /* the decision point answers each task as it arrives */
        running.push(node.animate(
          [{ transform: 'scale(1)' }, { transform: 'scale(1.45)' }, { transform: 'scale(1)' }],
          { duration: 300, delay: delay + travel * 0.36, easing: 'ease-out' }
        ));

        var counter = chip.closest('.sorter-col').querySelector('.sorter-n');
        timers.push(setTimeout(function () {
          counter.textContent = String(parseInt(counter.textContent, 10) + 1);
        }, delay + travel * 0.9));
      });

      timers.push(setTimeout(function () {
        Array.prototype.forEach.call(counters, function (c) {
          c.textContent = c.getAttribute('data-n');
        });
        chips.forEach(function (chip) { chip.style.zIndex = ''; });
        if (replay) replay.hidden = false;
      }, first + chips.length * gap + travel));
    }

    if (replay) replay.addEventListener('click', run);
    run();
  }

  if (sorter && canAnimate) {
    /* wait for fonts so the measured chip positions are the final ones */
    var startSorter = function () { whenSeen(sorter, playSorter, 0.3); };
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(startSorter, startSorter);
    } else {
      startSorter();
    }
  }

  /* ---------- 3. The numbers ---------- */

  var stats = document.querySelector('.stats');
  if (stats && canAnimate) {
    whenSeen(stats, function () {
      Array.prototype.forEach.call(stats.querySelectorAll('[data-count]'), function (el, i) {
        el.parentNode.animate(
          [{ opacity: 0, transform: 'translateY(12px)' }, { opacity: 1, transform: 'none' }],
          { duration: 600, delay: i * 90, easing: EASE_OUT, fill: 'backwards' }
        );
        countUp(el, 1400, i * 90);
      });
    }, 0.4);
  }

  /* ---------- 4. Drawn figures ----------
     A stroke is drawn by normalising its length to 1 and sliding a dash
     offset from 1 to 0. Nothing is forwards-filled, so when the animation
     ends the element returns to its own styles, a plain solid line. */

  function drawStroke(el, duration, delay) {
    el.setAttribute('pathLength', '1');
    return el.animate(
      [{ strokeDasharray: '1', strokeDashoffset: 1 }, { strokeDasharray: '1', strokeDashoffset: 0 }],
      { duration: duration, delay: delay || 0, easing: 'cubic-bezier(.45, 0, .2, 1)', fill: 'backwards' }
    );
  }

  var curve = document.querySelector('.record-curve');
  if (curve) {
    if (!canAnimate) {
      curve.classList.add('is-drawn');
    } else {
      whenSeen(curve, function () {
        var main = curve.querySelector('.rc-line:not(.rc-line--partial)');
        var partial = curve.querySelector('.rc-line--partial');
        var total = curve.querySelector('.rc-val strong');
        curve.classList.add('is-drawn');
        if (main) drawStroke(main, 1800);
        if (partial) {
          partial.animate([{ opacity: 0 }, { opacity: 1 }],
            { duration: 400, delay: 1800, fill: 'backwards' });
        }
        if (total && !total.hasAttribute('data-count')) {
          total.setAttribute('data-count', parseInt(total.textContent, 10));
        }
        if (total) countUp(total, 1800, 0);
      }, 0.5);
    }
  }

  var wave = document.querySelector('[data-wave]');
  if (wave) {
    if (!canAnimate) {
      wave.classList.add('is-drawn');
    } else {
      whenSeen(wave, function () {
        var line = wave.querySelector('.wave-line');
        var labels = wave.querySelectorAll('.wave-labels span');
        var duration = 2600;
        wave.classList.add('is-drawn');
        /* linear, so each label can appear as the trace reaches its sound */
        line.setAttribute('pathLength', '1');
        line.animate(
          [{ strokeDasharray: '1', strokeDashoffset: 1 }, { strokeDasharray: '1', strokeDashoffset: 0 }],
          { duration: duration, easing: 'linear', fill: 'backwards' }
        );
        Array.prototype.forEach.call(labels, function (label) {
          var at = parseFloat(label.style.left) / 100;
          label.animate(
            [{ opacity: 0, transform: 'translateY(6px)' }, { opacity: 1, transform: 'none' }],
            { duration: 420, delay: duration * at, easing: EASE_OUT, fill: 'backwards' }
          );
        });
      }, 0.5);
    }
  }

  /* The film on /method/ starts when it is on screen, and not at all under
     reduced motion. It is muted and carries its own controls. */
  var film = document.querySelector('[data-film] video');
  if (film && !reduced) {
    whenSeen(film, function () {
      var started = film.play();
      if (started && started.catch) started.catch(function () {});
    }, 0.5);
  }

  /* ---------- 5. Reveal on scroll ---------- */

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
      /* An element already on screen at load must not depend on the observer:
         on an unlucky paint it stays at opacity 0 with no second chance. Run
         its entrance on the next frame instead, so the animation still plays
         but cannot be missed. */
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

  /* ---------- 6. Mobile nav ---------- */

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

  /* ---------- 7. Booking clicks ---------- */

  /* utm_content on each booking href attributes the click on cal.com's side;
     this event attributes it here, by position on the page. */
  document.addEventListener('click', function (e) {
    if (!e.target || !e.target.closest) return;
    var a = e.target.closest('a[data-cta]');
    if (a && typeof window.gtag === 'function') {
      window.gtag('event', 'book_click', { cta_location: a.getAttribute('data-cta') });
    }
  });
})();
