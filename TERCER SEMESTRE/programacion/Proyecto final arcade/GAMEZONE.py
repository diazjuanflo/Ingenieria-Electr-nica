import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess

class Juego:
    def __init__(self, nombre, ruta, imagen_path):
        self.nombre = nombre
        self.ruta = ruta
        self.imagen_path = imagen_path

class InterfazJuegos:
    def __init__(self, root):
        self.root = root
        self.root.title("GAMERZONA")

        fondo_path = "RECURSOS/peligro_zona_gamer.jpg"  
        self.fondo = Image.open(fondo_path)
        self.fondo = ImageTk.PhotoImage(self.fondo)

        fondo_label = tk.Label(root, image=self.fondo)
        fondo_label.place(relwidth=1, relheight=1)

        self.root.geometry("800x600")

        self.cuadros_juegos = []

        for i in range(2):
            for j in range(4):
                cuadro_juego = tk.Frame(self.root, width=200, height=250, borderwidth=2, relief="groove")
                cuadro_juego.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                self.cuadros_juegos.append(cuadro_juego)

        self.juegos = [
            Juego("CONTRA 1", "JUEGOS/CONTRA/contra.exe", "RECURSOS/contra.png"),
            Juego("CONTRA 2", "JUEGOS/CONTRA/Super contra.exe", "RECURSOS/contra.png"),
            Juego("CONTRA 3", "JUEGOS/CONTRA/contra 3 the Alien Wars.exe", "RECURSOS/contra.png"),
            Juego("CONTRA 4", "JUEGOS/CONTRA/contra 4.exe", "RECURSOS/contra.png"),
            Juego("FUEGOYAGUA 1", "JUEGOS/FUEGOYAGUA/fuego y agua 1.exe", "RECURSOS/fuegoyagua.png"),
            Juego("FUEGOYAGUA 2", "JUEGOS/FUEGOYAGUA/fuego y agua 2.exe", "RECURSOS/fuegoyagua.png"),
            Juego("FUEGOYAGUA 3", "JUEGOS/FUEGOYAGUA/fuego y agua 3.exe", "RECURSOS/fuegoyagua.png"),
            Juego("FUEGOYAGUA 4", "JUEGOS/FUEGOYAGUA/fuego y agua 4.exe", "RECURSOS/fuegoyagua.png"),
        ]

        self.mostrar_juegos()

    def mostrar_juegos(self):
        for i, juego in enumerate(self.juegos):
            cuadro_juego = self.cuadros_juegos[i]

            # Cargar imagen y mostrar en un Label
            imagen = Image.open(juego.imagen_path)
            imagen = imagen.resize((150, 150))
            imagen = ImageTk.PhotoImage(imagen)
            
            # Vincular evento a todo el cuadro y la imagen
            cuadro_juego.bind("<Button-1>", lambda event, juego=juego: self.abrir_juego(juego.ruta))
            
            label_imagen = tk.Label(cuadro_juego, image=imagen)
            label_imagen.image = imagen
            label_imagen.grid(row=0, column=0, padx=10, pady=5)

            label_nombre = tk.Label(cuadro_juego, text=juego.nombre)
            label_nombre.grid(row=1, column=0, padx=10, pady=5)

            # Vincular evento a la imagen
            label_imagen.bind("<Button-1>", lambda event, juego=juego: self.abrir_juego(juego.ruta))

    def abrir_juego(self, ruta):
        try:
            subprocess.run([ruta])
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el juego: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazJuegos(root)
    root.mainloop()
