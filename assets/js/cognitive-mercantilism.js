/* Cognitive Mercantilism post: the elasticity chart. Diagram nodes and the dial
   are in explainer.js. Progressive enhancement only: with JavaScript off the
   post shows the formula and the table at the default setting. */
(() => {
  const $ = id => document.getElementById(id);

  // Elasticity chart: uses = p^-e, work for minds = 100 * p^(1-e)
  const svg = $("xp-chart");
  if (svg) {
    const NS = "http://www.w3.org/2000/svg";
    const L = 44, R = 528, T = 26, B = 220, STEPS = 10;
    const fmt = v => v >= 100 ? Math.round(v).toLocaleString("en-US") : v >= 10 ? v.toFixed(1) : v.toFixed(2);
    const pct = p => (p * 100 >= 10 ? Math.round(p * 100) : (p * 100).toFixed(1).replace(/\.0$/, "")) + "%";
    const niceMax = v => { const p = Math.pow(10, Math.floor(Math.log10(v))); for (const m of [1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10]) if (m * p >= v) return m * p; };
    const el = (tag, attrs, text) => {
      const e = document.createElementNS(NS, tag);
      for (const k in attrs) e.setAttribute(k, attrs[k]);
      if (text != null) e.textContent = text;
      return e;
    };
    const tip = $("xp-tip");

    const draw = () => {
      const p = +$("xp-price").value / 100, e = +$("xp-elas").value;
      $("xp-price-o").textContent = pct(p);
      $("xp-elas-o").textContent = e.toFixed(1);
      $("xp-t-use").textContent = fmt(Math.pow(p, -e)) + "× today";
      $("xp-t-work").textContent = fmt(100 * Math.pow(p, 1 - e)) + " (today 100)";
      $("xp-t-verdict").textContent = Math.abs(e - 1) < 1e-9 || p === 1 ? "Flat" : e > 1 ? "Grows: Rao's bet" : "Shrinks: the fear";

      const rows = [];
      for (let k = 0; k < STEPS; k++) {
        const pk = Math.pow(p, k / (STEPS - 1));
        rows.push({ pk, u: Math.pow(pk, -e), w: 100 * Math.pow(pk, 1 - e) });
      }
      $("xp-rows").innerHTML = rows.map(r => `<tr><td>${pct(r.pk)}</td><td>${fmt(r.u)}</td><td>${fmt(r.w)}</td></tr>`).join("");

      const ymax = niceMax(Math.max(100, ...rows.map(r => r.w)));
      const sx = k => L + (R - L) * k / (STEPS - 1), sy = v => B - (B - T) * v / ymax;
      svg.replaceChildren();
      svg.append(el("line", { class: "xp-base", x1: L, x2: R, y1: B, y2: B }));
      svg.append(el("line", { class: "xp-ref", x1: L, x2: R, y1: sy(100), y2: sy(100) }));
      svg.append(el("text", { class: "xp-axis", x: L - 8, y: sy(100) + 4, "text-anchor": "end" }, "100"));
      svg.append(el("text", { class: "xp-axis", x: L - 8, y: B + 4, "text-anchor": "end" }, "0"));
      svg.append(el("polyline", { class: "xp-line", points: rows.map((r, k) => `${sx(k)},${sy(r.w)}`).join(" ") }));

      // value labels on peak and last only; the first point is always 100, which the axis already labels
      let peak = 0;
      rows.forEach((r, k) => { if (r.w > rows[peak].w) peak = k; });
      const labelled = new Set([peak, STEPS - 1]);
      labelled.delete(0);
      rows.forEach((r, k) => {
        const dot = el("circle", { class: "xp-dot", cx: sx(k), cy: sy(r.w), r: 3.5, tabindex: "-1" });
        dot.addEventListener("pointerenter", () => {
          tip.textContent = `Price ${pct(r.pk)} of today: uses ${fmt(r.u)}× today, work for minds ${fmt(r.w)}`;
        });
        svg.append(dot);
        if (labelled.has(k)) {
          const above = sy(r.w) - 10 > T - 14;
          svg.append(el("text", { class: "xp-val", x: sx(k), y: above ? sy(r.w) - 10 : sy(r.w) + 18, "text-anchor": k === 0 ? "start" : k === STEPS - 1 ? "end" : "middle" }, fmt(r.w)));
        }
      });
      svg.append(el("text", { class: "xp-axis", x: L, y: B + 20, "text-anchor": "start" }, pct(rows[0].pk)));
      svg.append(el("text", { class: "xp-axis", x: R, y: B + 20, "text-anchor": "end" }, pct(rows[STEPS - 1].pk)));
      svg.append(el("text", { class: "xp-axis", x: (L + R) / 2, y: B + 38, "text-anchor": "middle" }, "price of intelligence, as a share of today"));
    };

    ["xp-price", "xp-elas"].forEach(id => $(id).addEventListener("input", draw));
    $("xp-controls").hidden = false;
    $("xp-chart-wrap").hidden = false;
    tip.hidden = false;
    draw();
  }
})();
