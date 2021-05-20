#!/usr/bin/env python3

import sys
import os
import argparse

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

    print(s+msg+getColor("END"),end="\n")
def parse(file):
    paquets = []
    print("\nTabla de %s\n" % sys.argv[1])
    print("Paquete\tLlegada\tMedida\tFlujo")
    for line in open(file):
        if len(line) != 1:
            if "!" not in line:
                package_data = line.split()
                if len(package_data) == 4:
                    print(package_data[0], "\t", package_data[1], "\t", package_data[2], "\t", package_data[3])
                    paquets.append(package_data)
                else:
                    print_color(
                        f"ADVERTENCIA!!\nEsta línea fue ignorada{package_data},\nesto puede llevar a resultados incorrectos",
                        "YELLOW,BOLD")
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
    if len(paquetes) == 0:
        exit("Error")
    else:
        if verbose:
            print_color("------ paquetes seleccionar menor tiempo -------", "GREEN,BOLD")

            print("Paquete\tLlegada\tMedida\tFlujo\tTiempo estimado")
            for p in paquetes:
                print(p[0], "\t", p[1], "\t", p[2], "\t", p[3], "\t", p[4])
            print()
    paquet_menor_temps = paquetes[0]
    min_temps = paquet_menor_temps[4]

    for paquet in paquetes:
        if paquet[4] < min_temps:
            min_temps = paquet[4]
            paquet_menor_temps = paquet
    if verbose:
        print_color("Paquete seleccionado", "GREEN")
        print_color("Paquete\tLlegada\tMedida\tFlujo", "GREEN")

        print_color(
            f"{paquet_menor_temps[0]}\t{paquet_menor_temps[1]}\t{paquet_menor_temps[2]}\t{paquet_menor_temps[3]}",
            "GREEN")

        print_color("------------------------------------------------", "GREEN,BOLD")
    return paquet_menor_temps


def fair_queuing(paquets, temps_finalitzacio_segment=0, paquets_rebuts=[], package_transmission_order=[]):
    if verbose:
        print_color(f"Inicio Algoritmo\nT-finalizacion segment={temps_finalitzacio_segment}", "CYAN,BOLD")

    for paquet in paquets:
        temps_arribada = int(paquet[1])
        mida = int(paquet[2])
        temps_estimat = max(temps_finalitzacio_segment, temps_arribada) + mida
        if verbose:
            print_color("Paquete analizado\nPaquete\tLlegada\tMedida\tFlujo")
            print_color(f"{paquet[0]}\t{paquet[1]}\t{paquet[2]}\t{paquet[3]}")
            print_color("Formula:\nTiempo estimado = Max (T-finalizacion segment,T-Llegada)+Medida")
            print("Tiempo estimado= Max(", temps_finalitzacio_segment, ",", temps_arribada, ")+", mida, "=",
                  temps_estimat)
            cond = "si" if temps_arribada <= temps_finalitzacio_segment else "No"
            print_color(
                f"Tiempo llegada({temps_arribada}) <= T-finalizacion segment({temps_finalitzacio_segment})? {cond}",
                "RED")

        if temps_arribada <= temps_finalitzacio_segment:
            tail = " añadido a la tabla de seleccion" if verbose else "\n"
            attr = "RED,BOLD" if verbose else ""
            print(f"El tiempo de finalizacion para el paquete {paquet[0]} es de {temps_estimat} "+tail,end="")
            if verbose:
                print_color(tail, attr)
            paquets_rebuts.append(paquet + [temps_estimat])
    if verbose:
        if paquets != []:
            print_color("Eliminado de la tabla inicial los paquetes que estan en la tabla de seleccion\n", "BLUE,BOLD")
        else:
            print_color("Ya no hay mas paquetes\n", "BLUE,BOLD")
    for paquete in paquets_rebuts:
        if paquete[:-1] in paquets:
            paquets.remove(paquete[:-1])

    paquete_recibido = select_less_time_to_complete(paquets_rebuts)
    tiempo_paquete = paquete_recibido[4]
    medida_paquete = int(paquete_recibido[2])
    anterior = temps_finalitzacio_segment
    if verbose:
        print_color(
            "(UPDATE) T-finalizacion segment =T-finalizacion segment Anterior+medida paquete seleccionado")
        print_color(f"T-finalizacion segment Anterior = {anterior}")
        print_color(f"Medida paquete seleccionado     = {medida_paquete}")
    temps_finalitzacio_segment += medida_paquete
    if verbose:
        print_color(f"UPDATED T-finalizacion segment={temps_finalitzacio_segment}", "GREEN")
    paquets_rebuts.remove(paquete_recibido)
    attr = "YELLOW,BOLD" if verbose else ""
    print_color(f"*** El paquete {paquete_recibido[0]} llega con un tiempo de {tiempo_paquete} ***", attr)


    package_transmission_order.append(paquete_recibido[0])

    if len(paquets_rebuts) == 0:
        if verbose:
            print_color(f"Fin Algoritmo\n", "CYAN,BOLD")
        print("Orden de trasmision (FQ): ", ",".join(package_transmission_order))
        exit(0)
    if verbose:
        print_color(f"Fin iteracion Algoritmo\n", "CYAN,BOLD")
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


if __name__ == "__main__":
    verbose = False
    try:
        idx =sys.argv.index("-explain")
        del_idx = idx
    except ValueError:
        del_idx=-1
    else:
        sys.argv.pop(del_idx)
        verbose = True




    #correct not found files
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
            sys.exit("Use: %s <tabla_paquetes> [-w <flujo1:ancho de banda1,flujo2:ancho de banda2...>] [-explain]" % sys.argv[0])
    else:
        fair_queuing(paquetes)
