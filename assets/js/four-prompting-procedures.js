/* Four Prompting Procedures post: the SIP calculator. Diagram nodes and the
   dial are in explainer.js. Progressive enhancement only: with JavaScript off
   the post shows the totals and the table at the default values. */
(() => {
  const $ = id => document.getElementById(id);
  const svg = $("xp-chart");
  if (!svg) return;
  const NS = "http://www.w3.org/2000/svg";
  const L = 60, R = 528, T = 26, B = 220;
  const money = v => "$" + Math.round(v).toLocaleString("en-US");
  const short = v => v >= 1e6 ? "$" + (v / 1e6).toFixed(v >= 1e7 ? 0 : 1) + "M" : v >= 1e3 ? "$" + Math.round(v / 1e3) + "k" : "$" + Math.round(v);
  const niceMax = v => { const p = Math.pow(10, Math.floor(Math.log10(v))); for (const m of [1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10]) if (m * p >= v) return m * p; };
  const el = (tag, attrs, text) => {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    return e;
  };
  const tip = $("xp-tip");

  // Deposits at the start of each month, compounded monthly
  const draw = () => {
    const P = +$("xp-amt").value, r = +$("xp-rate").value / 100, n = +$("xp-yrs").value, i = r / 12;
    $("xp-amt-o").textContent = money(P);
    $("xp-rate-o").textContent = r * 100 + "%";
    $("xp-yrs-o").textContent = n;
    let bal = 0;
    const rows = [{ y: 0, inv: 0, bal: 0 }];
    for (let y = 1; y <= n; y++) {
      for (let m = 0; m < 12; m++) bal = (bal + P) * (1 + i);
      rows.push({ y, inv: P * 12 * y, bal });
    }
    const last = rows[n];
    $("xp-t-in").textContent = money(last.inv);
    $("xp-t-gr").textContent = money(last.bal - last.inv);
    $("xp-t-fv").textContent = money(last.bal);
    $("xp-rows").innerHTML = rows.slice(1).map(d => `<tr><td>${d.y}</td><td>${money(d.inv)}</td><td>${money(d.bal - d.inv)}</td><td>${money(d.bal)}</td></tr>`).join("");

    const ymax = niceMax(last.bal), sx = y => L + (R - L) * y / n, sy = v => B - (B - T) * v / ymax;
    svg.replaceChildren();
    svg.append(el("line", { class: "xp-base", x1: L, x2: R, y1: B, y2: B }));
    svg.append(el("text", { class: "xp-axis", x: L - 8, y: B + 4, "text-anchor": "end" }, "$0"));
    svg.append(el("text", { class: "xp-axis", x: L - 8, y: sy(ymax) + 4, "text-anchor": "end" }, short(ymax)));
    svg.append(el("polyline", { class: "xp-line-2", points: rows.map(d => `${sx(d.y)},${sy(d.inv)}`).join(" ") }));
    svg.append(el("polyline", { class: "xp-line", points: rows.map(d => `${sx(d.y)},${sy(d.bal)}`).join(" ") }));
    svg.append(el("circle", { class: "xp-dot", cx: sx(n), cy: sy(last.bal), r: 3.5 }));
    svg.append(el("text", { class: "xp-val", x: sx(n), y: sy(last.bal) - 10, "text-anchor": "end" }, short(last.bal)));
    svg.append(el("text", { class: "xp-axis", x: sx(n), y: sy(last.inv) - 8, "text-anchor": "end" }, short(last.inv) + " put in"));
    svg.append(el("text", { class: "xp-axis", x: L, y: B + 20, "text-anchor": "start" }, "0"));
    svg.append(el("text", { class: "xp-axis", x: R, y: B + 20, "text-anchor": "end" }, n));
    svg.append(el("text", { class: "xp-axis", x: (L + R) / 2, y: B + 38, "text-anchor": "middle" }, "years"));

    // hover: read the nearest year
    const hit = el("rect", { x: L, y: T, width: R - L, height: B - T, fill: "transparent" });
    hit.addEventListener("pointermove", e => {
      const box = svg.getBoundingClientRect(), x = (e.clientX - box.left) / box.width * 540;
      const d = rows[Math.min(n, Math.max(1, Math.round((x - L) / (R - L) * n)))];
      tip.textContent = `Year ${d.y}: put in ${money(d.inv)}, growth ${money(d.bal - d.inv)}, balance ${money(d.bal)}`;
    });
    svg.append(hit);
  };

  ["xp-amt", "xp-rate", "xp-yrs"].forEach(id => $(id).addEventListener("input", draw));
  $("xp-controls").hidden = false;
  $("xp-chart-wrap").hidden = false;
  tip.hidden = false;
  draw();
})();
