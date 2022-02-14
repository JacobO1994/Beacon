from flask import Flask, redirect, render_template, request
from process import Process as p
import requests
import yaml
from geolocator import Geolocator
from weather import Weather

app = Flask(__name__)

# Loading API keys
with open('keys.yml', 'r') as file:
    api_keys = yaml.safe_load(file)

# Starter Data & Globals that will be updated
weather = Weather()
_location = 'Paris, France'
_map_src = f"https://www.google.com/maps/embed/v1/place?key={api_keys['google_maps_embed_key']}&q="
_news = []
_coordinates = Geolocator.get_coordinates(_location)
_weather_src = f"https://api.openweathermap.org/data/2.5/onecall?lat={_coordinates[0]}&lon={_coordinates[1]}&appid={api_keys['open_weather_key']}&units=metric"

# Flag denoting if we have progressed past starter data
flag = False
if flag:
    _news = []
else:
    _news = requests.get("http://192.168.0.142:5001/news/" + _location).json()
    _news = p.clean_news(_news)

# Base function of the application
@app.route('/', methods=['GET', 'POST'])
def index():
    global _location, _news, flag, _coordinates
    _weather_src = f"https://api.openweathermap.org/data/2.5/onecall?lat={_coordinates[0]}&lon={_coordinates[1]}&appid={api_keys['open_weather_key']}&units=metric"
    if request.method == 'POST':
        _location = request.form['location']
        try:
            # This is intended to hit the microservice endpoint for news data
            _news = requests.get("http://192.168.0.142:5001/news/" + _location).json()
            _news = p.clean_news(_news)
            _coordinates = Geolocator.get_coordinates(_location)
            flag = True
        except:
            return f"There was an error grabbing the news for {_location}"
        return redirect('/')
    else:
        loc = _location
        src = _map_src + loc
        news = _news
        weather.get_weather(_weather_src)
        return render_template('index.html', loc = loc, src = src, news = news[:5], weather=weather)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)