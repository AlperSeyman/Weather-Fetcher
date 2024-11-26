import requests

class Weather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self,city_name,API_KEY):
        self.city_name = city_name
        self.API_KEY = API_KEY
        
        self.url = f"{self.BASE_URL}?q={city_name}&appid={API_KEY}"

    def get_weather_info(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            self.display_weather(data)
        else:
            print("An error occurred. Please check your API key or city name.")

    @staticmethod
    def display_weather(data):
        weather = f"{data["weather"][0]["main"]} --- {data["weather"][0]["description"]}"
        print(f"Weather Condition: {weather}")
        print("Details: ")
        for key, values in data["main"].items():
            print(f"{key.capitalize()} : {values}")




API_KEY = input("Enter your API KEY : ")
city_name = input("Enter a city name: ")
print("*****************")
city_weather = Weather(city_name, API_KEY)
city_weather.get_weather_info()
