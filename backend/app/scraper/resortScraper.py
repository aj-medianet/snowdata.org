#!/usr/bin/python3
from urllib.request import urlopen
#from skiarea import SkiArea
from bs4 import BeautifulSoup

#import re #for regex
def mtBachelor():
    html = urlopen('https://www.mtbachelor.com/conditions-report/')
    html2 = urlopen('https://forecast.weather.gov/MapClick.php?lat=43.98886243884903&lon=-121.68182373046875&site=pdt&smap=1&unit=0&lg=en&FcstType=text#.Vky-y3arS71')
    bs = BeautifulSoup(html, 'html.parser')
    bs2 = BeautifulSoup(html2, 'html.parser')
    wind = bs2.find(id="current_conditions_detail").find('b', text="Wind Speed").find_next('td').string
    windDirection = wind.split(' ', 1)[0]
    speedList = wind.split()[-2:]
    windSpeed = ' '.join(speedList)
    temp = bs.find('div', 'weather-sections').find('div', 'current-section condition').find('div', {'class':'key'}).string
    snowfall = bs.find_all('div', 'current-sections conditions')[0] # maybe change to [1] which is currently base stats.
    snow24h = snowfall.find('div','current-section condition').find('div', {'class':'key'}).string
    snowDepth = snowfall.find('div', 'section-block full').find('div', {'class':'key'}).string
    snowYTD = snowfall.find('div', 'section-block full first').find('div', {'class':'key'}).string
    print(windDirection, windSpeed, temp, snow24h, snowDepth, snowYTD)
    #MISSING 12H SNOW AND 48H SNOW, CALL NONE

def jacksonHole():
    html = urlopen('https://www.jacksonhole.com/weather-snow-report.html')
    bs = BeautifulSoup(html, 'html.parser')
    #print(bs.prettify())
    temp = bs.find('div',{'class':'midTemp1'}).string
    wind = bs.find('div',{'class':'midWind1'}).string
    snow24h_raw = bs.find(text="24 Hrs").find_next('div').find_next('div').string
    snow48h_raw = bs.find(text="48 Hrs").find_next('div').find_next('div').string
    snowDepth_raw = bs.find(text="Snow Depth").find_next('div').find_next('div').string
    snowYTD_raw = bs.find(text="Season Total").find_next('div').find_next('div').string
    speedList = wind.split()[-2:]
    windSpeed = ' '.join(speedList)
    snow24h = snow24h_raw.replace("\n", "")
    snow48h = snow48h_raw.replace("\n", "")
    snowDepth = snowDepth_raw.replace("\n", "")
    snowYTD = snowYTD_raw.replace("\n", "")
    #print(repr(snow24h),repr(snow48h), repr(snowDepth), repr(snowYTD), repr(temp), repr(windSpeed))

def main():
    #mtBachelor()
    jacksonHole()


if __name__ == "__main__":
    main()    