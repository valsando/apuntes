import math as math
import numpy as np

#un banco reconoce intereses sobre capital invertido de acuerdo a la siguiente tabla:
# cap entre 1-1000000 : 0.5%interes
# cap entre 1000001-10000000 : 1%interes
# cap 10000001-100000000 : 2%intereses
# cap 100000000< : 3%interes
#se debe invertir el capital imprimido y el interes pagado
v = True
while bool(v) == True:
    cap = float(input("capital inicial: "))
    m = int(input("cuantos meses de interes desea calcular"))
    for i in np.arange(m):
        if cap < 1:
            print("valor invalido")
        elif cap < 1000000:
            p_int = 0.005
        elif cap <= 10000000:
            p_int = 0.01
        elif cap <= 100000000:
            p_int = 0.02
        else:
            p_int = 0.03
        int = p_int * cap
        cap += int
    print(f"el interes es {p_int} mensual y el capital es {cap} en {m} meses")
    v = bool(input("para salir presiona enter"))
