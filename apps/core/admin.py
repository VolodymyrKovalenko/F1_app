from django.contrib import admin
from apps.core.models import CarsSummary


class CarsSummaryPermission(admin.ModelAdmin):
    pass


admin.site.register(CarsSummary, CarsSummaryPermission)
