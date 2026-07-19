# -------------------------------------------------------------------- #
# LANGUAGE                                                             #
# -------------------------------------------------------------------- #
from django.utils.translation import gettext_lazy as _
from django.conf import settings

LOCALE_PATHS = [settings.BASE_DIR / "locale"]

LANGUAGE_CODE = "ar"  # اللغة الافتراضية (عربية في هذه الحالة)

LANGUAGE_COOKIE_NAME = "ui_language"  # اسم الكوكيز للغة

TIME_ZONE = "Asia/Amman"

USE_I18N = True

USE_TZ = True


LANGUAGES = [
    ("en", _("English")),
    ("ar", _("Arabic")),
]