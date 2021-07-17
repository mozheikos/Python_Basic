class Cell:

    auto_count = 0

    def __init__(self, part: (int, str)):
        Cell.auto_count += 1
        self.number = Cell.auto_count
        self.part = part

    def __add__(self, other):
        return Cell(self.part + other.part)

    def __sub__(self, other):
        if self.part > other.part:
            return Cell(self.part - other.part)
        else:
            return Cell(f'Клетка {self.number} ({self.part} ячеек) <= клетки {other.number} ({other.part} ячеек)')

    def __mul__(self, other):
        return Cell(self.part * other.part)

    def __truediv__(self, other):
        return Cell(self.part // other.part)

    def make_order(self, row):
        result = f''
        while self.part:
            if self.part >= row:
                result += '0' * row + '\n'
                self.part -= row
            else:
                result += '0' * self.part + '\n'
                self.part = 0
        return result

    def __str__(self):
        return f'{self.part}'


m = Cell(10)
n = Cell(4)
print(m - n)
print(m + n)
print(m * n)
print(m / n)
print(m.make_order(4))
