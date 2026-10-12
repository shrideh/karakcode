# -------------------------------------------------------------------- #
# إعدادات الأمان — تُفعَّل في الإنتاج فقط
# python manage.py check --deploy
from django.conf import settings
from karakcode.settings import MIDDLEWARE
if not settings.DEBUG:   # ← المتغير المحلي المعرّف أعلى الملف، وليس settings.DEBUG
    from django.utils.csp import CSP

    ALLOWED_HOSTS = ["karakcode.com", "www.karakcode.com"]

    # --- HTTPS ---
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
    SECURE_SSL_REDIRECT = True
    # إلزامي خلف بروكسي عكسي (nginx/Caddy) وإلا حلقة توجيه 310
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # --- الكوكيز ---
    # بادئة __Host- تشترط: Secure + Path=/ + بلا Domain (افتراضيات Django تحققها)
    SESSION_COOKIE_NAME = "__Host-sessionid"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    CSRF_COOKIE_NAME = "__Host-csrftoken"
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SAMESITE = "Lax"
    LANGUAGE_COOKIE_SECURE = True
    LANGUAGE_COOKIE_HTTPONLY = True
    CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]

    # --- XSS & Clickjacking ---
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"

    # --- CSP ---
    MIDDLEWARE += ["django.middleware.csp.ContentSecurityPolicyMiddleware"]

    SECURE_CSP = {
        "default-src": [CSP.SELF],
        # ★ بلا CSP.NONCE — غير متوافق مع cache_page_custom (انظر الشرح)
        # ★ بلا unsafe-inline — الكود السطري تحول لملفات خارجية مسبقاً
        "script-src": [CSP.SELF],
        "style-src": [CSP.SELF, "https://fonts.googleapis.com"],
        "font-src":  [CSP.SELF, "https://fonts.gstatic.com"],
        "img-src": [CSP.SELF],                 # أزلنا data: بعد الفافيكون الثابت
        "connect-src": [CSP.SELF],
        "object-src": [CSP.NONE],
        "base-uri": [CSP.SELF],
        "frame-ancestors": [CSP.NONE],
        "form-action": [CSP.SELF],
        "upgrade-insecure-requests": [],       # توجيه ضمني لأي http: إلى https:
    }

    # --- إشعارات الأخطاء للمشرفين ---
    # ★ الصيغة الصحيحة: tuples (الاسم، البريد) — القائمة النصية لن تعمل
    ADMINS = [("KarakCode", "karakcode@gmail.com")]
    # تنبيهات البريد تحتاج إعداد SMTP فعلي:
    # SERVER_EMAIL = "errors@karakcode.com"
    # EMAIL_HOST / EMAIL_PORT / EMAIL_HOST_USER ...