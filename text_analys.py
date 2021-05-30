#Программа предназначена для разделения полученной строки на слова для последующего синтеза
#Автор: Сафина А.М.
#На вход принимается строка
#Выходные данные: список слов

def text_analys(my_string):
    print("\nРазбиваю на слова... ")
    words = []
    i_1 = 0
    i_2 = -1
    for char in my_string:
        i_2 += 1
        if char == " ":
            words.append(my_string[i_1:i_2])
            i_1 = i_2 + 1
    print(words)
    return  words