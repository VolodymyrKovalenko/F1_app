import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('loyalty-tasks')

app.config_from_object('django.conf:settings', namespace='CELERY')  # variables start from CELERY...
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'daily-summary-task': {
        'task': 'apps.core.tasks.summary_task.daily_summary',
        'schedule': crontab(30, 11),
    },
}
