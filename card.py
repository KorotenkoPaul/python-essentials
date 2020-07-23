import random


class Card:
    """Card object represent a loto card"""

    def __init__(self, title):
        self.__title = title
        self.card = self.__create_card()

    @staticmethod
    def __gen_number():
        """Returns a generator object of unique integer numbers from 1 to 90"""
        numbers = list(range(1, 91))
        for _ in range(90):
            # Get a random number from numbers
            current = random.choice(numbers)
            # Remove it so that it doesn't show up again
            numbers.remove(current)
            yield current

    def cross_out(self, number):
        """Crosses out the number from the loto card"""
        for row in self.card:
            if str(number) in row:
                ind = row.index(str(number))
                row[ind] = '--'
                break

    def __create_card(self):
        """Creates a loto card with 15 numbers"""
        # Structured list of unique string numbers from 1 to 90
        rows = []
        # Get a generator object
        number = self.__gen_number()
        for _ in range(3):
            # Generate a row
            tmp = [f'{next(number):>2}' for _ in range(5)]
            tmp.sort()
            # Inserting empty cells in sorted tmp
            for _ in range(4):
                ind = random.randrange(len(tmp) + 1)
                tmp.insert(ind, '  ')
            # Add a row (tmp) to the list of rows
            rows.append(tmp)
        return rows

    def __str__(self):
        # The list of string rows
        rows = [' | '.join(row) for row in self.card]
        separator = '-' * len(rows[0])
        header = f'{self.__title:-^{len(rows[0])}}\n'
        footer = f'\n{separator}\n'
        return header + f'\n{separator}\n'.join(rows) + footer
