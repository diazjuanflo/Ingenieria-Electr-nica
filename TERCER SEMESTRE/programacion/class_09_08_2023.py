edad = int(input("Digite su edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres un niño") 


edad_dos = int(input("Digite su edad: "))
if edad_dos >= 0 and edad_dos < 18:
    print("Eres menor de edad")
elif edad_dos >= 18 and edad_dos <= 35:
    print("Pos adolecente")
elif edad_dos > 35 and edad_dos <= 60:
    print("Eres un adulto")
else:
    print("Adulto mayor")