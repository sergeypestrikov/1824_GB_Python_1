"""
Реализовать базовый класс Worker (работник). Определить атрибуты:
name, surname, position (должность), income (доход); последний атрибут должен быть защищённым и
ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income); проверить работу примера
на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров.
"""
income = {'wage': 10000, 'bonus': 5000}


class Worker:

    def __init__(self, name: str, surename: str, position: str, income: dict):
        self.name = name.title()
        self.surname = surename.title()
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


worker = Position('Стивен', 'Джобс', 'CEO', income)

print(worker.get_full_name(), worker.get_total_income())
