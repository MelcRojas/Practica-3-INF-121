from typing import Generic, TypeVar

# a)
T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self._contenido = None

    def guardar(self, valor: T):
        self._contenido = valor

    def obtener(self) -> T:
        return self._contenido

# b)
caja_entero = Caja[int]()
caja_entero.guardar(42)

caja_texto = Caja[str]()
caja_texto.guardar("Hola mundo")

# c)
print("Contenido de caja_entero:", caja_entero.obtener())
print("Contenido de caja_texto:", caja_texto.obtener())
