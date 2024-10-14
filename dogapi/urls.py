from django.urls import path, include
from rest_framework import routers
from .views import DogViewSet

router = routers.DefaultRouter()
router.register(r'dogs', DogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]