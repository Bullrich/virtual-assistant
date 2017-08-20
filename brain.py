from grey_matter import general_conversation
from grey_matter.actions import tell_time, weather, define_subject, open_firefox, play_music, connect_proxy, sleep
from grey_matter.voice_module import speak


def brain(name, speech_text, profile_data):
    def conversations():
        if check_message(['who', 'are', 'you']):
            speech_answer = general_conversation.who_are_you()
        elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
            speech_answer = general_conversation.how_am_i()
        elif check_message(['tell', 'joke']):
            speech_answer = general_conversation.tell_joke()
        elif check_message(['who', 'am', 'i']):
            speech_answer = general_conversation.who_am_i(name)
        elif check_message(['where', 'born']):
            speech_answer = general_conversation.where_born()
        elif check_message(['how', 'are', 'you']):
            speech_answer = general_conversation.how_are_you()
        else:
            speech_answer = general_conversation.undefined()

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

    if check_message(['time']):
        tell_time.what_is_time()
    elif check_message(['how', 'weather']) or check_message(['hows', 'weather']):
        weather.weather(profile_data['city_name'], profile_data['city_code'])
    elif check_message(['define']):
        define_subject.define_subject(speech_text)
    # elif check_message(['business', 'news']):
    #     business_news_reader.news_reader()
    elif check_message(['open', 'firefox']):
        open_firefox.open_firefox()
    elif check_message(['connect', 'proxy']):
        connect_proxy.connect_to_proxy('ble', None)
    elif check_message(['sleep']):
        sleep.go_to_sleep()
    elif check_message(['play', 'music']) or check_message(['music']):
        play_music.play_random(profile_data['music_path'])
    elif check_message(['play']):
        play_music.play_specific_music(speech_text, profile_data['music_path'])
    elif check_message(['party', 'time']) or check_message(['party', 'mix']):
        play_music.play_shuffle(profile_data['music_path'])
    else:
        conversations()
