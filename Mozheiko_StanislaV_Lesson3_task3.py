def thesaurus_name(name_):
    if names_table.get(name_[0].upper()):
        names_table[name_[0].upper()].append(name_)
    else:
        names_table.setdefault(name_[0].upper(), [name_])


names_table = dict.fromkeys([], [])
while True:
    name = input('Введите Имя или нажмите "Enter" для завершения \n')
    if name != '':
        thesaurus_name(name)
    else:
        break
print(names_table)
