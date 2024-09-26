#Ventana2.py

from tkinter import *
from tkinter import messagebox
from COONEXIONBD import DataBase
from tkinter import ttk, PhotoImage
from GAMEZONE import Juego, InterfazJuegos

class App:
    def __init__(self, root):
        self.root = root
        root.geometry("400x600")

        self.label_usuario = Label(root, text="Usuario:",font=("Bauhaus 93", 15),bg="#3FBD00")
        self.label_usuario.place(x=167,y=130)
        self.label_contrasena = Label(root,text="Contraseña:",font=("Bauhaus 93", 15),bg="#3FBD00")
        self.label_contrasena.place(x=150,y=230)

        self.entry_usuario = Entry(root,font=("Bauhaus 93", 15))
        self.entry_usuario.place(x=95,y=170)
        self.entry_contrasena = Entry(root, show="*",font=("Bauhaus 93", 15))
        self.entry_contrasena.place(x=95,y=270)

        self.button_iniciar_sesion = Button(root, text="Iniciar Sesión", command=self.iniciar_sesion,relief="solid",font=("Bauhaus 93", 20),bg="#3247B8" , fg="white")
        self.button_iniciar_sesion.place(x=114,y=360)
        self.button_registrar = Button(root, text="Registrar", command=self.abrir_ventana_registro,font=("Bauhaus 93", 20),  fg="black",relief="solid",bg="#358CB8")
        self.button_registrar.place(x=140,y=430)

        self.button_borrar_cuenta = Button(root, text="¿Quieres borrar tu cuenta?", command=self.borrar_cuenta,font=("Bauhaus 93", 10),  fg="black",relief="solid",bg="green")
        self.button_borrar_cuenta.place(x=125,y=510)    

        self.database = DataBase()


    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        user = self.database.select_user_by_credentials(usuario, contrasena)

        if user:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
            # Aquí puedes redirigir a otra ventana después del inicio de sesión exitoso.
            ventana_juegos=Toplevel(self.root)
            abrir_juegos=InterfazJuegos(ventana_juegos)
            self.root.deiconify()


        else:
            messagebox.showwarning("Error", "Credenciales incorrectas. Registrarse ahora.")
            self.abrir_ventana_registro()

    def abrir_ventana_registro(self):
        registro_window = Toplevel(self.root)
        registro_app = RegistroApp(registro_window, self.database)

    def borrar_cuenta(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        # Verificar si las credenciales del usuario son correctas antes de mostrar la ventana de eliminación
        if self.database.select_user_by_credentials(usuario, contrasena):
            # Mostrar ventana de eliminación
            self.mostrar_ventana_eliminar(usuario, contrasena)
        else:
            messagebox.showwarning("Error", "Credenciales incorrectas.")

    def mostrar_ventana_eliminar(self, usuario, contrasena):
        ventana_eliminar = Toplevel(self.root)
        ventana_eliminar.title("Eliminar Cuenta")

        label_confirmacion = Label(ventana_eliminar, text="¿Estás seguro que quieres borrar tu cuenta?")
        button_confirmar = Button(ventana_eliminar, text="Confirmar", command=lambda: [self.eliminar_cuenta(usuario, contrasena),ventana_eliminar.destroy()])
        button_cancelar = Button(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy)

        label_confirmacion.pack()
        button_confirmar.pack()
        button_cancelar.pack()

    def eliminar_cuenta(self, usuario, contrasena):
        try:
            self.database.delete_user(usuario, contrasena)
            messagebox.showinfo("Eliminación Exitosa", "Tu cuenta ha sido eliminada.")
            # Puedes realizar acciones adicionales después de eliminar la cuenta si es necesario.
        except Exception as e:
            messagebox.showerror("Error", "Error al eliminar la cuenta: {}".format(e))

class RegistroApp:
    def __init__(self, root, database):
        self.root = root
        self.root.title("REGISTRO")
        self.root.geometry("300x300")
    
        self.imagen_fondo = PhotoImage(file="RECURSOS/REGISTRO.png")
        # Escalar la imagen en un 52%
        self.ancho_nuevo = int(self.imagen_fondo.width() * 0.52)
        self.alto_nuevo = int(self.imagen_fondo.height() * 0.52)
        self.imagen_fondo = self.imagen_fondo.subsample(int(self.imagen_fondo.width()/self.ancho_nuevo), int(self.imagen_fondo.height()/self.alto_nuevo))

        # Crear un widget de etiqueta (Label) con la imagen de fondo
        self.etiqueta_fondo = Label(self.root, image=self.imagen_fondo)
        self.etiqueta_fondo.place(relwidth=1, relheight=1)  # Establecer el tamaño de la etiqueta al tamaño de la ventana

        self.label_nuevo_usuario = Label(root, text="Nuevo Usuario:",font=("Bauhaus 93", 15),bg="#FFD700")
        self.label_nueva_contrasena = Label(root, text="Nueva Contraseña:",font=("Bauhaus 93", 15),bg="#FFD700")

        self.entry_nuevo_usuario = Entry(root,font=("Bauhaus 93", 15))
        self.entry_nueva_contrasena = Entry(root, show="*",font=("Bauhaus 93", 15))

        self.button_registrar_nuevo = Button(root, text="Registrar", command=self.registrar_nuevo_usuario,font=("Bauhaus 93", 15),bg="#FFD700")

        self.label_nuevo_usuario.pack(pady=10)
        self.entry_nuevo_usuario.pack(pady=10)
        self.label_nueva_contrasena.pack(pady=10)
        self.entry_nueva_contrasena.pack(pady=10)
        self.button_registrar_nuevo.pack(pady=10)

        self.database = database

    def registrar_nuevo_usuario(self):
        nuevo_usuario = self.entry_nuevo_usuario.get()
        nueva_contrasena = self.entry_nueva_contrasena.get()

        # Verificar si el usuario ya existe en la base de datos
        if self.database.user_exists(nuevo_usuario):
            messagebox.showwarning("Error", "El usuario ya existe. Por favor, elige otro nombre de usuario.")
        else:
            # Si el usuario no existe, agregarlo a la base de datos
            self.database.add_user(nuevo_usuario, nueva_contrasena)
            messagebox.showinfo("Registro", "Usuario registrado correctamente.")
            self.root.destroy()

    
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
