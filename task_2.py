# Для этого задания используется файл, созданный в задаче №1
# Открываем этот файл в режиме чтения 'r'
with open('usr_input.txt') as file:
    # Поскольку файл - это "одноразовый" итератор, то сначала сохраним его содержимое в переменную row_amount
    # для последующего многократного использования
    row_array = file.readlines()
    # Переменная row_amount содержит количество строк файла file
    row_amount = len(row_array)
    # Инициализируем переменную word_amount, которая будет хранить список слов в каждой строке файла file
    word_amount = []
    for row_ind in range(row_amount):
        # Для каждой строки файла file мы добавляем в список word_amount количество слов в этой строке
        word_amount.append(len(row_array[row_ind].split()))

# Вывод необходимой информации в stdout
print(f'Количество строк: {row_amount}')
# print ниже выглядит так: "Количество слов в 1, 2, 3 строке соответственно: 5, 5, 4"
print(f'Количество слов в {", ".join([str(i + 1) for i in range(row_amount)])} '
      f'строке соответственно: {", ".join([str(i) for i in word_amount])}')


# Written by PaulKorotenko
