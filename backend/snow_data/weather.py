import requests


# returns the current forecast from weather.gov api
def get_current_forecast(coordinate_url):
    res = requests.get(coordinate_url)
    data = res.json()
    forecast_url = data['properties']['forecast']
    forecast_res = requests.get(forecast_url)
    forecast_data = forecast_res.json()
    return forecast_data
