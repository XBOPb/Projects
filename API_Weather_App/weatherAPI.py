import requests


def getweather(city):
    api = "96e3cd3e19571466a39662b984eec5f1"
    server = "https://api.openweathermap.org/data/2.5/weather"
    request = f"{server}?q={city}&appid={api}"
    output = requests.get(request)
    if output.status_code == 200:
        weather_data = output.json()
        weather = weather_data["weather"][0]["main"]
        description = weather_data["weather"][0]["description"]
        temperature = str(round(weather_data["main"]["temp"] - 273.15, 1)) + " °C"
        pressure = str(round(weather_data["main"]["pressure"] * 100 * 0.00750063755419211, 1)) + " mmHg"
        output_weather = \
f"""Weather: {weather}, {description}, 
  
t°: {temperature}, 
                    
Pressure: {pressure}"""
        return f"{output_weather}"
    else:
        return "City not found"

