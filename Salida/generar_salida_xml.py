import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime


def generar_salida_xml(lista_centros, lista_vms, ruta="salida/salida.xml"):

    root = ET.Element("resultadoCloudSync")

    
    timestamp = ET.SubElement(root, "timestamp")
    timestamp.text = datetime.now().isoformat()

    estado_centros = ET.SubElement(root, "estadoCentros")

    total_vms = 0
    total_contenedores = 0

    actual_centro = lista_centros.primero
    while actual_centro:
        centro = actual_centro.dato

        centro_xml = ET.SubElement(
            estado_centros, "centro", {"id": centro.id}
        )

        nombre = ET.SubElement(centro_xml, "nombre")
        nombre.text = centro.id   # si no tienes nombre, usamos el ID

        recursos = ET.SubElement(centro_xml, "recursos")

        cpu_total = ET.SubElement(recursos, "cpuTotal")
        cpu_total.text = str(centro.cpu_total)

        cpu_disp = ET.SubElement(recursos, "cpuDisponible")
        cpu_disp.text = str(centro.cpu_disponible)

        cpu_usada = centro.cpu_total - centro.cpu_disponible
        cpu_util = ET.SubElement(recursos, "cpuUtilizacion")
        cpu_util.text = f"{(cpu_usada * 100) / centro.cpu_total:.2f}%"

        ram_total = ET.SubElement(recursos, "ramTotal")
        ram_total.text = str(centro.ram_total)

        ram_disp = ET.SubElement(recursos, "ramDisponible")
        ram_disp.text = str(centro.ram_disponible)

        ram_usada = centro.ram_total - centro.ram_disponible
        ram_util = ET.SubElement(recursos, "ramUtilizacion")
        ram_util.text = f"{(ram_usada * 100) / centro.ram_total:.2f}%"

        vms_centro = 0
        contenedores_centro = 0

        actual_vm = lista_vms.primero
        while actual_vm:
            vm = actual_vm.dato
            if vm.centro_id == centro.id:
                vms_centro += 1
                total_vms += 1
                contenedores_vm = vm.contenedor.contar()
                contenedores_centro += contenedores_vm
                total_contenedores += contenedores_vm
            actual_vm = actual_vm.siguiente

        cant_vms = ET.SubElement(centro_xml, "cantidadVMs")
        cant_vms.text = str(vms_centro)

        cant_cont = ET.SubElement(centro_xml, "cantidadContenedores")
        cant_cont.text = str(contenedores_centro)

        actual_centro = actual_centro.siguiente

    estadisticas = ET.SubElement(root, "estadisticas")

    vms_activas = ET.SubElement(estadisticas, "vmsActivas")
    vms_activas.text = str(total_vms)

    cont_total = ET.SubElement(estadisticas, "contenedoresTotales")
    cont_total.text = str(total_contenedores)


    xml_str = minidom.parseString(
        ET.tostring(root)
    ).toprettyxml(indent="  ")

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(xml_str)

    print("✔ Archivo de salida generado:", ruta)
