from datetime import datetime

from grey_matter import speak


def what_is_time(predefined_message):
    speak(predefined_message + datetime.strftime(datetime.now(), '%H:%M:%S'))
