tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Валера', 'Игорь']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def stud_class_gen():
    for i in range(len(tutors)):
        try:
            some_tuple = [tutors[i], klasses[i]]
        except IndexError:
            some_tuple = [tutors[i], None]
        yield tuple(some_tuple)


person = stud_class_gen()
while True:
    try:
        print(next(person))
    except StopIteration:
        break
print(type(stud_class_gen()))
