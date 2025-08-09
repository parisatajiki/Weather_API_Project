from django.urls import path
from .views import WeatherVeiw ,GetCity

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('',GetCity.as_view(),name='home'),
    path('weather/',cache_page(60*5) (WeatherVeiw.as_view()), name='weather'),
]