## Core Algorithms

### Fetching Weather Data using OpenWeather API

The backend of the Weather App is built using Flask and includes an endpoint to fetch weather data from the OpenWeather API. Below is a detailed explanation of the core algorithm used in the `get_weather` function:

#### Backend (Flask API)

- **File:** `routes.py`
- **Function:** `get_weather`

```python
from flask import Blueprint, request, jsonify, current_app
import requests

main = Blueprint('main', __name__)

@main.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = current_app.config['OPENWEATHER_API_KEY']
    
    if city:
        # Fetch coordinates for the city from OpenWeather Geocoding API
        geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
        geo_params = {
            'q': city,
            'limit': 1,
            'appid': api_key
        }
        
        geo_response = requests.get(geo_url, params=geo_params)
        if geo_response.status_code != 200 or not geo_response.json():
            return jsonify({'error': 'City not found'}), 404
        
        geo_data = geo_response.json()[0]
        lat = geo_data['lat']
        lon = geo_data['lon']
    else:
        # Default to predefined coordinates if no city is provided
        lat = request.args.get('lat', '25.67')  # Default latitude
        lon = request.args.get('lon', '7.22')  # Default longitude
    
    # Fetch weather data from OpenWeather Weather API
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    weather_params = {
        'lat': lat,
        'lon': lon,
        'units': 'metric',
        'appid': api_key
    }
    
    weather_response = requests.get(weather_url, params=weather_params)
    
    if weather_response.status_code == 200:
        return jsonify(weather_response.json())
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), 404


# Explanation:
### City Parameter: The function first checks if a city parameter is provided in the request.
### Geocoding API: If a city is provided, it fetches the coordinates (latitude and longitude) for the city using the OpenWeather Geocoding API.
### Default Coordinates: If no city is provided, it uses default coordinates.
### Weather API: It then fetches the weather data for the given coordinates using the OpenWeather Weather API.
### Response Handling: The function returns the weather data in JSON format if the request is successful, otherwise, it returns an error message.
### Debounced Search Function in React
### The frontend of the Weather App is built using React. A debounced search function is implemented to manage API call frequency and improve user experience.

### Frontend (React)
### File: WeatherApp.js
### Function: fetchWeather

import React, { useState } from 'react';
import axios from 'axios';
import debounce from 'lodash.debounce';

const WeatherApp = () => {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null);

    const fetchWeather = async () => {
        try {
            const response = await axios.get('/api/weather', {
                params: { city }
            });
            setWeather(response.data);
        } catch (error) {
            console.error('Error fetching weather data:', error);
        }
    };

    const debouncedFetchWeather = debounce(fetchWeather, 300);

    const handleSearch = (e) => {
        e.preventDefault();
        debouncedFetchWeather();
    };

    return (
        <div>
            <h1>Weather App</h1>
            <form onSubmit={handleSearch}>
                <input
                    type="text"
                    value={city}
                    onChange={(e) => setCity(e.target.value)}
                    placeholder="Enter city"
                />
                <button type="submit">Search</button>
            </form>
            {weather && (
                <div>
                    <h2>Weather in {weather.name}</h2>
                    <p>Temperature: {weather.main.temp}°C</p>
                    <p>Condition: {weather.weather[0].description}</p>
                </div>
            )}
        </div>
    );
};

export default WeatherApp;
