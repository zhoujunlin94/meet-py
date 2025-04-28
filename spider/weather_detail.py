import requests
from bs4 import BeautifulSoup
import json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "weather.cma.cn",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

def weather_detial(url):
    headers['Referer'] = url
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    forecast_divs = soup.select('div.pull-left.day')
    weathers = []
    for forecast_div in forecast_divs:
        dayItemsDivs = forecast_div.select('div.day-item')
        dayWeather = {}
        for idx, dayItemsDiv in enumerate(dayItemsDivs):
            if idx == 0:
                dateText = dayItemsDiv.get_text(strip=True)
                weekDay = dateText[:3]  
                date = dateText[3:] 
                dayWeather['weekDay'] = weekDay
                dayWeather['date'] = date
            if idx == 1:
                weatherIcon = dayItemsDiv.select('img')[0].get('src')
                dayWeather['weatherIcon'] = 'https://weather.cma.cn' + weatherIcon
            if idx == 2:
                dayWeather['weather'] = dayItemsDiv.get_text(strip=True)
            if idx == 3:
                dayWeather['windDirection'] = dayItemsDiv.get_text(strip=True)
            if idx == 4:
                dayWeather['windForce'] = dayItemsDiv.get_text(strip=True)
            if idx == 5:
                dayWeather['highTemperature'] = dayItemsDiv.select('div.high')[0].get_text(strip=True).replace('℃', '')
                dayWeather['lowTemperature'] = dayItemsDiv.select('div.low')[0].get_text(strip=True).replace('℃', '')
        weathers.append(dayWeather)
    weathers.sort(key= lambda x: x['date'])    
    return weathers

print(json.dumps(weather_detial("https://weather.cma.cn/web/weather/58362.html"), ensure_ascii=False, indent=4))

