// Salad in Tin Box — minimal interactions
(function(){
  const $ = sel => document.querySelector(sel);
  const $$ = sel => Array.from(document.querySelectorAll(sel));

  // mobile nav toggle
  const toggle = $('.nav-toggle');
  const nav = $('#nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }

  // Menu page filtering
  const search = $('#menu-search');
  const chips = $$('#menu .chip'); // fallback if id used; but we'll query all chips by class
  const allChips = chips.length ? chips : $$('.chip');
  const grid = $('#menu-grid');
  if (grid && allChips.length) {
    let active = 'All';

    function apply() {
      const q = (search?.value || '').trim().toLowerCase();
      $$('#menu-grid .card').forEach(card => {
        const cat = card.getAttribute('data-category');
        const name = card.getAttribute('data-name') || '';
        const matchCat = active === 'All' || cat === active;
        const matchText = !q || name.includes(q);
        card.style.display = matchCat && matchText ? '' : 'none';
      });
    }

    allChips.forEach(chip => chip.addEventListener('click', () => {
      allChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      active = chip.getAttribute('data-filter') || 'All';
      apply();
    }));

    if (search) search.addEventListener('input', apply);
  }

  // Locations search
  const locSearch = $('#loc-search');
  const list = $('#locations-list');
  if (list && locSearch) {
    const items = $$('#locations-list .list-item');
    locSearch.addEventListener('input', () => {
      const q = locSearch.value.trim().toLowerCase();
      items.forEach(el => {
        const name = el.getAttribute('data-name') || '';
        el.style.display = name.includes(q) ? '' : 'none';
      });
    });
  }
})();
