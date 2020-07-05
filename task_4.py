import sys  # Модуль sys нужен для вывода в stderr сообщений о вводе неподходящих чисел


def my_func(x, y) -> float:
    """
    Возвращает результат возведения x в степень y.
    Аргумент x следует передевать как вещественное положительное число,
    а аргумент y - как целое отрицательное.
    В противном случае в stderr будет выведено сообщение о неправильном вводе.
    """
    if x > 0 and type(x) == float:
        if y < 0 and type(y) == int:
            tmp = x  # Временная переменая, в которую будем записывать x ** abs(y) в цикле for
            for each_time in range(abs(y) - 1):  # Уможаем x сам на себя |y| раз
                tmp *= x
            return 1 / tmp
        else:
            print('y должен быть целым отрицательным числом.', file=sys.stderr)
    else:
        print('x должен быть вещественным положительным числом.', file=sys.stderr)


if __name__ == '__main__':
    print('Ответ:', my_func(10.0, -1))
else:
    print(f'Модуль {__name__} импортирован.')


# Written by PaulKorotenko
