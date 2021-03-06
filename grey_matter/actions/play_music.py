import os
import random

from grey_matter.utils import clean_message, get_platform
from grey_matter.voice_module import speak


def mp3gen(music_path):
    """
    This function finds all the MP3 files in a folder and its subdfolders and returns a list
    """
    print music_path
    music_list = []
    for root, dirs, files in os.walk(music_path):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                music_list.append(os.path.join(root, filename))
    return music_list


def music_player(file_name):
    """
    Takes the name of a music file and plays it depending the OS
    """
    if get_platform() == "mac":
        player = 'afplay'
        return os.system(player)
    elif get_platform() == "linux":
        player = 'mpg123'
    return os.system("{} '{}'".format(player, file_name))


def play_random(music_path):
    try:
        music_listing = mp3gen(music_path)
        music_playing = random.choice(music_listing)
        speak("Now playing {}".format(music_playing))
        music_player(music_playing)
    except IndexError as e:
        speak('No music files found')
        print ("No music files found: {}".format(e))


def play_specific_music(speech_text, music_path):
    cleaned_message = clean_message(speech_text, 'play')
    music_listing = mp3gen(music_path)

    for i in range(0, len(music_listing)):
        if cleaned_message in music_listing[i]:
            music_player(music_listing[i])


def play_shuffle(music_path):
    try:
        music_listing = mp3gen(music_path)
        random.shuffle(music_listing)
        for i in range(0, len(music_listing)):
            music_player(music_listing[i])
    except IndexError as e:
        speak('No music files found.')
        print ("No music files found: {}".format(e))
