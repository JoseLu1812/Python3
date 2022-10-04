secreto = 'asdfa'
clave = input('Dime la  clave: ')
while clave != secreto:
    print('Clave no correcta...')
    otra = input('¿Quieres intentar con otra clave (Sí/No)? ')
    if otra.upper() == 'N':
        break;
    clave = input('Dime la  clave: ')
if clave == secreto:
    print('¡¡¡Clave correcta!!!')
print('FIN')