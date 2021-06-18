def format_string_task_a(some_list):
    new_l = []
    for i in range(0, len(some_list), 1):
        some_list[i] = str(some_list[i])
        some_price = some_list[i].split('.')
        rub = some_price[0]
        kop = some_price[1]
        if len(kop) < 2:
            kop = kop.zfill(len(kop)+1)
        st = f'{rub} руб {kop} коп'
        new_l.append(st)
    return new_l


prices = [57.8, 46.51, 97.18, 45.1, 6.2, 7.0, 23.34, 34.12, 36.60, 64.21]
print(format_string_task_a(prices))
