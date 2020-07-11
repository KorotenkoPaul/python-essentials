import json


# Открываем файл companies.txt в режиме чтения 'r'
with open('companies.txt') as file:
    # Создаём переменную profits, в которой будем хранить прибыли всех компаний листинга
    profits = []
    # Создаём список result с двумя вложенными словарями
    # Далее мы будем заполнять эти словари компаниями и их финансовыми результатами,
    # а также средней прибылью всех компаний листинга
    result = [{}, {}]
    for line in file:
        # Сохраняем в переменную company_name название компании
        company_name = line.split()[0]
        # Сохраняем в переменную current_res финансовый результат рассматриваемой компании
        current_res = int(line.split()[2]) - int(line.split()[3])
        # Добавляем в первый словарь списка result пару "компания: финансовый результат"
        result[0][company_name] = current_res
        # Добавляем в ранее созданный список profits финансовый результат рассматриваемой компании
        # если она закончила финансовый год с прибылью
        if current_res >= 0:
            profits.append(current_res)
    # Сохраняем в переменную average_profit средний финансовый результат всех компаний листинга,
    # закончивших финансовый год с прибылью
    average_profit = sum(profits) / len(profits)
    # Сохраняем во второй словарь списка result среднюю прибыль компаний листинга
    result[1]['average_profit'] = average_profit


# Открываем файл data.json на запись и сохраняем в него полученный ранее список result в формате JSON
with open('data.json', 'w') as file:
    json.dump(result, file, indent=4)

# Вывод сообщения о завершении работы программы
print('Сериализация завершена.')


# Written by PaulKorotenko
