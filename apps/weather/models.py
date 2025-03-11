from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.TextField()
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    feels_like = models.FloatField()
    condition = models.CharField(max_length=100)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
