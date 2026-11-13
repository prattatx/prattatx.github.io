/* Shared behaviour for the four-format explainer posts: clickable diagram nodes
   and the plain-English dial. Each post's chart lives in its own script.
   Progressive enhancement only: with JavaScript off the dial stays hidden and
   the diagrams are still readable as figures. */
(() => {
  const $ = id => document.getElementById(id);
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Figure 1: the first select shows the node's note, a second select jumps to its section
  const info = $("xp-nodeinfo");
  if (info) {
    info.textContent = info.dataset.hint || "Select a box to see what it means. Select it again to go to the section that covers it.";
    document.querySelectorAll(".xp-node").forEach(n => {
      const act = () => {
        if (n.classList.contains("on")) {
          const t = $(n.dataset.target);
          if (t) t.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
          return;
        }
        document.querySelectorAll(".xp-node").forEach(m => m.classList.remove("on"));
        n.classList.add("on");
        info.textContent = n.dataset.info;
      };
      n.addEventListener("click", act);
      n.addEventListener("keydown", e => {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); act(); }
      });
    });
  }

  // Dial: one idea at four levels of plain English, with live sentence stats.
  // Samples come from <script type="application/json" id="xp-dial-data">.
  const dial = $("xp-dial"), data = $("xp-dial-data");
  if (dial && data) {
    const { samples, verdicts, best } = JSON.parse(data.textContent);
    const show = i => {
      const s = samples[i], sents = s.split(/(?<=[.?!])\s+/), words = sents.map(x => x.split(/\s+/).length);
      const avg = (words.reduce((a, b) => a + b, 0) / sents.length).toFixed(1);
      $("xp-sample").textContent = s;
      $("xp-stats").innerHTML = `<span>Sentences <b>${sents.length}</b></span><span>Average words per sentence <b>${avg}</b></span><span>Longest <b>${Math.max(...words)}</b></span><span class="xp-verdict${i === best ? " is-best" : ""}">${verdicts[i]}</span>`;
      dial.querySelectorAll("[data-lvl]").forEach(b => b.setAttribute("aria-pressed", String(+b.dataset.lvl === i)));
    };
    dial.querySelectorAll("[data-lvl]").forEach(b => b.addEventListener("click", () => show(+b.dataset.lvl)));
    show(best);
    dial.hidden = false;
  }
})();
