def add(usr_input: str) -> float:
    """
    Принимает строку символов, разделённых пробелами.
    Если строка имеет в себе отличный от числа символ,
    то возвращается сумма всех чисел, а этот символ игнорируется.
    """
    # Преобразовываем переданную строку в список символов, которые в строке были разделены пробелами
    usr_str_list = usr_input.split()
    # Преобразовываем полученный ранее список символов в список чисел (нечисловые символы фильтруются)
    usr_num_list = list(map(float, filter(lambda x: x.isdigit(), usr_str_list)))
    return sum(usr_num_list)


total = 0
while True:
    # Запрашиваем ввод у пользователя
    get_input = input('Введите числа: ')
    # Прибавляем все введённые пользователем числа к переменной total
    total += add(get_input)
    # Вывод итоговой суммы в stdout
    print(f'Итог: {total}', end='\n\n')
    # Символ Q или q завершает работу программы
    if 'Q' in get_input.upper():
        break


# Written by PaulKorotenko
