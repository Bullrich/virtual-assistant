import os
import sys

from gtts import gTTS

use_google = True


def get_platform():
    if sys.platform == 'darwin':
        return 'mac'
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        return 'linux'


def tts(audio_string):
    """
This function takes a message as an argument and converts it to speech
depending on the OS.
    """
    if get_platform() == "mac":
        tts_engine = 'say'
    else:
        tts_engine = 'espeak'
    return os.system(tts_engine + ' "' + audio_string + '"')


def google_to_text(audio_string):
    print(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    audio_name = "audio.mp3"
    tts.save(audio_name)
    if get_platform() == "mac":
        tts_engine = 'afplay'
    else:
        tts_engine = 'mpg321'
    os.system('{} {}'.format(tts_engine, audio_name))
    os.remove(audio_name)


def speak(message):
    if use_google:
        google_to_text(message)
    else:
        tts(message)
