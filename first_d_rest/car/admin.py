from django.contrib import admin
from .models import CarBrand, CarModel, AutoModel


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ["brand"]


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["name", "brand"]


@admin.register(AutoModel)
class AutoModelAdmin(admin.ModelAdmin):
    list_display = ["vin_code", "model", "brand"]

