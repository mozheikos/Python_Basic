from time import sleep
"""
использовал CSI форматирование текста, для красоты. По не понятной для меня причине в консоли они не применяются
(просто отображаются служебные символы), Но зато в IDE выглядит симпатичнее
_______________________________
прикрепил в коммит файл lights.py, эта же задачка, только еще побаловался с graphics.py. По мне так симпатично
получилось, взгляни)
"""


class TrafficLight:

    def __init__(self):
        self.__colors = {('красный', '\033[91m\r'): 7, ('желтый', '\033[93m\r'): 3, ('зеленый', '\033[92m\r'): 10}

    def running(self):
        for color, count in self.__colors.items():
            count_ = 1
            print(f'{color[1]}Загорелся {color[0]}', end='')
            sleep(1)
            while count_ <= count:
                print(f'{color[1]}{color[0]}    {count}', end='')
                count -= 1
                sleep(1)
            sleep(0.25)


light = TrafficLight()
while True:
    light.running()
