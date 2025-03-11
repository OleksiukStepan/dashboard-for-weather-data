from django.contrib import admin

from apps.weather.models import WeatherData, City

admin.register(City)
admin.register(WeatherData)
