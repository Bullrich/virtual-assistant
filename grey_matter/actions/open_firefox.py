import webbrowser

from grey_matter import speak

def open_firefox(message):
    speak(message)
    webbrowser.open_new('https://google.com.ar')

    # fix https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
