def my_func(first_num, second_num, third_num) -> int:
    """Возвращает сумму двух (из трёх) наибольших переданных чисел."""
    # Создаём список всех переданных чисел
    numbers = list(locals().values())
    # Берём максимальное число из списка и удаляем его
    first_summand = max(numbers)
    numbers.remove(first_summand)
    # Берем максимальное число из оставшегося списка
    second_summand = max(numbers)
    return first_summand + second_num


if __name__ == '__main__':
    # Выводим результат сложения в stdout
    print('Ответ:', my_func(21, 17, 8))
else:
    print(f'Модуль {__name__} импортирован.')


# Written by PaulKorotenko
