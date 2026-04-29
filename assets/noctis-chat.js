/* ============================================================
   NOCTIS — Concierge Chat
   A self-contained chat widget. Smart keyword-driven responses
   covering pricing, fleet, delivery, insurance, drivers, etc.
   No external dependencies, no API key required.
   ============================================================ */
(function () {
  "use strict";

  // ---------- Knowledge base ----------
  // Each rule has { match: [keywords | regex], reply: string-or-fn }.
  // Rules are checked in order. First match wins.
  // The reply may include simple <strong>, <em>, line breaks (\n), and links.
  var FLEET = {
    spectre: { name: "Rolls-Royce Spectre", day: 6700, week: 32500, summary: "the silent electric coupe — 577 hp, 4 seats, 0–100 in 4.5 s" },
    db12:    { name: "Aston Martin DB12 Volante", day: 4950, week: 24000, summary: "twin-turbo V8, 680 hp, roof down, 0–100 in 3.6 s" },
    "750s":  { name: "McLaren 750S Spider", day: 6250, week: 30000, summary: "740 hp twin-turbo V8, dihedral doors, 0–100 in 2.7 s" },
    purosangue: { name: "Ferrari Purosangue", day: 7700, week: 37000, summary: "naturally-aspirated V12, 725 hp, 4 doors, 0–100 in 3.3 s" },
    g63:     { name: "Mercedes-AMG G 63", day: 3100, week: 15000, summary: "Obsidian Black, 577 hp V8, 5 seats, the icon" },
    "911":   { name: "Porsche 911 GT3 Touring", day: 4250, week: 20500, summary: "naturally-aspirated 4.0L flat-six, manual gearbox, 0–100 in 3.4 s" }
  };

  function fleetList() {
    var lines = [];
    for (var k in FLEET) {
      var c = FLEET[k];
      lines.push("• <strong>" + c.name + "</strong> — A$" + c.day.toLocaleString() + " / day · A$" + c.week.toLocaleString() + " / week");
    }
    return "Our six are:\n\n" + lines.join("\n") + "\n\nWhich one were you considering?";
  }

  var RULES = [
    // Greeting
    { m: [/^(hi|hey|hello|g'?day|yo|sup|good\s*(morning|afternoon|evening))\b/i],
      r: "Welcome to Noctis. I'm the after-hours concierge — a soft AI, but I know the fleet, the rates, and how we deliver. What can I help with?" },

    // Specific cars — return their summary
    { m: [/spectre|rolls/i], r: function () { var c = FLEET.spectre; return "<strong>" + c.name + "</strong> — " + c.summary + ". From A$" + c.day.toLocaleString() + " / day, A$" + c.week.toLocaleString() + " / week. Delivered in person anywhere in Greater Sydney.\n\nWant to lock in dates? <a href=\"/index.html?car=spectre#reserve\">Begin a Spectre reservation →</a>"; } },
    { m: [/db\s*12|aston/i],   r: function () { var c = FLEET.db12;    return "<strong>" + c.name + "</strong> — " + c.summary + ". From A$" + c.day.toLocaleString() + " / day, A$" + c.week.toLocaleString() + " / week.\n\n<a href=\"/index.html?car=db12#reserve\">Begin a DB12 reservation →</a>"; } },
    { m: [/750\s*s|mclaren/i], r: function () { var c = FLEET["750s"]; return "<strong>" + c.name + "</strong> — " + c.summary + ". From A$" + c.day.toLocaleString() + " / day, A$" + c.week.toLocaleString() + " / week.\n\n<a href=\"/index.html?car=750s#reserve\">Begin a 750S reservation →</a>"; } },
    { m: [/purosangue|ferrari/i], r: function () { var c = FLEET.purosangue; return "<strong>" + c.name + "</strong> — " + c.summary + ". From A$" + c.day.toLocaleString() + " / day, A$" + c.week.toLocaleString() + " / week.\n\n<a href=\"/index.html?car=purosangue#reserve\">Begin a Purosangue reservation →</a>"; } },
    { m: [/g\s*63|g[\s-]wagon|g\s*wagon|amg|mercedes/i], r: function () { var c = FLEET.g63; return "<strong>" + c.name + "</strong> — " + c.summary + ". From A$" + c.day.toLocaleString() + " / day, A$" + c.week.toLocaleString() + " / week.\n\n<a href=\"/index.html?car=g63#reserve\">Begin a G 63 reservation →</a>"; } },
    { m: [/911|porsche|gt3/i], r: function () { var c = FLEET["911"]; return "<strong>" + c.name + "</strong> — " + c.summary + ". From A$" + c.day.toLocaleString() + " / day, A$" + c.week.toLocaleString() + " / week.\n\n<a href=\"/index.html?car=911#reserve\">Begin a 911 reservation →</a>"; } },

    // Pricing / fleet overview
    { m: [/price|pricing|cost|rate|how much|daily|weekly|fees?\b/i, /list|fleet|cars|cars?\s*do you have|what\s*cars|inventory|range/i],
      r: function () { return fleetList(); } },

    // Delivery
    { m: [/deliver|drop\s*off|drop-off|where|home|hotel|address|jetty|helipad|airport/i],
      r: "We deliver in person, anywhere in Greater Sydney, the Northern Beaches, and the Southern Highlands — complimentary. Hunter Valley and Bowral are a small flat fee. We can deliver to a residence, hotel porte-cochère, jetty, or helipad. Available 24 hours.\n\nWhat suburb were you thinking?" },

    // Insurance / damage
    { m: [/insur|damage|excess|liability|crash|accident/i],
      r: "Every car is insured comprehensively for the duration of your reservation. Standard excess sits between <strong>A$5,000</strong> and <strong>A$15,000</strong> depending on the vehicle. Excess waiver is included on weekly bookings of the Spectre and Purosangue, and available on request elsewhere." },

    // Driver requirements
    { m: [/driver|licen[cs]e|age|young|under\s*\d|requirements|eligible|qualif/i],
      r: "Full Australian or international licence, held for at least three years. Minimum age <strong>30</strong> (35 for the McLaren and Ferrari). One short video call to verify identity. No counter, no queue, no paperwork left behind." },

    // Mileage / range / km
    { m: [/mileage|km|kilomet|distance|how far|km\/day|km per/i],
      r: "<strong>300 km included</strong> per day, <strong>1,500 km per week</strong> — generous for a Bowral weekend or a Palm Beach loop. Beyond that, A$3.50 / km. Cars may be driven anywhere in NSW; interstate by arrangement." },

    // Cancellation
    { m: [/cancel|refund|change\s*date|reschedule/i],
      r: "Full refund up to <strong>48 hours</strong> before delivery. Inside 48 hours, the deposit is held against a future booking — never lost. If we miss our delivery window by more than fifteen minutes, the day is on us." },

    // Booking / how to reserve
    { m: [/book|reserve|reservation|inquir|how do i|how to|next step/i],
      r: "Send the form on this site (delivery suburb + dates + the feeling you're after) — a member of our concierge team replies within the hour. Or speak directly: <a href=\"tel:+61292644471\">+61 2 9264 4471</a> · <a href=\"mailto:concierge@noctis.com.au\">concierge@noctis.com.au</a> · Signal @noctis.sydney." },

    // Privacy / discretion
    { m: [/privacy|discreet|discret|confiden|anonymous|anon/i],
      r: "Discretion is the house. Your details are read by a single concierge and held only for the duration of your stay. We are not on social media as a company-of-record. We do not photograph or post about our guests." },

    // Drives / where to go
    { m: [/where to drive|good road|best route|recommend.*drive|breakfast|sunday drive|day trip|where should|sydney.*drive|drive.*sydney/i],
      r: "A few favourites:\n\n• <strong>Old Pacific Highway</strong> before 7 — sandstone-cut, motorbike-quiet at dawn\n• <strong>West Head via Akuna Bay</strong> — narrower, slower, deeply pretty\n• <strong>Royal National Park</strong>, Audley → Bundeena, especially in autumn\n\nThere's a full guide in <a href=\"/journal/breakfast-drives.html\">our journal</a>." },

    // Hours / availability
    { m: [/hours|open|when.*available|24|night|after\s*hours|early|late/i],
      r: "We're a 24-hour concierge. Reservations confirmed within two hours by a human, including overnight. The fleet itself can be delivered at any time you specify, including before dawn for a long drive." },

    // Payment
    { m: [/pay|payment|deposit|wire|card|amex|visa|stripe|crypto|bitcoin/i],
      r: "30% deposit on confirmation (wire or card), final settlement after the car comes home. We accept Visa, Mastercard, AmEx, and direct wire. We don't accept crypto for now." },

    // Refund / return policy edge cases (kept tight)
    { m: [/return|drop\s*back|come back|hand over keys/i],
      r: "When you're done, leave the keys with the front desk or the driver we send. Final settlement follows by wire within seven days." },

    // About / company
    { m: [/who.*you|about\s*noctis|about you|history|founded|started|when did|story|owners?/i],
      r: "Noctis is a private automotive house at <strong>Pier 6/7, Walsh Bay</strong>. Established 2019. Six cars, three concierges, one head of fleet. ACN 638 472 901." },

    // Address / location
    { m: [/where.*you|address|located|location|office|workshop|walsh bay/i],
      r: "Pier 6/7, Walsh Bay, Sydney NSW 2000. By appointment only — guests don't usually visit, but the workshop is open if you'd like to see the fleet in person." },

    // Contact
    { m: [/contact|phone|number|call|email|signal|whatsapp/i],
      r: "<a href=\"tel:+61292644471\">+61 2 9264 4471</a> · <a href=\"mailto:concierge@noctis.com.au\">concierge@noctis.com.au</a> · Signal @noctis.sydney. Answered 24 hours." },

    // Yes / no / thanks / OK
    { m: [/^(yes|y|yeah|yep|sure|ok|okay|sounds good|cool)\b/i],
      r: "Lovely. Anything else? Pricing, delivery, drivers, or a specific car?" },
    { m: [/^(no|n|nah|not really|nope)\b/i],
      r: "Understood. If something comes up, the form on the page goes to a human within the hour." },
    { m: [/thank|thanks|appreciate|cheers/i],
      r: "Pleasure. Reply here any time, or send the form for a human reply within the hour." },

    // Goodbye
    { m: [/^(bye|goodbye|see you|cya|talk later|catch you)\b/i],
      r: "Drive well." },

    // Human / agent
    { m: [/human|real person|agent|speak to|talk to someone|customer service|operator/i],
      r: "Of course. You can reach a concierge directly: <a href=\"tel:+61292644471\">+61 2 9264 4471</a> · <a href=\"mailto:concierge@noctis.com.au\">concierge@noctis.com.au</a>. Or send the form on the page — replies within the hour." }
  ];

  // Default response
  function defaultReply() {
    return "I might've missed that one. Try asking about <strong>pricing</strong>, <strong>delivery</strong>, <strong>insurance</strong>, <strong>drivers</strong>, or a specific car (Spectre, DB12, 750S, Purosangue, G 63, 911). Or I can put you onto a human at <a href=\"mailto:concierge@noctis.com.au\">concierge@noctis.com.au</a>.";
  }

  function findReply(input) {
    var text = (input || "").trim();
    if (!text) return defaultReply();
    for (var i = 0; i < RULES.length; i++) {
      var rule = RULES[i];
      for (var j = 0; j < rule.m.length; j++) {
        var pat = rule.m[j];
        if (pat instanceof RegExp ? pat.test(text) : text.toLowerCase().indexOf(pat) !== -1) {
          return typeof rule.r === "function" ? rule.r() : rule.r;
        }
      }
    }
    return defaultReply();
  }

  // ---------- DOM / UI ----------
  var STYLE_ID = "noctis-chat-style";
  var ROOT_ID = "noctis-chat-root";

  function injectStyle() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement("style");
    s.id = STYLE_ID;
    s.textContent = "\n#noctis-chat-root { --nc-bg:#0f0f0f; --nc-line:#222; --nc-cream:#F5F1EA; --nc-muted:#8C8576; --nc-accent:#6B0F1A; }\n#noctis-chat-root * { box-sizing:border-box; font-family:'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif; }\n.noctis-fab { position:fixed; right:24px; bottom:24px; z-index:9999; display:flex; align-items:center; gap:10px; padding:14px 18px 14px 16px; background:#0f0f0f; color:#F5F1EA; border:1px solid #2a2a2a; border-radius:48px; box-shadow:0 10px 32px rgba(0,0,0,0.55); cursor:pointer; transition:transform 200ms ease, box-shadow 200ms ease, background 200ms ease; font-size:13px; letter-spacing:0.04em; }\n.noctis-fab:hover { transform:translateY(-1px); background:#161513; box-shadow:0 14px 38px rgba(0,0,0,0.6); }\n.noctis-fab .dot { width:8px; height:8px; border-radius:50%; background:#5DCC83; box-shadow:0 0 0 0 rgba(93,204,131,0.6); animation:nc-pulse 2.4s ease-out infinite; }\n@keyframes nc-pulse { 0% { box-shadow:0 0 0 0 rgba(93,204,131,0.6); } 70% { box-shadow:0 0 0 8px rgba(93,204,131,0); } 100% { box-shadow:0 0 0 0 rgba(93,204,131,0); } }\n.noctis-fab span.lbl { font-family:'Fraunces', serif; font-size:14px; letter-spacing:-0.01em; font-style:italic; font-weight:300; }\n.noctis-fab.is-open { display:none; }\n.noctis-panel { position:fixed; right:24px; bottom:24px; z-index:9999; width:360px; max-width:calc(100vw - 32px); height:540px; max-height:calc(100vh - 48px); background:#0d0d0d; border:1px solid #1f1f1f; border-radius:14px; box-shadow:0 20px 60px rgba(0,0,0,0.7); display:flex; flex-direction:column; overflow:hidden; transform:translateY(20px) scale(0.97); opacity:0; pointer-events:none; transition:transform 280ms cubic-bezier(0.22,1,0.36,1), opacity 220ms ease; }\n.noctis-panel.is-open { transform:translateY(0) scale(1); opacity:1; pointer-events:auto; }\n.noctis-head { display:flex; align-items:center; justify-content:space-between; padding:14px 18px; border-bottom:1px solid #1a1a1a; background:linear-gradient(to bottom, #131313, #0d0d0d); }\n.noctis-head .who { display:flex; align-items:center; gap:12px; }\n.noctis-head .av { width:34px; height:34px; border-radius:50%; background:#1a1a1a; display:flex; align-items:center; justify-content:center; color:#F5F1EA; font-family:'Fraunces',serif; font-style:italic; font-size:18px; border:1px solid #262626; }\n.noctis-head .name { font-family:'Fraunces',serif; font-size:14px; letter-spacing:-0.01em; color:#F5F1EA; }\n.noctis-head .role { font-size:11px; color:#8C8576; letter-spacing:0.05em; margin-top:2px; }\n.noctis-head .close { background:none; border:none; color:#8C8576; cursor:pointer; padding:6px; border-radius:6px; transition:color 0.2s, background 0.2s; }\n.noctis-head .close:hover { color:#F5F1EA; background:#1a1a1a; }\n.noctis-msgs { flex:1; overflow-y:auto; padding:20px 18px; display:flex; flex-direction:column; gap:14px; scroll-behavior:smooth; }\n.noctis-msgs::-webkit-scrollbar { width:6px; }\n.noctis-msgs::-webkit-scrollbar-thumb { background:#222; border-radius:3px; }\n.noctis-msg { font-size:14px; line-height:1.5; max-width:88%; }\n.noctis-msg.bot { align-self:flex-start; color:#F5F1EA; padding:11px 14px; background:#161616; border:1px solid #1f1f1f; border-radius:14px 14px 14px 4px; white-space:pre-wrap; }\n.noctis-msg.you { align-self:flex-end; color:#F5F1EA; padding:11px 14px; background:#6B0F1A; border-radius:14px 14px 4px 14px; }\n.noctis-msg a { color:#F5F1EA; text-decoration:underline; text-decoration-color:rgba(245,241,234,0.4); text-underline-offset:3px; }\n.noctis-msg a:hover { text-decoration-color:#F5F1EA; }\n.noctis-msg.bot strong { color:#fff; font-weight:500; }\n.noctis-typing { align-self:flex-start; padding:14px 16px; background:#161616; border:1px solid #1f1f1f; border-radius:14px 14px 14px 4px; display:flex; gap:5px; }\n.noctis-typing span { width:6px; height:6px; border-radius:50%; background:#8C8576; animation:nc-blink 1.4s infinite both; }\n.noctis-typing span:nth-child(2) { animation-delay:0.2s; }\n.noctis-typing span:nth-child(3) { animation-delay:0.4s; }\n@keyframes nc-blink { 0%,80%,100% { opacity:0.3; } 40% { opacity:1; } }\n.noctis-quick { padding:8px 18px 4px; display:flex; flex-wrap:wrap; gap:6px; }\n.noctis-quick button { background:#161616; border:1px solid #2a2a2a; color:rgba(245,241,234,0.85); padding:7px 12px; border-radius:18px; font-size:12px; cursor:pointer; transition:background .2s, border .2s, color .2s; }\n.noctis-quick button:hover { background:#1c1c1c; border-color:#3a3a3a; color:#F5F1EA; }\n.noctis-input { display:flex; gap:8px; padding:14px 14px 16px; border-top:1px solid #1a1a1a; background:#0a0a0a; }\n.noctis-input input { flex:1; background:#141414; border:1px solid #222; border-radius:24px; padding:11px 16px; color:#F5F1EA; font-size:14px; outline:none; transition:border-color .2s, background .2s; font-family:inherit; }\n.noctis-input input:focus { border-color:#3a3a3a; background:#181818; }\n.noctis-input input::placeholder { color:#5A564F; }\n.noctis-input button { background:#6B0F1A; color:#F5F1EA; border:none; border-radius:24px; padding:0 16px; font-size:13px; letter-spacing:0.04em; cursor:pointer; transition:background .2s; min-width:60px; }\n.noctis-input button:hover { background:#821426; }\n.noctis-foot { padding:6px 18px 10px; text-align:center; color:#5A564F; font-size:10px; letter-spacing:0.06em; }\n@media (max-width: 480px) { .noctis-fab { right:14px; bottom:14px; padding:12px 16px 12px 14px; font-size:12px; } .noctis-panel { right:8px; bottom:8px; left:8px; width:auto; height:calc(100vh - 16px); max-height:660px; border-radius:12px; } }\n";
    document.head.appendChild(s);
  }

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) for (var k in attrs) {
      if (k === "html") node.innerHTML = attrs[k];
      else if (k === "on") for (var ev in attrs.on) node.addEventListener(ev, attrs.on[ev]);
      else node.setAttribute(k, attrs[k]);
    }
    if (children) (Array.isArray(children) ? children : [children]).forEach(function (c) {
      if (c) node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    });
    return node;
  }

  function buildUI() {
    if (document.getElementById(ROOT_ID)) return;
    var root = document.createElement("div");
    root.id = ROOT_ID;

    // FAB (closed state)
    var fab = el("button", { class: "noctis-fab", "aria-label": "Open concierge chat" }, [
      el("span", { class: "dot" }),
      el("span", { class: "lbl" }, "Speak with concierge")
    ]);

    // Panel (open state)
    var msgs = el("div", { class: "noctis-msgs", "aria-live": "polite" });
    var quick = el("div", { class: "noctis-quick" });
    var input = el("input", { type: "text", placeholder: "Ask about a car, pricing, delivery…", "aria-label": "Type your message" });
    var sendBtn = el("button", null, "Send");

    var head = el("div", { class: "noctis-head" }, [
      el("div", { class: "who" }, [
        el("div", { class: "av" }, "N"),
        el("div", null, [
          el("div", { class: "name" }, "Noctis · Concierge"),
          el("div", { class: "role" }, "AI · usually replies instantly")
        ])
      ]),
      el("button", { class: "close", "aria-label": "Close" }, "✕")
    ]);

    var inputRow = el("div", { class: "noctis-input" }, [input, sendBtn]);
    var foot = el("div", { class: "noctis-foot" }, "AI assistant · For urgent matters call +61 2 9264 4471");

    var panel = el("div", { class: "noctis-panel", role: "dialog", "aria-label": "Noctis concierge chat" }, [head, msgs, quick, inputRow, foot]);

    root.appendChild(fab);
    root.appendChild(panel);
    document.body.appendChild(root);

    // Quick chips
    [
      { label: "Pricing", q: "What are your daily rates?" },
      { label: "Delivery", q: "Where do you deliver?" },
      { label: "Insurance", q: "What about insurance?" },
      { label: "Best drives near Sydney", q: "What's a good drive near Sydney?" }
    ].forEach(function (chip) {
      var b = el("button", null, chip.label);
      b.addEventListener("click", function () { send(chip.q); });
      quick.appendChild(b);
    });

    // ---------- behaviour ----------
    function open() { panel.classList.add("is-open"); fab.classList.add("is-open"); setTimeout(function () { input.focus(); }, 280); }
    function close() { panel.classList.remove("is-open"); fab.classList.remove("is-open"); }
    fab.addEventListener("click", open);
    head.querySelector(".close").addEventListener("click", close);

    function appendMsg(text, who) {
      var m = el("div", { class: "noctis-msg " + (who || "bot"), html: text });
      msgs.appendChild(m);
      msgs.scrollTop = msgs.scrollHeight;
    }

    function appendTyping() {
      var t = el("div", { class: "noctis-typing" }, [el("span"), el("span"), el("span")]);
      msgs.appendChild(t);
      msgs.scrollTop = msgs.scrollHeight;
      return t;
    }

    function send(raw) {
      var text = (raw == null ? input.value : raw).trim();
      if (!text) return;
      input.value = "";
      appendMsg(text.replace(/&/g, "&amp;").replace(/</g, "&lt;"), "you");
      var t = appendTyping();
      setTimeout(function () {
        t.remove();
        appendMsg(findReply(text), "bot");
      }, 600 + Math.random() * 600);
    }

    sendBtn.addEventListener("click", function () { send(); });
    input.addEventListener("keydown", function (e) { if (e.key === "Enter") send(); });

    // Greeting
    setTimeout(function () {
      appendMsg("Welcome to Noctis. I'm the after-hours concierge — happy to talk through the fleet, pricing, delivery, or a specific car. What can I help with?", "bot");
    }, 200);

    // Hide the FAB while the user is interacting with the Reserve form on
    // small screens — the chat pill otherwise sits on top of the Send button.
    function setupReserveHider() {
      var reserveSection = document.getElementById("reserve");
      if (!reserveSection || !("IntersectionObserver" in window)) return;
      var io = new IntersectionObserver(function (entries) {
        var isMobile = window.innerWidth <= 720;
        var inReserve = entries.some(function (e) { return e.isIntersecting; });
        if (panel.classList.contains("is-open")) return; // don't hide if user opened it
        if (inReserve && isMobile) {
          fab.style.opacity = "0";
          fab.style.pointerEvents = "none";
          fab.style.transform = "translateY(40px)";
        } else {
          fab.style.opacity = "";
          fab.style.pointerEvents = "";
          fab.style.transform = "";
        }
      }, { threshold: 0.25 });
      io.observe(reserveSection);
    }
    setupReserveHider();
  }

  function init() {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", function () { injectStyle(); buildUI(); });
    } else {
      injectStyle();
      buildUI();
    }
  }

  init();
})();
