def search_news(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove('busca')
    words_of_message.remove('noticias')
    cleaned_message = ' '.join(words_of_message)
    get_news(cleaned_message)


def get_news(newspaper):
    print (newspaper)

# import re
#
# import wikipedia
#
# from grey_matter import speak
#
# def define_subject(speech_text):
#     words_of_message = speech_text.split()
#     words_of_message.remove('define')
#     cleaned_message = ' '.join(words_of_message)
#
#     try:
#         wiki_data = wikipedia.summary(cleaned_message, sentences=5)
#
#         regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
#         m = regEx.match(wiki_data)
#         while m:
#             wiki_data = m.group(1) + m.group(2)
#             m = regEx.match(wiki_data)
#
#         wiki_data = wiki_data.replace("'", "")
#         speak(wiki_data)
#     except wikipedia.WikipediaException as e:
#         speak('There was an error, could you be more specific?')
#         print("Can you please be more specific? You may choose something from the following.; {0}".format(e))
