src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# самый "трудоемкий" способ
uniq_nums = [el for el in src if src.count(el) == 1]
print(uniq_nums)

# с несоблюдением последовательности
uniq_nums = set()
tmp = set()
for el in src:
    if el not in tmp:
        uniq_nums.add(el)
    else:
        uniq_nums.discard(el)
    tmp.add(el)
print(list(uniq_nums))

# правильный вариант
uniq_nums_ord = [el for el in src if el in uniq_nums]
print(uniq_nums_ord)