# -*- coding: utf-8 -*-
import random
    
def run():
    encontrado = False
    vida = 3
    numero_inicial = int (input ('Ingresa el número inicial: '))
    numero_final = int (input ('Ingresa el número final: '))
    numero_random = random.randint(numero_inicial, numero_final)
    print(numero_random)

    while not encontrado:
        numero = int (input ('Intenta un número: '))
        vida = vida - 1
        if numero == numero_random:
            print('Felicidades, encontraste el numero')
            encontrado = True
        
        if numero > numero_random:
            print('El número es más pequeño')
        
        if numero < numero_random:
            print('El número es más grande')

        if vida <= 0:
            print("Haz perdido. Utilizaste todas las vidas")
            encontrado = True
            print("")
            denuevo = input ('¿Quieres jugar de nuevo? Si - No ')
            if denuevo == 'Si':
                numero_inicial = int (input ('Ingresa el número inicial: '))
                numero_final = int (input ('Ingresa el número final: '))
                numero_random = random.randint(numero_inicial, numero_final)
                encontrado = False
                vida = 3
            else:
                print("Gracias por jugar")


if __name__ == '__main__':
    run()