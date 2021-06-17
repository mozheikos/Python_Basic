def number_mod_7(some_list):
    result = 0
    for num in some_list:
        a = 0
        num_1 = num
        while num != 0:
            a = a + num % 10
            num = num // 10
        if a % 7 == 0:
            result = result + num_1
    return result


basic_list = []
for i in range(0, 1000, 1):
    if i % 2 != 0:
        basic_list.append(i**3)

print(f'задание 1: {number_mod_7(basic_list)}')

for n in basic_list:
    i = basic_list.index(n)
    basic_list[i] = basic_list[i] + 17

print(f'задание 2: {number_mod_7(basic_list)}')
