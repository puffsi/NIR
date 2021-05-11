#Программа предназначена для завершения синтеза речи путем соединения звуковых дорожек и удаления речевых артефактов
# с применением технологии нейронных сетей
#Автор: Сафина А.М.
#На вход принимается звуковые дорожки
#Выходные данные: единая звуковая дорожка
import pyttsx3
import numpy as np
def speech_generation(my_string_1):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 250)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(my_string_1)
    engine.runAndWait()