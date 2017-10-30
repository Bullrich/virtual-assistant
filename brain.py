from grey_matter import word_processing
from grey_matter.actions import tell_time, weather, define_subject, open_firefox, play_music, sleep,    notes
from grey_matter.voice_module import speak


def brain(name, speech_text, profile_data):
    message = word_processing.get_command_from_phrase(speech_text)

    def conversations():
        # if check_message(['who', 'are', 'you']):
        #     speech_answer = general_conversation.who_are_you()
        # elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        #     speech_answer = general_conversation.how_am_i()
        # elif check_message(['tell', 'joke']):
        #     speech_answer = general_conversation.tell_joke()
        # elif check_message(['who', 'am', 'i']):
        #     speech_answer = general_conversation.who_am_i(name)
        # elif check_message(['where', 'born']):
        #     speech_answer = general_conversation.where_born()
        # elif check_message(['how', 'are', 'you']):
        #     speech_answer = general_conversation.how_are_you()
        # else:
        #     speech_answer = general_conversation.undefined()

        if is_command('!conv_who'):
            speech_answer = (message.get_random_answer()).format('Mellisa')
        elif is_command('!conv_who_am_i'):
            speech_answer = (message.get_random_answer()).format(name)
        else:
            speech_answer = message.get_random_answer()

        speak(speech_answer)

    def check_message(check):
        """
        This function checks if the items in the list(specified in
        argument) are present in the user's input speech.
        """
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    def is_command(command):
        return message.command == command

    if is_command('!time'):
        tell_time.what_is_time(message.get_random_answer())
    elif is_command('!weather'):
        weather.weather(profile_data['city_name'], profile_data['city_code'], message.get_random_answer())
    elif is_command('!wiki'):
        define_subject.define_subject(speech_text, message.get_random_answer())
    # elif check_message(['business', 'news']):
    #     business_news_reader.news_reader()
    elif is_command('!browser'):
        open_firefox.open_firefox(message.get_random_answer())
    # elif check_message(['connect', 'proxy']):
    #     connect_proxy.connect_to_proxy('ble', None)
    elif is_command('!sleep'):
        sleep.go_to_sleep(message.get_random_answer())
    elif is_command('!music'):
        play_music.play_random(profile_data['music_path'], message.answer)
    elif is_command('!music_specific'):
        play_music.play_specific_music(speech_text, profile_data['music_path'])
    elif is_command('!music_shuffle'):
        play_music.play_shuffle(profile_data['music_path'], message.get_random_answer())
    elif is_command('!write_note'):
        notes.note_something(speech_text, message.get_random_answer())
    elif is_command('!read_note'):
        notes.show_all_notes(message.get_random_answer())
    else:
        conversations()
