class Worker:
    """Работник"""

    def __init__(self, name, surname, position, income):
        # Создаём три публичных и одно защищённое поле
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    """Должность"""

    def get_full_name(self):
        """Возвращает полное имя сотрудника."""
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        """Возвращает полный оклад сотрудника."""
        # Суммируем значения словаря self._income,
        # благодаря чему мы не зависим от точных наименований ключей в этом словаре
        total_income = sum(self._income.values())
        return total_income


# Создаём Еву
eva_income = {'wage': 120000, 'bonus': 10000}
eva = Position('Eva', 'Williams', 'doctor', eva_income)
print(f'Имя: {eva.get_full_name()}')
print(f'Оклад: ${eva.get_total_income()}')
print(f'Должность: {eva.position}', end='\n\n')
# Создаём Джона
john_income = {'wage': 70000, 'bonus': 5000}
john = Position('John', 'Patterson', 'teacher', john_income)
print(f'Имя: {john.get_full_name()}')
print(f'Оклад: ${john.get_total_income()}')
print(f'Должность: {john.position}')


# Written by PaulKorotenko
