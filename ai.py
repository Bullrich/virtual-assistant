import sys
import unicodedata

import yaml

from brain import brain
from grey_matter.ears import listen
from grey_matter.voice_module import speak

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
speak('Welcome, {}, systems are ready'.format(name))


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def main():
    while True:
        speech_text = ''
        for arg in sys.argv:
            if arg == '-t':
                speech_text = raw_input("What can I help you with?\n")

        if speech_text is '':
            speech_text = strip_accents(listen())

        if speech_text != '':
            brain(name, speech_text.lower(), profile_data)


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
