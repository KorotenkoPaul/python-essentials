# Запрашиваем количество выручки
revenue = float(input('Выручка: '))
# Запрашиваем количество издержек
expenses = float(input('Издержки: '))
# Отработала ли компания в прибыль?
is_profitable = revenue > expenses
# Вывод информации о результатах работы компании
if is_profitable:
    profit = revenue - expenses
    profitability = 100 * (profit / revenue)
    print(f'Компания заработала: ${profit:.2f}')
    print(f'Рентабельность выручки: {profitability:.2f}%')
    staff = int(input('Количество сотрудников: '))
    print(f'Прибыль на сотрудника: ${profit / staff:.2f}')
else:
    loss = expenses - revenue
    print(f'Компания потеряла: ${loss:.2f}')  # ПОЧЕМУ ВЫВОДИТСЯ В ЭКСПОНЕНЦИАЛЬНОЙ ФОРМЕ?


# Written by PaulKorotenko
