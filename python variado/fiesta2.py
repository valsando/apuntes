import random

def frec(l):
    fre = {}
    for i in l:
        if i in fre:
            fre[i] += 1
        else:
            fre[i] = 1
    return fre
def regalo(n):
    S = []
    E = []
    a = 0
    R = []
    for i in range(n):
        s = bool(random.getrandbits(1))
        if s == True:
            s = "m"
        else:
            s = "f"
        S.append(s)
        e = random.randint(2,12)
        E.append(e)

        if s == "f":
            if e < 6:
                a = "coche"
            elif e <=9:
                a = "peluche"
            else:
                a = "muñequita"
        elif s == "m":
            if e < 5:
                a = "coche"
            elif e <=8:
                a = "disfraz"
            else:
                a = "bicicleta"
        R.append(a)
        print(f"invitado #{1+i}, edad:{e}, sexo:{s}")
    a = frec(S)
    b = frec(E)
    c = frec(R)
    print(f"sexos:\n{a} \n edades:\n{b} \n regalos:\n{c}")
regalo(30)
