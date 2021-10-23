# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
import re

result = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for row in f:
        pars = re.split('--|"| ', row)
        item = pars[0], pars[6], pars[7]
        result.append(item)

print(result)
