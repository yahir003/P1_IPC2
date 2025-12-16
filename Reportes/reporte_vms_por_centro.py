from graphviz import Digraph

def reporte_vms_por_centro(lista_vms):
    centro_id = input("Ingrese ID del centro: ")

    dot = Digraph("VMs por Centro", format="png")
    dot.attr(rankdir="TB")
    dot.attr("node", shape="box", style="filled", fillcolor="lightblue")

    actual = lista_vms.primero
    hay_vm = False

    while actual:
        vm = actual.dato
        if vm.centro_id == centro_id:
            dot.node(
                vm.id,
                f"VM {vm.id}\nSO: {vm.sistema}\nCPU: {vm.cpu}\nRAM: {vm.ram}GB"
            )
            hay_vm = True
        actual = actual.siguiente

    if not hay_vm:
        print("No hay VMs para ese centro")
        return

    dot.render(f"Reportes/vms_centro_{centro_id}", cleanup=True)
    print(f"Reporte generado: Reportes/vms_centro_{centro_id}.png")
