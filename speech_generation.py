#Программа предназначена для завершения синтеза речи путем соединения звуковых дорожек и удаления речевых артефактов
# с применением технологии нейронных сетей
#Автор: Сафина А.М.
#На вход принимается звуковые дорожки
#Выходные данные: единая звуковая дорожка
import pyttsx3
import numpy as np
def speech_generation(my_string_1):
    engine = pyttsx3.init()
    def sigmoid(x):
        return 1/ (1 + np.exp(-x))

    training_inputs = np.array([[0,0,1],
                               [1,1,1],
                               [1,0,1],
                                [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    np.random.seed(1)

    synaptic_weights = 2 * np.random.random((3,1)) - 1

    print("\nСлучайные инциализирующие веса: ")
    print(synaptic_weights)

    #Метод обратного распространения
    for i in range(20000):
        input_layer = training_inputs
        outputs = sigmoid( np.dot(input_layer, synaptic_weights))

        err = training_outputs - outputs
        adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
        synaptic_weights += adjustments

    print("Веса после обучения: ")
    print(synaptic_weights)

    print("Результат после обучения: ")
    print(outputs)

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 260)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(my_string_1)
    engine.save_to_file(my_string_1, 'test_speech_generation_3.mp3')
    engine.runAndWait()