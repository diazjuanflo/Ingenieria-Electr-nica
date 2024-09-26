class Libro:
    #Declaramos el constructor con los atributos
    def __init__(self,titulo, autor, paginas, disponible):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible

    def prestar(self):

        if self.disponible == False:
            return 'El libro esta disponible'
        else:
            return 'EL libro no esta disponible'
    
    def devolver(self):
        if(self.disponible):
            return 'El libro esta disponible'
        else:
            return 'EL libro no ha sido devolvido'
        
    def informacion(self):
        print(f'El nombre del libro es: {self.titulo}, el nombre del autor es: {self.autor}, el numero de paginas es: {self.autor}.')

# Solicitar la cantidad de libros al usuario
n = int(input("Ingrese la cantidad de libros: "))
libros = []

# Pedir la información de cada libro y crear objetos de la clase Libro
for i in range(n):
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    paginas = int(input("Paginas: "))
    disponible = True
    
    # Creamos un objeto de la clase Libros con la información ingresada
    objLibros = Libro(titulo, autor, paginas, disponible)
    
    # Agregamos los libors a la lista de libros
    libros.append(objLibros)

    objLibros.informacion()
    objLibros.devolver()
    objLibros.prestar()
