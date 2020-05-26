#!/usr/bin/env python3

import sys
import os

def parse(file):
    paquets = []
    print("Taula de paquets:\n")
    for line in open(file):
        print(line)

        paquets.append(line.split())
    print()
    return paquets


def select_less_time_to_complete(paquetes):
    paquet_menor_temps = paquetes[0]
    min_temps = paquet_menor_temps[4]

    for paquet in paquetes:
        if paquet[4] < min_temps:
            min_temps = paquet[4]
            paquet_menor_temps = paquet
    
    return paquet_menor_temps

def fair_queuing(paquets, temps_finalitzacio_segment=0, paquets_rebuts = [], package_transmission_order = []):

    # Tiempo de finalizacion con el servidor libre
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
    temps_finalitzacio_segment += paquete_recibido[4]

    paquets_rebuts.remove(paquete_recibido)

    print("*** El paquete",paquete_recibido[0], "llega con un tiempo de",temps_finalitzacio_segment,"***")

    package_transmission_order.append(paquete_recibido[0])

    if len(paquets_rebuts) == 0:
        return print("\nOrden de enviamiento de los paquetes", package_transmission_order)

    fair_queuing(paquetes, temps_finalitzacio_segment ,paquets_rebuts, package_transmission_order)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Use: %s <taula_paquets>" % sys.argv[0])

    if os.path.isfile(sys.argv[1]):
        taula_paquets_file = os.path.abspath(sys.argv[1])
    else:
        sys.exit("ERROR: Taula paquets not found (%s)" % sys.argv[1])

    paquetes = parse(taula_paquets_file)

    fair_queuing(paquetes)