from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        menu = """
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS

        1 - Rectangulo
        2 - Circulo
        3 - Salir
        Ingrese una opción: """

        opcion = input(menu)

        if opcion == '1':
            base = float(input('Ingrese Base: '))
            altura = float(input('Ingrese Altura: '))
            r = Rectangulo(base, altura)
            probar_figura(r)

        elif opcion == '2':
            radio = float(input('Ingrese Radio: '))
            c = Circulo(radio)
            probar_figura(c)
        elif opcion == '3':
            print('Cerrando sistema')
            break
        else:
            print('Opción incorrecta')


if __name__ == '__main__':
    main()