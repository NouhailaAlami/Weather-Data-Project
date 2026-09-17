import requests

api_key="046f979ee464e633a04bcac31e60d39a"
api_url ="https://api.weatherstack.com/current?access_key={api_key}&query=Japan"


# def fetch_data():
#     print("Fetching weather data from Weatherstack API...")
#     try:
#        response = requests.get(api_url)
#        response.raise_for_status()
#        print("API response received successfully.")
#        return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"An error occured: {e}")
#         raise
# fetch_data()


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Tokyo, Japan', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Tokyo', 'country': 'Japan', 'region': 'Tokyo', 'lat': '35.690', 'lon': '139.692', 'timezone_id': 'Asia/Tokyo', 'localtime': '2026-09-12 05:34', 'localtime_epoch': 1789191240, 'utc_offset': '9.0'}, 'current': {'observation_time': '08:34 PM', 'temperature': 20, 'weather_code': 176, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0025_light_rain_showers_night.png'], 'weather_descriptions': ['Patchy rain nearby'], 'astro': {'sunrise': '05:21 AM', 'sunset': '05:54 PM', 'moonrise': '06:14 AM', 'moonset': '06:15 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 1}, 'air_quality': {'co': '522', 'no2': '55.2', 'o3': '17', 'so2': '32.3', 'pm2_5': '15.8', 'pm10': '15.8', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 10, 'wind_degree': 43, 'wind_dir': 'NE', 'pressure': 1021, 'precip': 0, 'humidity': 85, 'cloudcover': 100, 'feelslike': 21, 'uv_index': 0, 'visibility': 10, 'is_day': 'yes'}}