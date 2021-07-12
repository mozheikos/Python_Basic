class Road:

    mass_to_1_square_meter = 20

    def __init__(self, length, width, _thickness):
        self._length = length
        self._width = width
        self._thickness = thickness

    def asphalt_mass(self):
        mass = self._length * self._width * self._thickness * Road.mass_to_1_square_meter
        quant = ' кг' if mass <= 1000 else ' т'
        mass = mass if quant == ' кг' else mass / 1000
        return str(mass) + quant


while True:
    try:
        length, width, thickness = map(float, input('Введите значения длины (м), ширины (м) участка дороги '
                                                    'и толщину покрытия (см)\n').split(' '))
        break
    except ValueError:
        print('Все значения должны быть числами, повторите ввод\n')

result = Road(length, width, thickness).asphalt_mass()
print(f'Для покрытия участка дороги длиной {length} м, шириной {width} м и толщиной {thickness} см потребуется {result}'
      f' асфальта')
