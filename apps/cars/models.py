from django.db import models
from apps.drivers.models import Driver


class Car(models.Model):
    category = models.CharField(max_length=64)
    company = models.CharField(max_length=54)
    model = models.CharField(max_length=64)
    creation_date = models.DateField()
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    file = models.FileField(upload_to='cars_files/', blank=True, null=True)
