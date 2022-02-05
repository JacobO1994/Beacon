from flask import Flask, redirect, render_template, request
from process import Process as p
import requests
import yaml

app = Flask(__name__)

# Loading API keys
with open('keys.yml', 'r') as file:
    api_keys = yaml.safe_load(file)

# Starter Data & Globals that will be updated
_location = 'Paris, France'
_map_src = f"https://www.google.com/maps/embed/v1/place?key={api_keys['google_maps_embed_key']}&q="
_news = []

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
    global _location, _news, flag
    if request.method == 'POST':
        _location = request.form['location']
        try:
            # This is intended to hit the microservice endpoint for news data
            _news = requests.get("http://192.168.0.142:5001/news/" + _location).json()
            _news = p.clean_news(_news)
            flag = True
        except:
            return f"There was an error grabbing the news for {_location}"
        return redirect('/')
    else:
        loc = _location
        src = _map_src + loc
        news = _news
        return render_template('index.html', loc = loc, src = src, news = news[:5])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)