import os
import requests

API_KEY = os.getenv("WEATHERAPIKEY")

def get_coords(place):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={place}&limit={1}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    lat = data[0]["lat"]
    long = data[0]["lon"]
    return lat, long

def get_data(place,forecast_days,category):
    lat,lon = get_coords(place)
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:(8*forecast_days)]

    if category == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if category == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="london",forecast_days=2,category="Sky"))