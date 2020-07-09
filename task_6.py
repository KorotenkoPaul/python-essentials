from itertools import count, cycle


# Первый требуемый итератор count(3) в контексте цикла for
for integer in count(3):
    if integer >= 10:  # Завершить цикл, как только итератор вернёт число большее или равное 10-и
        break
    print('int:', integer)


# Второй требуемый итератор cycle(iterable) в контексте функции enumerate
iterable = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for ordinal, day in enumerate(cycle(iterable)):  # для порядкового номера, дня недели в ...
    if ordinal == 15:  # если порядковый номер равен 15, то завершить цикл
        break
    print('day:', day)

