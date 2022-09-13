anno = int(input('Introduce un año: '))

if anno % 4 == 0:
    if anno % 100 == 0:
        if anno % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto,')
else:
    print('El año no es bisiesto.')
