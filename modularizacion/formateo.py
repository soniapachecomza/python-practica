from sys import argv

if len(argv) == 4:
    nombre = argv[1]
    edad = int(argv[2])
    altura = float(argv[3])

    #print(f'Nombre: {} \nEdad: {} \nAltura: {}'.format(nombre, edad, altura))
    print(f'Nombre: {nombre} \nEdad: {edad} \nAltura: {altura}')

else:
    print('Error, ingrese los argumentos correctamente')
    print('Ejemplo: formate.py "Nombre" 25 1.60')