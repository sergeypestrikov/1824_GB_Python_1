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
class Car:
    speed = None
    color = None
    name = None
    is_police = None


    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        direction = 'налево'
        print('Машина повернула', direction)



class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)


mini = TownCar(60, 'red', 'MINI')
print(mini.speed, mini.color, mini.name, mini.is_police)
mini.go()

dodge = SportCar(150, 'yellow', 'Dodge')
print(dodge.speed, dodge.color, dodge.name, dodge.is_police)
dodge.go()

ford = WorkCar(60, 'black', 'Ford')
print(ford.speed, ford.color, ford.name)
ford.turn('налево')

bmw = PoliceCar(120, 'white', 'BMW')
print(bmw.speed, bmw.color, bmw.name, bmw.is_police)
bmw.stop()

