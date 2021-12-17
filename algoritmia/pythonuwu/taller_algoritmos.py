def cuadrado():
    base = float(input("ingrsa el valor de la base"))
    altura = float(input("ingrsa el valor de la altura"))
    area = base * altura
    print(f"el valor de el area es {area}")
def dias():
    dias = int(input("ingresa el numero de dias"))
    minutos = dias * 24 * 60
    segundos = dias * 24 * 60 * 60
    print(f" esos {dias} dias son {minutos} minutos y tambien son {segundos} segundos")
def kilo():
    kilos = int(input("ingresa el numero de kilos"))
    libras = kilos * 2.20462
    gramos = kilos * 1000
    print(f" esos {kilos} kilos son {libras} libras y tambien son {gramos} gramos")
def hijos():
    sueldo_base = int(input("ingrese el valor del sueldo base: "))
    hijos = int(input("ingrese el numero de hijos: "))
    bonificacion = hijos * 150000
    total_mes = sueldo_base + bonificacion
    print(f"la bonificacion al tener {hijos} hijos es de {bonificacion}, el total a pagar es de {total_mes}")
def saldo():
    meses = int(input("cuantos meses vas a calcular"))
    while meses !="":
        saldo_ahorrado = float(input("ingrese el monto ahorrado"))
        interes = saldo_ahorrado * 0.015
        saldo_ahorrado = saldo_ahorrado + interes
        print(f"despues de un mes habria ganado gracias a los intereses {interes} y tendria un saldo de {saldo_ahorrado}")
def profesores():
    hora = int(input("ingrese el numero de horas trabajadas"))
    sueldo_base = 30000 * hora
    desc = sueldo_base * 0.05
    sueldo_total = float(sueldo_base) - desc
    print(f" despues de descontar el aporte al fondo de educadores de {desc} pesos, tendria un sueldo de {sueldo_total} pesos")
s = range(5)
def vacuna():
    poblacion = 5000
    vac = 3
    pob = poblacion + vac -1
    hdia = 8
    min = 30
    pph = 60/min
    vhora = pph * vac
    habdia = hdia * pph * vac
    dias = pob //habdia
    hsdia = pob%habdia
    horas = hsdia// vhora
    hshora = ((hsdia)% vhora)
    minutos = ((hshora)//vac) * min
    print(f" {dias} dias \n {horas} horas \n {minutos} minutos")