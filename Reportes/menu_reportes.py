from Reportes.reporte_centros import reporte_centros
from Reportes.reporte_vms_por_centro import reporte_vms_por_centro
from Reportes.reporte_contenedores_por_vm import reporte_contenedores_por_vm
from Reportes.reporte_cola_solicitudes import reporte_cola

def menu_reporte(lista_centros, lista_vms, cola):
    while True:
        print("\n===== MENÚ DE REPORTES =====")
        print("1. Reporte de centros de datos")
        print("2. Reporte de VMs por centro")
        print("3. Reporte de contenedores por VM")
        print("4. Reporte de cola de solicitudes")
        print("5. Volver")

        op = input("Seleccione: ")

        if op == "1":
            reporte_centros(lista_centros)
        elif op == "2":
            reporte_vms_por_centro(lista_vms)
        elif op == "3":
            reporte_contenedores_por_vm(lista_vms)
        elif op == "4":
            reporte_cola(cola)
        elif op == "5":
            break
        else:
            print("Opción inválida")
