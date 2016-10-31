import requests,json
url="http://www.accuweather.com/en/in/chennai/206671/daily-weather-forecast/206671?day=1"
#url="http://doj.mybluemix.net/students/60"
a= requests.get(url).text
print json.loads(a)
