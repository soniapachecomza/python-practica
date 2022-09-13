"""
Practica 5: Conversor de monedas

* Crear un sistema que convierta la moneda nacional a dolares por 
ejemplo de pesos argentinos a dólares, soles peruanos a dolares, pesos méxicanos a dólares, pesos colombianos a dólares.

* Para solucionar este problema se requiere que el usuario ingrese la cantidad de monedas nacionales
y luego realizar la conversión.

* Para este sistema debe hacer un menú de navegación para la cantidad de monedas nacionales y luego realizar la 
conversión.

"""
def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f'Ingrese cantidad de {pais}: '))

    dolares = cantidad_moneda / valor_dolar

    dolares = round(dolares, 2)
    print(f'Tienes ${dolares} Dolares')

def main():

    while True:
        menu = """
        1-Pesos Argentinos a Dolares
        2-Soles Peruanos a dolares
        3-Pesos Mexicanos a Dolares
        4-Pesos Colombianos a Dolares
        5_Pesos Chilenos a Dolares
        6-Real Brasileños a Dolares
        7-Salir
        Ingrese una opción: """

        opcion = input(menu)

        if opcion == '1':
            convertir(0.0077, 'pesos argentinos')
        elif opcion == '2':
            convertir(0.26, 'soles peruanos')
        elif opcion == '3':
            convertir(0.049, 'pesos mexicanos')
        elif opcion == '4':
            convertir(0.00022, 'pesos colombianos')
        elif opcion == '5':
            convertir(0.0011, 'pesos chilenos')
        elif opcion == '6':
            convertir(0.19, 'real brasileño')
        elif opcion == '7':
            print("Cerrando conversor de monedas")
            break
        else:
            print("Opción incorrecta!!!")
            print("Vuelve a imgresar la opción correcta")
#Inicio de la aplicación 
if __name__ == '__main__':
    main()