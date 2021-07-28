import requests

url ='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def get_weather(city_name:str):
    api_key = '51295a81e02c50293dea39a6534eebbf'
    response = requests.get(url.format(city_name,api_key))
    data = response.json()
    return {
        'city': data.get('name'),
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'temp':data['main']['temp'] - 273
    }
