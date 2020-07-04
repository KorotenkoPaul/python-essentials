# --- Первый способ ---
def person_info_first(name, surname, year_of_birth, city, email, phone_number):
    """
    Выводит информацию о пользователе.
    Для этого используется предварительно подготовленная строка output.
    """
    output = (f'Name: {name}  Surname: {surname}  Year of birth: {year_of_birth}  '
              f'City: {city}  E-mail: {email}  Phone number: {phone_number}')
    print(output)


# --- Второй способ ---
def person_info_second(name, surname, year_of_birth, city, email, phone_number):
    """
    Выводит информацию о пользователе.
    Для этого используется словарь локальных переменных.
    """
    for key, value in locals().items():
        print(f'{key.capitalize()}: {value}', end='  ')
    print()


# Запускаем первую (ordinal = 1) или вторую (ordinal = 2) функцию
ordinal = 1
if ordinal == 1:
    print('Вы запустили первый способ.')
    person_info_first(name='Paul', surname='Korotenko', year_of_birth=1996, city='Moscow',
                      email='dev.paul@mail.ru', phone_number='+7(985)208-43-96')
elif ordinal == 2:
    print('Вы запустили второй способ.')
    person_info_second(name='Paul', surname='Korotenko', year_of_birth=1996, city='Moscow',
                       email='dev.paul@mail.ru', phone_number='+7(985)208-43-96')
else:
    import sys
    print('Выберите одну из двух функций.\n'
          'Для это укажите её номер в переменной ordinal.', file=sys.stderr)


# Written by PaulKorotenko
