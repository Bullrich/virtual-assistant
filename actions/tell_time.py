from datetime import datetime
from voice_module import speak

def what_is_time():
    speak("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'))