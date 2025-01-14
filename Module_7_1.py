"""
Практическое задание
Домашнее задание по теме "Режимы открытия файлов"
=======================================================================
Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
-----------------------------------------------------------------------
ЗАДАЧА: "Учёт товаров":
    Необходимо реализовать 2 класса product и Shop, с помощью
        которых будет производиться запись в файл с продуктами.
    Объекты класса product будут создаваться следующим образом
        - product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
            1. Атрибут name - название продукта (строка).
            2. Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
            3. Атрибут category - категория товара (строка).
            4. Метод __str__, который возвращает строку в формате '<название>, <вес>,
                <категория>'. Все данные в строке разделены запятой с пробелами.

    Объекты класса Shop будут создаваться следующим образом
        - Shop() и обладать следующими свойствами:
            1. Инкапсулированный атрибут __file_name = 'products.txt'.
            2. Метод get_products(self), который считывает всю информацию
                из файла __file_name, закрывает его и возвращает единую строку
                    со всеми товарами из файла __file_name.
            3. Метод add(self, *products), который принимает неограниченное
                количество объектов класса product. Добавляет в файл __file_name
                каждый продукт из products, если его ещё нет в файле (по полю name
                И по полю category). Если такой продукт уже есть, то увеличивает
                общий вес и выводит строку 'Продукт <название> уже был в магазине,
                    его общий вес теперь равен <вес> .
"""

class Product : # Класс "Продукт"
    name = ''       # Название продукта
    weight = 0.0    # Общий вес товара
    category = ''   # Категория товара
    def __init__(self, name, weight, category) :
        self.name = name
        self.weight = weight
        self.category = category

    # Возвращает строку в формате '<название>, <вес>, <категория>'
    def __str__(self) :
        strP = self.name + ', ' + str( self.weight ) + ', ' + self.category
        return strP

class Shop :    # Класс "Магазин"
    __file_name__ = 'products.txt'

    # Cчитывает всю информацию из файла __file_name и закрывает файл.
    # Возвращает единую строку со всеми товарами из файла __file_name.
    def get_products(self) :
        file = open( self.__file_name__, 'r' )
        getProds = file.read()
        file.close()
        return getProds

    # Добавляет в файл __file_name каждый продукт из products,
    def add( self, *products ) :
        for new in products :
            self.addUnoProd( new )  # Добавляем продукты по одному...

    # Добавляет в файл __file_name один продукт из products,
    # если его ещё нет в файле (по полю name И по полю category)
    def addUnoProd(self, unoProd):
        strProds = self.get_products()  ## Получаем строку из файла "__file_name"
        splitProds = strProds.split( '\n' )  # Разделяем строку по продуктам
        # Формируем список в списке - продуктов записанных в файле "__file_name" строкой
        listProds = []
        for prod in splitProds:
            elemProds = prod.split( ', ' ) # Разделяем строку по параметрам
            listProds.append( elemProds )
        for prod in listProds : # Проверяем список считанный из файла "__file_name"
            nameNo = True   # Предполагаем, что название и категория НЕ содержатся в списке
            if unoProd.name == prod[0] :
                if unoProd.category == prod[2] : # Сносим, чтобы не возникала ошибка при первой записи в файл!
                    prod[1] = str( float( prod[1] ) + unoProd.weight )
                    print( f'Продукт { prod[0] } уже был в магазине, его общий вес теперь равен { prod[1] }' )
                    nameNo = False  # Оказалось, что продукт содержится в списке!
                    break
        newProd = ''
        if nameNo :
            newProd = unoProd.name + ', ' + str(unoProd.weight) + ', ' + unoProd.category + '\n'
            # Добавляем новый продукт в файл "__file_name"
            file = open(self.__file_name__, 'a')
            file.write( newProd )
            file.close()
        else : # В этом случае нужно переписывать весь файл с новым весом продукта!
            strProds = ''
            for prod in listProds :
                strProd = ''
                for elem in prod :
                    strProd += ( elem + ', ' )
                strProd = strProd[:-2]  # Убираем последний разделитель ', '
                strProds += ( strProd + '\n' )
            strProds = strProds[:-1]   # Убираем последний разделитель '\n'
            # Придётся полностью переписать файл "__file_name"
            with open( 'products.txt', 'w' ) : # Сначала очищаем содержимое файла!
                pass
            file = open(self.__file_name__, 'w')
            file.write( strProds )
            file.close()

#=== ПРОВЕРКИ КОДА =========================================
s1 = Shop()
p1 = Product('Potato'   , 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4 , 'Groceries')
p3 = Product('Potato'   , 5.5 , 'Vegetables')

#p4 = Product('Citrus'   , 40.5, 'Argentina')   ##
#p5 = Product('Tomato'   , 30.8, 'Turkey')      ##
#p6 = Product('Citrus'   , 75.0, 'Ekvador')    ##
#p7 = Product('Citrus'   , 5, 'Argentina')   ##
#p8 = Product('Citrus'   , 5.0, 'Ekvador')    ##

#print( '1=>  s1.get_products() =\n', s1.get_products() )  ##
s1.add(p1, p2, p3)
print( s1.get_products() )
#print( '2=>  s1.get_products() =\n', s1.get_products() )  ##
#s1.add(p4, p5, p6)  ##
#print( '3=>  s1.get_products() =\n', s1.get_products() )  ##
#s1.add( p7, p8 )  ##
#print( '4=>  s1.get_products() =\n', s1.get_products() )  ##

