"""
Q1
"""

import pandas as pd
from datetime import datetime

data = {
    "user_id": [101, 102, 103],
    "amount": [100, 500, 1000],
    "date": [datetime.now(), datetime.now(), datetime.now()],
}
df = pd.DataFrame(data)

x = df.groupby("user_id", dropna=True)["amount"].sum()
print(x)
x.to_csv("user_totals.csv")

############################################################

"""
Q2
"""

from dataclasses import dataclass
import random
import json


@dataclass
class WeatherResponse:
    city: str
    temperature: float
    humidity: float
    status_code: int

    def to_json(cls):
        return {
            "city": cls.city,
            "temperature": cls.temperature,
            "humidity": cls.humidity,
            "status_code": cls.status_code,
        }


def mock_weather_api(city: str):
    return WeatherResponse(
        city=city,
        temperature=random.randrange(-100, 100),
        humidity=random.randint(0, 100),
        status_code=random.choice([200, 400]),
    ).to_json()


def get_weather(city: str):
    weather_response = mock_weather_api(city)
    while weather_response["status_code"] != 200:
        weather_response = mock_weather_api(city)

    return weather_response


cities = ["delhi", "mumbai", "agra"]

weather_response = []

for city in cities:
    weather_response.append(get_weather(city))


with open("weather_response.json", "w") as f:
    json.dump(weather_response, f)
