
def buscar_vm_por_id(centro):
    buscado = input("Ingrese el ID de la VM: ")

    actual = centro.lista_vms.primero

    while actual is not None:
        if actual.dato.id == buscado:
            print("VM encontrada:")
            actual.dato.mostrar_info()
            return
        actual = actual.siguiente

    print("VM no encontrada")



def menu_vms(centro):
    while True:
        print("*"*20,"GESTIÓN DE MÁQUINAS VIRTUALES","*"*20)
        print("1. Listar VMs")
        print("2. Buscar VM por ID")
        print("3. Volver")

        op = input("Seleccione: ")

        if op == "1":
            actual = centro.lista_vms.primero
            if actual is None:
                print("No hay VMs")
            while actual is not None:
                actual.dato.mostrar_info()
                actual = actual.siguiente

        elif op == "2":
            buscar_vm_por_id(centro)

        elif op == "3":
            break