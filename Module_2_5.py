#Домашняя работа по уроку "Функции в Python.Функция с параметром"
#Цель: закрепить навык написания функций и их вызовов.
#
#Задача "Матрица воплоти":
##Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.
#
#Пункты задачи:
#   Объявите функцию get_matrix и напишите в ней параметры n, m и value.
#    Создайте пустой список matrix внутри функции get_matrix.
#    Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
#    В первом цикле добавляйте пустой список в список matrix.
#    Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
#    Во втором цикле пополняйте ранее добавленный пустой список значениями value.
#    После всех циклов верните значение переменной matrix.
#    Выведите на экран(консоль) результат работы функции get_matrix.
#
#Пример результата выполнения функции:
#Исходный код:
#result1 = get_matrix(2, 2, 10)
#result2 = get_matrix(3, 5, 42)
#result3 = get_matrix(4, 2, 13)
#print(result1)
#print(result2)
#print(result3)
#Вывод на консоль:
#[[10, 10], [10, 10]]
#[[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
#[[13, 13], [13, 13], [13, 13], [13, 13]]
#Примечания:
#    Вложенный список - это строка матрицы, элементы вложенных списков(глубже) - это столбцы матрицы.
#    В случае передачи аргумента со значением 0 или меньше, будет возвращаться пустой список.
#======================

def get_matrix1( n, m, value ) :  # n - количество строк, m - количество столбцов
    matrix1 = []
    for i in range( n ) :
            matrix1.append( [ value ] * m )
    return matrix1
#======================

def get_matrix2( n, m, value ) :  # n - количество строк, m - количество столбцов
    matrix2 = [[] * m] * n
#    print( matrix2 )
    for i in range( n ) :
        matrix2[i] = [ value ] * m
    return matrix2
#======================

def get_matrix3( n, m, value ) :  # n - количество строк, m - количество столбцов
    # Формирование пустой матрицы размерностью n * m
    line = [[]] * m
    matrix3 = [[]] * n
    for i in range(n):
        matrix3[i] = line
    # Заполнение пустой матрицы значениями "value"
    for i in range(n):
        for j in range(m):
            matrix3[i][j] = value
    return matrix3
#======================

result1 = get_matrix1( 2, 2, 10 )
result2 = get_matrix1( 3, 5, 42 )
result3 = get_matrix1( 4, 2, 13 )
print( 'result1 =', result1 )
print( 'result2 =', result2 )
print( 'result3 =', result3 )
print( '' )

result4 = get_matrix2( 2, 2, 10 )
result5 = get_matrix2( 3, 5, 42 )
result6 = get_matrix2( 4, 2, 13 )
print( 'result4 =', result4 )
print( 'result5 =', result5 )
print( 'result6 =', result6 )
print( '' )

result7 = get_matrix3( 2, 2, 10 )
result8 = get_matrix3( 3, 5, 42 )
result9 = get_matrix3( 4, 2, 13 )
print( 'result7 =', result7 )
print( 'result8 =', result8 )
print( 'result9 =', result9 )



