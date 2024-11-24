"""
Домашнее задание по теме "Множественное наследование"
=====================================================
Цель: закрепить знания множественного наследования в Python.
-----------------------------------------------------------
ЗАДАЧА "Ошибка эволюции":
Замечали, что некоторые животные в нашем мире обладают странными
и, порой, несовместимыми друг с другом свойствами? Например, утконос...
Вроде есть клюв, но не птица. Вроде милый, а есть шипы на задних лапах.
А ещё он откладывает яйца... Опустим факт о том, что они потеют молоком
и попробуем не эволюционным способом создать нашего утконоса.

"""
import random

class Animal :              # Животные
    live = True
    sound = None            # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0   # степень опасности существа
    DEGREE_OF_DANGER = _DEGREE_OF_DANGER
    _cords = [ 0, 0, 0 ]    # Начальные координаты существа

    def __init__(self, speed) :
        self.speed = speed

    def move(self, dx, dy, dz) :

        if self._cords[2] < 0 :
            print( "It's too deep, i can't dive :(" )   # Слишком глубоко, я не могу нырнуть
        else :
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print( f'X: {self._cords[0]}   Y: {self._cords[1]}   Z: {self._cords[2]}' )

    def attack(self):
        if self._DEGREE_OF_DANGER < 5 :
            print( "Sorry, i'm peaceful :)" )   # Извините, я мирный
        else :
            print( "Be careful, i'm attacking you 0_0" ) # Будьте осторожны, я нападаю на вас 0_0

    def speak(self) :
        print( '  sound:', self.sound )

class Bird( Animal ) :          # Птицы
    beak = True                 # наличие клюва

    def lay_eggs(self) :
        print( f"Here are(is) {random.randint( 1, 4 )} eggs for you", end='' )
        print( '   # Число может быть другим (1-4)' )

class AquaticAnimal( Animal ) : # Плавающие
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz) :
        self.speed /= 2
        self._cords[2] -= abs( dz ) * self.speed
        self._cords[2] = int( self._cords[2] )

class PoisonousAnimal( Animal ) :   # Ядовитые
    _DEGREE_OF_DANGER = 8

class Duckbill( PoisonousAnimal, AquaticAnimal, Bird ) :
    sound = "Click-click-click"

#======================================================================
db = Duckbill(10)

print( 'db.live:', db.live )
print( 'db.beak:', db.beak )

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()




