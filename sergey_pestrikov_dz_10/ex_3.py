"""
Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки
арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и округление до целого числа деления клеток, соответственно.
"""

class Cell:
    def __init__(self, cell_numb: int):
        self.cells = cell_numb

    def __str__(self):
        return f'В этой клетке {self.cells * "*"} ячеек'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return self.cells - other.cells if (self.cells - other.cells) > 0 else print('Отрицательно')

    def __mul__(self, other):
        return Cell(int(self.cells * other.cells))

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def __truediv__(self, other):
        return Cell(round(self.cells / other.cells))

    def make_order(self, cells_row):
        row = ''
        for i in range(int(self.cells / cells_row)):
            row += f'{"*" * cells_row} \\n'
        row += f'{"*" * (self.cells % cells_row)}'
        return row


cell_a = Cell(30)
cell_b = Cell(10)
print(cell_b)
print(cell_a + cell_b)
print(cell_a - cell_b)
print(cell_a.make_order(5))
print(cell_b.make_order(15))
print(cell_a / cell_b)
