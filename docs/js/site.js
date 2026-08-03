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

  // How many versions the log navigation shows before it starts scrolling.
  var VISIBLE_VERSIONS = 5;

  // How much of the row after them is left showing. Several platforms draw an
  // overlay scrollbar that stays invisible until you scroll, so a cut-off row is
  // what tells a reader there is more below — without it, five versions look
  // like all of them.
  var PEEK = 0.45;

  /**
   * Resolves a URL against the current page and drops a trailing "index.html",
   * so "/logs/skill/" and "/logs/skill/index.html" compare equal.
   */
  function pagePath(href) {
    return new URL(href, location.href).pathname.replace(/index\.html$/, "");
  }

  /**
   * This page's path relative to logs/, or null when it is not a log page.
   */
  function logsRelative(here) {
    var root = pagePath(ROOT + "logs/");
    return here.indexOf(root) === 0 ? here.slice(root.length) : null;
  }

  /**
   * Reads the product groups out of the loaded partial.
   *
   * Each group is an <h4> naming a product followed by its <ul> of versions.
   * Pairing them here rather than listing products in this file keeps the
   * partial the only place a product is declared.
   */
  function readGroups(nav) {
    var lists = nav.getElementsByTagName("ul");
    var groups = [];
    for (var i = 0; i < lists.length; i++) {
      var heading = lists[i].previousElementSibling;
      if (!heading || heading.tagName !== "H4") continue;
      groups.push({
        heading: heading,
        list: lists[i],
        // The core plugin's list has no data-product: it lives at logs/ itself.
        product: lists[i].getAttribute("data-product") || ""
      });
    }
    return groups;
  }

  /**
   * Shows one product's versions at a time, chosen from a dropdown.
   *
   * Stacked, the four lists ran twenty rows down the page. The dropdown names
   * the product, which is why each group's own heading is hidden once it is
   * built — the partial's headings supply the option labels rather than being
   * shown twice.
   */
  function buildProductPicker(nav, groups, here) {
    // Built from elements rather than a <select>: a native select's option list
    // is drawn by the operating system and no stylesheet can reach it, so it
    // could never match the rest of the site. This mirrors the header's
    // Platforms dropdown, and carries the keyboard behaviour a select gave for
    // free — arrow keys, Enter, Escape, and focus returning to the toggle.
    var picker = document.createElement("div");
    picker.className = "logs-picker";

    var toggle = document.createElement("button");
    toggle.type = "button";
    toggle.className = "logs-picker__toggle";
    toggle.setAttribute("aria-haspopup", "listbox");
    toggle.setAttribute("aria-expanded", "false");

    var menu = document.createElement("ul");
    menu.className = "logs-picker__menu";
    menu.setAttribute("role", "listbox");
    menu.setAttribute("aria-label", "Choose a product");
    menu.hidden = true;

    var options = [];
    for (var i = 0; i < groups.length; i++) {
      var option = document.createElement("li");
      option.className = "logs-picker__option";
      option.setAttribute("role", "option");
      option.setAttribute("tabindex", "-1");
      option.textContent = groups[i].heading.textContent.trim();
      menu.appendChild(option);
      options.push(option);
    }

    var selected = 0;

    function show(index) {
      selected = index;
      toggle.textContent = options[index].textContent;
      for (var j = 0; j < groups.length; j++) {
        groups[j].heading.hidden = true;
        groups[j].list.hidden = j !== index;
        options[j].setAttribute("aria-selected", j === index ? "true" : "false");
      }
      // Both need the list on screen: a hidden element measures zero.
      limitHeight(groups[index].list);
      revealCurrent(groups[index].list);
    }

    function setOpen(open, focusIndex) {
      menu.hidden = !open;
      picker.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      if (open) options[typeof focusIndex === "number" ? focusIndex : selected].focus();
    }

    function choose(index) {
      show(index);
      setOpen(false);
      toggle.focus();
    }

    toggle.addEventListener("click", function () { setOpen(menu.hidden); });
    toggle.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        setOpen(true, e.key === "ArrowDown" ? 0 : options.length - 1);
      }
    });

    menu.addEventListener("click", function (e) {
      var index = options.indexOf(e.target);
      if (index !== -1) choose(index);
    });
    menu.addEventListener("keydown", function (e) {
      var at = options.indexOf(document.activeElement);
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        var step = e.key === "ArrowDown" ? 1 : -1;
        options[(at + step + options.length) % options.length].focus();
      } else if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        if (at !== -1) choose(at);
      } else if (e.key === "Escape" || e.key === "Tab") {
        setOpen(false);
        if (e.key === "Escape") toggle.focus();
      }
    });

    // Anywhere outside closes it, the way every other menu on the web behaves.
    document.addEventListener("click", function (e) {
      if (!menu.hidden && !picker.contains(e.target)) setOpen(false);
    });

    picker.appendChild(toggle);
    picker.appendChild(menu);
    nav.insertBefore(picker, nav.firstChild);

    // Open on the product being read rather than on the first in the list.
    var relative = logsRelative(here);
    var product = relative ? relative.split("/")[0] : "";
    var start = 0;
    for (var k = 0; k < groups.length; k++) {
      if (groups[k].product && groups[k].product === product) start = k;
    }
    show(start);
  }

  /**
   * Caps a long list at VISIBLE_VERSIONS rows and lets it scroll.
   *
   * The height is measured from where the last visible row actually sits rather
   * than calculated from row heights and gaps. Spacing here comes from three
   * stylesheets at once — including a global li margin that grid does not
   * collapse — so measuring is the only way to stay right when one changes.
   *
   * @param list A list that is currently on screen.
   */
  function limitHeight(list) {
    if (list.children.length <= VISIBLE_VERSIONS || list.style.maxHeight) return;
    // Cut through the row after the last visible one rather than adding a gap
    // to the row before it: the space between rows is margin plus grid gap, so
    // measuring from the next row itself is what makes the cut land on it.
    var next = list.children[VISIBLE_VERSIONS].getBoundingClientRect();
    var cut = next.top + next.height * PEEK;
    list.style.maxHeight = (cut - list.getBoundingClientRect().top) + "px";
    list.classList.add("is-scrollable");
  }

  /**
   * Scrolls a list so the entry for the page being read is visible.
   *
   * Scrolls the list itself rather than calling scrollIntoView, which would be
   * free to scroll the whole window and jump the reader away from the top of
   * the page they just opened.
   *
   * Moves by the smallest amount that brings the entry into view, and not at
   * all when it is already there. Pinning it to the top instead would push the
   * newer releases above it out of sight, which is the context a reader looking
   * at an old version most wants.
   */
  function revealCurrent(list) {
    if (!list.classList.contains("is-scrollable")) return;
    var current = list.querySelector("a.is-current");
    if (!current) return;

    var view = list.getBoundingClientRect();
    var entry = current.getBoundingClientRect();
    if (entry.top < view.top) {
      list.scrollTop -= view.top - entry.top;
    } else if (entry.bottom > view.bottom) {
      list.scrollTop += entry.bottom - view.bottom;
    }
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

    var groups = readGroups(nav);
    if (groups.length > 1) buildProductPicker(nav, groups, here);

    // Where "back" goes depends on where this page sits under logs/. The
    // product folders come from the partial's own data-product attributes, so
    // adding a product needs no change here.
    var rest = logsRelative(here);
    if (rest === null) return;
    if (rest === "") return; // The logs index is already the top of this tree.

    var product = rest.split("/")[0];
    var known = false;
    for (var j = 0; j < groups.length; j++) {
      if (groups[j].product && groups[j].product === product) known = true;
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
