#Программа предназначена для исследования технологии синтеза речи в рамках научно-исследовательской работы
#Автор: Сафина А.М.
#На вход принимается текст из текстового файла на русском языке и преобразуется в строку
#Выходные данные: аудио-файл
import codecs
import text_analys


import pyttsx3

#tts = pyttsx3.init()

#voices = tts.getProperty('voices')

# Задать голос по умолчанию
#tts.setProperty('voice', 'ru')
#voices = tts.getProperty('voices')

# Попробовать установить предпочтительный голос
#for voice in voices:
    #if voice.name == 'Aleksandr':
        #tts.setProperty('voice', voice.id)

#tts.say('Командный голос вырабатываю, товарищ генерал-полковник!')
#tts.runAndWait()

List = []
i = 0
with codecs.open('text.txt', encoding='utf-8') as f:  # считывание из файла в список
    for line in f:
        List.append(line)

my_string = str(List[0])
print(my_string)
f.close #закрываем файл
my_string_1 = text_analys.text_analys(my_string)
print(my_string_1)
#my_string_2 = sound_choose.sound_choose(my_string_1)
#speech_generation.speech_generation(my_string_2)
#def Speech():
   # return  0
