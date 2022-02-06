from django.contrib import admin
from apps.cars.models import Car


class CarsPermission(admin.ModelAdmin):
    pass


admin.site.register(Car, CarsPermission)
