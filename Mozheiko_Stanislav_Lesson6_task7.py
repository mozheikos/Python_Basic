from csv import reader, writer
import os
from time import sleep


def string_num():
    with open('bakery.csv', 'r', encoding='UTF-8', newline='') as f:
        rows = reader(f, delimiter=',')
        num = 0
        for row in rows:
            if row and row[0] != 'Num' and int(row[0]) > num:
                num = int(row[0])
    return num


def menu():
    print('\n*****MENU*****')
    print('1. Show sales\n2. Add new sale\n3. Edit sale\n4. Exit program\n')
    option = int(input('choose an action: '))
    return option


def add_value():
    try:
        value = [string_num() + 1, float(input('input new sale: '))]
    except IndexError:
        value = [1, float(input('input new sale: '))]
    with open('bakery.csv', 'a', encoding='UTF-8', newline='') as f:
        row = writer(f, lineterminator='\n')
        row.writerow(value)


def read_value(start=0, stop=0):
    with open('bakery.csv', 'r', encoding='UTF-8', newline='') as f:
        rows = reader(f, delimiter=',')
        for row in rows:
            if row[0] != 'Num' and int(row[0]) in range(start, stop + 1, 1):
                print(f"{row[0]} - {row[1]}")


def edit_value(find, value):
    with open('bakery.csv', 'r', encoding='UTF-8') as f:
        rows_ = []
        rows = reader(f)
        for row in rows:
            if row[0].isdigit() and row[0] == str(find):
                row_ = [find, value]
            else:
                row_ = row
            rows_.append(row_)
    with open('bakery.csv', 'w', encoding='UTF-8', newline='') as f:
        rows = writer(f, lineterminator='\n')
        rows.writerows(rows_)


def main():
    user_choice = menu()
    total = string_num()
    if user_choice == 2:
        add_value()
    elif user_choice == 1:
        if total == 0:
            print('It is no records yet')
        else:
            start_ = input(f'number of 1st record you wanna watch or nothing to show from 1st (total - {total}): ')
            stop_ = input(f'number of last record you wanna watch or nothing to show to end (total - {total}): ')
            start = 0 if not start_ else int(start_)
            stop = total if not stop_ else int(stop_)
            read_value(start, stop)
    elif user_choice == 3:
        if total:
            find = int(input(f'input number of record (total - {total}): '))
            if find > total or not find:
                print('Invalid number of record')
            else:
                value = float(input('input new value: '))
                edit_value(find, value)
        else:
            print('It is no records yet')
    return user_choice


if 'bakery.csv' not in os.listdir():
    with open('bakery.csv', 'w', encoding='UTF-8', newline='') as f:
        head = writer(f, lineterminator='\n')
        head.writerow(['Num', 'Value'])

if __name__ == '__main__':
    while True:
        try:
            choice = main()
        except ValueError:
            continue
        if choice == 4:
            print("Good bye!!!")
            sleep(1)
            break
