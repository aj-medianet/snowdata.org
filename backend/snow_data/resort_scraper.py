#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import requests
from app import utils
from snow_data import const, weather


"""
 The data functions following each return an array 'data' with the necessary ski area information 
 data = [
    name,         - ski area name
    cur_temp,     - the current temperature at the ski area in Fahrenheit
    cur_depth,    - the measured snow pack depth in inches
    ytd,          - the year to date aka the total snowfall in inches
    wind_dir,     - the current wind direction
    wind_speed,   - the current wind speed in mph
    new_snow_12,  - the last 12 hours of snowfall in inches
    new_snow_24,  - the last 24 hours in snowfall in inches
    new_snow_48   - the last 48 hours in snowfall in inches
 ]
"""


def ssl_fix(url):
    bs = []
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
    except:
        html = requests.get(url, verify=False)
        bs = BeautifulSoup(html.text, 'html.parser')
        print("\n\n[DEBUG] SSL certifiate out of date:", url)
        print("\n")
    finally:
        return bs


def alpental():
    # get snow data directly from ski area website
    bs = ssl_fix(const.SKI_AREAS["Alpental"]["ski_area_url"])
    new_snow_12 = bs.find_all('span', {'class': 'js-measurement'})[42]['data-usc']
    new_snow_24 = bs.find_all('span', {'class': 'js-measurement'})[43]['data-usc']
    new_snow_48 = bs.find_all('span', {'class': 'js-measurement'})[44]['data-usc']
    ytd = bs.find_all('span', {'class': 'js-measurement'})[45]['data-usc']
    cur_depth = bs.find_all('span', {'class': 'js-measurement'})[46]['data-usc']

    # get weather data from weather.gov
    forecast_data = weather.get_current_forecast(const.SKI_AREAS["Alpental"]["weather_gov_url"])

    data = [str(forecast_data["properties"]["periods"][0]["temperature"]), cur_depth, ytd,
            forecast_data["properties"]["periods"][0]["windDirection"],
            forecast_data["properties"]["periods"][0]["windSpeed"].split(" ")[0], new_snow_12, new_snow_24, new_snow_48]

    # strip any special chars
    for i, j in enumerate(data):
        data[i] = utils.strip_special_chars(j)

    # add the name
    data.insert(0, "Alpental")
    return data


# TODO 
def big_sky():
    pass


# TODO 
def bridger_bowl():
    pass


def jackson_hole():
    bs = ssl_fix(const.SKI_AREAS["Jackson Hole"]["ski_area_url"])
    new_snow_24 = bs.find(text="24 Hrs").find_next('div').find_next('div').string.replace("\n", "")
    new_snow_48 = bs.find(text="48 Hrs").find_next('div').find_next('div').string.replace("\n", "")
    cur_depth = bs.find(text="Snow Depth").find_next('div').find_next('div').string.replace("\n", "")
    ytd = bs.find(text="Season Total").find_next('div').find_next('div').string.replace("\n", "")
    new_snow_12 = ""

    # get weather data from weather.gov
    forecast_data = weather.get_current_forecast(const.SKI_AREAS["Jackson Hole"]["weather_gov_url"])

    data = [str(forecast_data["properties"]["periods"][0]["temperature"]), cur_depth, ytd,
            forecast_data["properties"]["periods"][0]["windDirection"],
            forecast_data["properties"]["periods"][0]["windSpeed"].split(" ")[0], new_snow_12, new_snow_24, new_snow_48]

    for i, j in enumerate(data):
        data[i] = utils.strip_special_chars(j)

    data.insert(0, "Jackson Hole")  # insert ski area name after stripping special chars
    return data


def mt_bachelor():
    bs = ssl_fix(const.SKI_AREAS["Mt Bachelor"]["ski_area_url"])
    snowfall = bs.find_all('div', 'current-sections conditions')[0]  # [1] is base mountain stats
    new_snow_24 = snowfall.find('div', 'current-section condition').find('div', {'class': 'key'}).string
    cur_depth = snowfall.find('div', 'section-block full').find('div', {'class': 'key'}).string
    ytd = snowfall.find('div', 'section-block full first').find('div', {'class': 'key'}).string
    new_snow_12 = ""
    new_snow_48 = ""

    # get weather data from weather.gov
    forecast_data = weather.get_current_forecast(const.SKI_AREAS["Mt Bachelor"]["weather_gov_url"])

    data = [str(forecast_data["properties"]["periods"][0]["temperature"]), cur_depth, ytd,
            forecast_data["properties"]["periods"][0]["windDirection"],
            forecast_data["properties"]["periods"][0]["windSpeed"].split(" ")[0], new_snow_12, new_snow_24, new_snow_48]

    for i, j in enumerate(data):
        data[i] = utils.strip_special_chars(j)

    # insert ski area name
    data.insert(0, "Mt Bachelor")
    return data


def mt_hood():
    bs = ssl_fix(const.SKI_AREAS["Mt Hood"]["ski_area_url"])
    snow = bs.find('div', {'class': 'conditions-glance-widget conditions-snowfall'}).find_all('dl')
    new_snow_12 = snow[0].find('dd', {'class': 'reading depth', 'data-depth': True})['data-depth']
    new_snow_24 = snow[1].find('dd', {'class': 'reading depth', 'data-depth': True})['data-depth']
    new_snow_48 = snow[2].find('dd', {'class': 'reading depth', 'data-depth': True})['data-depth']
    cur_depth = bs.find('div', {'class': 'snowdepth-mid'}).find('span', {'class': 'reading depth', 'data-depth': True})['data-depth']
    ytd = bs.find('dl', {'class': 'snowdepth-ytd'}).find('dd', {'class': 'reading depth', 'data-depth': True})['data-depth']

    # get weather data from weather.gov
    forecast_data = weather.get_current_forecast(const.SKI_AREAS["Mt Hood"]["weather_gov_url"])

    data = [str(forecast_data["properties"]["periods"][0]["temperature"]), cur_depth, ytd,
            forecast_data["properties"]["periods"][0]["windDirection"],
            forecast_data["properties"]["periods"][0]["windSpeed"].split(" ")[0], new_snow_12, new_snow_24, new_snow_48]

    for i, j in enumerate(data):
        data[i] = utils.strip_special_chars(j)

    data.insert(0, "Mt Hood")  # insert ski area name after stripping special chars
    return data


def ski49n():
    bs = ssl_fix(const.SKI_AREAS["49 Degrees North"]["ski_area_url"])
    snow = bs.find('section', {'class': 'mountain-stats'}).find_all('div', {'class': 'row'})[2]
    new_snow_12 = snow.find(text="12 Hours").find_next('h3').string
    new_snow_24 = snow.find(text="24 Hours").find_next('h3').string
    new_snow_48 = snow.find(text="48 Hours").find_next('h3').string
    cur_depth = snow.find(text="Snow Depth").find_next('h3').string
    ytd = bs.find(text="Snowfall YTD (summit)").find_next('h3').string

    # get weather data from weather.gov
    forecast_data = weather.get_current_forecast(const.SKI_AREAS["49 Degrees North"]["weather_gov_url"])

    data = [str(forecast_data["properties"]["periods"][0]["temperature"]), cur_depth, ytd,
            forecast_data["properties"]["periods"][0]["windDirection"],
            forecast_data["properties"]["periods"][0]["windSpeed"].split(" ")[0], new_snow_12, new_snow_24, new_snow_48]

    # remove special chars
    for i, j in enumerate(data):
        data[i] = utils.strip_special_chars(j)

    data.insert(0, "49 Degrees North")
    return data


def snowbird():
    bs = ssl_fix(const.SKI_AREAS["Snowbird"]["ski_area_url"])
    # data was nicely organized for scraping on this site, everything needed had the class 'sb-condition_value'
    snow = bs.find('div', {'class': 'conditions'}).find_all('div', {'class': 'sb-condition_value'})
    new_snow_12 = snow[0].string
    new_snow_24 = snow[1].string
    new_snow_48 = snow[2].string
    cur_depth = snow[3].string
    ytd = snow[4].string

    # get weather data from weather.gov
    forecast_data = weather.get_current_forecast(const.SKI_AREAS["Snowbird"]["weather_gov_url"])

    data = [str(forecast_data["properties"]["periods"][0]["temperature"]), cur_depth, ytd,
            forecast_data["properties"]["periods"][0]["windDirection"],
            forecast_data["properties"]["periods"][0]["windSpeed"].split(" ")[0], new_snow_12, new_snow_24, new_snow_48]

    for i, j in enumerate(data):
        data[i] = utils.strip_special_chars(j)

    # insert ski area name after stripping special chars
    data.insert(0, "Snowbird")
    return data


def whitefish():
    bs = ssl_fix(const.SKI_AREAS["Whitefish"]["ski_area_url"])
    snow = bs.find_all('div', {'class': 'col-sm-6'})
    snow_str = str(snow[0]).replace("\t", "").replace("\n", "").replace('"', ' ').split('>')
    cur_depth = snow_str[2].split()[2]
    ytd = snow_str[3].split()[3]
    snow_str2 = str(snow[1]).replace("\t", "").replace("\n", "").replace('"', ' ').split('>')
    new_snow_12 = ""
    new_snow_24 = snow_str2[1].split()[2]
    new_snow_48 = ""

    # get weather data from weather.gov
    forecast_data = weather.get_current_forecast(const.SKI_AREAS["Whitefish"]["weather_gov_url"])

    data = [str(forecast_data["properties"]["periods"][0]["temperature"]), cur_depth, ytd,
            forecast_data["properties"]["periods"][0]["windDirection"],
            forecast_data["properties"]["periods"][0]["windSpeed"].split(" ")[0], new_snow_12, new_snow_24, new_snow_48]

    for i, j in enumerate(data):
        data[i] = utils.strip_special_chars(j)

    data.insert(0, "Whitefish")
    return data


# main switch statement to get data based on which ski area you want
def get_data(ski_area):
    if ski_area == "Alpental":
        return alpental()
    elif ski_area == "Big Sky":
        return big_sky()
    elif ski_area == "Bridger Bowl":
        return bridger_bowl()
    elif ski_area == "Jackson Hole":
        return jackson_hole()
    elif ski_area == "Mt Bachelor":
        return mt_bachelor()
    elif ski_area == "Mt Hood":
        return mt_hood()
    elif ski_area == "49 Degrees North":
        return ski49n()
    elif ski_area == "Snowbird":
        return snowbird()
    elif ski_area == "Whitefish":
        return whitefish()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("func")
    args = parser.parse_args()

    if args.func:
        print(get_data(args.func))
