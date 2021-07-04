from csv import reader, writer


def csv_reader(file):
    data = reader(file, delimiter=',')
    for data_ in data:
        yield data_


def data_parse(file_1, file_2, file_result):
    users_dossier = dict.fromkeys('', {})
    with open(file_1, 'r', encoding='UTF-8') as users:
        with open(file_2, 'r', encoding='UTF-8') as hobbys:
            while True:
                try:
                    user = next(csv_reader(users))
                except StopIteration:
                    break
                try:
                    hobby = next(csv_reader(hobbys))
                    if isinstance(hobby, list):
                        ', '.join(hobby)
                except StopIteration:
                    hobby = 'None'
                single_user = {'surname': user[0], 'name': user[1], 'father_name': user[2], 'hobby': hobby}
                with open(file_result, 'a', encoding='UTF-8') as f:
                    write_content = writer(f, delimiter=',')
                    write_content.writerow(list(single_user.values()))
                users_dossier.setdefault(f"{single_user['surname']} {single_user['name']}", single_user)
            print(users_dossier)


def run(file_1, file_2, file_result):
    with open(file_result, 'w', encoding='UTF-8') as f:
        write_content = writer(f, delimiter=',')
        write_content.writerow(('surname', 'name', 'father_name', 'hobby'))
    data_parse(file_1, file_2, file_result)


users_path = input('input path to <users.csv>\n')
hobby_path = input('input path to <hobby.csv>\n')
result = input('input path to result file <result.csv>\n')
run(users_path, hobby_path, result)
