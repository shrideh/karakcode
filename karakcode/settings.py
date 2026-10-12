from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------------------------------------- #
# local_settings                                                       #
try:
    from .local_settings import DEBUG
except ImportError:
    DEBUG = False

try:
    from .env import SECRET_KEY
except ImportError as exc:
    raise RuntimeError("env.py not found") from exc

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is missing or empty in env.py")
# -------------------------------------------------------------------- #






INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'karakcode.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': False,
        'OPTIONS': {
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                ),
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'karakcode.wsgi.application'






AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -------------------------------------------------------------------- #
# coustom apps                                                       #
INSTALLED_APPS += [
    'home.apps.HomeConfig',
]


# ==================================================================== #
# معرفة جهاز المستخدم  

INSTALLED_APPS += [
    "django_user_agents",
]
MIDDLEWARE += [
    "django_user_agents.middleware.UserAgentMiddleware",
]
USER_AGENTS_CACHE = "default"
# ==================================================================== #
# development settings
if DEBUG:
    INSTALLED_APPS += [
    "debug_toolbar",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    INTERNAL_IPS = [
    "127.0.0.1",
    ]
# -------------------------------------------------------------------- #


# ----------------------------------------------------------
# # python manage.py collectstatic                                                                                          
# ----------------------------------------------------------
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },

    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}


if DEBUG:
    STATIC_URL = "/static/"
else:
    STATIC_URL = "/karakcode/static/"

STATICFILES_DIRS = [
    BASE_DIR, 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = "/uploads/"

MEDIA_ROOT = BASE_DIR / "media"


# -------------------------------------------------------------------- #
# الاعدادات بملفات مستقلة لغايات الترتيب                             #
from .config.db_configuration import *
from .config.celery_beat_configuration import *
from .config.celery_configuration import *
from .config.django_redis_configuration import *
from .config.email_send_configuration import *
from .config.language_configuration import *
from .config.secure_deploy_configuration import *
from .config.logs_configuration import *
# -------------------------------------------------------------------- #

# -------------------------------------------------------------------- #
# -------------------------------------------------------------------- #
# local_settings                                                       #
try: 
    from .local_settings import *
except ImportError:
    pass
# -------------------------------------------------------------------- #