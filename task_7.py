def fact(x: int) -> int:
    """
    Возвращает факториал переданного числа num.
    Эквивалентна функции math.factorial(x).
    """
    if x == 1:
        # Базовый случай
        return 1
    else:
        # Рекурсивный вызов самой себя
        return x * fact(x - 1)


# --- Первый способ ---
def gen_fact_first(end):
    """
    Генерирует факториалы чисел, начиная с 1 до end включительно.
    """
    for num in range(1, end + 1):
        yield fact(num)


# Вывод первого способа в stdout
print('Первый способ: ', end='')
for factorial_first in gen_fact_first(5):
    print(factorial_first, end='  ')
print()


# --- Второй способ ---
def gen_fact_second(end):
    return (fact(num) for num in range(1, end + 1))


# Вывод второго способа в stdout
print('Второй способ: ', end='')
for factorial_second in gen_fact_second(5):
    print(factorial_second, end='  ')
print()
