from typing import Generic, TypeVar, List

# a)
T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def apilar(self, valor: T):  # a)
        self.elementos.append(valor)

    def desapilar(self) -> T:    # b)
        if self.elementos:
            return self.elementos.pop()
        raise IndexError("Pila vacía")

    def mostrar(self):           # d)
        print("Pila:", self.elementos)

# c)
pila_numeros = Pila[int]()
pila_numeros.apilar(10)
pila_numeros.apilar(20)

pila_textos = Pila[str]()
pila_textos.apilar("hola")
pila_textos.apilar("mundo")

# d)
pila_numeros.mostrar()
print("Desapilado:", pila_numeros.desapilar())
pila_numeros.mostrar()

pila_textos.mostrar()
print("Desapilado:", pila_textos.desapilar())
pila_textos.mostrar()
