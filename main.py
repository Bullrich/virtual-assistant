import os
import sys

import speech_recognition as sr
import yaml

import brain

voice_file = os.getcwd() + '/uploads/' + sys.argv[1]

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()


def main(voice_file):
    r = sr.Recognizer()
    with sr.WavFile(voice_file) as source:
        audio = r.record(source)

    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Melissa thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Melissa could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    brain("Javier", speech_text.lower(), profile_data)


main(voice_file)
