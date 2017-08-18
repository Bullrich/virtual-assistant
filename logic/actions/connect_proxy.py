from selenium import webdriver

from logic.voice_module import speak

def connect_to_proxy(proxy_username, proxy_password):
    speak("Connecting to proxy server.")
    browser = webdriver.Firefox()
    browser.get('http://www.yopmail.com/en/')

    id_number = browser.find_element_by_name('login')
    #password = browser.find_element_by_name('password')

    id_number.send_keys(proxy_username)
    #password.send_keys(proxy_password)

    browser.find_element_by_class_name('sbut').click()
