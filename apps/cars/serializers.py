from rest_framework import serializers

from apps.cars.models import Car


class CarsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['id']
