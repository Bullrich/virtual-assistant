import os

from gtts import gTTS

from grey_matter.utils import get_platform

use_google = True

language = 'en'


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


def set_language(lang):
    tts_command = ''
    if lang == 'es':
        tts_command = 'say -v Diego'
    global language
    language = lang


def google_to_text(audio_string):
    tts = gTTS(text=audio_string, lang=language)
    audio_name = "audio.mp3"
    tts.save(audio_name)
    if get_platform() == "mac":
        tts_engine = 'afplay'
    else:
        # from distro import linux_distribution
        tts_engine = 'mpg123'
    os.system('{} {}'.format(tts_engine, audio_name))
    os.remove(audio_name)


def speak(message):
    print(message)
    if use_google:
        google_to_text(message)
    else:
        tts(message)
