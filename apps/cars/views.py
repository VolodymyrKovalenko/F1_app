from rest_framework.response import Response
from rest_framework import status
from apps.cars.models import Car

from rest_framework.views import APIView
from apps.cars.serializers import CarsViewSerializer


class CarsView(APIView):

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        response_serializer = CarsViewSerializer(cars, many=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)



class PingView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(
            {'ping': 'pong123'}, status=status.HTTP_200_OK
        )