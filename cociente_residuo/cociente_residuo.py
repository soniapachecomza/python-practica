"""
Práctica 1: Calcular cociente y cociente_residuo
Enunciado: hallar el cociente y el residuo (resto)
de dos números enteros.
Análisis: para la solución de este problema, se requiere
que el usuario ingrese dos números enteros
y el sistema realice el cálculo respectivo 
para hallar el cociente y el residuo.
"""

print('Calcular cociente y residuo')

#entrada de datos
a = input('Ingrese el primer número: ')
b = input('Ingrese el segundo número: ')

#operación
a = int(a)
b = int(b)

cociente = a // b
residuo = a % b

print('El cociente es: ', cociente)
print('El residuo es: ', residuo)