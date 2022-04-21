import random
from django.db import models
from django.utils import timezone
from datetime import timedelta


class CarsSummary(models.Model):
    new_cars = models.IntegerField()
    aggregation_date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)


class CarsSummaryDAO:
    TIME_DELTA = timedelta(days=1)

    @classmethod
    def create_record(cls):
        cars_random_number = (random.randint(1, 101))
        return CarsSummary.objects.create(
            new_cars=cars_random_number,
            aggregation_date=timezone.localdate() - cls.TIME_DELTA,
        )

