# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os

folders = ['settings', 'mainapp', 'adminapp', 'authapp']

starter = os.path.join('my_project')
if not os.path.exists(starter):
    os.mkdir(starter)

for f in folders:
    folder = os.path.join(starter, f)
    if not os.path.exists(folder):
        os.mkdir(folder)