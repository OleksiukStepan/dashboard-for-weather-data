from rest_framework import serializers

from apps.weather.models import City, WeatherData


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class WeatherDataSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = WeatherData
        fields = "__all__"
