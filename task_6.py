def int_func(word: str) -> str:
    """Возвращает переданное слово, начинающееся с заглавной буквы."""
    return word.capitalize()


# Запрашиваем ввод у пользователя
usr_input = input('Введите предложение: ')
# Инициализируем пустой строкой переменную, которая будет содержать результирующее предложение
capitalized_sentence = ''
for each_word in usr_input.split():
    # Конкатенация результирующего предложения с каждым словом, написанным с заглавной буквы и пробелом в конце
    capitalized_sentence += (int_func(each_word) + ' ')
# Обрезаем завершающий пробел и выводим в stdout
print(capitalized_sentence.rstrip())


# Written by PaulKorotenko
