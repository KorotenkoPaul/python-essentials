# Открываем файл numbers.txt в режиме записи и чтения 'w+'
with open('numbers.txt', 'w+') as file:
    # Подготавливаем строку с числами, которые мы будем записывать в файл numbers.txt
    str_numbers = '1 2 3 4 5 6 7 8 9 10'
    # Записываем подготовленную строку в файл numbers.txt
    file.write(str_numbers)
    # Перемещаем указатель в начало файла
    file.seek(0)
    # Создаём список чисел, прочитанных из файла numbers.txt
    int_numbers = [int(num) for num in file.read().split()]

# Выводим сумму чисел в stdout
print(f'Сумма чисел: {sum(int_numbers)}')


# Written by PaulKorotenko
