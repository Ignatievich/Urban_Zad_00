# Функция интерпретирующая деление на ноль как бесконечность (infinity):
from math import inf

def true_divide( first, second ) :
    if second != 0 :
        result = first / second
    else :
        result = inf
    return result
