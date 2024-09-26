class Coches:
    def __init__(self, marca, kilometraje, color):
        self.__marca = marca
        self.__kilometraje = kilometraje
        self.color = color

    def arrancar(self, arrancamos):
        self.arrancamos = arrancamos 
        if(self.arrancamos):
            if(self.arrancamos):
                return "El coche esta en movimiento"
            else: "El coche esta detenido"

    def __str__(self):
        return 'El auto de marca {} con kilometraje {} es de color {} y esta {}'. format(self.__marca,self.__kilometraje,self.color, objMicoche.arrancar(True))
    objMicoche = Coche('Mazda', 45000, 'Rojo')
    
objMicoche.color = 'Verde'
print(str(objMicoche))