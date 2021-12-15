import pandas as pd


#base = float(input("ingrsa el valor de la base"))
#altura = float(input("ingrsa el valor de la altura"))
#area = base * altura
#print(f"el valor de el area es {area}")

#dias = int(input("ingresa el numero de dias"))
#minutos = dias * 24 * 60
#segundos = dias * 24 * 60 * 60
#print(f" esos {dias} dias son {minutos} minutos y tambien son {segundos} segundos")

#kilos = int(input("ingresa el numero de kilos"))
#libras = kilos * 2.20462
#gramos = kilos * 1000
#print(f" esos {kilos} kilos son {libras} libras y tambien son {gramos} gramos")

#sueldo_base = int(input("ingrese el valor del sueldo base: "))
#hijos = int(input("ingrese el numero de hijos: "))
#bonificacion = hijos * 150000
#total_mes = sueldo_base + bonificacion
#print(f"la bonificacion al tener {hijos} hijos es de {bonificacion}, el total a pagar es de {total_mes}")

#meses = int(input("cuantos meses vas a calcular"))
#while meses !="":
#    saldo_ahorrado = float(input("ingrese el monto ahorrado"))
#    interes = saldo_ahorrado * 0.015
#    saldo_ahorrado = saldo_ahorrado + interes
#    print(f"despues de un mes habria ganado gracias a los intereses {interes} y tendria un saldo de {saldo_ahorrado}")

hora = int(input("ingrese el numero de horas trabajadas"))
sueldo_base = 30000 * hora
desc = sueldo_base * 0.05
sueldo_total = float(sueldo_base) - desc
print(f" despues de descontar el aporte al fondo de educadores de {desc} pesos, tendria un sueldo de {sueldo_total} pesos")
lis = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
habi = pd.Series(lis)
vac = 3
hab= habi + vac -1
vac1 = 30
vvch = 60 / vac1
hdia = 8
dias = hab//(vac * vvch * hdia)

horas = ((hab%(vac * vvch * hdia)))//(vac * vvch)

minutos = 60 * (((hab%(vac * vvch * hdia))%(vac * vvch))/ vvch)
"""es la poblacion total(20000) divida los vacunados diarios (3 *8 *2)
cada vacunador (3) vacuna 2 personas por hora(2), trabajando 8 horas diarias(8)
print(f"{dias} ,\n {horas} ,\n {minutos} ")"""
