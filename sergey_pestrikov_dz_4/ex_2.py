import requests
import xml.etree.ElementTree as ET

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