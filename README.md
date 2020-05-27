# FQ-calculator
Calcula el orden de trasmisión de paquetes con una política Fair Queuing o Weighted Fair Queuing

## Ejemplos de uso

### Input
```
python fair-queuing-calculator.py tests/parcial-19.txt
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

El tiempo de finalizacion para el paquete  1  es de  65
El tiempo de finalizacion para el paquete  2  es de  40
El tiempo de finalizacion para el paquete  3  es de  25
El tiempo de finalizacion para el paquete  4  es de  20
*** El paquete 4 llega con un tiempo de 20 ***
El tiempo de finalizacion para el paquete  5  es de  60
*** El paquete 3 llega con un tiempo de 25 ***
El tiempo de finalizacion para el paquete  6  es de  85
El tiempo de finalizacion para el paquete  7  es de  110
El tiempo de finalizacion para el paquete  8  es de  50
El tiempo de finalizacion para el paquete  9  es de  115
El tiempo de finalizacion para el paquete  10  es de  65
*** El paquete 2 llega con un tiempo de 40 ***
El tiempo de finalizacion para el paquete  11  es de  105
El tiempo de finalizacion para el paquete  12  es de  100
El tiempo de finalizacion para el paquete  13  es de  100
El tiempo de finalizacion para el paquete  14  es de  95
*** El paquete 8 llega con un tiempo de 50 ***
El tiempo de finalizacion para el paquete  15  es de  125
*** El paquete 5 llega con un tiempo de 60 ***
*** El paquete 1 llega con un tiempo de 65 ***
*** El paquete 10 llega con un tiempo de 65 ***
*** El paquete 6 llega con un tiempo de 85 ***
*** El paquete 14 llega con un tiempo de 95 ***
*** El paquete 12 llega con un tiempo de 100 ***
*** El paquete 13 llega con un tiempo de 100 ***
*** El paquete 11 llega con un tiempo de 105 ***
*** El paquete 7 llega con un tiempo de 110 ***
*** El paquete 9 llega con un tiempo de 115 ***
*** El paquete 15 llega con un tiempo de 125 ***

Orden de trasmision (FQ):  4,3,2,8,5,1,10,6,14,12,13,11,7,9,15
```

### Input
```
python fair-queuing-calculator.py tests/parcial-19.txt -w 1:4,2:2,3:8,4:8
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
