from django.urls import path
from .views import WeatherVeiw

urlpatterns = [
    path('', WeatherVeiw.as_view(), name='weather'),
]