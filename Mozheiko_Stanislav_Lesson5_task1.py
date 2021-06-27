def not_even_gen(iterations):
    for number in range(1, iterations + 1, 2):
        yield number


count = int(input('введите конец диапазона для генерацци\nn = '))
num = not_even_gen(count)
while count:
    try:
        print(next(num))
        count -= 1
    except StopIteration:
        break
