#!/usr/bin/python3
from urllib.request import urlopen
#from skiarea import SkiArea
from bs4 import BeautifulSoup
#import re #for regex

# TODO
def strip_special_chars(string):
    string = ''.join(e for e in string if e.isalnum())   
    return string 


def mt_bachelor():
    name = "Mt Bachelor"

    html = urlopen('https://www.mtbachelor.com/conditions-report/')
    html2 = urlopen('https://forecast.weather.gov/MapClick.php?lat=43.98886243884903&lon=-121.68182373046875&site=pdt&smap=1&unit=0&lg=en&FcstType=text#.Vky-y3arS71')
    bs = BeautifulSoup(html, 'html.parser')
    bs2 = BeautifulSoup(html2, 'html.parser')
    wind = bs2.find(id="current_conditions_detail").find('b', text="Wind Speed").find_next('td').string
    windDirection = wind.split(' ', 1)[0]
    speedList = wind.split()[-2:]
    windSpeed = ' '.join(speedList)
    windSpeed = ''.join(e for e in windSpeed if e.isdecimal()) 
    temp = bs.find('div', 'weather-sections').find('div', 'current-section condition').find('div', {'class':'key'}).string
    snowfall = bs.find_all('div', 'current-sections conditions')[0] # maybe change to [1] which is currently base stats.
    snow24h = snowfall.find('div','current-section condition').find('div', {'class':'key'}).string
    snowDepth = snowfall.find('div', 'section-block full').find('div', {'class':'key'}).string
    snowYTD = snowfall.find('div', 'section-block full first').find('div', {'class':'key'}).string
    #print(windDirection, windSpeed, temp, snow24h, snowDepth, snowYTD)

    snow12h = ""
    snow48h = ""
    
    # strip special characters from the data and return it as a list in correct order
    data = [name, temp, snowDepth, snowYTD, windDirection, windSpeed, snow12h, snow24h, snow48h]
    for i, j in enumerate(data):
        data[i] = strip_special_chars(j)

    return data


def jackson_hole():
    name = "Jackson Hole"

    html = urlopen('https://www.jacksonhole.com/weather-snow-report.html')
    bs = BeautifulSoup(html, 'html.parser')
    #print(bs.prettify())
    temp = bs.find('div',{'class':'midTemp1'}).string.strip('°')
    wind = bs.find('div',{'class':'midWind1'}).string
    snow24h_raw = bs.find(text="24 Hrs").find_next('div').find_next('div').string
    snow48h_raw = bs.find(text="48 Hrs").find_next('div').find_next('div').string
    snowDepth_raw = bs.find(text="Snow Depth").find_next('div').find_next('div').string
    snowYTD_raw = bs.find(text="Season Total").find_next('div').find_next('div').string
    speedList = wind.split()[-2:]
    windSpeed = ' '.join(speedList).strip('mph').strip()
    snow24h = snow24h_raw.replace("\n", "")
    snow48h = snow48h_raw.replace("\n", "")
    snowDepth = snowDepth_raw.replace("\n", "")
    snowYTD = snowYTD_raw.replace("\n", "")
    print(repr(snow24h),repr(snow48h), repr(snowDepth), repr(snowYTD), repr(temp), repr(windSpeed))

    return [temp, snowDepth, snowYTD, windDirection, windspeed, snow12h, snow24h, snow48h]


def mt_hood():
    html = urlopen('https://www.skihood.com/en/the-mountain/conditions')
    bs = BeautifulSoup(html, 'html.parser')
    #print(bs.prettify())
    temp = bs.find('div',{'class':'conditions-glance-widget conditions-at-elevation'}).find('dd',{'class':'metric temperature', 'data-temperature': True})['data-temperature']
    windSpeed = bs.find('div', {'class':'conditions-glance-widget conditions-at-elevation'}).find('dd',{'class':'reading windspeed', 'data-windspeed': True})['data-windspeed']
    snow = bs.find('div',{'class':'conditions-glance-widget conditions-snowfall'}).find_all('dl')
    snow12h = snow[0].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    snow24h = snow[1].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    snow48h = snow[2].find('dd',{'class':'reading depth', 'data-depth': True})['data-depth']
    snowDepth = bs.find('div',{'class':'snowdepth-mid'}).find('span',{'class':'reading depth', 'data-depth': True})['data-depth'] 
    snowYTD = bs.find('dl',{'class':'snowdepth-ytd'}).find('dd',{'class':'reading depth', 'data-depth': True})['data-depth'] 
    #print(temp,windSpeed,snow12h,snow24h, snow48h, snowDepth, snowYTD)
    #MISSING WIND DIRECTION
    print(repr(snow24h),repr(snow48h), repr(snowDepth), repr(snowYTD), repr(temp), repr(windSpeed))

    return [temp, snowDepth, snowYTD, windDirection, windspeed, snow12h, snow24h, snow48h]


def summit_49degreesN():
    html = urlopen('https://www.ski49n.com/mountain-info/expanded-conditions')
    bs = BeautifulSoup(html, 'html.parser')
    summitSnow = bs.find('section', {'class':'mountain-stats'}).find_all('div', {'class':'row'})[2]
    snow12h = summitSnow.find(text="12 Hours").find_next('h3').string.strip('"')
    snow24h = summitSnow.find(text="24 Hours").find_next('h3').string.strip('"')
    snow48h = summitSnow.find(text="48 Hours").find_next('h3').string.strip('"')
    snowDepth = summitSnow.find(text="Snow Depth").find_next('h3').string.strip('"')
    temp = bs.find_all('div', {'class':'row'})[4].find(text="Temperature").find_next('h3').string.strip('°')
    windSpeed = bs.find_all('div', {'class':'row'})[4].find(text="Wind").find_next('h3').string.strip('mph')
    snowYTD = bs.find(text="Snowfall YTD (summit)").find_next('h3').string
    print(snow12h,snow24h,snow48h,snowDepth,snowYTD,temp,windSpeed)

    return [temp, snowDepth, snowYTD, windDirection, windspeed, snow12h, snow24h, snow48h]


def alpental():
    html = urlopen('https://summitatsnoqualmie.com/conditions')
    bs = BeautifulSoup(html, 'html.parser')
    temp = bs.find_all('div', {'class':'box box_flats2'})[1].find_next('span').find_next('span').find_next('span')['data-usc']
    snow12h = bs.find_all('span',{'class':'js-measurement'})[42]['data-usc']
    snow24h = bs.find_all('span',{'class':'js-measurement'})[43]['data-usc']
    snow48h = bs.find_all('span',{'class':'js-measurement'})[44]['data-usc']
    snowYTD = bs.find_all('span',{'class':'js-measurement'})[45]['data-usc']
    snowDepth = bs.find_all('span',{'class':'js-measurement'})[46]['data-usc']
    windSpeed = bs.find_all('span',{'class':'text text_48 text_72Md mix-text_color7 mix-text_alignCenter mix-text_alignLeftMd mix-text_strict'})[2].find_next('span')['data-usc']
    print(windSpeed, temp,snow12h,snow24h,snow48h,snowYTD,snowDepth)

    return [temp, snowDepth, snowYTD, windDirection, windspeed, snow12h, snow24h, snow48h]


def summit_whitefish():
    html = urlopen('https://skiwhitefish.com/snowreport/')
    bs = BeautifulSoup(html, 'html.parser')
    snow = bs.find_all('div', {'class':'col-sm-6'})
    snowStr = str(snow[0]).replace("\t", "").replace("\n","").replace('"',' ').split('>')
    snowDepth = snowStr[2].split()[2]
    snowYTD = snowStr[3].split()[3]
    snowStr2 = str(snow[1]).replace("\t", "").replace("\n","").replace('"',' ').split('>')
    snow12h = snowStr2[1].split()[2]
    wind = snowStr2[4].replace("/", " ").replace("mph", " ")
    windSpeed = wind.split()[5]
    windDirection = wind.split()[3]
    htmlTemp = urlopen('https://skiwhitefish.com/weather/')
    bs2 = BeautifulSoup(htmlTemp, 'html.parser')
    weatherString = bs2.find('h3', text="Summit Forecast").find_previous('span').string
    tempIndex = weatherString.find('°F')
    terminal = weatherString[:tempIndex].split()
    temp = terminal[-1]
    #print(snowDepth,snowYTD,snow12h, windSpeed,windDirection,temp)
    #MISSING SNOW 12H, SNOW 48H

    return [temp , snowDepth, snowYTD, windDirection, windspeed, snow12h, snow24h, snow48h]


def get_data(ski_area):
    if ski_area == "mt_bachelor":
        return mt_bachelor()


def main():
    pass
    #mt_bachelor()
    #jackson_hole()
    #mthood()
    #summit_49degreesN()
    #alpental()


if __name__ == "__main__":
    main()    