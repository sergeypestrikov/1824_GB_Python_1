duration = int(input('Введите число: '))

days = duration // 3600 // 24
hours = duration // 3600 % 24
minutes = duration // 60 % 60
seconds = duration % 60

print(f'{days} дн, {hours} час, {minutes} мин, {seconds} сек')

# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.