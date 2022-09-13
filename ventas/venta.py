"""
Práctica 2: Calcular precio de venta

Enunciado: dado el valor de venta de productos, 
hallar el IVA (21%) y el precio de venta 

Análisis: para la solución de este problema, 
se requiere que el usuario ingrese el valor de venta de producto
y el sistema debe realizar el cálculo respectivo para hallar el IVA y el
precio de venta, para esto use la siguiente expresión.

IVA = vv * 0.21

pv = vv + IVA

"""
#Mensaje de la aplicación 
print("---- REALIZAR UNA VENTA ----")

#Entrada de datos
vv = float(input('Ingrese el valor de venta: '))

#Operaciones
iva = vv * 0.21
pv = vv + iva

#Salida de datos
print('='*35)
print('---- FACTURA DE VENTA ----')
print('='*35)
print('Valor de venta: ',vv)
print('IVA: ', iva)
print('Precio de ventas: ',pv)
print('='*35)