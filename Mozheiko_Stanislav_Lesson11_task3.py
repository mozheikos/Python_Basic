class CheckList(Exception):

    def __init__(self, txt):
        self.txt = txt


user_list = []
while True:
    try:
        user_input = input('Введите число или "stop" для завершения ввода\n')
        if user_input == 'stop':
            break
        elif not user_input.isdigit():
            raise CheckList('необходимо ввести число, не строку')
    except CheckList as error:
        print(error)
    else:
        user_list.append(int(user_input))

print(user_list)
