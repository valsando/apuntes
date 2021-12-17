def frec(l):
    fre = {}
    for i in l:
        if i in fre:
            fre[i] += 1
        else:
            fre[i] = 1
    return fre
def nuevos_invitados(n):
    A = []
    R = []
    print(f"a continuacion ingresarás {n} invitados con su respectiva edad y sexo.\n masculino = m ; femenino = f")
    for i in range(n):
        p = []
        a = input("nombre: ")
        b = int(input("edad: "))
        c = input("sexo: ")
        r = 0
        if c == "f":
            if b < 6:
                r = "coche"
            elif b <=9:
                r = "peluche"
            else:
                r = "muñequita"
        elif c == "m":
            if b < 5:
                r = "coche"
            elif b <=8:
                r = "disfraz"
            else:
                r = "bicicleta"
        else: r = ("valor invalido")
        p = [a, b, c, r]        
        R.append(r)
        A.append(str(p))
        g = "\n".join(A)        
        print(p)
    print(f"la matriz de los invitados ({n}X4) se compone de los siguientes vectores:\n\n", g)
    print("\n en la siguiente lista la cantidad de regalos: \n", frec(R))
    #tarea: como hacer que el programa guarde resultados de pruebas despues de cerrar
num = int(input("cantidad de invitados"))
nuevos_invitados(num)