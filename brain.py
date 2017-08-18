from logic import general_conversation
from logic.actions import tell_time, weather, define_subject, business_news_reader, open_firefox, connect_proxy, sleep


def brain(name, speech_text, profile_data):
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

    if check_message(['who', 'are', 'you']):
        general_conversation.who_are_you()
    elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        general_conversation.how_am_i()
    elif check_message(['tell', 'joke']):
        general_conversation.tell_joke()
    elif check_message(['who', 'am', 'i']):
        general_conversation.who_am_i(name)
    elif check_message(['where', 'born']):
        general_conversation.where_born()
    elif check_message(['how', 'are', 'you']):
        general_conversation.how_are_you()
    elif check_message(['time']):
        tell_time.what_is_time()
    elif check_message(['how', 'weather']) or check_message(['hows', 'weather']):
        weather.weather(profile_data['city_name'], profile_data['city_code'])
    elif check_message(['define']):
        define_subject.define_subject(speech_text)
    elif check_message(['business', 'news']):
        business_news_reader.news_reader()
    elif check_message(['open', 'firefox']):
        open_firefox.open_firefox()
    elif check_message(['connect', 'proxy']):
        connect_proxy.connect_to_proxy('ble', None)
    elif check_message(['sleep']):
        sleep.go_to_sleep()
    else:
        general_conversation.undefined()
