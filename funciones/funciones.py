
def saludar(nombre):
    #global nombre
    #nombre = 'Sonia Pacheco'
    #edad = 40
    return f'Hola, {nombre} desde la función saludar', #nombre, edad
    #print('Hola desde la función saludar')
    #print('Hola', nombre)

    
saludo = saludar('Sonia')

def sumar(a, b):
    return a + b

def restar(a=None, b=None):
    if a == None or b == None:
        print('Error: debes enviar dos números a la función')
        return
    return a - b
"""
valor = saludar()
saludo, nombre, edad = saludar()
"""
#print(valor)
print(saludo)
#print(nombre, edad)
#print('Hola desde fuera de la función', nombre)
suma = sumar(20, 45)
print('La suma es: ', suma)

#resta = restar(b = 15, a = 30)
resta = restar()

print('La resta es: ', resta)