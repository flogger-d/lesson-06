#!/usr/bin/python3
# -*- encoding utf-8 -*-



# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


# Камень - ножницы - бумага. Person - ввод с консоли, Enemy - случайный выбор оружия

import random

weapons = [
     'камень',
     'ножницы',
     'бумага'
]

W = dict(zip(weapons, range(0,3)))
print(str(W))

class Person:
     def __init__(self):
          self._health = 100
          self._damage = 10
          self._armor = 20
          self._weapon = 'камень'
          self._name = ''

     def set_weapon(self):
          pass

     @property
     def health(self):
          return self._health

     @property
     def weapon(self):
          return self._weapon

     @property
     def name(self):
          return self._name

     def _hit(self, damage):
          print("{} получил повреждения {} ".format(self.name, damage))
          self._health -= damage

     def attack(self, enemy):
          I = self._weapon
          He = enemy._weapon
          if (I != 'бумага' and W[He]-W[I] == 1) or (I == 'бумага' and He == 'камень' ):
               enemy._hit( self._damage * self._health * 0.01 )


class Player(Person):
     def __init__(self):
          super().__init__()
          self._name = 'Player'

     def set_weapon(self):
          I = ''
          while I not in weapons:
               I = input("Ваш ход: ")
          self._weapon = I

class Enemy(Person):
     def __init__(self):
          super().__init__()
          self._name = 'Enemy'

     def set_weapon(self):
          self._weapon = weapons[random.randint(0,2)]

class Game:
     def __init__(self):
          self._player1 = Player()
          self._player2 = Enemy()

     def Loop(self):
          while self._player1.health > 0 and self._player2.health > 0:
               print("Начало раунда: ")
               print("Статус: вы - {}, враг - {}".format(self._player1.health, self._player2.health))

               self._player1.set_weapon()
               self._player2.set_weapon()

               print("Оружие: вы - {}, враг - {}".format(self._player1.weapon, self._player2.weapon))
               self._player1.attack(self._player2)
               self._player2.attack(self._player1)

               print("Конец раунда: ")
               print("Статус: вы - {}, враг - {}".format(self._player1.health, self._player2.health))

               input("Продолжим")

          if self._player1.health > 0:
               print("Победа")
          else:
               print("Поражение")


if __name__ == "__main__":
     game = Game()
     game.Loop()

