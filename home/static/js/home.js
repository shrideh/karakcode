/* js/home.js — كرك كود: التفاعلات العامة */
(function () {
    'use strict';
    var root = document.documentElement;

    /* ===== 1) تبديل الوضع الفاتح/الداكن ===== */
    var themeBtn = document.getElementById('theme-toggle');
    var metaTheme = document.querySelector('meta[name="theme-color"]');

    function applyTheme(theme, remember) {
        root.setAttribute('data-theme', theme);
        if (metaTheme) metaTheme.setAttribute('content', theme === 'dark' ? '#171209' : '#FAF5EC');
        if (themeBtn) themeBtn.setAttribute('aria-pressed', String(theme === 'dark'));
        if (remember) {
            try { localStorage.setItem('kc-theme', theme); } catch (e) { /* الوضع الخاص */ }
        }
    }

    if (themeBtn) {
        themeBtn.addEventListener('click', function () {
            applyTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark', true);
        });
    }

    /* تتبّع تفضيل النظام ما لم يختر المستخدم يدوياً */
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    var onSystemChange = function (e) {
        var saved = null;
        try { saved = localStorage.getItem('kc-theme'); } catch (err) {}
        if (!saved) applyTheme(e.matches ? 'dark' : 'light', false);
    };
    if (mq.addEventListener) mq.addEventListener('change', onSystemChange);

    /* ===== 2) قائمة الجوال ===== */
    var navToggle = document.getElementById('nav-toggle');
    var nav = document.getElementById('site-nav');

    function setMenu(open) {
        if (!nav || !navToggle) return;
        nav.classList.toggle('open', open);
        navToggle.setAttribute('aria-expanded', String(open));
        navToggle.setAttribute('aria-label', open ? 'إغلاق القائمة' : 'فتح القائمة');
    }

    if (navToggle && nav) {
        navToggle.addEventListener('click', function () {
            setMenu(!nav.classList.contains('open'));
        });
        nav.addEventListener('click', function (e) {
            if (e.target.closest('a')) setMenu(false);   /* إغلاق بعد اختيار رابط */
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') setMenu(false);
        });
        document.addEventListener('click', function (e) {
            if (nav.classList.contains('open') && !e.target.closest('.site-header')) setMenu(false);
        });
        window.addEventListener('resize', function () {
            if (window.innerWidth > 991) setMenu(false);
        });
    }

    /* ===== 3) ظلّ الشريط العلوي عند التمرير ===== */
    var header = document.querySelector('.site-header');
    var onScroll = function () {
        if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    /* ===== 4) الظهور التدريجي للعناصر ===== */
    var revealEls = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!('IntersectionObserver' in window) || reduceMotion) {
        revealEls.forEach(function (el) { el.classList.add('is-in'); });
    } else {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-in');
                    io.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
        revealEls.forEach(function (el) { io.observe(el); });
    }

    /* ===== 5) سنة الحقوق تلقائياً ===== */
    var yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();
})();