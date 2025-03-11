import logging

from django.db.utils import IntegrityError

from apps.weather.api import fetch_historical_weather
from apps.weather.cities import CITIES
from apps.weather.models import City, WeatherData

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def fetch_weather_data():
    for city_name in CITIES:
        try:
            data = fetch_historical_weather(city_name)

            if not data or "forecast" not in data:
                logging.warning(f"Skipping {city_name}: No valid forecast data")
                continue

            if data:
                location = data["location"]
                forecast_days = data["forecast"]["forecastday"]

                city, created = City.objects.get_or_create(
                    name=location["name"],
                    defaults={
                        "region": location["region"],
                        "country": location["country"],
                        "latitude": location["lat"],
                        "longitude": location["lon"],
                    }
                )

                for day in forecast_days:
                    try:
                        weather, created = WeatherData.objects.get_or_create(
                            city=city,
                            date=day["date"],
                            defaults={
                                "max_temperature": day["day"]["maxtemp_c"],
                                "min_temperature": day["day"]["mintemp_c"],
                                "avg_temperature": day["day"]["avgtemp_c"],
                                "condition": day["day"]["condition"]["text"],
                                "humidity": day["day"]["avghumidity"],
                                "max_wind_speed": day["day"]["maxwind_kph"],
                                "chance_of_rain": day["day"]["daily_chance_of_rain"],
                                "chance_of_snow": day["day"]["daily_chance_of_snow"],
                            }
                        )
                        if created:
                            logging.info(f"Added weather data: {city.name} - {day['date']}")
                        else:
                            logging.info(f"Weather data already exists: {city.name} - {day['date']}")
                    except IntegrityError as e:
                        logging.error(f"Failed to store weather data for {city.name} on {day['date']}: {e}")
        except Exception as e:
            logging.error(f"Error fetching weather for {city_name}: {e}")

    logging.info(f"Weather forecast updated for {len(CITIES)} cities")
