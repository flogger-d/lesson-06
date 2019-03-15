#!/usr/bin/python3
# encoding utf-8


# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
     def __init__(self):
          self.speed = 0
          self.direction = None
          self.color = None
          self.name = ''
          self.is_police = False

     def go(self):
          print("Едем вперед")

     def turn(self, direction):
          direction = direction
          print("Повернули на {}".format(self.direction) )

     def stop(self):
          print("Остановились")

class TownCar(Car):
     def __init__(self):
          super().__init__()
          self.speed = 60

class SportCar(Car):
     def __init__(self):
          Car.__init__(self)
          self.speed = 180

class WorkCar(Car):
     def __init__(self):
          Car.__init__(self)
          self.speed = 20
          self.color = 'желтый с синей полоской'

class PoliceCar(Car):
     def __init__(self):
          Car.__init__(self)
          self.speed = 120
          self.color = 'Белый с синей полоской'
          self.is_police = True

