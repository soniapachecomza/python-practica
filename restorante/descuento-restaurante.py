"""
Actividad 2
Descuentos de un restaurante 
Enunciado: un restaurante ofrece un descuento del 10% para 
consumo de hasta s/.100.00 y descuento del 20% para
consumos mayores, para ambos casos se aplica un impuesto del 
21%. Determinar el monto del descuento, el impuesto y el importe a pagar
Análisis: para la solución de este problema, se requiere que el usuario ingrese
el consumo y verifica y calcula el monto del descuento, el impuesto
y el importe a pagar

* monto del descuento
* impuesto
* importe a pagar
"""
# Entrada
from functools import total_ordering


consumo = float(input('Ingrese el consumo del cliente: '))

#Proceso
if consumo <= 100:
    #Descuemto del 10%
    dato_descuento = '10%'
    descuento = consumo * 0.10
elif consumo > 100: 
    #Descuento es del 20% 
    dato_descuento = '20%'
    descuento = consumo * 0.20

monto_descuento = consumo - descuento
iva = monto_descuento * 0.21
total_pagar = monto_descuento + iva

#Salida
print('='*30)
print('----FACTURA DE CONSUMO----')
print('Descuento que se aplica: ', dato_descuento)
print('='*30)
print('Consumo: ', consumo)
print('Descuento: ', descuento)
print('Monto con descuento: ', monto_descuento)
print('IVA: ', iva)
print('Total a pagar: ', total_pagar)
print('='*30)

