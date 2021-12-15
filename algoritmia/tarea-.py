
#edad = int(input("que edad tienes?"))
#ant = int(input("cuanto tiempo llevas trabajando?"))
#if ant < 25:
    #if edad < 60:
        #print("no te jubilas jaja")
    #else:
        #print("pension por edad")
#else:
    #if edad < 60:
    #    print("jubilacion por antiguedad joven")
    #else:
        #print("jubilacion por antiguedad adulta")




sal = float(input("¿cuantos salarios ganas al mes?"))
if sal > 30000:
    sal /= 908000
    print(f"ganas {int(sal)} salarios minimos,y ", end="")
else:
    print(f"para {int(sal)} salarios minimos ", end="")

if sal <= 1:
    print("la cuota moderadora es de 2.700 pesos")
elif sal <= 4:
    print("la cuota moderadora es de 7.200 pesos")
elif sal <= 6:
    print("la cuota moderadora es de 15.000 pesos")
else:
    print("la cuota moderadora es de 30.000 pesos")
