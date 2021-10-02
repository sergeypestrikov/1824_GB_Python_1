for number in range(1, 101):
    if number % 10 == 1 and number % 100 != 11:
        print(f'{number} процент')
    elif 1 < number < 5 and not 11 < number % 100 < 15:
        print(f'{number} процента')
    else:
        print(f'{number} процентов')