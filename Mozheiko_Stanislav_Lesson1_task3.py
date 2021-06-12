new_list = []
for i in range(1, 21, 1):
    new_list.append(i)

for n in new_list:
    if n == 1:
        dec = 'процент'
    elif 1 < n and n < 5:
        dec = 'процента'
    else: dec = 'процентов'
    print(n, dec)

# в первом задании в фунции decline реализовано то же самое для произвольного числа

