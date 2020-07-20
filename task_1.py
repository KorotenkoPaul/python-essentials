class Matrix:
    """Матрица"""

    def __init__(self, source):
        # Создаём приватное поле __source
        self.__source = source

    def __str__(self):
        # Возвращает строку, в которой все элементы ряда объединены символом табуляции
        # а все ряды - символом переноса строки
        return '\n'.join('\t'.join(str(num) for num in row) for row in self.__source)

    def __add__(self, other):
        # Количество строк
        rows = range(len(self.__source))
        # Количество столбцов
        cols = range(len(self.__source[0]))
        # Результирующий список
        result = [[self.__source[row][col] + other.__source[row][col] for col in cols] for row in rows]
        # Создаём новый экземпляр класса Matrix
        return Matrix(result)


# Первая матрица
first_array = [[31, 22, 3], [37, 43, 92], [51, 86, 11]]
first_matrix = Matrix(first_array)
print(first_matrix, end='\n\n')

# Вторая матрица
second_array = [[53, 12, 43], [7, 40, 12], [1, 73, 7]]
second_matrix = Matrix(second_array)
print(second_matrix, end='\n\n')

# Сумма матриц
print(first_matrix + second_matrix)
