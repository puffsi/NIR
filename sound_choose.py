#Программа предназначена для выбора звуковых секций из речевой базы для дальнейшего синтеза
#Автор: Сафина А.М.
#На вход принимается список слов
#Выходные данные: соответствующие списку звуковые дорожки
import pyttsx3
def sound_choose(my_string_1):
    print("\nЧитаю... ")
    my_string_2 = my_string_1
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(my_string_2)
    engine.runAndWait()
