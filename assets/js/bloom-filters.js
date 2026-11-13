/* Bloom filters post: the sizing calculator. Diagram nodes and the dial are in
   explainer.js. Progressive enhancement only: with JavaScript off the post shows
   the formula, the totals and the table at the default values. */
(() => {
  const $ = id => document.getElementById(id);
  const svg = $("xp-chart");
  if (!svg) return;
  const NS = "http://www.w3.org/2000/svg";
  const L = 56, R = 528, T = 20, B = 220, KMAX = 15, PMIN = 1e-5;
  const fp = (k, b) => Math.pow(1 - Math.exp(-k / b), k);
  const pct = p => p >= 0.1 ? (p * 100).toFixed(1) + "%" : p >= 0.001 ? (p * 100).toFixed(2) + "%" : (p * 100).toPrecision(2) + "%";
  const axisPct = p => (p * 100 >= 1 ? (p * 100).toFixed(0) : String(+(p * 100).toPrecision(1))) + "%";
  const bytes = v => v >= 1e9 ? (v / 1e9).toFixed(2) + " GB" : v >= 1e6 ? (v / 1e6).toFixed(2) + " MB" : v >= 1e3 ? (v / 1e3).toFixed(1) + " KB" : Math.round(v) + " B";
  const count = n => n >= 1e6 ? (n / 1e6).toFixed(n >= 1e7 ? 0 : 1) + " million" : Math.round(n).toLocaleString("en-US");
  const sx = k => L + (k - 1) / (KMAX - 1) * (R - L);
  const sy = p => T + (B - T) * -Math.log10(Math.max(p, PMIN)) / -Math.log10(PMIN);
  const el = (tag, attrs, text) => {
    const e = document.createElementNS(NS, tag);
    for (const a in attrs) e.setAttribute(a, attrs[a]);
    if (text != null) e.textContent = text;
    return e;
  };
  const tip = $("xp-tip");

  const draw = () => {
    const n = Math.pow(10, +$("xp-items").value), b = +$("xp-bpi").value, k = +$("xp-kh").value;
    const best = Math.max(1, Math.round(b * Math.LN2));
    $("xp-items-o").textContent = count(n);
    $("xp-bpi-o").textContent = b;
    $("xp-kh-o").textContent = k;
    $("xp-t-fp").textContent = pct(fp(k, b));
    $("xp-t-mem").textContent = bytes(n * b / 8);
    $("xp-t-k").textContent = best + " (" + pct(fp(best, b)) + ")";
    let rows = "";
    for (let kk = 1; kk <= KMAX; kk++) {
      rows += kk === k ? `<tr class="is-on"><td>${kk}, your k</td><td>${pct(fp(kk, b))}</td></tr>` : `<tr><td>${kk}</td><td>${pct(fp(kk, b))}</td></tr>`;
    }
    $("xp-rows").innerHTML = rows;

    svg.replaceChildren();
    svg.append(el("line", { class: "xp-base", x1: L, x2: R, y1: B, y2: B }));
    for (const e of [0, -1, -2, -3, -4, -5]) {
      svg.append(el("text", { class: "xp-axis", x: L - 8, y: sy(Math.pow(10, e)) + 4, "text-anchor": "end" }, axisPct(Math.pow(10, e))));
    }
    let d = "";
    for (let i = 0; i <= 140; i++) {
      const kk = 1 + i * (KMAX - 1) / 140;
      d += (i ? "L" : "M") + sx(kk).toFixed(1) + " " + sy(fp(kk, b)).toFixed(1);
    }
    svg.append(el("path", { class: "xp-line", d }));
    svg.append(el("line", { class: "xp-ref", x1: sx(k), x2: sx(k), y1: T, y2: B }));
    svg.append(el("circle", { class: "xp-dot is-on", cx: sx(k), cy: sy(fp(k, b)), r: 4.5 }));
    const below = sy(fp(k, b)) < (T + B) / 2;
    svg.append(el("text", {
      class: "xp-val", x: k > KMAX - 3 ? sx(k) - 8 : sx(k) + 8, y: below ? sy(fp(k, b)) + 20 : sy(fp(k, b)) - 10,
      "text-anchor": k > KMAX - 3 ? "end" : "start"
    }, pct(fp(k, b))));
    svg.append(el("text", { class: "xp-axis", x: L, y: B + 20, "text-anchor": "start" }, "1"));
    svg.append(el("text", { class: "xp-axis", x: R, y: B + 20, "text-anchor": "end" }, KMAX));
    svg.append(el("text", { class: "xp-axis", x: (L + R) / 2, y: B + 38, "text-anchor": "middle" }, "hash functions (k)"));

    const hit = el("rect", { x: L, y: T, width: R - L, height: B - T, fill: "transparent" });
    hit.addEventListener("pointermove", e => {
      const box = svg.getBoundingClientRect(), x = (e.clientX - box.left) / box.width * 540;
      const kk = Math.min(KMAX, Math.max(1, Math.round(1 + (x - L) / (R - L) * (KMAX - 1))));
      tip.textContent = `k = ${kk}: false positive rate ${pct(fp(kk, b))} at ${b} bits per item`;
    });
    svg.append(hit);
  };

  ["xp-items", "xp-bpi", "xp-kh"].forEach(id => $(id).addEventListener("input", draw));
  $("xp-controls").hidden = false;
  $("xp-chart-wrap").hidden = false;
  tip.hidden = false;
  draw();
})();
