from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


def get_soup_obj(url):
    bs = []
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
    except:
        html = requests.get(url, verify=False)
        bs = BeautifulSoup(html.text, 'html.parser')
    finally:
        return bs


def strip_special_chars(string):
    return ''.join(e for e in string if e.isalnum())


def alpental():
    bs = get_soup_obj("https://summitatsnoqualmie.com/conditions")
    new_snow_12 = bs.find_all('span', {'class': 'js-measurement'})[27]['data-usc']
    new_snow_24 = bs.find_all('span', {'class': 'js-measurement'})[28]['data-usc']
    new_snow_48 = bs.find_all('span', {'class': 'js-measurement'})[29]['data-usc']
    ytd = bs.find_all('span', {'class': 'js-measurement'})[30]['data-usc']
    cur_depth = bs.find_all('span', {'class': 'js-measurement'})[31]['data-usc']
    data = {
        "cur_depth": cur_depth,
        "ytd": ytd,
        "new_snow_12": new_snow_12,
        "new_snow_24": new_snow_24,
        "new_snow_48": new_snow_48
    }
    data = {x: strip_special_chars(data[x]) for x in data}
    return data


def alta():
    bs = get_soup_obj("https://www.alta.com/weather")

    print(bs.body)


def mt_bachelor():
    bs = get_soup_obj("https://www.mtbachelor.com/the-mountain/weather-operations/conditions-report")
    # doesn't work right now, need to use selenium
    print(bs.body)

        

def big_sky():
    print("big sky")
    bs = get_soup_obj("https://bigskyresort.com/snow-report")
    cur_depth = bs.find_all('span', {'class': 'js-measurement'})[12]['data-usc']
    ytd = ""
    new_snow_12 = bs.find_all('span', {'class': 'js-measurement'})[7]['data-usc']
    new_snow_24 = bs.find_all('span', {'class': 'js-measurement'})[8]['data-usc']
    new_snow_48 = bs.find_all('span', {'class': 'js-measurement'})[9]['data-usc']
    data = {
        "cur_depth": cur_depth,
        "ytd": ytd,
        "new_snow_12": new_snow_12,
        "new_snow_24": new_snow_24,
        "new_snow_48": new_snow_48
    }

    data = {x: strip_special_chars(data[x]) for x in data}
    return data


data = alta()
#print("data:", data)