// mobile nav toggle
  var navToggle = document.getElementById('navToggle');
  var navLinks = document.getElementById('navLinks');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function(){
      var open = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open);
    });
    navLinks.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // portfolio filter
  var filterButtons = document.querySelectorAll('.filter-btn');
  var cards = document.querySelectorAll('.project-card');
  var countEl = document.getElementById('projectCount');
  var grid = document.getElementById('projectGrid');

  // Honour the OS setting: no fade, no stagger, just swap.
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var FADE_MS = 160;   // must stay in step with .project-grid.is-filtering in style.css
  var STAGGER_MS = 40;
  var pending = null;

  // shown when a filter matches nothing, so the grid never just goes blank
  var emptyEl = null;
  if (grid) {
    emptyEl = document.createElement('p');
    emptyEl.className = 'project-empty';
    emptyEl.hidden = true;
    emptyEl.textContent = 'Nothing here yet.';
    grid.appendChild(emptyEl);
  }

  function matches(card, filter){
    if (filter === 'all') return true;
    if (filter === 'featured') return card.hasAttribute('data-featured');
    return card.getAttribute('data-category') === filter;
  }

  // Swap which cards are in the grid and keep the count label in step.
  function commit(filter){
    var shown = 0;
    cards.forEach(function(card){
      var show = matches(card, filter);
      card.classList.toggle('is-hidden', !show);
      if (show) shown++;
    });
    if (countEl) countEl.textContent = shown + (shown === 1 ? ' project' : ' projects');
    if (emptyEl) emptyEl.hidden = shown !== 0;
    return shown;
  }

  // Cards fade back in one after another. Re-adding the class needs a reflow
  // between removal and re-add, or the browser never restarts the animation.
  function stagger(){
    var i = 0;
    cards.forEach(function(card){
      card.classList.remove('is-entering');
      card.style.animationDelay = '';
      if (card.classList.contains('is-hidden')) return;
      void card.offsetWidth;
      card.style.animationDelay = (i * STAGGER_MS) + 'ms';
      card.classList.add('is-entering');
      i++;
    });
  }

  function applyFilter(filter, animate){
    if (!animate || reduceMotion || !grid) {
      commit(filter);
      return;
    }
    // A second click mid-transition shouldn't leave the grid stuck invisible.
    if (pending) clearTimeout(pending);
    grid.classList.add('is-filtering');
    if (countEl) countEl.classList.add('is-updating');
    pending = setTimeout(function(){
      pending = null;
      commit(filter);
      grid.classList.remove('is-filtering');
      if (countEl) countEl.classList.remove('is-updating');
      stagger();
    }, FADE_MS);
  }

  // Once the entrance has played, take the class off. Its fill-mode pins
  // transform:none, which would otherwise kill the hover lift.
  cards.forEach(function(card){
    card.addEventListener('animationend', function(e){
      if (e.animationName === 'cardIn') {
        card.classList.remove('is-entering');
        card.style.animationDelay = '';
      }
    });
  });

  filterButtons.forEach(function(btn){
    btn.addEventListener('click', function(){
      if (btn.classList.contains('active')) return; // already showing this one
      filterButtons.forEach(function(b){
        b.classList.remove('active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');
      applyFilter(btn.getAttribute('data-filter'), true);
    });
  });

  // Open on whichever filter the markup marks as active — Featured, so the
  // grid leads with the work worth seeing rather than everything at once.
  if (cards.length) {
    var initial = document.querySelector('.filter-btn.active');
    applyFilter(initial ? initial.getAttribute('data-filter') : 'all', false);
  }
