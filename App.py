from Finanzas import Finanza

while True:
    print("instrucciones:")
    print("1. Iniciar cuenta en $0.0")
    print("2. Registrar ingreso o egreso")
    print("3. Registro de ingreso")
    print("4. Registro de egreso")
    print("5. Registro de transacciones")
    print("6. Total de cuenta")
    print("0. Cerrar app")
    option = int(input("Eliga la opcion que desee: "))

    if option == 1:
        id = int(input("Ingrese el Id de su cuenta: "))
        monto = 0.0
        cuenta = Finanza(id, monto)
        print(f"Se ha iniciado su cuenta con id {id} con un monto de ${monto}")

    elif option == 2:
        opcion = int(input("Ingrese una opcion: 1. Ingreso 2. Egreso "))
        if opcion == 1:
            id = int(input("Escriba el id del ingreso: "))
            monto = float(input("Monto a ingresar: "))
            cuenta.registrarIngreso(id, monto)
        elif opcion == 2:
            id = int(input("Ingrese el id del egreso: "))
            monto = float(input("Monto a egresar: "))
            cuenta.registrarEgreso(id, monto)

    elif option == 3:
        print("Ingresos:")
        cuenta.mostrarIngresos()

    elif option == 4:
        print("Egresos:")
        cuenta.mostrarEgresos()

    elif option == 5:
        print("Transacciones:")
        cuenta.mostrarTransacciones()

    elif option == 6:
        total = cuenta.montoTotal()
        print(f"Total de cuenta: ${total}")

    elif option == 0:
        break
