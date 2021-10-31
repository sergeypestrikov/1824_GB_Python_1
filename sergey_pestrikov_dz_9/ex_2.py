"""
Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
"""

class Road:
    _length = None
    _width = None
    weight = None
    depth = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('На строительство дороги')

    def _createRoad(self):
        self.weight = 25
        self.depth = 5
        create = int(self.length * self.width * self.weight * self.depth / 1000)
        print(f'Требуется {create} тонн астфальта')


road = Road(20, 5000)
road._createRoad()