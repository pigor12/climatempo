from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

OPEN_WEATHER_MAP_API_KEY = "bcde9ec02a068b30e1fbd73ae693bc05" # Chave criada somente para este fim.

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', default = 'Belo Horizonte', type = str)
    country = request.args.get('country', default = 'br', type = str)

    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={OPEN_WEATHER_MAP_API_KEY}"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={OPEN_WEATHER_MAP_API_KEY}"

    current_weather_response = requests.get(current_weather_url).json()
    forecast_response = requests.get(forecast_url).json()

    return jsonify({
        'current_weather': current_weather_response,
        'forecast': forecast_response
    })


if __name__ == '__main__':
    app.run(debug=True)
