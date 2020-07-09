# Запрашиваем у пользователя исходное количество секунд
usr_sec = int(input('Введите количество секунд: '))
# Формируем количество часов
hours = usr_sec // 3600
# Формируем количество минут
minutes = usr_sec % 3600 // 60
# Формируем количество секунд
seconds = usr_sec % 60
# Создаём переменную time для последующего вывода в stdout
time = f'{hours:02}:{minutes:02}:{seconds:02}'
print(time)


# Written by PaulKorotenko
