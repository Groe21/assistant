import requests

def get_weather(city_name):
    api_key = "tu_clave_api"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]
        weather_report = f"Temperatura: {temperature}K\nPresión: {pressure}hPa\nHumedad: {humidity}%\nDescripción: {weather_desc}"
        return weather_report
    else:
        return "Ciudad no encontrada"
