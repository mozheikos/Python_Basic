from time import sleep

"""Женя, привет. Немного увлекся, с этой задачей, возможно просмотрел какие то исключения, но большую часть вроде обработал
__________________________________
поясню по поводу такого количества статик методов: мне это было нужно чтобы обойтись без переменных, т.к. если сюда
приделать Easy Gui какой нибудь - переменные будут проблемой (ну по крайней мере пока я не умею работать с базами данных, 
там наверное все проще. Разбираться некогда было, аврал на работе. Но надеюсь на твердую 4 решил задачу
__________________________________
и да, не сделал сохранения в файл, т.к. в такой структуре это заняло бы время, а у меня на этой неделе совсем туго (см выше)"""


class Warehouse:
    space = '-' * 125
    total = []

    def __init__(self, w_name, capacity):
        self.capacity = capacity
        self.name = w_name
        self.items = []
        self.load = 0
        Warehouse.total.append(self)

    @staticmethod
    def warehouse_add(name, *nums):
        for num in nums:
            for i in range(len(Technics.total)):
                if Technics.total[i].__dict__['inv_num'] == num:
                    Warehouse.income(name, Technics.total[i])

    @staticmethod
    def warehouse_drop(name, *nums):
        for num in nums:
            for i in range(len(Technics.total)):
                if Technics.total[i].__dict__['inv_num'] == num:
                    Warehouse.warehouse_remove(name, Technics.total[i])

    @staticmethod
    def income(name, item):
        for i in range(len(Warehouse.total)):
            if Warehouse.total[i].__dict__['name'] == name:
                Warehouse.total[i].items.append(item)
                item.place = input(f'Введите место хранения для {item.model}\n')
                Warehouse.total[i].load += 1

    @staticmethod
    def warehouse_remove(name, item):
        for i in range(len(Warehouse.total)):
            if Warehouse.total[i].__dict__['name'] == name:
                Warehouse.total[i].items.remove(item)
                Warehouse.total[i].load -= 1

    @staticmethod
    def get_items(ware_name, equip_type=None, model=None, paper_format=None, color=None, inv_num=None, place=None):
        params = (equip_type, model, paper_format, color, inv_num, place)
        for i in range(len(Warehouse.total)):
            if Warehouse.total[i].__dict__['name'] == ware_name:
                items = Warehouse.sorting(Warehouse.total[i].items, params)
                print(f'Склад: {ware_name}')
                print(Warehouse.space)
                header = list(map(str, items[0].__dict__.keys()))
                length = max(map(len, header)) + 5
                print(' № ', end=' | ')
                for f in range(len(header)):
                    header[f] = header[f].ljust(length, ' ')
                    print(header[f], end=' | ')
                print(f'\n{Warehouse.space}')
                count = 1
                for item in items:
                    values = list(map(str, item.__dict__.values()))
                    print(f' {count} ', end=' | ')
                    for j in range(len(values)):
                        values[j] = values[j].ljust(length, ' ')
                        print(values[j], end=' | ')
                    print()
                    count += 1

    @staticmethod
    def sorting(data, params_):
        params = [x for x in params_ if x]
        data_ = data[:]
        for item in data_:
            _ = len(params)
            for param in params:
                if param in item.__dict__.values():
                    _ -= 1
            if _ != 0:
                data.remove(item)
        return data

    def loads(self):
        return self.load

    @classmethod
    def warehouse_list(cls):
        ware_list = ''
        for item in cls.total:
            ware_list += f"{item.__dict__['name']}\n"
        return ware_list

    @staticmethod
    def replace_item(name, name_2, *nums):
        for num in nums:
            for i in range(len(Technics.total)):
                if Technics.total[i].__dict__['inv_num'] == num:
                    Warehouse.income(name_2, Technics.total[i])
                    Warehouse.warehouse_remove(name, Technics.total[i])


class Technics:
    total = []

    def __init__(self, model, paper_format, inv_num):
        self.inv_num = inv_num
        self.equip_type = ''
        self.model = model
        self.paper_format = paper_format


class Printer(Technics):
    __name__ = 'Printer'

    def __init__(self, model, paper_format, color: bool, inv_num):
        super().__init__(model, paper_format, inv_num)
        self.equip_type = 'printer'
        self.color = color
        Technics.total.append(self)


class Scanner(Technics):
    __name__ = 'Scanner'

    def __init__(self, model, paper_format, inv_num):
        super().__init__(model, paper_format, inv_num)
        self.equip_type = 'scanner'
        self.color = 'N/A'
        Technics.total.append(self)


class Copier(Technics):
    __name__ = 'Copier'

    def __init__(self, model, paper_format, color: bool, inv_num):
        super().__init__(model, paper_format, inv_num)
        self.equip_type = 'copier'
        self.color = color
        Technics.total.append(self)


def menu():
    print()
    print('-----MENU-----\n--------------')
    print('1. View warehouses list')
    print('2. Create new warehouse')
    print('3. View items at warehouse')
    print('4. Add item')
    print('5. Put item into warehouse (works in auto mode after option 4)')
    print('6. Move item to another warehouse')
    print('7. Delete item from balance')
    print('8. Find item in warehouse')
    print('0. Exit program')
    user = input('Choose you option\n')
    try:
        user_choice = int(user)
    except ValueError:
        user_choice = user
    return user_choice


while True:
    choice = menu()
    if choice == 1:
        if len(Warehouse.total) > 0:
            print(Warehouse.warehouse_list())
        else:
            print("There isn't warehouses yet")
    elif choice == 2:
        _ = 0
        while _ != 1:
            new_warehouse = input('Input description: ')
            if new_warehouse not in Warehouse.warehouse_list():
                Warehouse(new_warehouse, capacity=200)
                print(f'Successful\n{Warehouse.warehouse_list()}')
                break
            else:
                input('Such warehouse already exists')
    elif choice == 3:
        warehouse_name = []
        name = input(f'Input warehouse:\n{Warehouse.warehouse_list()}')
        warehouse_name.append(name)
        if not name:
            for ware in Warehouse.total:
                warehouse_name.append(ware.__dict__['name'])
        if len(Warehouse.total) > 0:
            for name in warehouse_name:
                try:
                    Warehouse.get_items(name)
                except IndexError:
                    print('This warehouse is empty')
        else:
            print("There isn't warehouses yet")
    elif choice == 4:
        eq_type = input('Input item type (printer/scanner/copier) ')
        model = input('Input model name ')
        paper = input('Input paper format ')
        color = True if input('Is it color?(Y/N) ') == 'Y' else False
        try:
            number = int(input('Input inventory number '))
        except ValueError:
            number = None
        if eq_type == 'printer':
            Printer(model=model, paper_format=paper, color=color, inv_num=number)
        elif eq_type == 'scanner':
            Scanner(model=model, paper_format=paper, inv_num=number)
        elif eq_type == 'copier':
            Copier(model=model, paper_format=paper, color=color, inv_num=number)
        warehouse = input(f'input warehouse to add item:\n{Warehouse.warehouse_list()}')
        if warehouse not in Warehouse.warehouse_list():
            name = input('It is no warehouse such name, you must create it first')
        else:
            Warehouse.warehouse_add(warehouse, number)
            print('Successful')
    elif choice == 6:
        war_out = input(f'Input warehouse name to take:\n{Warehouse.warehouse_list()}')
        war_in = input(f'Input warehouse name to put:\n{Warehouse.warehouse_list()}')
        if war_out not in Warehouse.warehouse_list() or war_in not in Warehouse.warehouse_list():
            print('Wrong warehouse name')
        else:
            number = int(input('Input inventory number'))
            Warehouse.replace_item(war_out, war_in, number)
            print('Successful')
    elif choice == 7:
        war_out = input(f'Input warehouse name:\n{Warehouse.warehouse_list()}')
        if war_out not in Warehouse.warehouse_list():
            print('Wrong warehouse name')
        else:
            number = int(input('Input inventory number'))
            Warehouse.warehouse_drop(war_out, number)
            print('Successful')
    elif choice == 8:
        warehouse = input(f'input warehouse name:\n{Warehouse.warehouse_list()}')
        if warehouse not in Warehouse.warehouse_list():
            print('Wrong warehouse name')
        else:
            eq_type = input('Input item type (printer/scanner/copier) (nothing to all): ')
            model = input('model - ? (nothing to all): ')
            paper = input('paper format - ? (nothing to all): ')
            color = True if input('color - ? (Y/N) (nothing to all): ') == 'Y' else False
            try:
                number = int(input('Input inventory number (nothing to all) (nothing to all): '))
            except ValueError:
                number = None
            place = input("input holding place (nothing to all): ")
            Warehouse.get_items(ware_name=warehouse, equip_type=eq_type, model=model, paper_format=paper, color=color,
                            inv_num=number, place=place)
    elif choice == 0:
        sleep(1)
        print('Good bye')
        break
    else:
        print('wrong command')
