class OperadorException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        
def divir(a, b):
    if b == 0:
        raise ZeroDivisionError('Error: No se puede dividir por cero!')
    else:
        return a / b

divir(4, 0)