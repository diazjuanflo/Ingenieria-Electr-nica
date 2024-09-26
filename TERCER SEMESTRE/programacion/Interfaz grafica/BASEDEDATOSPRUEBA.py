# Tarea final de la 2ª Evaluación: BD + Aplicación Python de acceso a la BD
# Marcos Sanz Gómez

import mysql.connector
import sys

#--------------- Función de conexión a BD
def Conexion_BD(marcosBD):
    try:
        conexion1=mysql.connector.connect(host="localhost",
                        user="root", passwd="", database=marcosBD)
        cursor1=conexion1.cursor()
        cursor1.execute("Muestra las tablas:")
        myresult = cursor1.fetchall() 
        for x in myresult: 
            print(x) 
    except:
        return conexion1
#-----------------Funciones Insertar-----------------------
def Insertar_BD_cesta(Dato1, Dato2, Dato3, Dato4, Mi_Conexion): #Funcion insertar en cesta
    try:
        cursor1=Mi_Conexion.cursor()
        sql="insert into cesta(codigo, descripcion, precio, cantidad) values (%s,%s,%s,%s)"
        datos=(int(Dato1),Dato2,int(Dato3), int(Dato4))
        cursor1.execute(sql, datos)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("INSERCIÓN REALIZADA")
    except:
        print(sql)
        print("Error de Inserción de Datos en BD!!!")

def Insertar_BD_clientes(Dato1, Dato2, Dato3, Dato4, Dato5, Mi_Conexion): #Funcion insertar en clientes
    try:
        cursor1=Mi_Conexion.cursor()
        sql="insert into clientes(codigo, nombre, email, cesta_cliente, domicilio_cliente) values (%s,%s,%s,%s,%s)"
        datos=(int(Dato1),Dato2,Dato3, int(Dato4), int(Dato5))
        cursor1.execute(sql, datos)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("INSERCIÓN REALIZADA")
    except:
        print(sql)
        print("Error de Inserción de Datos en BD!!!") 

def Insertar_BD_domicilio(Dato1, Dato2, Dato3, Dato4, Mi_Conexion): #Funcion insertar en domicilio
    try:
        cursor1=Mi_Conexion.cursor()
        sql="insert into domicilio(codigo, localidad, calle, numero) values (%s,%s,%s,%s)"
        datos=(int(Dato1),Dato2,Dato3, Dato4)
        cursor1.execute(sql, datos)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("INSERCIÓN REALIZADA")
    except:
        print(sql)
        print("Error de Inserción de Datos en BD!!!")

#-----------------Funciones Eliminar-----------------------

def eliminar_BD_cesta(columna, condicion, Mi_Conexion): #Funcion eliminar en cesta
    try:
        cursor1=Mi_Conexion.cursor()
        sql="delete from cesta where "+columna+condicion
        cursor1.execute(sql)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("ELIMINACIÓN REALIZADA")

    except:
        print(sql)
        print("Error de eliminación de Datos en BD!!!")

def eliminar_BD_clientes(columna, condicion, Mi_Conexion): #Funcion eliminar en clientes
    try:
        cursor1=Mi_Conexion.cursor()
        sql="delete from clientes where "+columna+condicion
        cursor1.execute(sql)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("ELIMINACIÓN REALIZADA")     
    except:
        print(sql)
        print("Error de eliminación de Datos en BD!!!")

def eliminar_BD_domicilio(columna, condicion, Mi_Conexion): #Funcion eliminar en domicilio
    try:
        cursor1=Mi_Conexion.cursor()
        sql="delete from domicilio where "+columna+condicion
        cursor1.execute(sql)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("ELIMINACIÓN REALIZADA")
    except:
        print(sql)
        print("Error de eliminación de Datos en BD!!!")
        
#-----------------Funciones CAMBIAR-----------------------

def cambiar_BD_cesta(columna, valor_nuevo, valor_antiguo, Mi_Conexion): #Funcion cambiar en cesta
    try:
        cursor1=Mi_Conexion.cursor()
        sql="update cesta set "+columna+"="+valor_nuevo+" where "+columna+"="+valor_antiguo
        cursor1.execute(sql)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("CAMBIOS REALIZADOS")
        mydb.commit()

    except:
        print(sql)
        print("Error al cambiar de Datos en BD!!!")

def cambiar_BD_clientes(columna, valor_nuevo, valor_antiguo, Mi_Conexion): #Funcion cambiar en clientes
    try:
        cursor1=Mi_Conexion.cursor()
        sql="update clientes set "+columna+"="+valor_nuevo+" where "+columna+"="+valor_antiguo
        cursor1.execute(sql)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("CAMBIOS REALIZADOS")
        mydb.commit()

    except:
        print(sql)
        print("Error al cambiar de Datos en BD!!!")

def cambiar_BD_domicilio(columna, valor_nuevo, valor_antiguo, Mi_Conexion): #Funcion cambiar en domicilio
    try:
        cursor1=Mi_Conexion.cursor()
        sql="update domicilio set "+columna+"="+valor_nuevo+" where "+columna+"="+valor_antiguo
        cursor1.execute(sql)
        Mi_Conexion.commit()
        #Mi_Conexion.close()
        print(sql)
        print("CAMBIOS REALIZADOS")
        mydb.commit()

    except:
        print(sql)
        print("Error al cambiar de Datos en BD!!!")

#--------- Consulta --------------------
        
def Consulta_BD(Mi_Conexion,Mi_SQL):
    cursor1=Mi_Conexion.cursor()
    print("Nombre de campos en la tabla:")
    cursor1.execute(Mi_SQL)
    for i in range(len(cursor1.description)):
         print(cursor1.description[i][0])  #Saca el nombre de los campos/tabla
    #-----------------------------------------------
    print("Resultados de la búsqueda:")
    for fila in cursor1:
        print(fila)
        
#------------- PROGRAMA PRINCIPAL -------

print("--PROGRAMA BASE DE DATOS MARCOS SANZ--")
Mi_BD=input("Nombre de la BD: ")

try:
    My_connexion=Conexion_BD(Mi_BD)
except:
    print("Error de conexion")
    sys.exit(1)

print("Conexión a BD....")

print(My_connexion)

#-------- Mostrar las tablas existente -------

print("----Lista de Tablas---------")
mydb = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="", 
    database=Mi_BD
) 
mycursor = mydb.cursor() 
mycursor.execute("Show tables;")  
myresult = mycursor.fetchall() 
for lista_tablas in myresult: 
    print(lista_tablas)

#-------------TABLA DE TRABAJO-----------
    
print("----Selecciona la tabla donde trabajar---------")
Tabla=input("Dame el nombre de la TABLA:")

#------------TIPO DE ACCIÓN-------------

print("----Selección de tipo de consulta ---------")
Tipo_consulta=input("Elije: CONSULTAR, ELIMINAR, AÑADIR, CAMBIAR: ")

if Tipo_consulta == "CONSULTAR" : # CONSULTAS
    print("----Se inica la CONSULTA---------")
    sql="select * from "+Tabla+" limit 0"
    Consulta_BD(My_connexion,sql)
    Campo=input("Dame el nombre del CAMPO DE BUSQUEDA")
    Criterio=input("Dame el CRITERIO DE BUSQUEDA:")

    #CONSTRUCCION DE LA CADENA SQL:

    sql="select * from "  #parte comun
    espacio=" "
    palabra_where=" where "
    sql=sql+Tabla+palabra_where+Campo+Criterio

    print("La consulta es: "+sql)
    
elif Tipo_consulta == "ELIMINAR" : # ELIMINACIONES
    
    if Tabla == "cesta": # ELIMINAR EN CESTA
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        columna=input("Dame la columna a eliminar")
        condicion=input("Dame la condicion a eliminar")

        print("Eliminamos estos datos....")
        
        eliminar_BD_cesta(columna, condicion, My_connexion)
        
        My_connexion.close()

    elif Tabla == "clientes": # ELIMINAR EN CLIENTES
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        columna=input("Dame la columna a eliminar")
        condicion=input("Dame la condicion a eliminar")

        print("Eliminamos estos datos....")
        
        eliminar_BD_cesta(columna, condicion, My_connexion)

        My_connexion.close()

    elif Tabla == "domicilio": # ELIMINAR EN DOMICILIO
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        columna=input("Dame la columna a eliminar")
        condicion=input("Dame la condicion a eliminar")

        print("Eliminamos estos datos....")
        
        eliminar_BD_domicilio(columna, condicion, My_connexion)

        My_connexion.close()


elif Tipo_consulta == "AÑADIR" : # INSERCIONES
    
    if Tabla == "cesta": # INSERTAR EN CESTA
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        Mi_dato1=int(input("Dame el ID"))
        Mi_dato2=input("Dame DESCRIPCIÓN..")
        Mi_dato3=input("Dame EL PRECIO..")
        Mi_dato4=input("Dame LA CANTIDAD..")

        print("Insertamos estos datos....")
        Insertar_BD_cesta(Mi_dato1, Mi_dato2, Mi_dato3, Mi_dato4, My_connexion)
        Todos_datos=[]
        Todos_datos = [Mi_dato1] + [Mi_dato2] + [Mi_dato3] + [Mi_dato4]

        My_connexion.close()

    elif Tabla == "clientes": # INSERTAR EN CLIENTES
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        Mi_dato1=int(input("Dame el ID"))
        Mi_dato2=input("Dame EL NOMBRE..")
        Mi_dato3=input("Dame EL EMAIL..")
        Mi_dato4=int(input("Dame LA ID DE CESTA.."))
        Mi_dato5=int(input("Dame LA ID DE DOMICILIO.."))

        print("Insertamos estos datos....")
        Insertar_BD_clientes(Mi_dato1, Mi_dato2, Mi_dato3, Mi_dato4, Mi_dato5, My_connexion)
        Todos_datos=[]
        Todos_datos = [Mi_dato1] + [Mi_dato2] + [Mi_dato3] + [Mi_dato4] + [Mi_dato5]

        My_connexion.close()

    elif Tabla == "domicilio": # INSERTAR EN DOMICILIO
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        Mi_dato1=int(input("Dame el ID"))
        Mi_dato2=input("Dame LA LOCALIDAD..")
        Mi_dato3=input("Dame LA CALLE..")
        Mi_dato4=input("Dame EL NUMERO..")

        print("Insertamos estos datos....")
        Insertar_BD_domicilio(Mi_dato1, Mi_dato2, Mi_dato3, Mi_dato4, My_connexion)
        Todos_datos=[]
        Todos_datos = [Mi_dato1] + [Mi_dato2] + [Mi_dato3] + [Mi_dato4]

        My_connexion.close()

    else:
        print("Selecciona una tabla correcta")

elif Tipo_consulta == "CAMBIAR" : # CAMBIOS
    
    if Tabla == "cesta": # CAMBIO EN CESTA
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        columna=input("Dame la columna que desea cambiar")
        valor_nuevo=input("Dame el valor nuevo")
        valor_antiguo=input("Dame el valor antiguo")

        print("Cambiamos estos datos....")
        
        cambiar_BD_cesta(columna, valor_nuevo, valor_antiguo, My_connexion)

        My_connexion.close()

    elif Tabla == "clientes": # CAMBIO EN CLIENTES
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        columna=input("Dame la columna que desea cambiar")
        valor_nuevo=input("Dame el valor nuevo")
        valor_antiguo=input("Dame el valor antiguo")

        print("Cambiamos estos datos....")
        
        cambiar_BD_clientes(columna, valor_nuevo, valor_antiguo, My_connexion)

        My_connexion.close()

    elif Tabla == "domicilio": # CAMBIO EN DOMICILIO
        print("Conexión a BD....")
        print("Introduce 4 datos de la tabla "+Tabla)
        columna=input("Dame la columna que desea cambiar")
        valor_nuevo=input("Dame el valor nuevo")
        valor_antiguo=input("Dame el valor antiguo")

        print("Cambiamos estos datos....")
        
        cambiar_BD_domicilio(columna, valor_nuevo, valor_antiguo, My_connexion)

        My_connexion.close()

    else:
        print("Elije una tabla correcta")

#----- Llamada para obtener los nombres de los campos de la tabla
        
try:
    Consulta_BD(My_connexion,sql)
    print("final")
    My_connexion.close()   #Cerramos la conexion a la BD
except:
    print("Error de consulta")
    sys.exit(1)
    