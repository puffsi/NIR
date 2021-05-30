#Программа предназначена для исследования технологии синтеза речи в рамках научно-исследовательской работы
#Автор: Сафина А.М.
#На вход принимается текст из текстового файла на русском языке и преобразуется в строку
#Выходные данные: аудио-файл
import codecs
import text_analys
import sound_choose
import speech_generation


List = []
i = 0
def Reading(): #функция четния из файла
    with codecs.open('Text_3.txt', encoding='utf-8') as f:  # считывание из файла в список
        for line in f:
            List.append(line)

    f.close  # закрываем файл
    return(List)

List_1 = Reading()
my_string = List_1[0]
print("\nПрочитанный текст: " + my_string)
my_string_1 = text_analys.text_analys(my_string)
sound_choose.sound_choose(my_string_1)
speech_generation.speech_generation(my_string_1)
