/* ==========================================================================
   MCIdentity docs — shared client-side include loader & nav behaviour
   Loads docs/partials/header.html + footer.html into every page and wires up
   the mobile menu and active-section highlighting. No external dependencies.
   ========================================================================== */
(function () {
  "use strict";

  // Relative path from the current page back to /docs. Each page sets this.
  var ROOT = window.SITE_ROOT || "";
  var SECTION = window.PAGE_SECTION || "";

  function injectPartial(targetId, file, after) {
    var mount = document.getElementById(targetId);
    if (!mount) { if (after) after(); return; }
    fetch(ROOT + "partials/" + file)
      .then(function (r) { return r.ok ? r.text() : ""; })
      .then(function (html) {
        // Resolve root-relative links inside the partial.
        mount.innerHTML = html.replace(/\{\{ROOT\}\}/g, ROOT);
        if (after) after();
      })
      .catch(function () { if (after) after(); });
  }

  function wireHeader() {
    // Active section highlight.
    if (SECTION) {
      var links = document.querySelectorAll('[data-section="' + SECTION + '"]');
      for (var i = 0; i < links.length; i++) links[i].classList.add("is-active");
    }
    // Mobile toggle.
    var toggle = document.querySelector(".nav__toggle");
    var links = document.getElementById("nav-links");
    if (toggle && links) {
      toggle.addEventListener("click", function () {
        links.classList.toggle("is-open");
      });
      links.addEventListener("click", function (e) {
        if (e.target.closest("a") && !e.target.closest(".nav__dd-toggle")) {
          links.classList.remove("is-open");
        }
      });
    }
    // Update footer year.
    var y = document.getElementById("footer-year");
    if (y) y.textContent = new Date().getFullYear();
  }

  function ensureFavicon() {
    if (document.querySelector('link[rel="icon"]')) return;
    var svg =
      "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>" +
      "<rect width='32' height='32' rx='7' fill='%23d7dde6'/>" +
      "<text x='16' y='22' font-family='Arial, sans-serif' font-size='15' " +
      "font-weight='bold' text-anchor='middle' fill='%233f5872'>ID</text></svg>";
    var link = document.createElement("link");
    link.rel = "icon";
    link.href = "data:image/svg+xml," + svg;
    document.head.appendChild(link);
  }

  document.addEventListener("DOMContentLoaded", function () {
    ensureFavicon();
    injectPartial("site-header", "header.html", wireHeader);
    injectPartial("site-footer", "footer.html", function () {
      var y = document.getElementById("footer-year");
      if (y) y.textContent = new Date().getFullYear();
    });
  });
})();
