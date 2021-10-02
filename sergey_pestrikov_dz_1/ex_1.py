duration = int(input('Введите число: '))

days = duration // 3600 // 24
hours = duration // 3600 % 24
minutes = duration // 60 % 60
seconds = duration % 60

print(f'{days} дн, {hours} час, {minutes} мин, {seconds} сек')