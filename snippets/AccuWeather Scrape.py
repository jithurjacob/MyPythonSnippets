import requests,re
from bs4 import BeautifulSoup

url="http://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671"
data=requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')
data=soup.find(id="feed-main").find(class_="realfeel").text
print re.findall(r'\d+',data)[0]
#print soup.title