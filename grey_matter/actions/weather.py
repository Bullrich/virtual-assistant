import pywapi

from grey_matter import voice_module


def weather(city_name, city_code, predefined_message):
    weather_com_result = pywapi.get_weather_from_weather_com(city_code)
    weather_result = predefined_message.format(
        weather_com_result['current_conditions']['text'].lower(),
        weather_com_result['current_conditions']['temperature'], city_name)

    voice_module.speak(weather_result)
