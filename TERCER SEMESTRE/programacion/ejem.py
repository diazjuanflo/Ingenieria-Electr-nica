def verificar_edad(edades):
    for edad in edades:
        if edad < 19:
            print("No puede ingresar!")
        else:
            print("Bienvenido!")

edad_uno = int(input("Digite su edad: "))
edad_dos = int(input("Digite su edad: "))
edad_tres = int(input("Digite su edad: "))
edad_cuatro = int(input("Digite su edad: "))
edad_cindo = int(input("Digite su edad: "))

# Vector de edades
edades = [edad_uno, edad_dos, edad_tres, edad_cuatro, edad_cindo]

# Llamamos a la función para verificar las edades
verificar_edad(edades)