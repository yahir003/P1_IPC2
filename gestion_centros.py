def listar_centros(lista_centros):
    actual = lista_centros.primero
    if actual is None:
        print("No hay centros registrados")
        return

    while actual:
        actual.dato.mostrar_info()
        actual = actual.siguiente

def buscar_centro_por_id(lista_centros):
    buscado = input("Ingrese ID del centro: ")
    actual = lista_centros.primero

    while actual:
        if actual.dato.id == buscado:
            actual.dato.mostrar_info()
            return
        actual = actual.siguiente

    print("Centro no encontrado")


def centro_con_mas_recursos(lista_centros):
    actual = lista_centros.primero
    if actual is None:
        print("No hay centros")
        return

    mayor = actual.dato
    actual = actual.siguiente

    while actual:
        disp_actual = (
            actual.dato.cpu_disponible +
            actual.dato.ram_disponible +
            actual.dato.alm_disponible
        )
        disp_mayor = (
            mayor.cpu_disponible +
            mayor.ram_disponible +
            mayor.alm_disponible
        )

        if disp_actual > disp_mayor:
            mayor = actual.dato

        actual = actual.siguiente

    print("Centro con mas recursos: ")
    mayor.mostrar_info()


def menu_centros(lista_centros):
    while True:
        print('*'*20,'GESTION DE CENTROS','*'*20)
        print('1. Listar centros')
        print('2. Buscar por ID')
        print('3. Centro con mas recursos')
        print('4. Volver al menu principal')

        op = input('Seleccione una Opcion: ')

        if op == '1':
            listar_centros(lista_centros)
        elif op == '2':
            buscar_centro_por_id(lista_centros)
        elif op == '3':
            centro_con_mas_recursos(lista_centros)
        elif op == '4':
            break
        else:
            print('Opcion no valida intente de nuevo...')
