import random


def adivina_el_numero_computadora(x):
    print(f"selecciona un numero entre 1 y {x}")
    limite_inferior = 1
    limite_superior = x
    respuesta = input("dime")
    while respuesta!= "c":
        if limite_inferior!= limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
        respuesta = input(f"tu numero es {prediccion} ,si es menor escribe a, si es mayor escribe b, si es correcto escribe c")
        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta =="b":
            limite_inferior = prediccion + 1

    print(" yo sabia jaajaajaaajja")
adivina_el_numero_computadora(5)
