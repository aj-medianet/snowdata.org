from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import requests
from snow_data import const
from app.utils import strip_special_chars
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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


def alpental():
    bs = get_soup_obj(const.SKI_AREAS["Alpental"]["ski_area_url"])
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


# needs selenium probably
def alta():
    pass


def big_sky():
    bs = get_soup_obj(const.SKI_AREAS["Big Sky"]["ski_area_url"])
    cur_depth = bs.find_all('span', {'class': 'js-measurement'})[12]['data-usc']
    ytd = "" # does not report
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


# TODO 
def bridger_bowl():
    pass


def jackson_hole():
    bs = get_soup_obj(const.SKI_AREAS["Jackson Hole"]["ski_area_url"])
    new_snow_12 = ""
    # broken -> new_snow_24 = bs.find(text="24 Hrs").find_next('div').find_next('div').string.replace("\n", "")
    new_snow_24 = bs.find(text="48 Hrs").find_previous('div').find_previous('div').find_previous('div').find_previous('div').string.replace("\n", "")
    new_snow_48 = bs.find(text="48 Hrs").find_next('div').find_next('div').string.replace("\n", "")
    cur_depth = bs.find(text="Snow Depth").find_next('div').find_next('div').string.replace("\n", "")
    ytd = bs.find(text="Season Total").find_next('div').find_next('div').string.replace("\n", "")
    data = {
        "cur_depth": cur_depth,
        "ytd": ytd,
        "new_snow_12": new_snow_12,
        "new_snow_24": new_snow_24,
        "new_snow_48": new_snow_48
    }

    data = {x: strip_special_chars(data[x]) for x in data}
    return data


def mt_bachelor():
    print("[DEBUG] starting mt bachelor")
    start = time.time()

    options = Options()
    options.add_argument("--headless")
    driver = Firefox(firefox_options=options)
    driver.get(const.SKI_AREAS["Mt Bachelor"]["ski_area_url"])
    # wait until the snow data is visable
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[contains(@class, 'amount ng-binding')]"))
    )
    elements = driver.find_elements(By.XPATH, "//h3[contains(@class, 'amount ng-binding')]")
    new_snow_12, new_snow_24, new_snow_48, ytd, cur_depth  = elements[0].text, elements[1].text, elements[2].text, elements[4].text, elements[5].text
    data = {
        "cur_depth": cur_depth,
        "ytd": ytd,
        "new_snow_12": new_snow_12,
        "new_snow_24": new_snow_24,
        "new_snow_48": new_snow_48
    }
    data = {x: strip_special_chars(data[x]) for x in data}
    # driver.quit()
    print("[DEBUG] Execution time: {} seconds".format(time.time() - start))
    print("[DEBUG] finish mt bachelor")
    return data
    



def mt_hood():
    bs = get_soup_obj(const.SKI_AREAS["Mt Hood"]["ski_area_url"])
    snow = bs.find('div', {'class': 'conditions-glance-widget conditions-snowfall'}).find_all('dl')
    new_snow_12 = snow[0].find('dd', {'class': 'reading depth', 'data-depth': True})['data-depth']
    new_snow_24 = snow[1].find('dd', {'class': 'reading depth', 'data-depth': True})['data-depth']
    new_snow_48 = snow[2].find('dd', {'class': 'reading depth', 'data-depth': True})['data-depth']
    cur_depth = bs.find('div', {'class': 'snowdepth-mid'}).find('span', {'class': 'reading depth', 'data-depth': True})['data-depth']
    ytd = bs.find('dl', {'class': 'snowdepth-ytd'}).find('dd', {'class': 'reading depth', 'data-depth': True})['data-depth']
    data = {
        "cur_depth": cur_depth,
        "ytd": ytd,
        "new_snow_12": new_snow_12,
        "new_snow_24": new_snow_24,
        "new_snow_48": new_snow_48
    }
    return data


def ski49n():
    bs = get_soup_obj(const.SKI_AREAS["49 Degrees North"]["ski_area_url"])
    snow = bs.find('section', {'class': 'mountain-stats'}).find_all('div', {'class': 'row'})[2]
    new_snow_12 = snow.find(text="12 Hours").find_next('h3').string
    new_snow_24 = snow.find(text="24 Hours").find_next('h3').string
    new_snow_48 = snow.find(text="48 Hours").find_next('h3').string
    cur_depth = snow.find(text="Snow Depth").find_next('h3').string
    ytd = bs.find(text="Snowfall YTD (summit)").find_next('h3').string
    data = {
        "cur_depth": cur_depth,
        "ytd": ytd,
        "new_snow_12": new_snow_12,
        "new_snow_24": new_snow_24,
        "new_snow_48": new_snow_48
    }
    data = {x: strip_special_chars(data[x]) for x in data}
    return data


def snowbird():
    bs = get_soup_obj(const.SKI_AREAS["Snowbird"]["ski_area_url"])
    # data was nicely organized for scraping on this site, everything needed had the class 'sb-condition_value'
    snow = bs.find('div', {'class': 'conditions'}).find_all('div', {'class': 'sb-condition_value'})
    new_snow_12 = snow[0].string
    new_snow_24 = snow[1].string
    new_snow_48 = snow[2].string
    cur_depth = snow[3].string
    ytd = snow[4].string
    data = {
        "cur_depth": cur_depth,
        "ytd": ytd,
        "new_snow_12": new_snow_12,
        "new_snow_24": new_snow_24,
        "new_snow_48": new_snow_48
    }

    data = {x: strip_special_chars(data[x]) for x in data}
    return data


def whitefish():
    bs = get_soup_obj(const.SKI_AREAS["Whitefish"]["ski_area_url"])
    snow = bs.find_all('div', {'class': 'col-sm-6'})
    snow_str = str(snow[0]).replace("\t", "").replace("\n", "").replace('"', ' ').split('>')
    cur_depth = snow_str[2].split()[2]
    ytd = snow_str[3].split()[3]
    snow_str2 = str(snow[1]).replace("\t", "").replace("\n", "").replace('"', ' ').split('>')
    new_snow_12 = ""
    new_snow_24 = snow_str2[1].split()[2]
    new_snow_48 = ""
    data = {
        "cur_depth": cur_depth,
        "ytd": ytd,
        "new_snow_12": new_snow_12,
        "new_snow_24": new_snow_24,
        "new_snow_48": new_snow_48
    }
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
