import functools
import operator  # Этот импорт необяхателен (только для operator.mul)


# Создаём генератор чётных чисел от 100 до 1000 включительно
even_nums = (num for num in range(100, 1001) if num % 2 == 0)
# Перемножаем между собой ранее полученный ряд чисел
# operator.mul - это то же самое, что и lambda x, y: x * y
total = functools.reduce(operator.mul, even_nums)
# Выводим полученное произведение в stdout
print(f'Ответ: {total}')
