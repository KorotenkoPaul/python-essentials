def divide(divident, divisor):
    """
    Выводит частное от деления divident на divisor в stdout.
    В случае деления на 0 выводит сообщение об ошибке в stderr.
    """
    try:
        print(divident / divisor)
    except ZeroDivisionError:
        import sys
        print('Делить на 0 запрещено!', file=sys.stderr)


if __name__ == '__main__':
    # Запрашиваем делимое и делитель у пользователя
    usr_divident = float(input('Введите делимое: '))
    usr_divisor = float(input('Введите делитель: '))
    # Выводим результат деления
    divide(usr_divident, usr_divisor)
else:
    print(f'Модуль {__name__} импортирован.')


# Written by PaulKorotenko
