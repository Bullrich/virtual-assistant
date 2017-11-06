import argparse
import unicodedata

import yaml

from brain import brain
from grey_matter import ears
from grey_matter import speak
from grey_matter import word_processing
from grey_matter import set_language

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', help='Type instead of speak', action='store_true')
    parser.add_argument('-d', '--debug', help='Debug mode', action='store_true')
    parser.add_argument('--lang', nargs=1, help='Set language. \'en\' for english, \'es\' for spanish.')
    args = parser.parse_args()
    lang = 'en'
    if args.lang:
        lang = args.lang[0]

    set_language(lang)

    if args.debug:
        from grey_matter import debug
        debug.set_debug_state(True)

    if args.text:
        global listening_method
        listening_method = read_text


def listen():
    while True:
        speech_text = listening_method()

        if speech_text != '':
            brain(name, speech_text.lower(), profile_data)


def read_text():
    return input("> ")


def listen_voice():
    return strip_accents(ears.listen())

def main():
    parse_arguments()
    speak(str.format(word_processing.get_command('!greeting').answer[0], name))
    listen()


listening_method = listen_voice


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


main()
