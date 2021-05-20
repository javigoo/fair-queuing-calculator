
# FQ-calculator
Calcula l'ordre de trasmissión dels paquets amb una política de Fair Queuing o Weighted Fair Queuing


## Millores fetes
 - [x] Output explicatiu de Fair Queuing
 - [x] Output resumit de Fair Queuing 
 - [ ] Output explicatiu de Weighted Fair Queuing
 - [x] Output resumit de Weighted Fair Queuing (original)
 - [ ] Multiidioma?

Fair Queueing

## Exemples d'ús

### Input
```
python3 fair-queuing-calculator.py tests/reduced_test.txt 
```
```
./fair-queuing-calculator.py tests/reduced_test.txt
```


### Output resumit
```
Tabla de tests/reduced_test.txt

Paquete	Llegada	Medida	Flujo
1 	 0 	 40 	 1
2 	 0 	 30 	 1
3 	 5 	 10 	 3

El tiempo de finalizacion para el paquete 1 es de 40 
El tiempo de finalizacion para el paquete 2 es de 30 
*** El paquete 2 llega con un tiempo de 30 ***
El tiempo de finalizacion para el paquete 3 es de 40 
*** El paquete 1 llega con un tiempo de 40 ***
*** El paquete 3 llega con un tiempo de 40 ***
Orden de trasmision (FQ):  2,1,3

```
### Output apliat 
```
python3 fair-queuing-calculator.py tests/reduced_test.txt -explain
```
```
./fair-queuing-calculator.py tests/reduced_test.txt -explain
```
```
TTabla de tests/reduced_test.txt

Paquete	Llegada	Medida	Flujo
1 	 0 	 40 	 1
2 	 0 	 30 	 1
3 	 5 	 10 	 3

Inicio Algoritmo
T-finalizacion segment=0
Paquete analizado
Paquete	Llegada	Medida	Flujo
1	0	40	1
Formula:
Tiempo estimado = Max (T-finalizacion segment,T-Llegada)+Medida
Tiempo estimado= Max( 0 , 0 )+ 40 = 40
Tiempo llegada(0) <= T-finalizacion segment(0)? si
El tiempo de finalizacion para el paquete 1 es de 40  añadido a la tabla de seleccion añadido a la tabla de seleccion
Paquete analizado
Paquete	Llegada	Medida	Flujo
2	0	30	1
Formula:
Tiempo estimado = Max (T-finalizacion segment,T-Llegada)+Medida
Tiempo estimado= Max( 0 , 0 )+ 30 = 30
Tiempo llegada(0) <= T-finalizacion segment(0)? si
El tiempo de finalizacion para el paquete 2 es de 30  añadido a la tabla de seleccion añadido a la tabla de seleccion
Paquete analizado
Paquete	Llegada	Medida	Flujo
3	5	10	3
Formula:
Tiempo estimado = Max (T-finalizacion segment,T-Llegada)+Medida
Tiempo estimado= Max( 0 , 5 )+ 10 = 15
Tiempo llegada(5) <= T-finalizacion segment(0)? No
Eliminado de la tabla inicial los paquetes que estan en la tabla de seleccion

------ paquetes seleccionar menor tiempo -------
Paquete	Llegada	Medida	Flujo	Tiempo estimado
1 	 0 	 40 	 1 	 40
2 	 0 	 30 	 1 	 30

Paquete seleccionado
Paquete	Llegada	Medida	Flujo
2	0	30	1
------------------------------------------------
(UPDATE) T-finalizacion segment =T-finalizacion segment Anterior+medida paquete seleccionado
T-finalizacion segment Anterior = 0
Medida paquete seleccionado     = 30
UPDATED T-finalizacion segment=30
*** El paquete 2 llega con un tiempo de 30 ***
Fin iteracion Algoritmo

Inicio Algoritmo
T-finalizacion segment=30
Paquete analizado
Paquete	Llegada	Medida	Flujo
3	5	10	3
Formula:
Tiempo estimado = Max (T-finalizacion segment,T-Llegada)+Medida
Tiempo estimado= Max( 30 , 5 )+ 10 = 40
Tiempo llegada(5) <= T-finalizacion segment(30)? si
El tiempo de finalizacion para el paquete 3 es de 40  añadido a la tabla de seleccion añadido a la tabla de seleccion
Eliminado de la tabla inicial los paquetes que estan en la tabla de seleccion

------ paquetes seleccionar menor tiempo -------
Paquete	Llegada	Medida	Flujo	Tiempo estimado
1 	 0 	 40 	 1 	 40
3 	 5 	 10 	 3 	 40

Paquete seleccionado
Paquete	Llegada	Medida	Flujo
1	0	40	1
------------------------------------------------
(UPDATE) T-finalizacion segment =T-finalizacion segment Anterior+medida paquete seleccionado
T-finalizacion segment Anterior = 30
Medida paquete seleccionado     = 40
UPDATED T-finalizacion segment=70
*** El paquete 1 llega con un tiempo de 40 ***
Fin iteracion Algoritmo

Inicio Algoritmo
T-finalizacion segment=70
Ya no hay mas paquetes

------ paquetes seleccionar menor tiempo -------
Paquete	Llegada	Medida	Flujo	Tiempo estimado
3 	 5 	 10 	 3 	 40

Paquete seleccionado
Paquete	Llegada	Medida	Flujo
3	5	10	3
------------------------------------------------
(UPDATE) T-finalizacion segment =T-finalizacion segment Anterior+medida paquete seleccionado
T-finalizacion segment Anterior = 70
Medida paquete seleccionado     = 10
UPDATED T-finalizacion segment=80
*** El paquete 3 llega con un tiempo de 40 ***
Fin Algoritmo

Orden de trasmision (FQ):  2,1,3
```

### Input
```
python3 fair-queuing-calculator.py tests/parcial-19.txt -w 1:4,2:2,3:8,4:8
```
```
./fair-queuing-calculator.py tests/parcial-19.txt -w 1:4,2:2,3:8,4:8
```
### Output
```
Tabla de tests\parcial-19.txt

Paquete Llegada Medida  Flujo
1        0       65      1
2        0       40      1
3        0       25      4
4        0       20      2
5        15      40      2
6        25      40      4
7        30      65      4
8        30      5       2
9        30      70      1
10       40      20      4
11       55      20      2
12       60      15      1
13       70      15      3
14       75      10      4
15       90      35      2

El tiempo de finalizacion para el paquete  1  es de  260
El tiempo de finalizacion para el paquete  2  es de  160
El tiempo de finalizacion para el paquete  3  es de  200
El tiempo de finalizacion para el paquete  4  es de  40
*** El paquete 4 llega con un tiempo de 40 ***
El tiempo de finalizacion para el paquete  5  es de  100
*** El paquete 5 llega con un tiempo de 100 ***
El tiempo de finalizacion para el paquete  6  es de  380
El tiempo de finalizacion para el paquete  7  es de  580
El tiempo de finalizacion para el paquete  8  es de  70
El tiempo de finalizacion para el paquete  9  es de  340
El tiempo de finalizacion para el paquete  10  es de  220
El tiempo de finalizacion para el paquete  11  es de  100
El tiempo de finalizacion para el paquete  12  es de  120
*** El paquete 8 llega con un tiempo de 70 ***
*** El paquete 11 llega con un tiempo de 100 ***
El tiempo de finalizacion para el paquete  13  es de  205
El tiempo de finalizacion para el paquete  14  es de  165
*** El paquete 12 llega con un tiempo de 120 ***
El tiempo de finalizacion para el paquete  15  es de  170
*** El paquete 2 llega con un tiempo de 160 ***
*** El paquete 14 llega con un tiempo de 165 ***
*** El paquete 15 llega con un tiempo de 170 ***
*** El paquete 3 llega con un tiempo de 200 ***
*** El paquete 13 llega con un tiempo de 205 ***
*** El paquete 10 llega con un tiempo de 220 ***
*** El paquete 1 llega con un tiempo de 260 ***
*** El paquete 9 llega con un tiempo de 340 ***
*** El paquete 6 llega con un tiempo de 380 ***
*** El paquete 7 llega con un tiempo de 580 ***

Orden de trasmision (WFQ):  4,5,8,11,12,2,14,15,3,13,10,1,9,6,7
```




## Autors

* **Javier Roig** - *[Initial work](https://github.com/Javigoo/fair-queuing-calculator)* - [Javigoo](https://github.com/Javigoo)

## Acknowledgments

* Gràcies a Javier Roig per progrmar l'algoritme, sense ell no podria haver tret una abstracció i una forma alternativa d'entrendre el Fair Queuing
