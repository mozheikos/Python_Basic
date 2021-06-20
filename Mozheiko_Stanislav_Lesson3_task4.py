def dict_sort(dictionary):     # сортируем полученный словарь по ключам
    dictionary_sorted = {}
    keys_list = list(dictionary.keys())
    keys_list.sort()
    for key in keys_list:
        dictionary_sorted[key] = dictionary[key]
    return dictionary_sorted


def thesaurus_adv(dictionary):
    for key in dictionary.keys():
        names = dictionary[key]
        names_table = dict.fromkeys([], [])
        for name__ in names:
            thesaurus_name(name__, names_table)
        dictionary[key] = dict_sort(names_table)


def thesaurus_name(name_, names_table_, i=0):
    if names_table_.get(name_[i].upper()):
        names_table_[name_[i].upper()].append(name_)
    else:
        names_table_.setdefault(name_[i].upper(), [name_])


surnames_table = dict.fromkeys([], [])
while True:
    name = input('Введите Имя и Фамилию в формате <Имя Фамилия> или нажмите "Enter" для завершения \n')
    if name != '':
        thesaurus_name(name, surnames_table, i=name.find(' ') + 1)
    else:
        break
thesaurus_adv(surnames_table)
print(surnames_table)
print()
print(dict_sort(surnames_table))
