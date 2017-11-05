import csv
import random
from grey_matter.debug.debug_message import simple_log

undefined = {}


class Message:
    def __init__(self, command, keyword, answer):
        self.command = command
        splitted_keywords = keyword.split(';')
        kw = []
        for group in splitted_keywords:
            kw.append(group.split(' '))
        self.keyword = kw
        self.answer = answer.split(';')

    def is_command(self, words):
        for kw in self.keyword:
            if set(kw).issubset(set(words)):
                return True
        return False

    def get_random_answer(self):
        return random.choice(self.answer)


def generate_commands_list(csv_file):
    with open(csv_file) as csv_commands:
        # dict reader keeps the order!
        reader = csv.DictReader(csv_commands)
        cmd = []
        for index, row in enumerate(reader):
            if row["Command"] == '!undefined':
                global undefined
                undefined = Message(row["Command"], row['keyword'], row["answers"])
            else:
                cmd.append(Message(row["Command"], row['keyword'], row["answers"]))
        return cmd


commands = []


def set_language(language):
    global commands
    simple_log('Setting language to ' + language)
    commands = generate_commands_list(str.format('dialogues/{}.csv'.format(language)))
    simple_log(str.format('Language set: {}', commands is not None))
    simple_log(commands[0].command)
    simple_log(get_command('!greeting'))



def get_command_from_phrase(phrase):
    words_of_message = phrase.split()
    for command in commands:
        if command.is_command(words_of_message):
            return command
    return undefined


def get_command(command_order):
    for command in commands:
        if command.command == command_order:
            return command
    return None

