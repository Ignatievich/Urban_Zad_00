# Функция интерпретирующая деление на ноль как ошибку:

def fake_divide( first, second ) :
    if second != 0 :
        result = first / second
    else :
        result = 'Ошибка!'
    return result

