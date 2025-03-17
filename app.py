from flask import Flask, request, render_template
import requests

app = Flask(__name__)
API_KEY = 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Weather condition-based background images
BACKGROUND_IMAGES = {
    "clear-sky": "https://source.unsplash.com/1600x900/?sky,sunny",
    "rain": "https://source.unsplash.com/1600x900/?rain",
    "clouds": "https://source.unsplash.com/1600x900/?clouds",
    "snow": "https://source.unsplash.com/1600x900/?snow",
    "mist": "https://source.unsplash.com/1600x900/?mist"
}

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_info = None
    background_url = BACKGROUND_IMAGES["clear-sky"]  # Default background
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if response.status_code == 200:
                description = data["weather"][0]["description"].lower()

                # Select background image based on weather
                if "rain" in description:
                    background_url = BACKGROUND_IMAGES["rain"]
                elif "cloud" in description:
                    background_url = BACKGROUND_IMAGES["clouds"]
                elif "snow" in description:
                    background_url = BACKGROUND_IMAGES["snow"]
                elif "mist" in description or "fog" in description:
                    background_url = BACKGROUND_IMAGES["mist"]

                weather_info = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": description,
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"]
                }
            else:
                error_message = data.get("message", "Could not fetch weather data")

    return render_template("index.html", weather=weather_info, error=error_message, background_url=background_url)

if __name__ == '__main__':
    app.run(debug=True)
