import wolframalpha
import json
from urllib.request import urlopen
import requests
from decouple import config

class Api:
    def __init__(self, query, statusvar, speak, enginepropfunc) -> bool:
        url = f'https://api.freegeoip.app/json/?apikey={config("FREEGEOAPI_API_KEY")}'
        geo_requests = requests.get(url)
        
        # Global variables
        self.condition = "Yes"
        self.geo_data = geo_requests.json()

        if "calculate" in query:
            statusvar.set("Calculating...")
            try:
                app_id = config("WOLFRAMALPHA_API_KEY")
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except Exception:
                self.condition = "No"

        elif 'news about' in query:
            query = query.replace("about", '')
            query = query.replace("show", '')
            query = query.replace("news", '')
            query = query.replace(" ", '')
            try:
                statusvar.set("Searching...")
                jsonObj = urlopen(f'https://newsapi.org/v2/everything?apiKey={config("NEWSAPI_API_KEY")}&q={query}')
                data = json.load(jsonObj)
                print(data)
                i = 1

                speak("here is today's top news headlines")
                statusvar.set("Fetching and printing data...")
                for item in data['articles']:
                    # print(str(i) + '. ' + item['title'] + '\n')
                    # print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    if i == 5:
                        break
                    i += 1
            except Exception as e:
                print(str(e))
                self.condition = "No"
     
        elif 'news' in query:
            try:
                statusvar.set("Searching...")
                jsonObj = urlopen(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={config("NEWSAPI_API_KEY")}')
                data = json.load(jsonObj)
                i = 1

                speak("here is today's top news headlines")
                statusvar.set("Fetching and printing data...")
                for item in data['articles']:
                    # print(str(i) + '. ' + item['title'] + '\n')
                    # print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    if i == 5:
                        break
                    i += 1
            except Exception as e:
                print(str(e))
                self.condition = "No"

        elif "weather" in query:
            statusvar.set("Forecasting...")
            list = ["weather", "report", "of", 'forecast', "forecasting",'show']
            for i in list:
                query = query.replace(i, "")
            city_name = query
            api_key = config('OPENWEATHERMAP_API_KEY')
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = self.geo_data['city_name']

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_inCelcius = current_temperature - 273.15

                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                # print following values
                print(" Temperature (in kelvin unit) = " +
                      str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

                speak("Temperature is " + str(current_temperature_inCelcius) + "℃" + ",\nAtmospheric pressure is " + str(
                    current_pressure) + "hpa" + ",\nHumidity is" + str(current_humidiy) + "%" + "\nAnd today is " + str(weather_description))
      
        elif 'where i am' in query or 'where we are' in query or 'where i live' in query or 'find my location' in query or 'trace my location' in query:
            speak("Wait i check now")
            self.statusvar.set("Locating...")
            try:
                speak(f"You are in {self.geo_data['city']}, {self.geo_data['region_name']}, {self.geo_data['country_name']} on {self.geo_data['latitude']} latitude and {self.geo_data['longitude']} longitude and the time zone is {self.geo_data['time_zone']}")
            except Exception as e:
                print(e)
                speak("Sorry, I can't figure out where we are, probably because of a network issue")
                self.condition = "No"
        
        elif "location info" in query:
            try:
                    self.statusvar.set("Locating...")
                    url = f'https://api.freegeoip.app/json/?apikey={config("FREEGEOAPI_API_KEY")}'
                    geo_requests = requests.get(url)
                    self.geo_data = geo_requests.json()
                    for i in self.geo_data:
                        speak(f"{i}: {self.geo_data[i]}")                    
            except Exception as e:
                print(e)
                speak("Sorry, I can't figure out your location info, probably because of a network issue")
                self.condition = "No"  

        elif "country code" in query:
            self.statusvar.set("Locating...")
            try:
                speak(f"Your country code is {self.geodata['country_code']}")
            except Exception as e:
                print(e)
                speak("Sorry, I can't figure out, probably because of a network issue")
                self.condition = "No"
        
        elif "zip code" in query:
            self.statusvar.set("Locating...")
            try:
                speak(f"Your zip code is {self.geodata['zip_code']}")
            except Exception as e:
                print(e)
                speak("Sorry, I can't figure out, probably because of a network issue")
                self.condition = "No"

        elif "region code" in query or "state code" in query:
            self.statusvar.set("Locating...")
            try:
                speak(f"Your regio code code is {self.geodata['region_code']}")
            except Exception as e:
                print(e)
                speak("Sorry, I can't figure out, probably because of a network issue")
                self.condition = "No"
        
        elif "latitude" in query or "state code" in query:
            self.statusvar.set("Locating...")
            try:
                speak(f"{self.geodata['latitude']} latidude\n{self.geodata['longitude']} longitude")
            except Exception as e:
                print(e)
                speak("Sorry, I can't figure, probably because of a network issue")
                self.condition = "No"

        else:
            try:
                app_id = config("WOLFRAMALPHA_API_KEY")
                client = wolframalpha.Client(app_id)
                res = client.query(query)
                answer = next(res.results).text
                speak(answer)
            except Exception as err:
                print(err)
                self.condition = "No"
    
    def __str__(self) -> str:
        return self.condition

def tc():
    return "Aligarh"

def speak(q):
    print(q)

a = "Hello"

if __name__ == '__main__':
    a = Api("location info", a, speak, tc)
    print(a)
    a = str(a)
    if a == "Yes":
        print("Y")
    else:
        print("N")