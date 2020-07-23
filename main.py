from card import Card
import random


class Game:
    def __init__(self):
        # Composition: when we instantiate Game we cause Card instantiation
        self.user = Card("Your card")
        self.computer = Card("Computer's card")

    @staticmethod
    def __gen_number():
        """Returns a generator object of unique integer numbers from 1 to 90"""
        numbers = list(range(1, 91))
        while numbers:
            # Get a random number from numbers
            current = random.choice(numbers)
            # Remove it so that it won't show up again
            numbers.remove(current)
            yield current, len(numbers)

    @staticmethod
    def __total_numbers_left(card):
        """
        Returns False if the passed loto card has at least one number left
        Otherwise returns True
        """
        all_cells_list = sum(card, [])
        left_numbers = [number for number in all_cells_list if number.strip().isdigit()]
        return False if left_numbers else True

    def __check_usr_numbers(self, current_number):
        """
        Checks if a current number presents among user loto card numbers
        If so - cross that number out
        """
        for usr_row in self.user.card:
            if str(current_number) in usr_row:  # If there is the number among user numbers
                while True:  # Loop until user enters 'y' or 'n'
                    response = input('Do you want to cross the number out? (y/n)\n>>> ')
                    if response == 'y':
                        self.user.cross_out(current_number)
                        print(f'{current_number} is crossed out!', end='\n\n')
                        break  # Break while loop
                    elif response == 'n':
                        print('YOU LOSE!')
                        return True  # Should we break the game (external) loop? Yes
                break  # Break for loop
        else:  # If there is no such number among user numbers
            while True:  # Loop until user enters 'y' or 'n'
                response = input('Do you want to cross the number out? (y/n)\n>>> ')
                if response == 'y':
                    print('YOU LOSE!')
                    return True  # Should we break the game (external) loop? Yes
                elif response == 'n':
                    break

    def __check_cmt_numbers(self, current_number):
        """
        Checks if a current number presents among computer loto card numbers
        If so - cross that number out
        """
        for cmt_row in self.computer.card:
            if str(current_number) in cmt_row:
                self.computer.cross_out(current_number)

    def play(self):
        """Starts playing process"""
        # Create a new generator
        number = self.__gen_number()
        while True:
            tuple_ = next(number)  # next(number) should not be called twice
            current_number, numbers_left = f'{tuple_[0]:>2}', tuple_[1]
            print(self.computer, self.user, sep='\n')
            print(f'NUMBER: {current_number} (left: {numbers_left})', end='\n\n')
            if self.__check_usr_numbers(current_number) or self.__check_cmt_numbers(current_number):
                break  # Break the game loop if user misprinted
            if self.__total_numbers_left(self.user.card):
                print('YOU WIN!')
                break  # Break the game loop if user wins
            if self.__total_numbers_left(self.computer.card):
                print('YOU LOSE!')
                break  # Break the game loop if user loses


game = Game()
game.play()
