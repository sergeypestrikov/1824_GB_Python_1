"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        new_matrix = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                new_matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matrix]))


result = Matrix([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]],
                [[1, 2 , 3],
                [4, 5, 6],
                [7, 8, 9]])

print(result.__add__())
