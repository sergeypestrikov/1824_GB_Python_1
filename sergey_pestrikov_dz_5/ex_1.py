import sys

n = 15
# создание генератора
odd_nums_gen = (num for num in range(1, n + 1, 2))
print(next(odd_nums_gen), next(odd_nums_gen), next(odd_nums_gen), sep= ', ')
print(type(odd_nums_gen))


# использование yield
def nums_gen(start, end):
    for num in range(start, end + 1, 2):
        yield num


nums_list = nums_gen(1, n + 1)
print(*nums_list, sep=', ')
