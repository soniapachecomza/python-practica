# -*- coding: utf-8 -*-

def protected(func):

    def wrapped(password):
        if password == 'platzi':
            return func()

        else:
            print('La contraseña es incorrecta')

    return wrapped

@protected
def protected_func():
    print('Tu contraseña es correcta.')

if __name__ == '__main__':
    password = str(input('Ingrese tu contraseña: '))

   
    protected_func(password)