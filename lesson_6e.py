# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)




# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от н

class Car:
    def __init__(self,color,name):
        self.speed=0 #stoped
        self.dir=1#up 2 right 3 down 4 left
        self.color=color
        self.name=name

        self.is_police=False#all cars are not rotten

    def go(self):
        self.speed = self.speed + 5

    def stop(self):
        self.speed = 0

    def turn(self,_dir):
        self.dir = _dir

    def get_vel(self):
        return self.speed

    def get_dir(self):
        return self.dir

    def get_police(self):
        return self.is_police

    def set_police(self,is_police):
        self.is_police=is_police


class XCar(Car):
    def __init__(self,color,name,car_type):
        Car.__init__(self,color,name)

        self.car_type=car_type

        if self.car_type=="PoliceCar":
            Car.set_police(self,True)
        else:
            Car.set_police(self,False)

    def getXCar_type(self):
        return self.car_type


#create each cars

TownCar = XCar("red","buick","TownCar")

PoliceCar = XCar("none","lada","PoliceCar")


#TownCar.go()
if TownCar.get_vel():
    print("car is moving")
else:
    print("car is stopped")

print("direction of",TownCar.getXCar_type()," is ", TownCar.get_dir())

print (PoliceCar.get_police())
print (TownCar.get_police())

PoliceCar.turn(2)

print("direction of",PoliceCar.getXCar_type()," is ", PoliceCar.get_dir())



