from django.db import models


class CarBrand(models.Model):
    brand = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.brand}"


class CarModel(models.Model):
    name = models.CharField(unique=True, max_length=255)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class AutoModel(models.Model):
    vin_code = models.CharField(unique=True, max_length=255)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vin_code}"


