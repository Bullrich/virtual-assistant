import random


def who_are_you():
    messages = ['I am Melissa, your lovely personal grey_matter', 'Melissa, didn\'t I tell you before?',
                'You ask that so many times! I am Melissa.']
    return random.choice(messages)


def how_am_i():
    replies = ['You are goddamn handsome!', 'My knees go weak when I see you.',
               'You are sexy!', 'You look like the kindest person that I have met.']

    return random.choice(replies)


def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toadaway.',
             'Why was six scared of seven? Because seven ate nine.', 'No, I always forget the punch line.']
    return random.choice(jokes)


def who_am_i(name):
    return 'You are ' + name + ', a brilliant person. I love you!'


def where_born():
    return 'I was created by a magician named Tanay, in India, the magical land of Himalayas.'


def how_are_you():
    return 'I am fine, thank you.'


def undefined():
    return 'I dont know what that means!'
