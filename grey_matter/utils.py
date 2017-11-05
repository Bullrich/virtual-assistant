import sys
import platform


def clean_message(speech_text, word_filter):
    message = speech_text.split()
    message.remove(word_filter)
    cleaned_message = ' '.join(message)
    return cleaned_message


def delete_after_word(speech_text, word):
    l1 = speech_text.split()
    target_index = l1.index(word)
    del l1[0: target_index + 1]


def get_platform():
    if sys.platform == 'darwin':
        return 'mac'
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        return 'linux'
