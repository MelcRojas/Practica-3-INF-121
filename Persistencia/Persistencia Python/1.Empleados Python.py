import pickle
import os

# Clase Empleado
class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} - Edad: {self.edad}, Salario: {self.salario}"

# Clase ArchivoEmpleado
class ArchivoEmpleado:
    def __init__(self, nombre_archivo: str):
        self.nomA = nombre_archivo
        self.empleados = []
        self.crear_archivo()

    def crear_archivo(self):
        if os.path.exists(self.nomA):
            with open(self.nomA, "rb") as f:
                self.empleados = pickle.load(f)
        else:
            self.empleados = []

    # a)
    def guardar_empleado(self, e: Empleado):
        self.empleados.append(e)
        with open(self.nomA, "wb") as f:
            pickle.dump(self.empleados, f)

    # b)
    def busca_empleado(self, nombre: str) -> Empleado:
        for e in self.empleados:
            if e.nombre.lower() == nombre.lower():
                return e
        return None

    # c)
    def mayor_salario(self, sueldo: float) -> Empleado:
        for e in self.empleados:
            if e.salario > sueldo:
                return e
        return None

# Prueba
if __name__ == "__main__":
    archivo = ArchivoEmpleado("empleados.pkl")

    # a)
    archivo.guardar_empleado(Empleado("Ana", 30, 3000))
    archivo.guardar_empleado(Empleado("Luis", 40, 4500))

    # b)
    encontrado = archivo.busca_empleado("Ana")
    print("Encontrado:", encontrado)

    # c)
    mayor = archivo.mayor_salario(3500)
    print("Mayor salario que 3500:", mayor)
