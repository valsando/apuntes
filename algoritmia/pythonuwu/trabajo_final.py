import datetime
import time


#salario minimo y sub. transporte:
smmv= 908526
subsidioTransporte = 106454
# matriz de los empleados actuales:
A = [[ 1,"pepe",1, 15],[2,"juan",2, 14],
[3,"vegeta",3, 17],['4', 'willirex', 4, 26],
[5,"jenny",5, 1],['6', 'carlos', 6, 16],
[7,"marcelo",7, 24],['8', 'andres', 8, 6],
[9,"bowser",9, 34],['10', 'mario', 10, 27]]
#salario neto:
def salarioIndividual(nombre):  
    for i in A:
        if nombre == i[1]:
            return (i[2]*0.92)
#asignador de id:
def asignaId(matriz):
    c = 0
    for i in matriz:
        c+=1
        i[0]="AA"+str(int(c)+100)
#asignador de salario:
def salario(matriz):
    for i in matriz:
        if i[3]> 30:
            i[3] -= 30
        i[2] = 2*smmv*(i[3]/30)
        if i[2] <= (2*smmv):
            i[2] +=subsidioTransporte*(i[3]/30)
        i[2] = i[2]//1
#ajustar salario minimo y subsidio de transporte:
def ajustarCant(texto):
    if texto == "sm":
        global smmv
        smmv = int(input("valor a colocar para el salario mínimo: "))
    elif texto == "st":
        global subsidioTransporte
        subsidioTransporte = int(input("valor a colocar para el subsidio de transporte: "))
    else:
        print("comando invalido")
#agregar n cantidad de empleados:
def agregarEmpleados(numero):
    for i in range(numero):
        l = []
        a = 0
        b = input("nombre:")
        c = 0
        d = int(input("dias trabajados:"))
        l +=a,b,c,d
        A.append(l)
        asignaId(A)
        salario(A)
        print(l)
#impromir matriz de empleados:
def MatrizEmpleados(matriz):
    print("\n".join(map(str,matriz)))
#imprimir nomina:
def nomina(matriz):
    p = 0
    for i in matriz:
        p += i[2]
    p /=1000000
    print("la nomina es de "+ str(p) + " millon(es) de pesos" )
    print("de ésta, se debe pagar en seguridad social "+ str((p*0.08)*1000000) + " pesos")
# todo entra aquí:
def trabajoFinal():
    owo = 0
    while owo !="x":
        asignaId(A)
        salario(A)
        print("--------------------------------------------------------------------------")
        print("------------------------------bienvenido----------------------------------")
        print(f"salario minimo : ${smmv} pesos       subsidio de transporte: ${subsidioTransporte} pesos")
        print("comandos:\npara salir escriba X")
        print("cambiar el salario minimo: sal   cambiar el subsidio de transporte: trans")
        print("imprimir la matriz de los empleados: mat     imprimir la nomina: nom")
        print("agregar empleados: emp + espacio +(numero de empleados a agregar)")
        print("salario neto de un empleado: salario + espacio +(nombre)")
        owo = input("que accion deseas realizar\n").lower()
        if owo == "sal":
            ajustarCant("sm")
            salario(A)
        elif owo == "trans":
            ajustarCant("st")
            salario(A)
        elif owo == "mat":
            MatrizEmpleados(A)
            time.sleep(5)
        elif owo == "nom":
            nomina(A)
            time.sleep(5)
        elif " " in owo:
            frase = owo.split(" ")
            if frase[0] == "emp":
                agregarEmpleados(int(frase[1]))
                time.sleep(3)
            elif frase[0] == "salario":
                print(f"el salario neto de {frase[1]} es de " + str(salarioIndividual(frase[1]))+ " pesos")
                time.sleep(3)
        elif owo == "x":
            print("breve pues")
            time.sleep(2)
        else:
            print("ahh yo no se mano...")
            time.sleep(2)
    print("hasta pronto!")
#espacio de chequeo y pruebas:
trabajoFinal()