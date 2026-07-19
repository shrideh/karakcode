from __future__ import absolute_import, unicode_literals
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karakcode.settings')
app = Celery('karakcode')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# Add this line to enable broker connection retry on startup
app.conf.broker_connection_retry_on_startup = True

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))