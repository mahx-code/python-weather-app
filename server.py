from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # if not bool(city.strip()):
    #     city = "Lagos"

    weather_data = get_current_weather(city)

    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        title = weather_data["name"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']}°C",
        feels_like = f"{weather_data['main']['feels_like']}°C",
    )

def index():
    return render_template('index.html')

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)