def name_modify(name):
    name_ = name.split()
    name = name_[-1].capitalize()
    return name


some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for name_ in some_list:
    name = name_modify(name_)
    print('Привет, {}!'.format(name))
