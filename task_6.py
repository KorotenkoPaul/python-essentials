# Результат в первый день
first_day_distance = int(input('Введите расстояние в первый день: '))
# Цель
target_distance = int(input('Введите целевое расстояние: '))
day = 1
# Пока расстояние (которое каждый день увеличивается на 10%) меньше целевого расстояния
while first_day_distance < target_distance:
    first_day_distance *= 1.1
    day += 1

# Выводим ответ в stdout
print(f'Цель будет достигнута на {day}-ый день')


# Written by PaulKorotenko
