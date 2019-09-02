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
class Person:
    def __init__(self,health,armour,weapon):
        self.health=health
        self.armour=armour
        self.weapon=weapon
        self.no_armour=False
        self.no_live=False
        self.num_attacks=0
        self.num_defends=0

    def get_health(self):
        return self.health,self.armour,self.no_armour,self.no_live,self.num_attacks,self.num_defends

    def attacks(self):
        self.num_attacks=self.num_attacks+1

    def defends(self,weapon):
        if self.armour>0:
            self.armour=self.armour-weapon
        else:
            self.no_armour=True

        if self.health>0 and self.no_armour:
            self.health=self.health-weapon

        if self.health<0:
            self.no_live=True

        self.num_defends = self.num_defends + 1

class Fighter(Person):
    def __init__(self,side,health,armour,weapon):
        Person.__init__(self,health,armour,weapon)
        self.side=side
    def is_dead(self):
        state = Person.get_health(self)
        return state[3]



#side 0 player 1, side 1 player 2

Player1 = Fighter(0,100,120,25)
Player2 = Fighter(1,100,100,30)
import random

while True:
    choice = random.randint(0,1)
    if choice > 0:
        print ("#player 1 gets attacked by player 2")
        Player2.attacks()
        Player1.defends(Player2.weapon)
    else:
        print ("#player 2 gets attacked by player 1")
        Player1.attacks()
        Player2.defends(Player1.weapon)

    print("        state","hlth","arm","arm","dead","att","def")
    print("player1 state",Player1.get_health())
    print("Player2 state",Player2.get_health())


    if Player1.is_dead():
        print("fight is over Player2 won")
        break;

    if Player2.is_dead():
        print("fight is over Player1 won")
        break;

    print("press key to next round,1-exit")
    key=input()

    if key == "1":
        break;
