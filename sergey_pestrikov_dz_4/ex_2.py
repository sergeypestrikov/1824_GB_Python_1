import requests
import xml.etree.ElementTree as ET

# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
# возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат
# числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо
# float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре
# был передан аргумент? В качестве примера выведите курсы доллара и евро.

url = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(code):
    code = code.upper()
    response = requests.get(url)

    for valute in ET.fromstring(response.text).findall('Valute'):
        if code == valute.find('CharCode').text:
            return float(valute.find('Value').text.replace(',', '.'))


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))