# Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 
# y el propio número y se representa por el número seguido de un signo de exclamación. 
# Por ejemplo 5! = 1x2x3x4x5=120),

cont = 1
factorial = 1
num = int(input('Indica un número: '))
for var in range(1,num):
    while cont <= num:
        factorial = factorial * cont
        cont += 1
print('El factorial de ',num,' es: ',factorial)
