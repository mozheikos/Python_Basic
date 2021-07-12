class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def full_name(self):
        return f'{self.name} {self.surname}'

    def total_income(self):
        return self._income['wage'] + (self._income['wage'] * self._income['bonus'] / 100)


surname = input('Введите фамилию\n').title()
name = input('Введите имя\n').title()
position = input('введите должность\n')
wage = float(input('введите оклад, руб\n').replace(',', '.'))
bonus = int(input('введите размер премии в %\n').replace(',', '.'))

developer = Worker(name, surname, position, wage, bonus)
print(f'Работник {developer.full_name()} принят на должность "{developer.position.title()}" с доходом:\n'
      f'оклад - {wage:.2f} рублей\n'
      f'премия - {bonus}%\n'
      f'общий доход - {developer.total_income():.02f} рублей в месяц')
