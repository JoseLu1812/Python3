indicador = False
for var in range(1,6):
    num = int(input('Dime un número: '))
    if num % 2 == 0:
        indicador = True
if indicador:
    print('Sí se ha encontrado al menos un número par.')
else:
    print('No se ha encontrado ningún número par.')