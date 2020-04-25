#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
#import re #for regex


# strips all special characters from string
def strip_special_chars(string):
    return ''.join(e for e in string if e.isalnum())   


def alpental():
    html = urlopen('https://summitatsnoqualmie.com/conditions')
    bs = BeautifulSoup(html, 'html.parser')
    cur_temp = bs.find_all('div', {'class':'box box_flats2'})[1].find_next('span').find_next('span').find_next('span')['data-usc']
    new_snow_12 = bs.find_all('span',{'class':'js-measurement'})[42]['data-usc']
    new_snow_24 = bs.find_all('span',{'class':'js-measurement'})[43]['data-usc']
    new_snow_48 = bs.find_all('span',{'class':'js-measurement'})[44]['data-usc']
    ytd = bs.find_all('span',{'class':'js-measurement'})[45]['data-usc']
    cur_depth = bs.find_all('span',{'class':'js-measurement'})[46]['data-usc']
    wind_speed = bs.find_all('span',{'class':'text text_48 text_72Md mix-text_color7 mix-text_alignCenter mix-text_alignLeftMd mix-text_strict'})[2].find_next('span')['data-usc']
    
    wind_dir =""
    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]

    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)
    
    data.insert(0, "Alpental")
    return data


def big_sky():
    # i think we should do a few that aren't currently working and not presenting data
    # that way we can handle that 'error' correctly and make sure it works
    # since this is what will happen to all the ski areas in the summer most likely
    pass


def bridger_bowl():
    pass


def jackson_hole():
    html = urlopen('https://www.jacksonhole.com/weather-snow-report.html')
    bs = BeautifulSoup(html, 'html.parser')
    cur_temp = bs.find('div',{'class':'midTemp1'}).string.strip('°')
    wind = bs.find('div',{'class':'midWind1'}).string
    snow24h_raw = bs.find(text="24 Hrs").find_next('div').find_next('div').string
    snow48h_raw = bs.find(text="48 Hrs").find_next('div').find_next('div').string
    snowDepth_raw = bs.find(text="Snow Depth").find_next('div').find_next('div').string
    snowYTD_raw = bs.find(text="Season Total").find_next('div').find_next('div').string
    #speedList = wind.split()[-2:]
    #wind_speed = ' '.join(speedList).strip('mph').strip()
    new_snow_24 = snow24h_raw.replace("\n", "")
    new_snow_48 = snow48h_raw.replace("\n", "")
    cur_depth = snowDepth_raw.replace("\n", "")
    ytd = snowYTD_raw.replace("\n", "")
    
    # set any unknown data points to empty strings
    new_snow_12 = ""
    wind_dir = ""

    # was previously working but removed as they stopped reporting mid mountain wind speed
    wind_speed =""
    
    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)

    data.insert(0, "Jackson Hole") # insert ski area name after stripping special chars
    return data


def mt_bachelor():
    html = urlopen('https://www.mtbachelor.com/conditions-report/')
    html2 = urlopen('https://forecast.weather.gov/MapClick.php?lat=43.98886243884903&lon=-121.68182373046875&site=pdt&smap=1&unit=0&lg=en&FcstType=text#.Vky-y3arS71')
    bs = BeautifulSoup(html, 'html.parser')
    bs2 = BeautifulSoup(html2, 'html.parser')
    wind = bs2.find(id="current_conditions_detail").find('b', text="Wind Speed").find_next('td').string
    wind_dir = wind.split(' ', 1)[0]
    speedList = wind.split()[-2:]
    wind_speed = ' '.join(speedList)
    wind_speed = ''.join(e for e in wind_speed if e.isdecimal()) 
    cur_temp = bs.find('div', 'weather-sections').find('div', 'current-section condition').find('div', {'class':'key'}).string
    snowfall = bs.find_all('div', 'current-sections conditions')[0] # maybe change to [1] which is currently base stats.
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
    
    data.insert(0, "Mt Bachelor") # insert ski area name after stripping special chars
    return data


def mt_hood():
    html = urlopen('https://www.skihood.com/en/the-mountain/conditions')
    bs = BeautifulSoup(html, 'html.parser')
    cur_temp = bs.find('div',{'class':'conditions-glance-widget conditions-at-elevation'}).find('dd',{'class':'metric temperature', 'data-temperature': True})['data-temperature']
    wind_speed = bs.find('div', {'class':'conditions-glance-widget conditions-at-elevation'}).find('dd',{'class':'reading windspeed', 'data-windspeed': True})['data-windspeed']
    snow = bs.find('div',{'class':'conditions-glance-widget conditions-snowfall'}).find_all('dl')
    new_snow_12  = snow[0].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    new_snow_24  = snow[1].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    new_snow_48  = snow[2].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    cur_depth = bs.find('div',{'class':'snowdepth-mid'}).find('span',{'class':'reading depth', 'data-depth': True})['data-depth'] 
    ytd = bs.find('dl',{'class':'snowdepth-ytd'}).find('dd',{'class':'reading depth', 'data-depth': True})['data-depth'] 
    
    wind_dir = ""
    
    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)

    data.insert(0, "Mt Hood") # insert ski area name after stripping special chars
    return data


def ski49n():
    html = urlopen('https://www.ski49n.com/mountain-info/expanded-conditions')
    bs = BeautifulSoup(html, 'html.parser')
    summitSnow = bs.find('section', {'class':'mountain-stats'}).find_all('div', {'class':'row'})[2]
    new_snow_12 = summitSnow.find(text="12 Hours").find_next('h3').string
    new_snow_24 = summitSnow.find(text="24 Hours").find_next('h3').string
    new_snow_48 = summitSnow.find(text="48 Hours").find_next('h3').string
    cur_depth = summitSnow.find(text="Snow Depth").find_next('h3').string
    cur_temp = bs.find_all('div', {'class':'row'})[4].find(text="Temperature").find_next('h3').string
    ytd = bs.find(text="Snowfall YTD (summit)").find_next('h3').string
    wind_speed_check = bs.find_all('div', {'class':'row'})[4].find(text="Wind").find_next('h3').string.strip('mph')

    # Remove "Calm" because it is not quantitative data
    if wind_speed_check == "Calm ":
        wind_speed = ""
    else:
        wind_speed = wind_speed_check
    
    wind_dir = ""

    data = [cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48]
    
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)
    
    data.insert(0, "49 Degrees North")
    return data


def snowbird():
    html = urlopen('https://www.snowbird.com/mountain-report/')
    bs = BeautifulSoup(html, 'html.parser')
    sbList = bs.find('div', {'class':'conditions'}).find_all('div', {'class':'sb-condition_value'})
    #print(summitSnow[:])
    new_snow_12 = sbList[0].string
    new_snow_24 = sbList[1].string
    new_snow_48 = sbList[2].string
    cur_depth = sbList[3].string
    ytd = sbList[4].string
    cur_temp = sbList[6].string
    wind_dir = sbList[8].contents[0].upper()
    wind = sbList[8].contents[2].split("-")
    wind_speed = int(round((int(wind[0]) + int(wind[1]))/2))
    
    data = [cur_temp, cur_depth, ytd, wind_dir, new_snow_12, new_snow_24, new_snow_48]
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)

    data.insert(4, str(wind_speed))
    data.insert(0, "Snowbird") # insert ski area name after stripping special chars
    return data


def whitefish():
    html = urlopen('https://skiwhitefish.com/snowreport/')
    bs = BeautifulSoup(html, 'html.parser')
    snow = bs.find_all('div', {'class':'col-sm-6'})
    snowStr = str(snow[0]).replace("\t", "").replace("\n","").replace('"',' ').split('>')
    cur_depth = snowStr[2].split()[2]
    ytd = snowStr[3].split()[3]
    snowStr2 = str(snow[1]).replace("\t", "").replace("\n","").replace('"',' ').split('>')
    new_snow_12 = snowStr2[1].split()[2]
    wind = snowStr2[4].replace("/", " ").replace("mph", " ")
    wind_speed = wind.split()[5]
    wind_dir = wind.split()[3]
    htmlTemp = urlopen('https://skiwhitefish.com/weather/')
    bs2 = BeautifulSoup(htmlTemp, 'html.parser')
    weatherString = bs2.find('h3', text="Summit Forecast").find_previous('span').string
    tempIndex = weatherString.find('°F')
    terminal = weatherString[:tempIndex].split()
    cur_temp = terminal[-1]
    
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
