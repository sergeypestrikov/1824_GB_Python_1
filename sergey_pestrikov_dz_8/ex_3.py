# Написать декоратор для логирования типов позиционных аргументов функции

def type_logger(func):
   def wrapper(*args):
       val = func(5)
       return val

   return wrapper


@type_logger
def calc_cube(х):
   return х ** 3

a = calc_cube()

print(a)
print(type(calc_cube))
print(type(type_logger))