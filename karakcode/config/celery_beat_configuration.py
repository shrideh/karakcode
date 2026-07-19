####################################################################
#                         المهام المجدولة                          #
# celery -A core beat -l info
# CELERY_BEAT_SCHEDULE = {
#     "update-top-ads": {
#         "task": "foundation.home.tasks.update_top_ads",
#         "schedule":  60 * 15,  # كل 15 دقيقة
#     },
# }
#################################################