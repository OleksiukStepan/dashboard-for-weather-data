from datetime import timedelta

from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.generics import ListCreateAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.weather.cities import CITIES
from apps.weather.models import City, WeatherData
from apps.weather.serializers import CitySerializer, WeatherDataSerializer


def index(request):
    context = {
        "cities": CITIES,
        "days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    }
    return render(request, "index.html", context)


class CityListView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class WeatherDataListView(ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["city__name", "date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        city_name = self.request.GET.get("city__name")
        days = self.request.GET.get("days")

        if city_name:
            queryset = queryset.filter(city__name=city_name)

        if days:
            days = int(days)
            start_date = now().date() - timedelta(days=days)
            queryset = queryset.filter(date__gte=start_date)

        return queryset
