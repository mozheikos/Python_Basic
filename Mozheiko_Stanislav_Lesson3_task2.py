translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'exit': 1, '': 1}


def num_translate_adv(key):
    return translate.get(key.lower())


while True:
    word = num_translate_adv(input('введите слово для перевода или "exit" для выхода из программы\n'))
    if word != 1:
        print(word)
    else:
        break
