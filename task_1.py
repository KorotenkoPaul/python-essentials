import sys


def salary(hours, rate, bonus) -> float:
    """Расчитывает заработную плату по формуле."""
    return (hours * rate) + bonus


try:
    # Множественное присваивание генератора-коллекции
    # передаваемых пользователем числовых значений
    # Первым параметром следует передавать количество отработанных часов
    # Вторым - почасовую ставку, третьим - премию
    usr_hours, usr_rate, usr_bonus = map(float, sys.argv[1:])
    # Вывод подсчитанной заработной платы в stdout
    print(f'Итог: ${salary(usr_hours, usr_rate, usr_bonus)}')
except ValueError:
    # Вывод сообщения о неправильном вводе в stderr
    print('Введите три значения!', file=sys.stderr)
