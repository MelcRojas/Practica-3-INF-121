import pickle
import os

# a)
class Cliente:
    def __init__(self, id: int, nombre: str, telefono: int):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}"

# a)
class ArchivoCliente:
    def __init__(self, nomA: str):
        self.nomA = nomA
        self.clientes = []
        self.crear_archivo()

    def crear_archivo(self):
        if os.path.exists(self.nomA):
            with open(self.nomA, 'rb') as f:
                self.clientes = pickle.load(f)
        else:
            self.clientes = []

    def guardaCliente(self, c: Cliente):
        self.clientes.append(c)
        with open(self.nomA, 'wb') as f:
            pickle.dump(self.clientes, f)

    # b)
    def buscarCliente(self, id: int) -> Cliente:
        for c in self.clientes:
            if c.id == id:
                return c
        return None

    # c)
    def buscarCelularCliente(self, id: int) -> str:
        for c in self.clientes:
            if c.id == id:
                return f"{c.nombre} - Teléfono: {c.telefono}"
        return "Cliente no encontrado"

# Pruebas
if __name__ == "__main__":
    archivo = ArchivoCliente("clientes.pkl")

    # a)
    archivo.guardaCliente(Cliente(1, "Mario", 123456789))
    archivo.guardaCliente(Cliente(2, "Laura", 987654321))

    # b)
    cliente = archivo.buscarCliente(1)
    print("Cliente encontrado:", cliente)

    # c)
    celular_info = archivo.buscarCelularCliente(2)
    print("Cliente + Teléfono:", celular_info)
