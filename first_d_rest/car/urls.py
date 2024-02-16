from django.urls import path, include

from .views import CarViewSet, CarModelViewSet, CarBrandViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('car', CarViewSet)
router.register("brand", CarBrandViewSet)
router.register("model", CarModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]