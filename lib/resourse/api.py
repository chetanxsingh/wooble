import requests

api_key = "your_api_key"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

if data["cod"] != "404":
    main = data["main"]
    temperature = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather_description = data["weather"][0]["description"]

    print(f"Temperature: {temperature}")
    print(f"Atmospheric pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description}")
else:
    print("City Not Found!")
