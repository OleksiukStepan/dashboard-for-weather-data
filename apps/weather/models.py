from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.TextField()
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    avg_temperature = models.FloatField()
    condition = models.CharField(max_length=100)
    humidity = models.IntegerField()
    max_wind_speed = models.FloatField()
    chance_of_rain = models.IntegerField()
    chance_of_snow = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ("city", "date")

    def __str__(self):
        return f"{self.city.name} - {self.date} - {self.avg_temperature}°C"
