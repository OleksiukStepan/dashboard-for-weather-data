from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json


class Command(BaseCommand):
    help = "Create interval schedule for fetching data from WeatherAPI"

    def handle(self, *args, **kwargs):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.HOURS,
        )

        task, created = PeriodicTask.objects.get_or_create(
            name="Fetch Weather Data Every 1 Hour",
            defaults={
                "interval": schedule,
                "task": "apps.weather.tasks.fetch_weather_data",
                "args": json.dumps([]),
                "queue": "celery",
            }
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS("Successfully created interval task")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Interval task already exists")
            )
