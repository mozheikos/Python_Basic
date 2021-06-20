from random import randrange


def choose(some_list, flag):
    i = randrange(0, len(some_list))
    if flag == 1:
        word = some_list.pop(i)
    else:
        word = some_list[i]
    return word


#  в идеале я бы списки передавал в функцию в виде *args, но это будет противоречить условию задачи
def get_jokes(n, flag=0):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    """ проверка на флаг и для того, чтобы избежать 
    ошибки когда список опустеет
    """
    if n > len(nouns) and flag == 1:
        n = len(nouns)
    jokes = []
    while n:
        joke = f'{choose(nouns, flag)} {choose(adverbs, flag)} {choose(adjectives, flag)}'
        jokes.append(joke)
        n -= 1
    return jokes


"""это совсем уж для красоты"""
n = int(input('Какое количество шуток сгенерировать?\n'))
f = int(input('Разрешено ли повторять одни и те же слова в разных шутках (0 - да, 1 - нет)?\n'))
if n > 5 and f == 1:
    a = input('Без повторов возможно сгенерировать только 5 шуток (введите 0 если передумали или enter - продолжить)')
    if a == '0': f = 0
print(f'\n{get_jokes(n, flag=f)}')
