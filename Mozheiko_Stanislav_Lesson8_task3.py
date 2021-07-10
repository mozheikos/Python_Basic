def type_logger(func):

    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        print(f)
        args_type = []
        for arg in args:
            args_type.append(f'{arg}: {type(arg)}')
        args_ = ', '.join(args_type)
        print(f'{func.__name__}({args_})\n')

    return wrapper


@type_logger
def my_sum(a, b):
    return f'{a} + {b} = {a + b}'


@type_logger
def my_sqr(a):
    return f'{a}^2 = {a ** 2}'


my_sum(2, 3)
my_sqr(6)
