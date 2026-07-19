#################################
# # REDIS CONFIGURATION OPTIONS #
from django.conf import settings

if not settings.DEBUG:
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/3",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "IGNORE_EXCEPTIONS": True,
                "SOCKET_CONNECT_TIMEOUT": 5,
                "SOCKET_TIMEOUT": 5,
                #"COMPRESSOR": "django_redis.compressors.zstd.ZStdCompressor", # TODO اضافة الضغط على باقي المشاريع
            },
        }
    }
