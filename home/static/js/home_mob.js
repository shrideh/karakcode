/*
 * home_mob.js — منطق الصفحة الرئيسية (نسخة الهاتف)
 * يُحمَّل بـ defer فينُفَّذ بعد بناء الشجرة وقبل حدث DOMContentLoaded.
 * لا اعتماد على أي مكتبة خارجية.
 */
(function () {
    "use strict";

    var d = document, root = d.documentElement;
    var motionOK = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* ---------- السنة الحالية في التذييل ---------- */
    var y = d.getElementById('year');
    if (y) y.textContent = new Date().getFullYear();

    /* ---------- التبديل بين الوضع الفاتح والداكن ---------- */
    var tgl = d.getElementById('theme-toggle'),
        meta = d.querySelector('meta[name="theme-color"]');
    if (tgl) {
        tgl.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark');
        tgl.addEventListener('click', function () {
            var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            root.setAttribute('data-theme', next);
            try { localStorage.setItem('kc-theme', next); } catch (e) {}
            if (meta) meta.setAttribute('content', next === 'dark' ? '#171209' : '#FAF5EC');
            tgl.setAttribute('aria-pressed', next === 'dark');
        });
    }

    /* ---------- إخفاء الترويسة عند النزول + شريط تقدّم القراءة ---------- */
    var header = d.querySelector('.site-header'), lastY = window.scrollY, ticking = false;

    function onScroll() {
        var yy = window.scrollY, h = root.scrollHeight - window.innerHeight;
        if (header) {
            header.style.setProperty('--p', h > 0 ? (yy / h) * 100 + '%' : '0%');
            if (yy > lastY + 6 && yy > 140) header.classList.add('hide');
            else if (yy < lastY - 6 || yy <= 140) header.classList.remove('hide');
        }
        lastY = yy; ticking = false;
    }

    window.addEventListener('scroll', function () {
        if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
    }, { passive: true });

    /* ---------- الظهور التدريجي عند التمرير (.reveal) ---------- */
    var reveals = d.querySelectorAll('.reveal');
    if (motionOK && 'IntersectionObserver' in window) {
        var revIO = new IntersectionObserver(function (es) {
            es.forEach(function (e) {
                if (e.isIntersecting) { e.target.classList.add('in'); revIO.unobserve(e.target); }
            });
        }, { threshold: .15, rootMargin: '0px 0px -8% 0px' });
        reveals.forEach(function (el) { revIO.observe(el); });
    } else {
        reveals.forEach(function (el) { el.classList.add('in'); });
    }

    /* ---------- نقاط الشرائح الأفقية (Swipe) — تُولَّد تلقائياً ---------- */
    d.querySelectorAll('[data-carousel]').forEach(function (row) {
        var wrap = row.parentElement.querySelector('.dots');
        if (!wrap) return;

        var cards = Array.prototype.slice.call(row.children);
        var dots = cards.map(function (card, i) {
            var b = d.createElement('button');
            b.type = 'button';
            b.setAttribute('aria-label', 'الانتقال إلى العنصر ' + (i + 1));
            b.addEventListener('click', function () {
                card.scrollIntoView({ behavior: motionOK ? 'smooth' : 'auto', inline: 'center', block: 'nearest' });
            });
            wrap.appendChild(b);
            return b;
        });

        if ('IntersectionObserver' in window) {
            var io = new IntersectionObserver(function (es) {
                es.forEach(function (e) {
                    if (e.isIntersecting) {
                        var i = cards.indexOf(e.target);
                        dots.forEach(function (dg, j) { dg.classList.toggle('on', j === i); });
                    }
                });
            }, { root: row, threshold: .6 });
            cards.forEach(function (c) { io.observe(c); });
        } else {
            dots[0].classList.add('on');
        }
    });

    /* ---------- تفعيل عنصر التنقل السفلي حسب القسم المرئي ---------- */
    var navLinks = Array.prototype.slice.call(d.querySelectorAll('.bn-item'));
    var byId = {};
    navLinks.forEach(function (l) { byId[l.getAttribute('href').slice(1)] = l; });

    if ('IntersectionObserver' in window) {
        var secIO = new IntersectionObserver(function (es) {
            es.forEach(function (e) {
                if (e.isIntersecting && byId[e.target.id]) {
                    navLinks.forEach(function (l) { l.classList.remove('active'); });
                    byId[e.target.id].classList.add('active');
                }
            });
        }, { rootMargin: '-40% 0px -55% 0px' });

        ['hero', 'services', 'heritage', 'contact'].forEach(function (id) {
            var s = d.getElementById(id);
            if (s) secIO.observe(s);
        });
    }
})();