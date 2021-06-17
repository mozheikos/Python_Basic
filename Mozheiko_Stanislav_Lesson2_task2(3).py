def join_to_string(some_list):
    for elem in some_list:
        if elem.isdigit() or elem[1:].isdigit():
            i = some_list.index(elem)
            some_list[i] = ''.join(some_list[i - 1:i + 2])
    while some_list.count('"'):
        some_list.remove('"')
    some_string = ' '.join(some_list)
    return some_string


def ins_func(some_list):
    count = 0
    while count < 2:
        for elem in some_list:
            if elem.isdigit() or elem[1:].isdigit():
                i = some_list.index(elem)
                some_list.insert(i + 1, '"')
                if count == 0 and int(elem) < 10:
                    some_list[i] = some_list[i].zfill(len(some_list[i]) + 1)
        some_list.reverse()
        count += 1
    return some_list


basic_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(basic_list)
print(id(basic_list))
print(ins_func(basic_list))
print(id(basic_list))
print(join_to_string(basic_list))
print(id(basic_list))
