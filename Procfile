web: gunicorn --bind :8000 --workers 3 --threads 4 config.wsgi:application
celery_beat: celery -A config.celery.app beat --loglevel=INFO
celery_worker: celery -A config.celery.app worker --concurrency=1 --loglevel=INFO -n worker.%%h
