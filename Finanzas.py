from Egresos import Egreso
from Ingreso import Ingreso

egreso = Egreso()
ingreso = Ingreso()


class Finanza:
    def __init__(self, id, monto):
        self.id = id
        self.monto = monto

    def registrarIngreso(self, id, monto):
        ingreso.nuevoIngreso(id, monto)

    def registrarEgreso(self, id, monto):
        egreso.nuevoEgreso(id, monto)

    def montoTotal(self):
        ingresos = ingreso.totalIngresos()
        egresos = egreso.totalEgresos()
        montoTotal = float(ingresos - egresos)
        return montoTotal

    def mostrarIngresos(self):
        ingreso.showIngresos()

    def mostrarEgresos(self):
        egreso.showEgresos()

    def mostrarTransacciones(self):
        print("Ingresos:")
        ingreso.showIngresos()
        print("Egresos:")
        egreso.showEgresos()