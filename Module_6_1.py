"""
Домашнее задание по теме "Зачем нужно наследование"
===================================================
Цель: применить базовые знания о наследовании классов для решения задачи
------------------------------------------------------------------------
ЗАДАЧА "Съедобное, несъедобное":
Разнообразие животного мира давно будоражит умы человечества.
    Царства, классы, виды... Почему бы и нам не попробовать
    выстроить что-то подобное используя наследования классов?
Необходимо описать пример иерархии животного мира,
            используя классы и принцип наследования.
"""
#=================================================================
class Animal :
    alive = True    # Живой
    fed = False     # Накормленный
    def __init__( self, name ) :    # Название животного
        self.name = name

    def eat( self, food ) : # food - принимает объекты классов растений.
        self.food = food
#        print( '  self.food =', self.food )
#        print( '  food.name =', food.name )
#        print( 'food.edible =', food.edible )

        if self.food.edible :
            self.fed = True
            print( f'{self.name} съел {food.name}' )
        else :
            self.fed = False
            print( f'{self.name} не стал есть {food.name}' )

        if self.fed :
            self.alive = True
            print( f'{self.name} насытился!' )  ##
        else :
            self.alive = False
            print( f'{self.name} умер!' )       ##


class Mammal( Animal ) :
    pass

class Predator( Animal ) :
    pass

class Plant :
    edible = True   # Съедобность по умолчанию!
    def __init__( self, name ) :    # Название растения
        self.name = name

class Flower( Plant ) :
    edible = False  # Несъедобно
    pass

class Fruit( Plant ) :
    edible = True  # Съедобно
    pass

#=================================================================
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print( ' a1.name =', a1.name )
print( ' a2.name =', a2.name )
print( ' p1.name =', p1.name )
print( ' p2.name =', p2.name, '\n' )

print( 'a1.alive =', a1.alive )
print( '  a2.fed =', a2.fed )
print( '-----------' )
a1.eat( p1 )
a2.eat( p2 )
print( '-----------' )
print( 'a1.alive =', a1.alive )
print( '  a2.fed =', a2.fed )




