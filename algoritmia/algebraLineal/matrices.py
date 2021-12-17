import random

def matriz_identidad(n):
    for i in range(n):
        for j in range(n):
            if i ==j:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print("\n")
def matiz(p,q):
    for i in range(q):
        for j in range(q):
            print(p, end=" ")
        print("\n")
filas = 5#int(input("numero de filas"))
col = 3#int(input("numero de columnas"))
#otra forma rapida de fabricar matrices:
a = [[random.randint(1,100) for i in range(col)]for i in range(filas)]

for i in a:
    print(i)
    
