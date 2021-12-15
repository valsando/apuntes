#1.	Dada la siguiente función: Y = x2 – 2x
#Se requiere desarrollar un algoritmo que imprima en pantalla, para valores de x desde 1 a 10, lo siguiente:
#a)	Cada uno de los valores de Y
#b)	La suma de todos los valores de Y.
#c)	Valores de Y múltiplos de 3.
#d)	Suma de los valores de Y múltiplos de 3.

x = list(range(1,11))
y = []
for j in x:
    i = j**2 -(2 * j)
    print(f"x = {j} y = {i}")
    y.append(i)
print("a:", y)      #a
def sumar_lista(l):
    p = 0
    for i in l:
        p += i
    return p
b = sumar_lista(y)
print("b:", b)      #b
q = []
for i in y:
    if i % 3 == 0:
        q.append(i)
q.remove(0)
print("c:", q)      #c
d = sumar_lista(q)
print("d:", d)      #d
