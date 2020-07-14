class Car:
    """Автомобиль"""

    def __init__(self, speed: int, color: str, name: str, *, is_police: bool):
        # Создаём 4 публичных поля
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """Возвращает информацию о начале движения."""
        return f'{self.name} starts driving'

    def stop(self):
        """Возвращает информацию о торможении."""
        return f'{self.name} has braked'

    def turn(self, direction: str):
        """Возвращает информацию о повороте в определённом направлении."""
        return f'{self.name} turned {direction}'

    def show_speed(self):
        """Возвращает информацию о скорости автомобиля."""
        return f"{self.name}'s speed is {self.speed} km/h"


class TownCar(Car):
    """Городской автомобиль"""

    def show_speed(self):
        """
        Возвращает информацию о скорости автомобиля,
        а также предупреждает, если было превышено ограничение скорости 60 км/ч.
        """
        if self.speed > 60:
            print(f'ATTENTION: Exceeding the speed limit!')
        return super().show_speed()


class SportCar(Car):
    """Спортивный автомобиль"""

    def accelerate(self):
        """Возвращает информацию об ускорении."""
        return f'{self.name} has accelerated'


class WorkCar(Car):
    """Рабочий автомобиль"""

    def show_speed(self):
        """
        Возвращает информацию о скорости автомобиля,
        а также предупреждает, если было превышено ограничение скорости 40 км/ч.
        """
        if self.speed > 40:
            print(f'ATTENTION: Exceeding the speed limit!')
        return super().show_speed()


class PoliceCar(Car):
    """Полицейский автомобиль"""

    def __init__(self, speed: int, color: str, name: str, *, is_police: bool, siren: str):
        # Вызываем метод __init__ родителя и передаём ему необходимые аргументы
        super().__init__(speed, color, name, is_police=is_police)
        # Создаём новое публичное поле siren (полицеская сирена)
        self.siren = siren

    def toggle_siren(self, mode: str):
        """Переключает сирену, а также возвращает информацию о текущем состоянии сирены."""
        self.siren = mode
        return f'Siren: {self.siren}'


# BMW
bmw = TownCar(70, 'red', 'BMW', is_police=False)
print(f'{bmw.name} >>> {bmw.color}')
print(f'{bmw.go()}')
print(bmw.show_speed(), end='\n\n')

# Bugatti
bugatti = SportCar(210, 'blue', 'Bugatti', is_police=False)
print(f'{bugatti.name} >>> {bugatti.color}')
print(f'{bugatti.go()}')
print(bugatti.accelerate())
print(bugatti.show_speed())
print(bugatti.stop(), end='\n\n')

# Ford
ford = WorkCar(50, 'gray', 'Ford', is_police=False)
print(f'{ford.name} >>> {ford.color}')
print(f'{ford.go()}')
print(ford.show_speed(), end='\n\n')

# Mercedes
mercedes = PoliceCar(60, 'white', 'Mercedes', is_police=True, siren='off')
print(f'{mercedes.name} >>> {mercedes.color}')
print(f'{mercedes.go()}')
print(mercedes.toggle_siren('on'))
print(f"{mercedes.turn('right')}")
print(mercedes.show_speed(), end='\n\n')


# Written by PaulKorotenko
