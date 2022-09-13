"""
Actividad 3
Descuentos del restaurante:
Enunciado: debido a los excelentes resultados decide 
ampliar sus ofertas de acuerdo a la siguiente escala 
de consumo, ver la tabla. Determinar el monto del descuento,
el importe del impuesto y el importe a pagar.

Consumo(S/.)      Descuento (%)
    * Hasta 100        10
    * Mayor a 100      20
    * Mayor a 200      30

Análisis: para la solución de este problema, se requiere que el 
usuario ingrese el consumo y el sistema verifica y calcula el monto
del descuento y el impuesto a pagar.
"""
# Entrada
from functools import total_ordering


consumo = float(input('Ingrese el consumo del cliente: '))

#Proceso
if consumo > 0:
    if consumo <= 100:
        #Descuemto del 10%
        dato_descuento = '10%'
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200: 
        #Descuento es del 20% 
        dato_descuento = '20%'
        descuento = consumo * 0.20
    elif consumo > 200: 
        #Descuento es del 30% 
        dato_descuento = '30%'
        descuento = consumo * 0.30

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
else:
    print('Error al ingresar el consumo')