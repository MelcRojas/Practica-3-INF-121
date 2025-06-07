from typing import Generic, TypeVar, List

# a)
T = TypeVar('T')

class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def agregar(self, elemento: T):
        self.elementos.append(elemento)

    def buscar(self, criterio) -> List[T]:
        return [e for e in self.elementos if criterio(e)]

# b)
class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

catalogo_libros = Catalogo[Libro]()
catalogo_libros.agregar(Libro("1984", "George Orwell"))
catalogo_libros.agregar(Libro("Fahrenheit 451", "Ray Bradbury"))

resultados_libros = catalogo_libros.buscar(lambda l: "19" in l.titulo)
for libro in resultados_libros:
    print(libro)

# c)
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

catalogo_productos = Catalogo[Producto]()
catalogo_productos.agregar(Producto("Laptop", 999.99))
catalogo_productos.agregar(Producto("Mouse", 25.5))

resultados_productos = catalogo_productos.buscar(lambda p: p.precio < 100)
for producto in resultados_productos:
    print(producto)
