"""
Домашнее задание по теме
"Доступ к свойствам родителя. Переопределение свойств."
============================================================
Цели: Применить сокрытие атрибутов и повторить наследование.
Рассмотреть на примере объекта из реального мира.
------------------------------------------------------------
ЗАДАЧА "Изменять нельзя получать":
В этой задаче мы реализуем классы транспорта, в которых нельзя будет
        просто так поменять цвет, мощность двигателя и прочие свойства,
т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных
        сервисах. Да, узнать значения этих свойств мы сможем, но вот изменить - нет.
Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт,
        а Sedan(седан) - наследник класса Vehicle.
"""
class Vehicle :
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''
    __COLOR_VARIANTS = ['Blue', 'Red', 'Green', 'Black', 'White']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def set_color(self, new_color ):
        self.New_color = new_color
        self.new_color = self.New_color.lower()    # Перевести новый цвет в ниж.рег
        color_variants = self.__COLOR_VARIANTS
        for n in range( len( color_variants ) ):   # Перевести все цвета в ниж.рег
            color_variants[n] = color_variants[n].lower()
        if self.new_color in color_variants :
            print(f'Можно сменить цвет на {new_color}')
            self.__color = new_color
        else :
            print(f'Нельзя смерить цвет на {new_color}')

    def print_info(self):
        print( '            Модель: ', self.get_model() )
        print( 'Мощность двигателя: ', self.get_horsepower() )
        print( '   Цвет транспорта: ', self.get_color() )
        print( '          Владелец: ', self.owner )
#        print( ' Модель автомобиля: ', self.__model )

class Sedan( Vehicle ) :
    __PASSENGERS_LIMIT = 5  # в седан может поместиться только 5 пассажиров

#============================================================================
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()





