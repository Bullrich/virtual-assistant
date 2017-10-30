from selenium import webdriver

from grey_matter.voice_module import speak


def open_firefox(message):
    speak(message)
    webdriver.Firefox()

    # fix https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
