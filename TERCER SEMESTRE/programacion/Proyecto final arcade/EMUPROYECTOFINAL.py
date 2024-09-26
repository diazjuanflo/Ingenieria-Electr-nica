#PRINCIPAL.py
from tkinter import *
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
import pygame
from Ventana2 import App, RegistroApp
from GAMEZONE import Juego, InterfazJuegos


def seleccionar_opcion(opcion):
    if opcion == "INVITADO":
        abrir_ventana1()
    elif opcion == "ACCEDER":
        abrir_ventana2()

def abrir_ventana1():
    global ventana_invitado
    ventana_invitado = Toplevel(root)
    atras_button=Button(ventana_invitado, text="Volver al Inicio", width=20, command=lambda: volver_inicio(ventana_invitado)).place(x=10, y=20)
    app_ventana1 = InterfazJuegos(ventana_invitado)
    root.iconify()
    



def abrir_ventana2():
    # Crea una instancia de la clase App
    ventana_acceso = Toplevel(root)
    ventana_acceso.geometry("400x600")
    ventana_acceso.resizable(0, 0)
    ventana_acceso.title("MODO LOGIN")

    imagen_fondo = PhotoImage(file="RECURSOS/ventana2.png")
        # Escalar la imagen en un 53%
    ancho_nuevo = int(imagen_fondo.width() * 0.53)
    alto_nuevo = int(imagen_fondo.height() * 0.53)
    imagen_fondo = imagen_fondo.subsample(int(imagen_fondo.width()/ancho_nuevo), int(imagen_fondo.height()/alto_nuevo))

    # Crear un widget de etiqueta (Label) con la imagen de fondo
    etiqueta_fondo = Label(ventana_acceso, image=imagen_fondo)
    etiqueta_fondo.place(relwidth=1, relheight=1)  # Establecer el tamaño de la etiqueta al tamaño de la ventana

    atras_Button=Button(ventana_acceso, text="Volver al Inicio", width=20, command=lambda: volver_inicio(ventana_acceso)).place(x=10, y=10)
    # Crea una instancia de la clase App
    app_ventana2 = App(ventana_acceso)

    root.iconify()
    ventana_acceso.mainloop()

def volver_inicio(ventana):
    root.deiconify()
    ventana.destroy()
    
def toggle_reproducir_pausar():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


# Inicializar pygame mixer para la reproducción de música
pygame.mixer.init()

# Cargar la canción (reemplaza con la ruta correcta de tu archivo de música)
pygame.mixer.music.load("RECURSOS/sonidosincopy.mp3")
pygame.mixer.music.play(loops=-1)  # '-1' para reproducir infinitamente

root = Tk()
root.title("PROYECTO EMULADOR V1.0")

root.geometry("850x600")
root.resizable(0, 0)


# Abrir la imagen y redimensionarla para que se ajuste a las dimensiones de la ventana
imagen_pil = Image.open("RECURSOS/FONDO.jpg")
imagen_redimensionada = imagen_pil.resize((850, 600), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Crear un widget de etiqueta para mostrar la imagen de fondo
fondo_label = Label(root, image=imagen_tk)
fondo_label.place(relwidth=1, relheight=1)

# Crear las opciones de botones
btn_invitado = Button(root, text="INVITADO", bg="#A80000", fg="#11A5D9", font=("Bauhaus 93", 30), command=lambda: seleccionar_opcion("INVITADO"), relief="solid")
btn_invitado.place(x=120, y=420)

btn_acceder = Button(root, text="ACCEDER", bg="#000770", fg="#11A5D9", font=("Bauhaus 93", 30), command=lambda: seleccionar_opcion("ACCEDER"), relief="solid")
btn_acceder.place(x=530, y=420)

# Cargar la imagen y redimensionarla
imagen_reproducir_pausar = PhotoImage(file="RECURSOS/mute.png")
imagen_reproducir_pausar = imagen_reproducir_pausar.subsample(30, 30)  # Ajusta los valores de subsample según sea necesario

# Reemplazar el texto con la imagen en el botón
btn_reproducir_pausar = Button(root, image=imagen_reproducir_pausar, command=toggle_reproducir_pausar)
btn_reproducir_pausar.place(x=818, y=0)

# ETIQUETAS Y TEXTO
label1 = Label(root, text="Julian Rodrigo Perdomo Olaya", bg="black", fg="#11A5D9", font=("Arial", 10), relief="solid")
label1.place(x=20, y=20)

label2 = Label(root, text="Juan Esteban Diaz Delgado",bg="black",fg="#11A5D9",font=("Arial",10),relief="solid")
label2.place(x=20,y=40)

label3 = Label(root, text="PROYECTO FINAL PROGRAMACION 2-USCO", bg="black", fg="#11A5D9", font=("Arial", 10), relief="solid")
label3.place(x=20, y=570)

if __name__ == "__main__":
    root.mainloop()