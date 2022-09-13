class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def moverse(self):
        print('Ando caminado')

class Atleta(Persona):

    def moverse(self):
        print('Ando corriendo')

class Ciclista(Persona):
    
    def moverse(self):
        print('Ando moviendome en mi bicicleta')