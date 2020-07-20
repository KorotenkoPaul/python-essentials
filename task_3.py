import sys


class Cell:
    """Клетка"""

    def __init__(self, stars):
        # Ячейки были названы "stars", чтобы избежать тавтологии
        self.stars = stars

    def make_order(self, cols):
        """Возвращает строку, состоящую из cols столбцов."""
        # Создаём стартовую строку, из которой будет забирать неободимое количество звёзд
        initial = '*' * self.stars
        # Инициализируем результирующую строку
        output = ''
        while initial:  # Пока строка initial не пуста
            output += initial[:cols] + '\n'  # Прибавляем к output (нужное нам число звезд + перенос строки)
            initial = initial[cols:]  # Отнимаем прибавленное ранее число звёзд из initial
        else:
            # Убираем лишний перенос строки в конце
            output = output.rstrip()
        return output

    def __str__(self):
        return f'Cell({self.stars})'

    def __add__(self, other):
        return Cell(self.stars + other.stars)

    def __sub__(self, other):
        if self.stars - other.stars > 0:
            return Cell(self.stars - other.stars)
        else:
            print('Вычитание невозможно!', file=sys.stderr)

    def __mul__(self, other):
        return Cell(self.stars * other.stars)

    def __floordiv__(self, other):
        return Cell(self.stars // other.stars)


# Первая клетка
first_cell = Cell(24)
print(first_cell.make_order(9), end='\n\n')

# Вторая клетка
second_cell = Cell(17)
print(second_cell.make_order(5), end='\n\n')

# Сложение
print(first_cell + second_cell)
# Разница
print(first_cell - second_cell)
# Умножение
print(first_cell * second_cell)
# Деление
print(first_cell // second_cell)
