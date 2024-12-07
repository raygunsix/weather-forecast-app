import os
import requests

API_KEY = os.getenv("API_KEY")

def get_data(place, forecast_days=None):
    try:
        url = "http://api.openweathermap.org/data/2.5/forecast?" \
            f"q={place}&" \
            f"appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        filtered_data = data["list"]
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]
    except KeyError:
        filtered_data = []
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))