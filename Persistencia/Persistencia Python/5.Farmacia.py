import pickle
import os

# Clase Medicamento
class Medicamento:
    def __init__(self, nombre, codMedicamento, tipo, precio):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - ${self.precio}"

# Clase Farmacia
class Farmacia:
    def __init__(self, nombreFarmacia, sucursal, direccion):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = []

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def buscar_por_tipo(self, tipo):
        return [m for m in self.medicamentos if m.tipo.lower() == tipo.lower()]

    def tiene_medicamento(self, nombre):
        return any(m.nombre.lower() == nombre.lower() for m in self.medicamentos)

    def __str__(self):
        meds = "\n  ".join(str(m) for m in self.medicamentos)
        return f"Sucursal {self.sucursal} - {self.direccion}\n  {meds}"

# Clase ArchFarmacia
class ArchFarmacia:
    def __init__(self, archivo):
        self.archivo = archivo
        self.farmacias = self._leer_archivo()

    def _leer_archivo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "rb") as f:
                return pickle.load(f)
        return []

    def _guardar_archivo(self):
        with open(self.archivo, "wb") as f:
            pickle.dump(self.farmacias, f)

    def adicionar(self, farmacia):
        self.farmacias.append(farmacia)
        self._guardar_archivo()

    def listar(self):
        for f in self.farmacias:
            print(f)

    def mostrar_medicamentos_resfrios(self, sucursal):
        for f in self.farmacias:
            if f.sucursal == sucursal:
                print(f"Medicamentos para la tos en sucursal {f.sucursal}:")
                for m in f.buscar_por_tipo("Tos"):
                    print(m)

    def mostrar_farmacias_con_golpex(self):
        for f in self.farmacias:
            if f.tiene_medicamento("Golpex"):
                print(f"Sucursal: {f.sucursal}, Dirección: {f.direccion}")

# Prueba
if __name__ == "__main__":
    arch = ArchFarmacia("farmacias.pkl")

    f1 = Farmacia("Farmacia Uno", 101, "Av. Salud 123")
    f1.agregar_medicamento(Medicamento("Golpex", 1, "Tos", 12.5))
    f1.agregar_medicamento(Medicamento("Ibuprofeno", 2, "Dolor", 7.5))
    arch.adicionar(f1)

    f2 = Farmacia("Farmacia Dos", 102, "Calle Bienestar 45")
    f2.agregar_medicamento(Medicamento("Jarabe Miel", 3, "Tos", 8.0))
    arch.adicionar(f2)

    arch.listar()
    arch.mostrar_medicamentos_resfrios(102)
    arch.mostrar_farmacias_con_golpex()
