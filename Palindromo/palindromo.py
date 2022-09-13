"""
*Crear un sistema que detecte si una palabra es palindromo o no.

* Para solucionar este problema el usuario tiene que ingresar por 
pantalla una palabra y el sistema verifica si es palindroma o no.

* Una palabra palindroma se lee de igual forma de derecha  y de izquierda.

"""

def palindromo(palabra):
    #luzazul
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

#Función principal
def main():
    palabra = input('Ingrese una palabra: ')

    es_palindromo = palindromo(palabra)

    if es_palindromo: 
        print('Es Palindromo')
    else:
        print('No es Palindromo')

#Entrada
if __name__ == '__main__':
    main()