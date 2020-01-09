from requests import get
from htaccess import *

class Weather():
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def currentTemperature(Localization='Florianopolis'):
        url ='http://api.openweathermap.org/data/2.5/weather?q='+Localization+'&appid='+WeatherApiKey+'&units=metric&lang=pt'
        site = get(url)
        weather = site.json()
        try:
            temp = weather['main']['temp']
            description = weather['weather'][0]['description']
            return f'Atualmente esta fazendo {temp} graus lá fora, e o céu está {description}'
        except:
            return f'Não consegui encontrar {Localization}'

    @staticmethod
    def weatherForecast(Localization='Florianopolis'):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + Localization + '&appid=' + WeatherApiKey + '&units=metric&lang=pt'
        site = get(url)
        weather = site.json()
        try:
            temp_min = weather['main']['temp_min']
            temp_max = weather['main']['temp_max']
            return f'A previsão para hoje é que tenha a máxima de {temp_max} graus  e a mínima de {temp_min} graus lá fora'
        except:
            return f'Não consegui encontrar {Localization}'

