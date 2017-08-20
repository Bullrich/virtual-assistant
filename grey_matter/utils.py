import sys


def clean_message(speech_text, filter):
    message = speech_text.split()
    message.remove(filter)
    cleaned_message = ' '.join(message)
    return cleaned_message


def get_platform():
    if sys.platform == 'darwin':
        return 'mac'
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        return 'linux'
