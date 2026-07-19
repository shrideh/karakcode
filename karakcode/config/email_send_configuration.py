# ----------------------------------------------------------
# #############################                             
# # إعدادات البريد الالكتروني (الحديثة) #                             
# # #############################                             
# ----------------------------------------------------------
from karakcode.env import EMAIL_PASSWORD
# هذه الإعدادات تبقى كما هي خارج MAILERS لأنها تحدد هوية المرسل (Metadata)
SERVER_EMAIL = "karakcode@gmail.com"
DEFAULT_FROM_EMAIL = "karakcode@gmail.com"

# تجميع كل إعدادات الاتصال والسيرفر في مكان واحد
MAILERS = {
    "default": {
        # نضع هنا موديول Celery الخاص بك لإرسال البريد في الخلفية
        "BACKEND": "djcelery_email.backends.CeleryEmailBackend",
        "OPTIONS": {
            "host": "smtp.gmail.com",
            "port": 587,
            "use_tls": True,
            "username": "karakcode@gmail.com",
            "password": EMAIL_PASSWORD,  # ضع رمز تطبيق Gmail (App Password) هنا
        },
    },
}