import requests
from bs4 import BeautifulSoup
url="http://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671"
r=requests.get(url).text

print BeautifulSoup(r, 'html.parser')
