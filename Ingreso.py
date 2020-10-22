class Ingreso:
    def __init__(self):
        self.listaIngresos = []

    def nuevoIngreso(self, id, monto):
        ingresoNuevo = (id, monto)
        self.listaIngresos.append(ingresoNuevo)
        return self.listaIngresos

    def showIngresos(self):
        for ingreso in self.listaIngresos:
            print(f"Id: {ingreso[0]} Monto: {ingreso[1]}")

    def totalIngresos(self):
        total = 0.0
        for ingreso in self.listaIngresos:
            total += float(ingreso[1])
        return total