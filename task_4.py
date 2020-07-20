# Создаём список пользовательских слов
usr_words = input('Введите слова: ').split()

# Для каждого индекса и слова в usr_words
for ind, word in enumerate(usr_words):
    # Устанавливаем слово в зависимости от его длины
    word = word if len(word) <= 10 else word[:10]
    # Выводим пронумерованный список в stdout
    print(f'{ind + 1}. {word}')


# Written by PaulKorotenko
