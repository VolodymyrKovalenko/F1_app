from django.db import models
from apps.drivers.models import Driver

# Create your models here.


class Car(models.Model):
    category = models.CharField(max_length=64)
    company = models.CharField(max_length=54)
    model = models.CharField(max_length=64)
    creation_date = models.DateField()
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT)
