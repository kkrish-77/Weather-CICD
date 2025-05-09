from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = os.getenv('WEATHER_API_KEY', 'YOUR_API_KEY_HERE')  # Replace with your actual API key for testing
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity']
            }
            return jsonify(weather_data)
        else:
            return jsonify({'error': 'City not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 