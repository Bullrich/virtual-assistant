import unicodedata
from grey_matter.debug.debug_message import log

import speech_recognition as sr


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def listen():
    speech_text = ''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        log("Say something")
        audio = r.listen(source)

    try:
        # second value of recognize_google is API_KEY
        speech_text = r.recognize_google(audio)  # .lower().replace("'", "")
        # to make it work in spanish call it as r.recognize_google(audio, None, "es-AR")
        log("Melissa thinks you said '" + bcolors.UNDERLINE + speech_text + bcolors.ENDC + "'")
    except sr.UnknownValueError:
        log("Melissa could not understand audio")
    except sr.RequestError as e:
        log("Could not request results from Google Speech Recognition service; {0}".format(e))

    return strip_accents(speech_text)
