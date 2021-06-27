count = int(input('введите конец диапазона для генерацци\nn = '))
num = (number for number in range(1, count + 1, 2))
while count:
    try:
        print(next(num))
        count -= 1
    except StopIteration:
        break
