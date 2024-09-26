#1. Escriba un programa que almacene la cadena de caracteres contraseña en una 
# variable, para luego preguntarle al usuario por la contraseña. 
#Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con 
# la guardada en variable.

#2. Realice un programa que le pida al usuario dos números por teclado y muestre por 
# consola su división. Si el divisor es cero el programa debe mostrar un error y solicitar
#nuevamente el numero.

#3. Escriba un programa que le pida al usuario por teclado un numero entero y 
# muestre en consola si es par o impar.

#4. Escriba que mediante un vector  de 5 item, lea cada item y evalué el ingreso a menores de 
# edad, si la persona tiene menos de 19 años el programa le debe mostrar 
#en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!

print("")
saludo = """
Bienvenido al programa de de inicio.

Por favor escriba su contraseña.
nota: las contraseñas deben ser con numeros.
"""
print(saludo)
contrasena = int(input("Escriba su contraseña: "))
print("")
print("")

saludo_2 = """
Por favor digite de nuevo su contraseña para entrar el programa
:)
"""

def ciclo():
    print(saludo_2)
    contrasena_2 = int(input("Digite su contraseña: "))

    if contrasena == contrasena_2:
        print("Felicidades la contraseña es correcta.")

    elif contrasena != contrasena_2:
        print("La contraseña es incorrecta")
        print("")
        print("Vuelva a intentarlo")
        ciclo()
    else:
        print("Ha ocurrido un error")
ciclo()

division = """

---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------

"""
print(division)

saludo_3 = """

Bienvenido al programa de division de 2 numeros

Por favor digite dos numero:

"""
print("")
print(saludo_3)

def division_num():

    num_uno = int(input("Digite el primer numero: "))
    num_dos = int(input("Digite el segundo numero: "))

    if num_dos == 0:
        print("")
        print("El numero dos no puede ser cero")
        print("No se puede dividir entre cero")
        print("Vuelve a intertarlo")
        division_num()
    elif num_dos != 0:
        resultado_division = num_uno / num_dos
        print("El resultado de la divisiòn es: ")
        print(resultado_division)

division_num()

division = """

---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------

"""
print(division)

#3. Escriba un programa que le pida al usuario por teclado un numero entero y 
# muestre en consola si es par o impar.


saludo_4 = """

Bienvenido al programa que te permite saber si el numero que ingresas es par

"""

print(saludo_4)
num_1 = int(input("Digite un numero: "))

resul = num_1 % 2
if resul != 0:
    print("El numero es impar")

elif resul == 0:
    print("El numero es par")
else:
    print("Ha ocurrido un error")
    
division = """

---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------

"""
#Escriba que mediante un vector  de 5 item, lea cada item y evalué el ingreso a menores de 
# edad, si la persona tiene menos de 19 años el programa le debe mostrar 
#en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!

saludo_5 = """

Bienvenido al programa que te permite saber saber si eres o no eres bienbenido al programa

"""
def verificar_edad(edades):
    for edad in edades:
        if edad < 19:
            print("No puede ingresar!")
        else:
            print("Bienvenido!")


print(saludo_5)
print("")
edad_uno = int(input("Digite su edad: "))
edad_dos = int(input("Digite su edad: "))
edad_tres = int(input("Digite su edad: "))
edad_cuatro = int(input("Digite su edad: "))
edad_cindo = int(input("Digite su edad: "))

# Vector de edades
edades = [edad_uno, edad_dos, edad_tres, edad_cuatro, edad_cindo]

# Llamamos a la función para verificar las edades
verificar_edad(edades)





