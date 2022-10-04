secreto = 'asdf'
while True:
    clave = input('dime la clave: ')
    if clave != secreto:
        print('Error...')
    if clave ==  secreto:
        break;
print('FIN')