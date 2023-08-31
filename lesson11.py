#Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
#Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Transport:
    name = ''
    max_speed = 0
    weight = 0

class Car(Transport):
    name = 'BMW'
    max_speed = 250
    weight = 1.5
class Airplane(Transport):
    name = 'AirBus'
    max_speed = 800
    weight = 80

class Ship(Transport):
    name = 'Titanic'
    max_speed = 42
    weight = 52

