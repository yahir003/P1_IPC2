def listar_solicitudes(lista):
    actual = lista.primero
    if actual is None:
        print("No hay solicitudes")
        return

    while actual:
        actual.dato.mostrar_info()
        actual = actual.siguiente


def buscar_solicitud_por_id(lista):
    buscado = input("Ingrese ID de la solicitud: ")
    actual = lista.primero

    while actual:
        if actual.dato.id == buscado:
            actual.dato.mostrar_info()
            return
        actual = actual.siguiente

    print("Solicitud no encontrada")


def procesar_solicitudes(lista_solicitudes, lista_centros):
    actual = lista_solicitudes.primero
    if actual is None:
        print("No hay solicitudes para procesar")
        return

    while actual:
        solicitud = actual.dato
        centro_actual = lista_centros.primero

        while centro_actual:
            centro = centro_actual.dato
            if (centro.cpu_disponible >= solicitud.cpu and
                centro.ram_disponible >= solicitud.ram and
                centro.alm_disponible >= solicitud.almacenamiento):

                centro.cpu_disponible -= solicitud.cpu
                centro.ram_disponible -= solicitud.ram
                centro.alm_disponible -= solicitud.almacenamiento

                print(f"Solicitud {solicitud.id} procesada en centro {centro.id}")
                break

            centro_actual = centro_actual.siguiente

        actual = actual.siguiente


def menu_solicitudes(lista_solicitudes, lista_centros,cola):
    while True:
        print("*" * 20, "GESTIÓN DE SOLICITUDES", "*" * 20)
        print("1. Listar solicitudes")
        print("2. Buscar solicitud por ID")
        print("3. Procesar solicitudes")
        print("4. Mostrar cola de solicitudes")
        print("5 Volver")

        op = input("Seleccione: ")

        if op == "1":
            listar_solicitudes(lista_solicitudes)
        elif op == "2":
            buscar_solicitud_por_id(lista_solicitudes)
        elif op == "3":
            procesar_solicitudes(lista_solicitudes, lista_centros)
        elif op == "4":
            cola.mostrar()
        elif op == "5":
            break
