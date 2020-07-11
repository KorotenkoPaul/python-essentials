# Открываем заранее созданный файл staff.txt в режиме чтения 'r'
with open('staff.txt') as file:
    # Создаём словарь "сотрудник: оклад"
    info = {person: int(salary) for person, salary in (line.split() for line in file.readlines())}
    # Создаём список сотрудников с окладом менее $20000
    less_than_twenty = [person for person in info.keys() if info[person] < 20000]
    # В переменную average_salary записываемсредний оклад сотрудников фирмы
    average_salary = sum(info.values()) / len(info)

# Выводим необходимую информацию в stdout
print(f'Сотрудники с окладом менее $20.000: {", ".join(less_than_twenty)}')
print(f'Средний оклад: ${average_salary:.2f}')


# Written by PaulKorotenko
