from tkinter import *

root = Tk()
root.title("Mi primera interfaz gráfica")
root.geometry("500x500")  # Establece las dimensiones de la ventana
root.config(bg="blue")

label1 = Label(root, text="Nombre:")
label1.place(x=20, y=50)
label1.config(bg="Red", font=("Courier", 30))

label2 = Label(root, text="Apellido:")
label2.place(x=20, y=100)  
label2.config(bg="Red", font=("Courier", 30))

label3 = Label(root, text="Teléfono:")
label3.place(x=20, y=150)  
label3.config(bg="Red", font=("Courier", 30))

label4 = Label(root, text="Dirección:")
label4.place(x=20, y=200)  
label4.config(bg="Red", font=("Courier", 30))


nombre_entry = Entry(root, width=45)
nombre_entry.place(x=200, y=50)  

apellido_entry = Entry(root, width=45)
apellido_entry.place(x=250, y=100)  

telefono_entry = Entry(root, width=45)
telefono_entry.place(x=250, y=150)  

direccion_entry = Entry(root, width=45)
direccion_entry.place(x=270, y=200)  



guardar_boton = Button(root, text="Guardar")
guardar_boton.place(x=20, y=250) 

root.mainloop()