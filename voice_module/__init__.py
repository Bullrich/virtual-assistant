from gtts import gTTS
import os, sys

use_google = True


def tts(audioString):
    """
This function takes a message as an argument and converts it to speech
depending on the OS.
    """
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + audioString)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(tts_engine + ' "' + audioString + '"')


def google_to_text(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    audioName = "audio.mp3"
    tts.save(audioName)
    os.system("mpg321 " + audioName)
    os.remove(audioName)


def speak(message):
    if use_google:
        google_to_text(message)
    else:
        tts(message)
