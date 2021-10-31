"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class TrafficLight:
    __color = None
    __color_1 = 'red'
    __color_2 = 'yellow'
    __color_3 = 'green'


    def __init__(self):
        self.__color = self.__color_1
        self.__color = self.__color_2
        self.__color = self.__color_3


    def running(self, red: int=7, yellow: int=2, green: int=5):
        while red:
            print(f'Красный свет. Осталось: {red} сек')
            time.sleep(1)
            red -= 1
        print('Включается желтый')


        while yellow:
            print(f'Желтый свет. Осталось: {yellow} сек')
            time.sleep(1)
            yellow -= 1
        print('Включается зеленый')


        while green:
            print(f'Зеленый свет. Осталось: {green} сек')
            time.sleep(1)
            green -= 1
        print('Включается красный')


traffic_light = TrafficLight()
traffic_light.running()

