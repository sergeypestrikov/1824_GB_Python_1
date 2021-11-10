"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
**********************************
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение
компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
"""


class Warehouse:
    pass


class Equipment:
    def __init__(self, name, quantity, price, guarantee: bool, *args):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.guarantee = guarantee
        self.my_warehouse_full = []
        self.my_warehouse = []
        self.unit = {'Модель': self.name, 'Количество': self.quantity, 'Цена': self.price, 'Гарантия': self.guarantee}

    def __str__(self):
        return f'{self.name}, {self.quantity}, {self.price}, {self.guarantee}'


    def accept(self):
        try:
            unit_name = input(f'Введите название: ')
            unit_quantity = int(input(f'Введите количество: '))
            unit_price = int(input(f'Введите цену: '))
            unit_guarantee = input(f'Введите данные по гарантии: ')
            uniq = {'Модель': unit_name, 'Количество': unit_quantity, 'Цена': unit_price, 'Гарантия': unit_guarantee}
            self.unit.update(uniq)
            self.my_warehouse.append(self.unit)
            print(f'Список доступных устройств {self.my_warehouse}')
        except:
            return f'Ошибка'

        print(f'Нажать Enter для продолжения, q для выхода')
        q = input(f'>>> ')
        if q == 'Q' or q == 'q':
            self.my_warehouse_full.append(self.my_warehouse)
            print(f'Все товары {self.my_warehouse_full}')
            return f'Выход'
        else:
            return Equipment.accept(self)

class Printer(Equipment):
    def print(self):
        return f'Указать кол-во {self.numb}'

class Scanner(Equipment):
    def scan(self):
        return f'Указать кол-во {sef.numb}'

class Copier (Equipment):
    def copy(self):
        return f'Указать кол-во {self.numb}'


unit_1 = Printer('epson', 3, 5000, True)
unit_2 = Scanner('hp', 1, 10000, False)
unit_3 = Copier('xerox', 5, 7000, True)
print(unit_1.accept())
print(unit_2.accept())
print(unit_3.accept())
# print(unit_1.print())
# print(unit_2.scan())
# print(unit_3.copy())