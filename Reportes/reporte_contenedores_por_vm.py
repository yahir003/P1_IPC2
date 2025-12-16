from graphviz import Digraph

def reporte_contenedores_por_vm(lista_vms):
    vm_id = input("Ingrese el ID de la VM: ")

    actual = lista_vms.primero
    vm_encontrada = None

    while actual:
        if actual.dato.id == vm_id:
            vm_encontrada = actual.dato
            break
        actual = actual.siguiente

    if vm_encontrada is None:
        print("VM no encontrada")
        return

    dot = Digraph(
        comment="Reporte de Contenedores por VM",
        format="png"
    )
    dot.attr(rankdir="TB")

    # Nodo VM
    dot.node(
        vm_encontrada.id,
        f"VM {vm_encontrada.id}\nSO: {vm_encontrada.sistema}",
        shape="box",
        style="filled",
        fillcolor="lightblue"
    )

    actual_cont = vm_encontrada.contenedor.primero

    if actual_cont is None:
        dot.node("sin_cont", "Sin contenedores", shape="ellipse")
        dot.edge(vm_encontrada.id, "sin_cont")
    else:
        while actual_cont:
            cont = actual_cont.dato
            dot.node(
                cont.id,
                f"Contenedor {cont.id}\nCPU: {cont.cpu}\nRAM: {cont.ram}",
                shape="ellipse",
                style="filled",
                fillcolor="lightyellow"
            )
            dot.edge(vm_encontrada.id, cont.id)
            actual_cont = actual_cont.siguiente

    dot.render("Reportes/reporte_contenedores_vm", view=True)
    print("Reporte de contenedores generado correctamente")
