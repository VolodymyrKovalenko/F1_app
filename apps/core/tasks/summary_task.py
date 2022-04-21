from config.celery import app
from apps.core.models import CarsSummaryDAO


@app.task(bind=True)
def daily_summary(self):
    CarsSummaryDAO.create_record()
