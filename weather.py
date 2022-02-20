import requests

class Weather:
    def __init__(self) -> None:
        self.current_temp = None
        self.feels_like_temp = None
        self.wind = None
        self.condition = None
        self.icon = None

    def get_weather(self, url):
        """
        Grabs weather data from the openweather api url.
        """
        data = requests.get(url).json()['current']
        self.current_temp = data['temp']
        self.feels_like_temp = data['feels_like']
        self.wind = data['wind_speed']
        self.icon = data['weather'][0]['icon']
        self.condition = data['weather'][0]['main']