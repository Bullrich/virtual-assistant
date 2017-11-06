import pywapi

from grey_matter import speak


def weather(city_name, city_code, predefined_message):
    weather_com_result = pywapi.get_weather_from_weather_com(city_code)
    weather_result = predefined_message.format(
        weather_com_result['current_conditions']['text'].lower(),
        weather_com_result['current_conditions']['temperature'], city_name)

    speak(weather_result)
