def format_string_task_a(some_list):
    new_l = []
    some_prices = []
    for i in range(0, len(some_list), 1):
        some_prices.append(str(some_list[i]))
        some_price = some_prices[i].split('.')
        rub = some_price[0]
        kop = (some_price[1])
        if len(kop) < 2:
            kop = kop + '0'
        st = f'{rub} руб {kop} коп'
        new_l.append(st)
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
