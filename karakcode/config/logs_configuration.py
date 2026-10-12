from django.conf import settings
from pathlib import Path


# =========================================================
# LOGS DIRECTORY
# =========================================================
LOGS_DIR = Path(settings.BASE_DIR) / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

error_filename = LOGS_DIR / "debug.log"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": str(error_filename),
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}