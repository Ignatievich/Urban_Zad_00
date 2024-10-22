"""
Домашняя работа по уроку "Пространство имен."
=============================================
 Урок "Пространства имен и области видимости"
---------------------------------------------
  - Создайте новый проект в PyCharm
  - Запустите созданный проект

Ваша задача:
  - Создайте новую функцию test_function
  - Создайте внутри test_function другую функцию - inner_function,
  Эта функция должна печатать значение "Я в области видимости функции test_function"
  - Вызовите функцию inner_function внутри функции test_function
  - Попробуйте вызывать inner_function вне функции test_function и посмотрите
                                            на результат выполнения программы

Файл с кодом module_4_2.py загрузите на GitHub репозиторий и пришлите ссылку на него.
"""

#=== Описание вложенных функций ===============
# В Python не предусмотрено средств для запуска вложенных функций,
# однако, если внешнюю функцию создать как класс, то это возможно:
class test_function() :
    print('Я в области видимости функции (класса) test_function')
    def inner_function() :
        print( 'Я в области видимости функции inner_function' )

#=== Тестирование функций =====================
test_function()
test_function.inner_function()
