from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import AutoModel, CarModel, CarBrand
from .serializers import CarSerializer, CarBrandSerializer, CarModelSerializer


class CarViewSet(ModelViewSet):
    queryset = AutoModel.objects.all()
    serializer_class = CarSerializer


class CarBrandViewSet(ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

