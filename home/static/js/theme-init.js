(function () {
    var t = null;
    try { t = localStorage.getItem('kc-theme'); } catch (e) { }
    if (t !== 'light' && t !== 'dark') {
        t = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    document.documentElement.setAttribute('data-theme', t);
    document.documentElement.classList.add('js');
    var m = document.querySelector('meta[name="theme-color"]');
    if (m) m.setAttribute('content', t === 'dark' ? '#171209' : '#FAF5EC');
})();