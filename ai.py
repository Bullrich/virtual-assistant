import yaml
import sys

import speech_recognition as sr

from logic.voice_module import speak
from brain import brain

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
speak('Welcome, {}, systems are ready'.format(name))

def main():
    speech_text = ''
    for arg in sys.argv:
        if arg == '-t':
            speech_text = raw_input("What can I help you with?\n")

    if speech_text is '':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)

        try:
            # second value of recognize_google is API_KEY
            speech_text = r.recognize_google(audio)  # .lower().replace("'", "")
            # to make it work in spanish call it as r.recognize_google(audio, None, "es-AR")
            print("Melissa thinks you said '" + speech_text + "'")
        except sr.UnknownValueError:
            print("Melissa could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    brain(name, speech_text.lower(), profile_data)


main()
