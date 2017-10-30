from grey_matter.voice_module import speak
from . import debug_message


def log(message):
    print(message)
    if debug_message:
        speak(message)

def simple_log(speak_message):
    print(speak_message)