#!/usr/bin/env python3

import sys
import os

def parse(file):
    paquets = []
    print("\nTabla de %s\n" % sys.argv[1])
    print("Paquete\tLlegada\tMedida\tFlujo")
    for line in open(file):
        package_data = line.split()
        print(package_data[0],"\t",package_data[1],"\t",package_data[2],"\t",package_data[3])
        paquets.append(package_data)
    print()
    
    return paquets

def parse_flujo(flujos):
    flow_weight = {}
    flow_data = flujos.split(",")
    for flow in flow_data:
        flow = flow.split(":")
        if(len(flow[1]) == 3):
            weight = flow[1].split("/")[1]
        else:
            weight = flow[1]

        flow_weight[flow[0]] = weight

    return flow_weight

def select_less_time_to_complete(paquetes):
    paquet_menor_temps = paquetes[0]
    min_temps = paquet_menor_temps[4]

    for paquet in paquetes:
        if paquet[4] < min_temps:
            min_temps = paquet[4]
            paquet_menor_temps = paquet
    
    return paquet_menor_temps

def fair_queuing(paquets, temps_finalitzacio_segment=0, paquets_rebuts = [], package_transmission_order = [], flow = {}):

    for paquet in paquets:
        temps_arribada = int(paquet[1])
        mida = int(paquet[2])
        temps_estimat = max(temps_finalitzacio_segment ,temps_arribada) + mida

        if temps_arribada <= temps_finalitzacio_segment:
            print("El tiempo de finalizacion para el paquete ",paquet[0]," es de ",temps_estimat)
            paquets_rebuts.append(paquet+[temps_estimat])

    for paquete in paquets_rebuts:
        if paquete[:-1] in paquets:
            paquets.remove(paquete[:-1])

    paquete_recibido = select_less_time_to_complete(paquets_rebuts)
    tiempo_paquete = paquete_recibido[4]
    medida_paquete = int(paquete_recibido[2])

    temps_finalitzacio_segment += medida_paquete
    paquets_rebuts.remove(paquete_recibido)

    print("*** El paquete",paquete_recibido[0], "llega con un tiempo de",tiempo_paquete,"***")

    package_transmission_order.append(paquete_recibido[0])

    if len(paquets_rebuts) == 0:
        return print("\nOrden de trasmision: ", ",".join(package_transmission_order))

    fair_queuing(paquetes, temps_finalitzacio_segment ,paquets_rebuts, package_transmission_order)

def weighted_fair_queuing(paquetes, flujo):
    fair_queuing(paquets = paquetes, flow = {})

if __name__ == "__main__":

    print(len(sys.argv))

    if len(sys.argv) <= 1:
        sys.exit("Use: %s <tabla_paquetes>" % sys.argv[0])

    if os.path.isfile(sys.argv[1]):
        taula_paquets_file = os.path.abspath(sys.argv[1])
    else:
        sys.exit("Error! %s not found" % sys.argv[1])

    paquetes = parse(taula_paquets_file)
    
    if len(sys.argv) >= 3:
        if sys.argv[2]=="-w" and len(sys.argv) == 4:
            flujos = parse_flujo(sys.argv[3])
            weighted_fair_queuing(paquetes, flujos)
        else:
            sys.exit("Use: %s <tabla_paquetes> [-w <flujo1:ancho de banda1,flujo2:ancho de banda2...>]" % sys.argv[0])

    fair_queuing(paquetes)