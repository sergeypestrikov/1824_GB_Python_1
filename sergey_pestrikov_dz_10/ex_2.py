"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""

class Clothers:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def make_coat(self):
        return self.size / 6.5 + 0.5

    def make_suite(self):
        return self.height * 2 + 0.3

    @property
    def full_production(self):
        return str(f'Общая площадь ткани {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')



class Coat(Clothers):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.make_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь такани для пальто {self.make_coat}'

class Suit(Clothers):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.make_suite = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани для костюма {self.make_suite}'


coat = Coat(5, 3)
suit = Suit(5, 3)
print(coat)
print(suit)
print(coat.full_production)
