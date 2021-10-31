"""
Реализовать базовый класс Worker (работник). Определить атрибуты:
name, surname, position (должность), income (доход); последний атрибут должен быть защищённым и
ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income); проверить работу примера
на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров.
"""
class Worker:
    name = None
    surename = None
    position = None
    __income = None

    def __init__(self, name, surename, position, income):
        self.name = name
        self.surname = surename
        self.position = position
        self.income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        self.__income = income
        return self.__income


worker = Worker('Стивен', 'Джобс', 'CEO', {'wage': 10000, 'bonus': 5000})

worker.get_full_name()
worker.get_total_income()