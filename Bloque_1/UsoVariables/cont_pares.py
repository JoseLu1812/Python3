cont = 0
for var in range(1,6):
    num = int(input('Introduzca un número: '))
    if num % 2 == 0:
        cont = cont + 1
print('Has introducido ',cont,' número pares.')