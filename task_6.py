# Создаём "Товары"
goods = [(1, {'title': '', 'price': '', 'amount': '', 'unit': ''}),
         (2, {'title': '', 'price': '', 'amount': '', 'unit': ''}),
         (3, {'title': '', 'price': '', 'amount': '', 'unit': ''})]

# Запрашиваем все данные у пользователя и обновляем "Товары"
for item in goods:  # Для каждого товара
    for param in item[1]:  # Для каждой характеристики
        item[1][param] = input(f'{item[0]}. {param} >>> ')

# Создаём словарь со статистикой
stats = {'title': [item[1]['title'] for item in goods],
         'price': [item[1]['price'] for item in goods],
         'amount': [item[1]['amount'] for item in goods],
         'unit': [item[1]['unit'] for item in goods]}

# Товары
print(f'Товары: {goods}')
# Статистика
print(f'Статистика: {stats}')


# Written by PaulKorotenko
