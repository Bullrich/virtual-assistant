from selenium import webdriver

from logic.voice_module import speak

def open_firefox():
    speak('Aye aye captain, opening Firefox')
    webdriver.Firefox()

# fix https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path