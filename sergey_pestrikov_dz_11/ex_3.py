"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""

class My_Numb_Exception:
    def __init__(self, *args):
        self.list_numbers = []

# self.list_numbers = [int(i) for i in input('Введите значения через пробел ').split()]
# val = int(input('Введите значения и нажимайте Enter - '))
# self.list_numbers.append(val)

    def input_number(self):
        while True:
            try:
                val = int(input('Введите число, затем enter: '))
                self.list_numbers.append(val)
                print(f'Список {self.list_numbers} \n')
            except:
                print(f'Недопустимый формат')
                try_again = input(f'Хотите попробовать снова? Введите Yes or No для продолжения: ')

                if try_again == 'Yes' or try_again == 'yes':
                    print(exception.input_number())
                elif try_again == 'No' or try_again == 'no':
                    return  f'До свидания'
                else:
                    return f'Команда не ясна. До свидания'


exception = My_Numb_Exception(10)
print(exception.input_number())