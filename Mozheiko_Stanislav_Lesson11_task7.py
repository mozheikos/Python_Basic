class ComplexNum:

    def __init__(self, r_e, i_m):
        self.r_e = r_e
        self.i_m = i_m

    def __add__(self, other):
        result_r_e = self.r_e + other.r_e
        result_i_m = self.i_m + other.i_m
        return ComplexNum(result_r_e, result_i_m)

    def __mul__(self, other):
        result_r_e = (self.r_e * other.r_e - self.i_m * other.i_m)
        result_i_m = (self.r_e * other.i_m + other.r_e * self.i_m)
        return ComplexNum(result_r_e, result_i_m)

    def __str__(self):
        sympol_1 = ''
        sympol_2 = '+' if self.i_m > 0 else ''
        result = f'{sympol_1}{self.r_e}{sympol_2}{self.i_m}i'
        return result


def create():
    a = input('Введите комплексное число в формате "x + yi"')
    a_ = a.split(' ', 1)
    r = int(a_[0])
    i = int(a_[1].replace(' ', '').rstrip('i'))
    return ComplexNum(r, i)


z_1 = create()
z_2 = create()

print(f'Вы ввели: 1е число = {z_1}, 2е число = {z_2}')
print(f'сумма равна = {z_1 + z_2}')
print(f'Произведение равно = {z_1 * z_2}')
