class MyException(Exception):

    def __init__(self, txt):
        self.txt = txt


def division(x, y):
    if y == 0:
        raise MyException('Деление на 0')
    else:
        return x / y


while True:
    try:
        a = int(input('Введите делимое'))
        b = int(input('Введите делитель'))
    except ValueError:
        print('Вы ввели не число')
    else:
        break

try:
    print(division(a, b))
except MyException as error:
    print(error)
