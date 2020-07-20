# Инициализируем структуру рейтинга
rating = [7, 5, 3, 3, 2]

# Запрашиваем у пользователя число
usr_number = int(input('Введите число: '))
# Добавляем пользовательское число в структуру рейтинга
rating.append(usr_number)
# Сортируем структуру рейтинга в порядке убывания
rating.sort(reverse=True)

# Вывод в stdout
print(f'Результат: {rating}')


# Written by PaulKorotenko
