from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

schedule, created = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.MINUTES,
)

PeriodicTask.objects.create(
    interval=schedule,
    name="Fetch Weather Data Every 30 Minutes",
    task="apps.weather.tasks.fetch_weather_data",
    args=json.dumps([]),
)
