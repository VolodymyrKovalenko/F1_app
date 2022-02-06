from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name} {self.surname}'
