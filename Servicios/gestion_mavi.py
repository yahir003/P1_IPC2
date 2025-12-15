def buscar_mavi_por_id(lista_vms):
    buscado = input("Ingrese el ID de la VM: ").strip()
    actual = lista_vms.primero

    while actual:
        if actual.dato.id == buscado:
            print('VM encontrado:')
            actual.dato.mostrar_info()
            return
        actual = actual.siguiente

    print("VM no encontrado")

def listar_vms_centro(lista_vms):
    centro_id = input('ingrese el ID del centro: ').strip()

    print(f"\n=== VMs en {centro_id} ===")

    actual = lista_vms.primero
    contador = 1
    existe = False

    while actual:
        vm = actual.dato

        if vm.centro_id == centro_id:
            vm.mostrar_general_vm(contador)
            contador += 1
            existe = True

        actual = actual.siguiente

    if not existe:
        print("✗ No hay VMs registradas en este centro.")

def migrar_mv(lista_vms, lista_centros):
    id_vm = input('Ingresa el ID de la VM a migrar:').strip()

    #---------------------------------------------------------------Realizar busqueda
    nodo_vm = lista_vms.primero
    vm_encontrado = None
    while nodo_vm:
        if nodo_vm.dato.id == id_vm:
            vm_encontrado = nodo_vm.dato
            break
        nodo_vm = nodo_vm.siguiente
    if vm_encontrado is None:
        print('No se encontro la VM con el id ')
        return
    print(f"Vm Seleccionado: {vm_encontrado.id} (Actual centro:){vm_encontrado.centro_id}")
    print(f"Recursos requeridos: Cpu{vm_encontrado.cpu}, Ram:{vm_encontrado.ram}GB, Almacenamiento:{vm_encontrado.almacenamiento}")

    id_destino = input("ingresa el ID del centro de datos: ").strip()

    if id_destino == vm_encontrado.centro_id:
        print('error es el mismo centro actual')
        return
    #---------------------------------------------------------------Busca centro destino
    nodo_centro = lista_centros.primero
    centro_destino = None
    while nodo_centro:
        if nodo_centro.dato.id == id_destino:
            centro_destino = nodo_centro.dato
            break
        nodo_centro = nodo_centro.siguiente
    #---------------------------------------------------------------validar si cenrto tiene espacio
    if (centro_destino.cpu_disponible >= vm_encontrado.cpu and centro_destino.ram_disponible >= vm_encontrado.ram and
        centro_destino.alm_disponible >= vm_encontrado.almacenamiento):
        nodo_antiguo = lista_centros.primero
        centro_antiguo = None
        while nodo_antiguo:
            if nodo_antiguo.dato.id == vm_encontrado.centro_id:
                centro_antiguo = nodo_antiguo.dato
                break
            nodo_antiguo = nodo_antiguo.siguiente

        if centro_antiguo:
            centro_antiguo.cpu_disponible += vm_encontrado.cpu
            centro_antiguo.ram_disponible += vm_encontrado.ram
            centro_antiguo.alm_disponible += vm_encontrado.almacenamiento
            centro_antiguo.vms_activas -= 1

        centro_destino.cpu_disponible -= vm_encontrado.cpu
        centro_destino.ram_disponible -= vm_encontrado.ram
        centro_destino.alm_disponible -= vm_encontrado.almacenamiento
        centro_destino.vms_activas += 1

        vm_encontrado.centro_id = id_destino

        print('la accion se a realizado con exito')
    else:
        print('Error el centro no tiene recursos disponibles')


    if centro_destino is None:
        print(f"Error centro destino'{id_destino}' no encontrado")
        return

def menu_mavi(lista_vms, lista_centros):
    while True:
        print('*'*20,'  BUSCAR MAQUINA VIRUTAL  ','*'*20)
        print('1. Buscar VM por ID')
        print('2. Listar VMs de un centro')
        print('3. Migrar VM entre centros')
        print('4. Volver al menu principal')

        op = input('Seleccione una Opcion: ')

        if op == '1':
            buscar_mavi_por_id(lista_vms)
        elif op == '2':
            listar_vms_centro(lista_vms)
        elif op == '3':
            migrar_mv(lista_vms, lista_centros)
        elif op == '4':
            break
        else:
            print('Opcion no valida intente de nuevo...')