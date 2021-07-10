from time import sleep


def param(function):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if function(*args):
                return func(*args)
            else:
                raise ValueError('Введите значение больше 0')
        return wrapper
    return decorator


@param(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


while True:
    user_input = input('input number or "exit": ')
    if user_input.lower() == 'exit':
        print('Good bye')
        sleep(3)
        break
    try:
        result = calc_cube(int(user_input))
    except ValueError:
        print('number must be above 0')
    else:
        print(result)
