

adsi = int(input("alumnnos de adsi"))
redes = int(input("alumnnos de redes"))
diseno = int(input("alumnnos de diseño"))

preg = 1
preg2 = 1

ad = adsi /( adsi + redes + diseno) * 100
re = redes /(adsi + redes + diseno) * 100
di = diseno /(adsi + redes + diseno) * 100

while (preg or preg2) != "x":
    preg = input( " sobre que curso deseas saber?")
    preg2 = input(" deseas la... \n a)cantidad de alumnos \n b)el porcentaje")

    if preg == "adsi" and preg2 == "a":
        print (str(adsi))
    if preg == "adsi" and preg2 == "b":
        print (str(ad))
    if preg == "redes" and preg2 == "a":
            print (str(redes))
    if preg == "redes" and preg2 == "b":
        print (str(re))
    if preg == "diseño" and preg2 == "a":
            print (str(diseno))
    if preg == "diseño" and preg2 == "b":
        print (str(di))

print("hasta luego")
