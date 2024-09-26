#camelCase< suma resta < funciones, metodos, variables o objetos
#PascalCase< Funciones < SumaDosNumeros < Archivos, Paquetes, Clases

#FUNCIONES-> def


def suma():
    a=20
    b=30
    print('Suma',a+b)

suma()

#Ejemplo 2

def resta():
    c=30
    d=10
    return (c-d)

print(resta())

def resta_dos():
    c=30
    d=15
    return ("saludo")

print(resta_dos())

incremento = resta() + 20

print("El resultado es: ", incremento)

def alum():
    return ["Juan","diaz"]
print(alum())
print(alum()[0])

for val in alum():
    print("Nombre")

def nombre():
    return {'Maria':"Juan",'Pedro':'Miguel'}

for i in nombre():
    print("Nombre: {i} Apellido: ", nombre()[])