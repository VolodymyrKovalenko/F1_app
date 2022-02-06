from django.contrib import admin
from apps.drivers.models import Driver


class DriversPermission(admin.ModelAdmin):
    pass


admin.site.register(Driver, DriversPermission)
