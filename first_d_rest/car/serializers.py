from rest_framework import serializers

from .models import AutoModel, CarModel, CarBrand


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoModel
        fields = ['brand', 'model', 'vin_code']


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ["brand"]


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ["brand", "name"]
