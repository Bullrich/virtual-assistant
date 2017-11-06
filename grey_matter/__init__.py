from . import voice_module
from . import word_processing
from .debug import debug_message
from .debug import sound_debug


def speak(message):
    voice_module.speak(message)


def log(message):
    debug_message.debug_log(message)
    if sound_debug:
        speak(message)


def set_language(lang):
    word_processing.set_language(lang)
    voice_module.set_language(lang)
