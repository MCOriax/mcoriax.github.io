/* ==========================================================================
   MCIdentity docs — shared client-side include loader & nav behaviour
   Loads docs/partials/header.html, footer.html, and (on log pages)
   logs-nav.html into every page, and wires up the mobile menu, the
   active-section highlighting, and the log version navigation.
   No external dependencies.
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

  /**
   * Resolves a URL against the current page and drops a trailing "index.html",
   * so "/logs/skill/" and "/logs/skill/index.html" compare equal.
   */
  function pagePath(href) {
    return new URL(href, location.href).pathname.replace(/index\.html$/, "");
  }

  /**
   * Marks the entry pointing at this page, and appends the "back" link.
   *
   * Both are per-page, which is exactly why they are computed here instead of
   * being written into the partial — the partial stays one shared list of
   * versions with nothing page-specific in it.
   */
  function wireLogsNav() {
    var nav = document.getElementById("logs-nav");
    if (!nav) return;

    var here = pagePath(location.pathname);

    var links = nav.getElementsByTagName("a");
    for (var i = 0; i < links.length; i++) {
      // The newest entry stands for two URLs: the index that mirrors it, and
      // its own permalink. Either one means the reader is on that release.
      var permalink = links[i].getAttribute("data-permalink");
      if (pagePath(links[i].getAttribute("href")) === here
          || (permalink && pagePath(permalink) === here)) {
        links[i].classList.add("is-current");
      }
    }

    // Where "back" goes depends on where this page sits under logs/. The
    // product folders come from the partial's own data-product attributes, so
    // adding a product needs no change here.
    var logsRoot = pagePath(ROOT + "logs/");
    if (here.indexOf(logsRoot) !== 0) return;

    var rest = here.slice(logsRoot.length);
    if (rest === "") return; // The logs index is already the top of this tree.

    var product = rest.split("/")[0];
    var lists = nav.querySelectorAll("ul[data-product]");
    var known = false;
    for (var j = 0; j < lists.length; j++) {
      if (lists[j].getAttribute("data-product") === product) known = true;
    }

    var back = document.createElement("p");
    back.className = "logs-nav__back";
    var link = document.createElement("a");
    if (known && rest === product + "/") {
      // A product's own index: the only way out is up to the core logs.
      link.href = ROOT + "logs/index.html";
      link.textContent = "← MCIdentity logs";
    } else {
      link.href = known ? ROOT + "logs/" + product + "/index.html" : ROOT + "logs/index.html";
      link.textContent = "← Back to latest";
    }
    back.appendChild(link);
    nav.appendChild(back);
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
    // Only the log pages carry the mount; everywhere else this is a no-op.
    injectPartial("logs-nav", "logs-nav.html", wireLogsNav);
  });
})();
