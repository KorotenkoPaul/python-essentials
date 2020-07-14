import time
from itertools import cycle


class TrafficLight:
    """Светофор"""

    def __init__(self, color):
        # Создаём приватное поле __color (цвет светофора)
        self.__color = color

    def running(self):
        """При вызове данного метода цвет __color светофора начинает переключаться по списку цветов modes."""
        # В переменную modes сохраняем цвет и количество секунд, отведённое на него
        modes = [('red', 7), ('yellow', 2), ('green', 5)]
        # В цикле for бесконечно меняем цвет светофора
        for self.__color, wait in cycle(modes):
            print(self.__color)
            time.sleep(wait)


# Создаём экземпляр класса TrafficLight
tl = TrafficLight('green')
# Вызываем метод running созданного экземпляра
tl.running()


# Written by PaulKorotenko
