from abc import ABC, abstractmethod


class Clothes(ABC):
    """Одежда"""

    @abstractmethod
    def tc(self):
        """Возвращает расход ткани (tissue consumption) для каждого вида одежды."""
        pass


class Coat(Clothes):
    """Пальто"""

    def __init__(self, size):
        # Размер пальто
        self.size = size

    @property
    def tc(self):
        return (self.size / 6.5) + 0.5


class Costume(Clothes):
    """Костюм"""

    def __init__(self, height):
        # Рост костюма
        self.height = height

    @property
    def tc(self):
        return (2 * self.height) + 0.3


# Пальто
my_coat = Coat(44)
print(f'Пальто: {my_coat.tc}')

# Костюм
my_costume = Costume(180)
print(f'Костюм: {my_costume.tc}')
