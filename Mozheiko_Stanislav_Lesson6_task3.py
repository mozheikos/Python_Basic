from csv import reader, writer


def reading(file_name_1):
    data_ = reader(file_name_1, delimiter=",")
    for data in data_:
        yield data


users_data = {}
with open('result.csv', 'w', encoding='UTF-8') as result_file:
    write_content = writer(result_file, delimiter=',')
    write_content.writerow(['Фамилия Имя Отчество', 'Увлечения'])
with open('users.csv', 'r', encoding='UTF-8') as users, open('hobby.csv', 'r', encoding='UTF-8') as hobbys:
    while True:
        try:
            hobby = ', '.join(next(reading(hobbys)))
        except StopIteration:
            hobby = None
        try:
            user = ' '.join(next(reading(users)))
            users_data.setdefault(user, hobby)
            with open('result.csv', 'a', encoding='UTF-8') as result_file:
                write_content = writer(result_file, delimiter=',')
                if hobby:
                    hobby = hobby.replace(',', ';')
                else:
                    hobby = 'None'
                write_content.writerow([user, hobby])
        except StopIteration:
            if hobby:
                print(users_data)
                exit(1)
            else:
                print(users_data)
                break
