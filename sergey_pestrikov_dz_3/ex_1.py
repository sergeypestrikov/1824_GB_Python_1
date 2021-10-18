dict_translate = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(num):
    for i in dict_translate:
        if num in i:
            print(dict_translate.get(i))
    else:
        return None


num_translate('five')

# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.