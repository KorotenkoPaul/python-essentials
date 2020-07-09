# Запрашиваем ввод в упользователя
usr_int = input('Введите число: ')
# Создаём переменную, в которую будет сохранять максимальную цифру в пользовательском числе
max_num = 0
# Создаём цикл, в котором проверяем каждую цифру пользовательского числа на то,
# больше ли она чем цифра, сохранённая в max_num
while usr_int:
    current_digit, usr_int = int(usr_int[0]), usr_int[1:]
    if current_digit > max_num:
        max_num = current_digit

# Вывод максимальной цифры в stdout
print(max_num)


# Written by PaulKorotenko
