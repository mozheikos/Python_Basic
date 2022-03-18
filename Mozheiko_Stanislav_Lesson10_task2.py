from abc import ABC, abstractmethod


class Clother(ABC):

    def __init__(self, name, size):
        self.size = size
        self.name = name

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clother):

    @property
    def calculate(self):
        return self.size / 6.5 + 0.5


class Suit(Clother):

    @property
    def calculate(self):
        return self.size * 2 + 0.3


suit = Suit('Костюм', 1.8)
coat = Coat('Пальто', 52)
print(suit.calculate)
print(coat.calculate)
total = coat.calculate + suit.calculate
print(f'Для пошива {coat.name} и {suit.name} требуется {total} метров ткани')
