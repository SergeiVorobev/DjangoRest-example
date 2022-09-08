from django.urls import path
from django.contrib.auth.models import User
from .views import CarsAPIView


urlpatterns = [
    path('cars', CarsAPIView.as_view())
]