#Практическое задание по уроку "Базовые структуры данных"

# Задача №1 (просто) "Арифметика":
print( "1st program", '"Арифметика"' )
print( 9 ** 0.5 * 5 )

# Задача №2 (просто) "Логика":
print( "2st program", '"Логика"' )
print( 9.99 > 9.98 )
print( 1000 != 1000.1 )

# Задача №3 (средне) "Школьная загадка":
print( "3st program", '"Школьная загадка"' )
print( 2 * 2 + 2 )
print( 2 * ( 2 + 2 ) )
print( ( 2 * 2 + 2 ) == ( 2 * ( 2 + 2 ) ) )

#Задача №4 (сложно) "Первый после точки":
sStroka = '123.456'
print( "4st program", '"Первый после точки"' )
print( 'sStroka =', sStroka )
fStroka = float( sStroka )
print( 'fStroka =', fStroka )
iRezultat = int( ( ( fStroka - ( fStroka // 1 ) ) * 10 ) // 1 )
print( 'Rezultat =',  iRezultat )

