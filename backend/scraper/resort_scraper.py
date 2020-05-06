#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import requests

# strips all special characters from string
def strip_special_chars(string):
    return ''.join(e for e in string if e.isalnum())   

"""
 The scraper functions following each return an array 'data' with the necessary ski area information 
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
def SSLfix(url):
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
    url = 'https://summitatsnoqualmie.com/conditions'
    url2 = 'https://forecast.weather.gov/MapClick.php?lat=47.439538&lon=-121.434713&site=pdt&smap=1&unit=0&lg=en&FcstType=text#.Vky-y3arS71'
    bs = SSLfix(url)
    
    # select the elements that have the data and take that directly
    cur_temp = bs.find_all('div', {'class':'box box_flats2'})[1].find_next('span').find_next('span').find_next('span')['data-usc'] 
    new_snow_12 = bs.find_all('span',{'class':'js-measurement'})[42]['data-usc']
    new_snow_24 = bs.find_all('span',{'class':'js-measurement'})[43]['data-usc']
    new_snow_48 = bs.find_all('span',{'class':'js-measurement'})[44]['data-usc']
    ytd = bs.find_all('span',{'class':'js-measurement'})[45]['data-usc']
    cur_depth = bs.find_all('span',{'class':'js-measurement'})[46]['data-usc']
    wind_speed = bs.find_all('span',{'class':'text text_48 text_72Md mix-text_color7 mix-text_alignCenter mix-text_alignLeftMd mix-text_strict'})[2].find_next('span')['data-usc']
    
    # wind direction not reported by alpental so get from weather.gov
    bs2 = SSLfix(url2)
    wind = bs2.find(id="current_conditions_detail").find('b', text="Wind Speed").find_next('td').string
    wind_dir = wind.split(' ', 1)[0]

    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]

    # strip any special chars
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)
    
    # add the name of the 
    data.insert(0, "Alpental")
    return data

# todo - not reporting data anymore
def big_sky():
    # i think we should do a few that aren't currently working and not presenting data
    # that way we can handle that 'error' correctly and make sure it works
    # since this is what will happen to all the ski areas in the summer most likely
    pass

# todo - a js site vs html so will need to use a web driver
def bridger_bowl():
    pass


def jackson_hole():
    url = 'https://www.jacksonhole.com/weather-snow-report.html'
    bs = SSLfix(url)
    cur_temp = bs.find('div',{'class':'midTemp1'}).string 
    wind = bs.find('div',{'class':'midWind1'}).string
    # finding the variables by text values and selecting the string before tag closure
    snow24h_raw = bs.find(text="24 Hrs").find_next('div').find_next('div').string     
    snow48h_raw = bs.find(text="48 Hrs").find_next('div').find_next('div').string
    snowDepth_raw = bs.find(text="Snow Depth").find_next('div').find_next('div').string
    snowYTD_raw = bs.find(text="Season Total").find_next('div').find_next('div').string
    
    url2 = url2 = 'https://forecast.weather.gov/MapClick.php?lat=43.598628&lon=-110.852088&site=pdt&smap=1&unit=0&lg=en&FcstType=text#.Vky-y3arS71'
    bs2 = SSLfix(url2)
    wind = bs2.find(id="current_conditions_detail").find('b', text="Wind Speed").find_next('td').string
    wind_dir = wind.split(' ', 1)[0]
    speedList = wind.split()[-2:]
    wind_speed = ' '.join(speedList)
    wind_speed = ''.join(e for e in wind_speed if e.isdecimal()) 
    
    # removed the wind speed as jackson hole stopped reporting mid mountain data for this mid april
    #speedList = wind.split()[-2:]
    #wind_speed = ' '.join(speedList).strip('mph').strip()

    # removing new line chars from the strings
    new_snow_24 = snow24h_raw.replace("\n", "")
    new_snow_48 = snow48h_raw.replace("\n", "")
    cur_depth = snowDepth_raw.replace("\n", "")
    ytd = snowYTD_raw.replace("\n", "")
    
    # set any unknown data points to empty strings
    new_snow_12 = ""
    
    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]
    
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)

    data.insert(0, "Jackson Hole") # insert ski area name after stripping special chars
    return data


def mt_bachelor():
    # mt bachelor required scraping a second noaa site for wind speed and direction data as they did not report it on their site
    url2 = 'https://forecast.weather.gov/MapClick.php?lat=43.98886243884903&lon=-121.68182373046875&site=pdt&smap=1&unit=0&lg=en&FcstType=text#.Vky-y3arS71'
    bs2 = SSLfix(url2)
    wind = bs2.find(id="current_conditions_detail").find('b', text="Wind Speed").find_next('td').string
    wind_dir = wind.split(' ', 1)[0]
    speedList = wind.split()[-2:]
    wind_speed = ' '.join(speedList)
    wind_speed = ''.join(e for e in wind_speed if e.isdecimal()) 
    
    url = 'https://www.mtbachelor.com/conditions-report/'
    bs = SSLfix(url)

    # extracting the strings from the bachelor site
    cur_temp = bs.find('div', 'weather-sections').find('div', 'current-section condition').find('div', {'class':'key'}).string
    snowfall = bs.find_all('div', 'current-sections conditions')[0] # [1] is base mountain stats 
    new_snow_24 = snowfall.find('div','current-section condition').find('div', {'class':'key'}).string
    cur_depth = snowfall.find('div', 'section-block full').find('div', {'class':'key'}).string
    ytd = snowfall.find('div', 'section-block full first').find('div', {'class':'key'}).string

    # set any unknown data points to empty strings
    new_snow_12 = ""
    new_snow_48 = ""
    
    # strip special chars from the data and return it as a list in correct order
    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)
    
    # insert ski area name
    data.insert(0, "Mt Bachelor") 
    return data


def mt_hood():
    url = 'https://www.skihood.com/en/the-mountain/conditions'
    bs = SSLfix(url)
    # added check to make sure that 'data-depth' is actually a variable 
    cur_temp = bs.find('div',{'class':'conditions-glance-widget conditions-at-elevation'}).find('dd',{'class':'metric temperature', 'data-temperature': True})['data-temperature']
    wind_speed = bs.find('div', {'class':'conditions-glance-widget conditions-at-elevation'}).find('dd',{'class':'reading windspeed', 'data-windspeed': True})['data-windspeed']
    snow = bs.find('div',{'class':'conditions-glance-widget conditions-snowfall'}).find_all('dl')
    new_snow_12  = snow[0].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    new_snow_24  = snow[1].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    new_snow_48  = snow[2].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    cur_depth = bs.find('div',{'class':'snowdepth-mid'}).find('span',{'class':'reading depth', 'data-depth': True})['data-depth'] 
    ytd = bs.find('dl',{'class':'snowdepth-ytd'}).find('dd',{'class':'reading depth', 'data-depth': True})['data-depth'] 
    
    url2 = 'https://forecast.weather.gov/MapClick.php?lat=45.340579&lon=-121.670934&site=pdt&smap=1&unit=0&lg=en&FcstType=text#.Vky-y3arS71'
    bs2 = SSLfix(url2)
    wind = bs2.find(id="current_conditions_detail").find('b', text="Wind Speed").find_next('td').string
    wind_dir = wind.split(' ', 1)[0]

    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]
    
    # todo - remove as no longer necessary, there are no special chars in this instance
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)

    data.insert(0, "Mt Hood") # insert ski area name after stripping special chars
    return data


def ski49n():
    url = 'https://www.ski49n.com/mountain-info/expanded-conditions'
    bs = SSLfix(url)
    summitSnow = bs.find('section', {'class':'mountain-stats'}).find_all('div', {'class':'row'})[2]
    new_snow_12 = summitSnow.find(text="12 Hours").find_next('h3').string
    new_snow_24 = summitSnow.find(text="24 Hours").find_next('h3').string
    new_snow_48 = summitSnow.find(text="48 Hours").find_next('h3').string
    cur_depth = summitSnow.find(text="Snow Depth").find_next('h3').string
    cur_temp = bs.find_all('div', {'class':'row'})[4].find(text="Temperature").find_next('h3').string
    ytd = bs.find(text="Snowfall YTD (summit)").find_next('h3').string
    
    #wind_speed_check = bs.find_all('div', {'class':'row'})[4].find(text="Wind").find_next('h3').string.strip('mph')
    # Remove "Calm" because it is not quantitative data
    #if wind_speed_check == "Calm ":
    #    wind_speed = ""
    #else:
    #    wind_speed = wind_speed_check
    
    url2 = 'https://forecast.weather.gov/MapClick.php?lat=48.294215&lon=-117.568209&site=pdt&smap=1&unit=0&lg=en&FcstType=text#.Vky-y3arS71'
    bs2 = SSLfix(url2)
    wind = bs2.find(id="current_conditions_detail").find('b', text="Wind Speed").find_next('td').string
    wind_dir = wind.split(' ', 1)[0]
    speedList = wind.split()[-2:]
    wind_speed = ' '.join(speedList)
    wind_speed = ''.join(e for e in wind_speed if e.isdecimal())
    
    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]
    
    # remove special chars
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)
    
    data.insert(0, "49 Degrees North")
    return data


def snowbird():
    url = 'https://www.snowbird.com/mountain-report/'
    bs = SSLfix(url)
    # data was nicely organized for scraping on this site, everything needed had the class 'sb-condition_value'
    sbList = bs.find('div', {'class':'conditions'}).find_all('div', {'class':'sb-condition_value'})
    new_snow_12 = sbList[0].string
    new_snow_24 = sbList[1].string
    new_snow_48 = sbList[2].string
    cur_depth = sbList[3].string
    ytd = sbList[4].string
    cur_temp = sbList[6].string

    # convert the wind direction to uppercase
    wind_dir = sbList[8].contents[0].upper()
    # site reported wind speed as a range remove dash
    wind = sbList[8].contents[2].split("-")
    # convert the string to an int and take average of - seperated values
    wind_speed = int(round((int(wind[0]) + int(wind[1]))/2))
    
    # strip special chars
    data = [cur_temp, cur_depth, ytd, wind_dir, new_snow_12, new_snow_24, new_snow_48]
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)

    # convert back to string for db
    data.insert(4, str(wind_speed))
    # insert ski area name after stripping special chars
    data.insert(0, "Snowbird") 
    return data


def whitefish():
    url = 'https://skiwhitefish.com/snowreport/'
    bs = SSLfix(url)
    snow = bs.find_all('div', {'class':'col-sm-6'})
    # remove some special chars but not all from string
    snowStr = str(snow[0]).replace("\t", "").replace("\n","").replace('"',' ').split('>')
    cur_depth = snowStr[2].split()[2]
    ytd = snowStr[3].split()[3]
    snowStr2 = str(snow[1]).replace("\t", "").replace("\n","").replace('"',' ').split('>')
    new_snow_12 = snowStr2[1].split()[2]
    wind = snowStr2[4].replace("/", " ").replace("mph", " ")
    wind_speed = wind.split()[5]
    wind_dir = wind.split()[3]
    # white fishe required scraping an additional site, 
    # todo add to the except above to check SSL cert
    htmlTemp = urlopen('https://skiwhitefish.com/weather/')
    bs2 = BeautifulSoup(htmlTemp, 'html.parser')
    weatherString = bs2.find('h3', text="Summit Forecast").find_previous('span').string
    # find the '°F' in sentence and split the string so that last word is the temperature
    tempIndex = weatherString.find('°F')
    # select last word as temp
    terminal = weatherString[:tempIndex].split()
    cur_temp = terminal[-1]
    
    # whitefish does not report 24h or 48h snow data so set as empty strings
    new_snow_24 =""
    new_snow_48 =""

    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)
    
    data.insert(0, "Whitefish")
    return data


# main switch statement to get data based on which ski area you want
def get_data(ski_area):
    if ski_area == "alpental":
        return alpental()
    elif ski_area == "big_sky":
        return big_sky()
    elif ski_area == "bridger_bowl":
        return bridger_bowl()
    elif ski_area == "jackson_hole":
        return jackson_hole()
    elif ski_area == "mt_bachelor":
        return mt_bachelor()
    elif ski_area == "mt_hood":
        return mt_hood()
    elif ski_area == "ski49n":
        return ski49n()
    elif ski_area == "snowbird":
        return snowbird()
    elif ski_area == "whitefish":
        return whitefish()



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("func")
    args = parser.parse_args()

    if args.func:
        print(get_data(args.func))
