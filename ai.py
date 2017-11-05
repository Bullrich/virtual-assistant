import sys
import unicodedata

import yaml
import argparse
from brain import brain
from grey_matter import ears
from grey_matter.voice_module import speak
from grey_matter import word_processing

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
word_processing.set_language('english')
speak(str.format(word_processing.get_command('!greeting').answer[0], name))


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', help='Type instead of speak', action='store_true')
    parser.add_argument('-d', '--debug', help='Debug mode', action='store_true')
    args = parser.parse_args()
    if args.debug:
        from grey_matter import debug
        debug.set_debug_state(True)
    if args.type:
        listen(True)
    else:
        listen(False)


def listen(type_text):
    while True:
        speech_text = ''
        if type_text:
            speech_text = input("What can I help you with?\n")
        else:
            speech_text = strip_accents(ears.listen())

        if speech_text != '':
            brain(name, speech_text.lower(), profile_data)

        speech_text = None


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


parse_arguments()
