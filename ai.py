import sys
import yaml
import speech_recognition as sr
from voice_module import speak
from brain import brain

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
speak('Welcome, {}, systems are ready'.format(name))

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    try:
        # second value of recognize_google is API_KEY
        speech_text = r.recognize_google(audio)#.lower().replace("'", "")
        # to make it work in spanish call it as r.recognize_google(audio, None, "es-AR")
        print("Melissa thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Melissa could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    brain(name, speech_text)

main()
