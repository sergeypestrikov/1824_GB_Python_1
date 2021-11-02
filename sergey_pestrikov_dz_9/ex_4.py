"""
Реализуйте базовый класс Car. у класса должны быть следующие атрибуты:
speed, color, name, is_police(булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда); опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""
import random

class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = random.randint(10, 100)
        print(f'Машина едет со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Машина остановилась')

    def turn(self, direction: str):
        if self.speed > 30:
            print(f'Машина повернула на скорости {self.speed} км/ч')
        else:
            print(f'Машина повернула на {direction}')


    def show_speed(self):
        if self.speed == 0:
            print(f'Машина стоит')
        else:
            print(f'Текущая сторость {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if 0 < self.speed <= 60:
            print(f'Скорость машины {self.speed} км/ч')
        elif self.speed > 60:
            print(f'Превышение! Скорость {self.speed} км/ч')
        else:
            print(f'Машина стоит')

class WorkCar(Car):

    def show_speed(self):
        if 0 < self.speed <= 30:
            print(f'Скорость машины {self.speed} км/ч')
        elif self.speed > 30:
            print(f'Превышение! Скорость {self.speed} км/ч')
        else:
            print(f'Машина стоит')

class SportCar(Car):
    color: str = 'желтый'
    name: str = 'Dodge Charger'
    is_polise: bool = False


class PoliceCar(Car):
    color: str = 'белый'
    name: str = 'BMW'
    is_polise: bool = True

    def show_speed(self):
        print(f'Со спецсигналами')


mini = TownCar(30, 'красный', 'MINI', False)
mini.go()
mini.show_speed()
mini.turn('лево')

ford = TownCar(40, 'черный', 'Ford', False)
ford.go()
ford.show_speed()
ford.turn('право')

dodge = SportCar(120, 'желтый', 'Dodge Charger', False)
dodge.go()
dodge.show_speed()
dodge.turn('лево')

bmw = PoliceCar(100, 'белый', 'BMW', True)
bmw.go()
bmw.show_speed()
bmw.turn('лево')

