# -------------------------------------------------------------------- #
# اعدادت الامان 
# python manage.py check --deploy
from django.conf import settings
if not settings.DEBUG:  
    # Host Header Validation
    ALLOWED_HOSTS = ["karakcode.com", "www.karakcode.com"] 
    # https     
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # Cookies
    SESSION_COOKIE_NAME = "__Host-sessionid"
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    LANGUAGE_COOKIE_SECURE = True
    LANGUAGE_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    # CSRF
    CSRF_COOKIE_NAME = "__Host-csrftoken"
    CSRF_TRUSTED_ORIGINS = [f'https://{host}' for host in ALLOWED_HOSTS]
    CSRF_COOKIE_HTTPONLY = True
    # XSS & Clickjacking
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
    # SECURE_CSP
    from django.utils.csp import CSP
    settings.MIDDLEWARE += [
        "django.middleware.csp.ContentSecurityPolicyMiddleware",
    ]
    SECURE_CSP = {
        "default-src": [CSP.SELF],
        "script-src": [CSP.SELF, CSP.NONCE],
        "style-src": [CSP.SELF, CSP.NONCE],
        "img-src": [CSP.SELF, "data:"],
        "object-src": [CSP.NONE],
        "base-uri": [CSP.SELF],
        "frame-ancestors": [CSP.NONE],
        "form-action": [CSP.SELF],
    }
    
    # -----------------------------------------------------
    # ADMINS (إشعارات المشرفين)
    # هذا الإعداد مخصص لـ الإخطار الفني عند حدوث خطأ برمجية أثناء تشغيل الموقع  
    # (DEBUG=False).
    # -----------------------------------------------------
    ADMINS = [
    'karakcode@gmail.com',                  # يمكن استخدام بريد إلكتروني بسيط بهذا الشكل
    ]