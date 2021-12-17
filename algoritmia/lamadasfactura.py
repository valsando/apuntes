"""2.	Determinar el valor de una llamada telefónica, si por los primeros 3 minutos se 
cobran 300 pesos c/u y 150 por cada minuto adicional.
Suponer que las llamadas siempre duran más de 3 minutos.
"""
import random as rd

p = []
q = []
n = 1#int(input("numero de llamadas a calcular"))
m = 0
c = 0
while c == 0:
    m = int(input(" minutos"))
    if m < 3:
        print("otro valor")
    else:
        c = 1
        for i in range(n):
            l = m #rd.randint(3,m)
            c = 900 + (l - 3) * 150
            p.append(l)
            q.append(c)
        print(p)
        print(q)
