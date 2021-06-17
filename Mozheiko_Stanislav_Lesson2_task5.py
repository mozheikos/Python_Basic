def format_string_task_a(some_list):
    new_l = []
    for i in range(0, len(some_list), 1):
        rub = int(some_list[i] // 1)
        kop = int((some_list[i] % 1)*100)
        st = f'{rub} руб {kop:02d} коп'
        new_l.append(st)
    new_l = ', '.join(new_l)
    return new_l


prices = [57.8, 46.51, 97.18, 45.1, 6.2, 7.0, 23.34, 34.12, 36.60, 64.21]

print(f'Задание А - \n{format_string_task_a(prices)}')
print(f'Задание Б - \n{prices}')
print(f'id prices до сортировки {id(prices)}')
prices.sort()
print(prices)
print(f'id prices после сортировки {id(prices)}')
prices_2 = prices[::-1] #prices_2 = sorted(prices, reverse=True) - аналогичный результат
print(f'Задание В - \n{prices_2}')
print(f'Задание Г - \n{sorted(prices_2[:5])}')