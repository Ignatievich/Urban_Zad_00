"""
Дополнительное практическое задание по модулю: "Наследование классов."
======================================================================
Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
-------------------------------------------------------------------------------------
ЗАДАНИЕ "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт,
            но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты,
            но... Что лежит в основе удобного использования таких объектов?
По названию задачи можно понять, что все геометрические фигуры обладают
            схожими свойствами, такими как: длины сторон, цвет и др.
Давайте попробуем реализовать простейшие классы для некоторых таких фигур
            и при этом применить наследование (в будущем, изучая сторонние
            библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):
--------------------------------------------------------------------------------------
Общее ТЗ:
            Реализовать классы Figure(родительский), Circle, Triangle и Cube,
            объекты которых будут обладать методами изменения размеров, цвета и т.д.
            Многие атрибуты и методы должны быть инкапсулированны и для них должны
            быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
--------------------------------------------------------------------------------------
"""
from math import pi, sqrt

class Figure :
    sides_count = 0
    def __init__(self, color, *sides) :  # Цвет и стороны
        self.__sides = []     # создаём список сторон ( целые числа )
        self.__color = list( color )  # заполняем список цветов в формате RGB
        self.sides = list( sides )   # длина каждой из сторон ( целые числа )
        self.filled  = False    # Закрашенный, bool
        if self.__is_valid_sides( *sides ) :
            for i in range( self.sides_count ) :
                self.__sides.append( self.sides[i] ) # Заполняем список значениями
        else :
            for i in range( 0, self.sides_count ) :
                if self.n == 1 :
                    self.__sides.append( *self.sides )  # Заполняем список значениями 1
                else :
                    self.__sides.append( 1 )  # Заполняем список self.__sides значениями 1

    # Метод возвращает список RGB цветов
    def get_color( self ) :
        return list( self.__color)

    # Метод проверяет корректность переданных значений ( от 0 до 255 )
    def __is_valid_color( self, r, g, b ) :
        return ( 0 <= r <= 255 ) and ( 0 <= g <= 255 ) and ( 0 <= b <= 255 )

    # Изменяет атрибут __color на соответствующие значения, предварительно
    # проверив их на корректность. Если некорректны -- цвет остаётся прежним!
    def set_color( self, r, g, b ) :
        if self.__is_valid_color( r, g, b) :
            self.__color = ( r, g, b )

    # Служебный метод, принимает неограниченное кол-во сторон, возвращает
    # True если все стороны целые положительные числа и кол-во новых
    # сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides( self, *new_sides ) :
        self.new_sides = list( new_sides )       # Вынимаем кортеж из кортежа...
        flgPos = True   # Все стороны - положительные числа
        self.n = 0       # Счётчик переданного количества сторон
        for sid in self.new_sides :
            self.n += 1
            if sid <= 0 :     # Чтобы длины сторон были неотрицательными
                flgPos = False  # Сторона оказалась отрицательной
        return flgPos and ( self.n == self.sides_count )

    # Метод возвращает значения атрибута __sides
    def get_sides( self ) :
        return self.__sides

    # Метод возвращает периметр фигуры.
    def __len__( self ) :
        return sum( self.__sides )

    # Метод принимает новые стороны, если их количество не равно sides_count,
    # то не изменяет, в противном случае - меняет
    def set_sides( self, *new_sides  ) :
        new_sid = list( new_sides )
        if self.__is_valid_sides( *new_sides ) :     # Проверка новых длин на достоверность
            self.__sides = new_sid
        else :
            if self.n == 1 :    # Если передана одна сторона, то все делаем равными новой!
                self.__sides = []
                for i in range( self.sides_count ) :
                    self.__sides.append( *new_sid )  # Заполняем список значениями = 1


class Circle( Figure ) :
    sides_count = 1
    def __init__( self, color, *sides ) :
        super().__init__( color, *sides )
        sid = list( sides )
        self.__radius = int( sid[0] ) / ( 2 * pi )

    def get_radius(self):       ## Чисто для проверки!!!!
        return self.__radius

    # Метод возвращает площадь круга (определить через дл.окружности или радиус)
    def get_square( self ) :
        AreaOfCircle = self.__radius ** 2 * pi
        return AreaOfCircle


class Triangle( Figure ) :
    sides_count = 3

    # Метод возвращающий площадь треугольника (по формуле Герона)
    def get_square( self ) :
        a = self._Figure__sides[0]
        b = self._Figure__sides[1]
        c = self._Figure__sides[2]
        p = ( a + b + c ) / 2
        p = ( p * (p-a)*(p-b)*(p-c))
        AreaOfTriangle = sqrt( p )
        return AreaOfTriangle

class Cube( Figure ) :
    sides_count = 12
    def __init__( self, color, *sides ):
        super().__init__( color, *sides )

    # Метод возвращающий объём куба.
    def get_volume( self ) :
        self.volume = int( *self.sides ) ** 3
        return self.volume

#======================================================
#=== Код для проверки: ================================
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

## Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

## Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

## Проверка периметра (круга), это и есть длина:
print(len(circle1))

## Проверка объёма (куба):
print(cube1.get_volume())
