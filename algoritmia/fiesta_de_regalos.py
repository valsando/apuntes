def frec(l):
    fre = {}
    for i in l:
        if i in fre:
            fre[i] += 1
        else:
            fre[i] = 1
    return fre
class invitado:
    def __init__(self, edad, sexo):
        self.edad= edad
        self.sexo= sexo
    def regalo(self):
        if self.sexo == "f":
            if self.edad < 6:

                return "coche"
            elif self.edad <=9:

                return "peluche"
            else:
                return "muñequita"
        elif self.sexo == "m":
            if self.edad < 5:

                return "coche"
            elif self.edad <=8:

                return "disfraz"
            else:
                return "bicicleta"
        else: print("valor invalido")


cristina =invitado(11, "f")
camilo =invitado(4, "m")
fabiola =invitado(7, "f")
daniel =invitado(6, "m")
pablo =invitado(9, "m")
andrea =invitado(12, "f")
natalia =invitado(9, "f")
carlos = invitado(3, "m")
cesar = invitado(5, "m")
maria = invitado(10, "f")
invitados = [cristina, camilo, fabiola, daniel, pablo, andrea, natalia, carlos, cesar, maria]
r = []
def gift(l):
    for i in l:
        r.append(i.regalo())
gift(invitados)


print(frec(r))
