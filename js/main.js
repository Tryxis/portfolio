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

  // shown when a filter matches nothing, so the grid never just goes blank
  var emptyEl = null;
  if (grid) {
    emptyEl = document.createElement('p');
    emptyEl.className = 'project-empty';
    emptyEl.hidden = true;
    emptyEl.textContent = 'Nothing here yet.';
    grid.appendChild(emptyEl);
  }

  function applyFilter(filter){
    var shown = 0;
    cards.forEach(function(card){
      var match = filter === 'all' || card.getAttribute('data-category') === filter;
      card.classList.toggle('is-hidden', !match);
      if (match) shown++;
    });
    if (countEl) countEl.textContent = shown + (shown === 1 ? ' project' : ' projects');
    if (emptyEl) emptyEl.hidden = shown !== 0;
  }

  filterButtons.forEach(function(btn){
    btn.addEventListener('click', function(){
      filterButtons.forEach(function(b){
        b.classList.remove('active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');
      applyFilter(btn.getAttribute('data-filter'));
    });
  });

  // keep the count honest on first paint, however many cards are in the markup
  if (cards.length) applyFilter('all');
