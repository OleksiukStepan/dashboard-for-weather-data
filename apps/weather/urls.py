from django.urls import path

from apps.weather.views import CityListView, WeatherDataListView, index


urlpatterns = [
    path("", index, name="dashboard"),
    path("cities/", CityListView.as_view(), name="city-list"),
    path("weather/", WeatherDataListView.as_view(), name="weather-list"),
]

app_name = "weather"
