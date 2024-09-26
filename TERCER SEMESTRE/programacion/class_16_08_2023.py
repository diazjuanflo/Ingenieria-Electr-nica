#Listas
lista = ["Juan",2,"Mango", 1.85]
print(lista)
print(lista[0])
print("")
print("")
print("")
lista.insert(2,"Rodrigo") #Agrega un elemnto a la lista en una posiciòn en especifico
lista.append("usco") #Agrega un elemento al final de la lista
lista.append(input("Digite la ciudad: ")) #Agrega un elemento al final de la lista
del lista[0] #Elimina un elemento de la lista 
for z in lista:
    print(z)

w = len(lista)
q = 0

print("")
print("")
print("")

while q < w:
    print(lista[q])
    q +=1

eliminar = input("Digite el valor que desea eliminar: ")
contador = 0

for z in lista: #Con este codigo podemos eliminar un valor
    if eliminar ==z:
        del lista[contador]
    else:
        contador += 1
print(lista)

datos = [['hola','efe','rodrigo'],['holis','veneco','huila'],['javio', 'pola','o miedo']]]

for z in datos: #Con este codigo podemos imprimir una matriz
    for u in z:
        print(u)
    print("----------------")

