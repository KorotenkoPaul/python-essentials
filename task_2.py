# Инициализируем список пользовательских строк
usr_list = []
# Бесконечный цикл, в котором пользователь каждый раз вводит некоторую строку
while True:
    usr_item = input('Введите элемент: ')
    if usr_item.capitalize() == 'Q':
        # Символ Q или q завершает работу цикла
        break
    else:
        # Введённая строка доавляется в список пользовательских строк
        usr_list.append(usr_item)

# Initial list: ['1', '2', 'Hello', 'Hi', 'Bye', 'Take care', '100%']
print(f'Initial list: {usr_list}')

# Обходим каждый элемент списка usr_list
for ind in range(len(usr_list)):
    # Если это элемент с нечётным значением индекса, т.е. 1, 3, 5, 7 ...
    if ind % 2 == 1:
        # ... то меняем значеними этот и предыдущий элемент
        usr_list[ind], usr_list[ind - 1] = usr_list[ind - 1], usr_list[ind]

# Changed list: ['2', '1', 'Hi', 'Hello', 'Take care', 'Bye', '100%']
print(f'Changed list: {usr_list}')


# Written by PaulKorotenko
