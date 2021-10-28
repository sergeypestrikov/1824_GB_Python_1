# Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.

import re


def email_parse(email):
    parsed = re.findall(r'([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$', email)
    if not parsed:
        raise ValueError(f'Неверный e-mail: {email}')
    return dict(zip(['username', 'domain'], parsed[0]))


print(email_parse('someone@geekbrains.ru'))