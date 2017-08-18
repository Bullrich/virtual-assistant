import pywapi
from logic import voice_module

def weather(city_name, city_code):
    weather_com_result = pywapi.get_weather_from_weather_com(city_code)
    weather_result = "Weather.com says: It is {} and {} degree celcius now in {}".format(weather_com_result['current_conditions']['text'].lower(), weather_com_result['current_conditions']['temperature'], city_name)

    voice_module.speak(weather_result)
