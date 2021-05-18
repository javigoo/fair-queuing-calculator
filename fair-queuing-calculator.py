#!/usr/bin/env python3

import sys
import os


def parse(file):
    paquets = []
    print(f"\nTabla inicial de {sys.argv[1]}\n")
    print("Paquete\tLlegada\tMedida\tFlujo")
    for line in open(file):
        if len(line) != 1:
            if "!" not in line:
                package_data = line.split()

                if len(package_data)==4:
                    print(package_data[0], "\t", package_data[1], "\t", package_data[2], "\t", package_data[3])
                    paquets.append(package_data)
                else:
                    print_color(f"ADVERTENCIA!!\nEsta línea fue ignorada{package_data},\nesto puede llevar a resultados incorrectos","YELLOW,BOLD")
    print()

    return paquets


def parse_flow(flows):
    flow_weight = {}
    flow_data = flows.split(",")
    for flow in flow_data:
        flow = flow.split(":")
        if (len(flow[1]) == 3):
            weight = flow[1].split("/")[1]
        else:
            weight = flow[1]

        flow_weight[flow[0]] = weight

    return flow_weight


def select_less_time_to_complete(paquetes):

    print_color("------ paquetes seleccionar menor tiempo -------","GREEN,BOLD")

    print("Paquete\tLlegada\tMedida\tFlujo\tTiempo estimado")
    for p in paquetes:
        print(p[0], "\t", p[1], "\t", p[2], "\t", p[3], "\t", p[4])
    print()
    if len(paquetes) == 0:
        exit()
    paquet_menor_temps = paquetes[0]
    min_temps = paquet_menor_temps[4]

    for paquet in paquetes:
        if paquet[4] < min_temps:
            min_temps = paquet[4]
            paquet_menor_temps = paquet

    print_color("Paquete seleccionado","GREEN")
    print_color("Paquete\tLlegada\tMedida\tFlujo","GREEN")

    print_color(f"{paquet_menor_temps[0]}\t{paquet_menor_temps[1]}\t{paquet_menor_temps[2]}\t{paquet_menor_temps[3]}","GREEN")

    print_color("------------------------------------------------", "GREEN,BOLD")
    return paquet_menor_temps


def fair_queuing(paquets, temps_finalitzacio_segment=0, paquets_rebuts=[], package_transmission_order=[]):

    print_color(f"Inicio Algoritmo\nT-finalizacion segment={temps_finalitzacio_segment}","CYAN,BOLD")

    for paquet in paquets:
        temps_arribada = int(paquet[1])
        mida = int(paquet[2])
        temps_estimat = max(temps_finalitzacio_segment, temps_arribada) + mida

        print_color("Paquete analizado\nPaquete\tLlegada\tMedida\tFlujo")
        print_color( f"{paquet[0]}\t{paquet[1]}\t{paquet[2]}\t{paquet[3]}")
        print_color("Tiempo estimado = Max (T-finalizacion segment,T-Llegada)+Medida")
        print("Tiempo estimado= Max(", temps_finalitzacio_segment, ",", temps_arribada, ")+", mida, "=", temps_estimat)





        cond = "si" if temps_arribada <= temps_finalitzacio_segment else "No"

        print_color(f"Tiempo llegada({temps_arribada}) <= T-finalizacion segment({temps_finalitzacio_segment})? {cond}","RED")



        if temps_arribada <= temps_finalitzacio_segment:
            print_color(f"El tiempo de finalizacion para el paquete { paquet[0]} es de {temps_estimat} añadido a la tabla de seleccion","RED,BOLD,UNDERLINE")


            paquets_rebuts.append(paquet + [temps_estimat])

        print("\n")

    # print("---------------------------------------------------\npaquets rebut\n")
    if paquets!=[]:
        print_color("Eliminado de la tabla inicial los paquetes que estan en la tabla de seleccion\n", "BLUE,BOLD")
    else:
        print_color("Ya no hay mas paquetes\n", "BLUE,BOLD")
    for paquete in paquets_rebuts:
        if paquete[:-1] in paquets:
            paquets.remove(paquete[:-1])


    # print("---------------------------------------------------")

    paquete_recibido = select_less_time_to_complete(paquets_rebuts)
    tiempo_paquete = paquete_recibido[4]

    medida_paquete = int(paquete_recibido[2])

    anterior = temps_finalitzacio_segment

    print_color("(UPDATE) T-finalizacion segment =T-finalizacion segment Anterior+medida paquete seleccionado")#, anterior, "+", medida_paquete)
    print_color(f"T-finalizacion segment Anterior = {anterior}")
    print_color(f"Medida paquete seleccionado     = {medida_paquete}")
    temps_finalitzacio_segment = temps_finalitzacio_segment + medida_paquete
    print_color(f"UPDATED T-finalizacion segment={temps_finalitzacio_segment}","GREEN")  # ,"=",anterior,"+",medida_paquete,"\033[0m")

    paquets_rebuts.remove(paquete_recibido)
    print_color(f"*** El paquete {paquete_recibido[0]} llega con un tiempo de {tiempo_paquete} ***\n","YELLOW,BOLD")

    package_transmission_order.append(paquete_recibido[0])

    if len(paquets_rebuts) == 0:
        print("\nOrden de trasmision (FQ): ", ",".join(package_transmission_order))
        return

    fair_queuing(paquetes, temps_finalitzacio_segment, paquets_rebuts, package_transmission_order)


# ole ole los patrones de diseño
def weighted_fair_queuing(paquets, flow, temps_finalitzacio_segment=0, paquets_rebuts=[],
                          package_transmission_order=[]):
    for paquet in paquets:
        temps_arribada = int(paquet[1])
        mida = int(paquet[2])
        temps_estimat = max(temps_finalitzacio_segment, temps_arribada) + mida * int(flow[paquet[3]])

        if temps_arribada <= temps_finalitzacio_segment:
            print("El tiempo de finalizacion para el paquete ", paquet[0], " es de ", temps_estimat)
            paquets_rebuts.append(paquet + [temps_estimat])

    for paquete in paquets_rebuts:
        if paquete[:-1] in paquets:
            paquets.remove(paquete[:-1])

    paquete_recibido = select_less_time_to_complete(paquets_rebuts)
    tiempo_paquete = paquete_recibido[4]
    medida_paquete = int(paquete_recibido[2])

    temps_finalitzacio_segment += medida_paquete
    paquets_rebuts.remove(paquete_recibido)

    print("*** El paquete", paquete_recibido[0], "llega con un tiempo de", tiempo_paquete, "***")

    package_transmission_order.append(paquete_recibido[0])

    if len(paquets_rebuts) == 0:
        return print("\nOrden de trasmision (WFQ): ", ",".join(package_transmission_order))

    weighted_fair_queuing(paquetes, flow, temps_finalitzacio_segment, paquets_rebuts, package_transmission_order)


def print_color(msg:str, attr="END"):
    switcher = {
        "HEADER": '\033[95m',
        "BLUE": '\033[94m',
        "CYAN": '\033[96m',
        "GREEN": '\033[92m',

        "YELLOW": '\033[93m',
        "RED": '\033[91m',
        "END": '\033[0m',
        "BOLD": '\033[1m',
        "UNDERLINE": '\033[4m',
    }

    getColor= lambda Attribute: switcher.get(Attribute, '\033[0m')

    s=""
    for attribute in attr.split(","):
        s=s+getColor(attribute)

    print(s+msg+getColor("END"))


if __name__ == "__main__":

    if len(sys.argv) <= 1:
        sys.exit("Use: %s <tabla_paquetes>" % sys.argv[0])

    if os.path.isfile(sys.argv[1]):
        taula_paquets_file = os.path.abspath(sys.argv[1])
    else:
        sys.exit("Error! %s not found" % sys.argv[1])

    paquetes = parse(taula_paquets_file)

    if len(sys.argv) >= 3:
        if sys.argv[2] == "-w" and len(sys.argv) == 4:
            flujos = parse_flow(sys.argv[3])
            weighted_fair_queuing(paquets=paquetes, flow=flujos)
        else:
            sys.exit("Use: %s <tabla_paquetes> [-w <flujo1:ancho de banda1,flujo2:ancho de banda2...>]" % sys.argv[0])

    fair_queuing(paquetes)
