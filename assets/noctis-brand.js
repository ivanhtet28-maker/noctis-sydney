/* ============================================================
   NOCTIS — per-buyer wordmark swap
   Reads ?b=<slug> from the URL (set by Vercel rewrite for
   /<slug> URLs) OR sessionStorage.brandSlug (for in-site
   navigation), looks up the brand in window.NOCTIS_BRANDS,
   and swaps every "Noctis" wordmark on the page.
   ============================================================ */
(function () {
  "use strict";

  // Resolve the brand slug from URL → sessionStorage → null.
  function getBrand() {
    var url = new URL(window.location.href);
    var slug = (url.searchParams.get("b") || url.searchParams.get("for") || "").toLowerCase().trim();
    var STORAGE_KEY = "noctisBrandSlug";

    // If a slug arrives in the URL, treat it as authoritative — overwrite
    // any previously-stored slug. Empty slug means "reset to Noctis".
    if (slug) {
      try { sessionStorage.setItem(STORAGE_KEY, slug); } catch (e) {}
    } else {
      try { slug = sessionStorage.getItem(STORAGE_KEY) || ""; } catch (e) {}
    }

    if (!slug) return null;
    if (!window.NOCTIS_BRANDS || !window.NOCTIS_BRANDS[slug]) return null;
    return Object.assign({ slug: slug }, window.NOCTIS_BRANDS[slug]);
  }

  // Swap the wordmark text everywhere it appears.
  function applyBrand(brand) {
    var name = brand.name;

    // 1. NAV wordmark — every page has a <span class="font-serif"> "Noctis" </span>
    //    inside <header class="noctis-nav">.
    var navMarks = document.querySelectorAll('header .font-serif, header.noctis-nav .font-serif');
    navMarks.forEach(function (el) {
      if ((el.textContent || "").trim() === "Noctis") {
        el.textContent = name;
        el.dataset.brandMark = "nav";
        if (name.length > 14) el.style.fontSize = "calc(1em - 2px)";
      }
    });

    // 2. FOOTER wordmark — index.html has a large <p> with "Noctis";
    //    fleet/journal/legal pages have a smaller <p class="name"> or
    //    <p class="font-serif"> with "Noctis".
    var footerMarks = document.querySelectorAll('footer .font-serif, footer .name, footer p');
    footerMarks.forEach(function (el) {
      if ((el.textContent || "").trim() === "Noctis") {
        el.textContent = name;
        el.dataset.brandMark = "footer";
      }
    });

    // 3. CRM sidebar — replace "Concierge CRM" label with "[Buyer] · Concierge CRM"
    var crmLabel = document.querySelector('.brand .label');
    if (crmLabel && /Concierge CRM/i.test(crmLabel.innerHTML) && !crmLabel.dataset.brandApplied) {
      // Preserve the <small>...</small> sibling
      var small = crmLabel.querySelector('small');
      crmLabel.innerHTML = name + ' · Concierge CRM';
      if (small) crmLabel.appendChild(small);
      crmLabel.dataset.brandApplied = "1";
    }

    // 4. Document title — replace any "Noctis" substring
    if (document.title.indexOf("Noctis") !== -1) {
      document.title = document.title.replace(/Noctis/g, name);
    }

    // 5. The chat widget greeting refers to "Noctis"; we leave the bot's
    //    persona alone since it's the assistant identity, not the buyer's.
    //    But we do hide the small "Noctis" inline inside the chat panel
    //    if it would be visually loud — currently it isn't, so no change.

    // 6. Floating "Demo prepared for [Buyer]" pill — bottom-left.
    if (!document.getElementById("noctis-demo-tag")) {
      var tag = document.createElement("div");
      tag.id = "noctis-demo-tag";
      tag.style.cssText = [
        "position:fixed",
        "bottom:14px",
        "left:14px",
        "z-index:48",
        "padding:8px 14px 8px 12px",
        "background:rgba(10,10,10,0.78)",
        "border:1px solid #1F1E1B",
        "border-radius:22px",
        "font-family:'Inter', system-ui, sans-serif",
        "font-size:10px",
        "letter-spacing:0.14em",
        "text-transform:uppercase",
        "color:#8C8576",
        "backdrop-filter:blur(18px)",
        "-webkit-backdrop-filter:blur(18px)",
        "display:flex",
        "align-items:center",
        "gap:8px",
        "max-width:calc(100vw - 28px)"
      ].join(";");
      tag.innerHTML =
        '<span style="width:6px;height:6px;border-radius:50%;background:#5DCC83;flex-shrink:0;"></span>' +
        '<span>Demo prepared for ' +
          '<strong style="color:#F5F1EA;font-weight:500;letter-spacing:0.04em;font-family:\'Fraunces\', serif;font-style:italic;font-size:13px;text-transform:none;">' +
            escapeHtml(name) +
          '</strong>' +
        '</span>';
      document.body.appendChild(tag);
    }
  }

  function escapeHtml(s) {
    return (s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function init() {
    var brand = getBrand();
    if (!brand) return; // Default Noctis branding — nothing to do.
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", function () { applyBrand(brand); });
    } else {
      applyBrand(brand);
    }
  }

  init();
})();
