import time

#salario minimo y sub. transporte:
smmv= 908526
subsidioTransporte = 106454
Nomina = 0
sub = {}
# matriz de los empleados actuales (muestra salarios totales):
A = [[1328985934,"pepe",1, 15,0],[100224141,"juan",2, 14,0],
    [8325020583,"vegeta",3, 17,0],[993326431, 'willirex', 4, 26,0],
    [5487256653,"jenny",5, 1,0],[982227431, 'carlos', 6, 16,0],
    [3525642467,"marcelo",7, 24,0],[953356431, 'andres', 8, 6,0],
    [1009545434,"bowser",9, 34,0],[793326431, 'mario', 10, 27,0]]
matrix = 0
#actualiza impresion, salario, id, y nomina:
def actualizaMatriz(matriz):
    global A
    global Nomina
    global sub
    global matrix
    Nomina=0
    for i in matriz:
        #asignador de salario:
        if i[3]> 30:
            i[3] -= 30
        sueldo = i[2]*smmv*(i[3]/30)
        #asignador de subsidio de transporte:
        subsidio = 0
        if i[2] <= 2:
            subsidio += subsidioTransporte*(i[3]/30)
            sueldo +=subsidio
        sub[i[1]]=subsidio
        #suma de la nomina:
        Nomina += sueldo
        i[4]= int(sueldo)
    #organizador de registros y matriz:
    A = sorted(A, key=lambda x: x[0])
    matrix = "\n".join(map(str,A))
#salario, subsido y salario neto por empleado:
def sIndividual(nombre, s):
    if nombre =="todos":
        if s =="salario":
            print(f"salario menos impuestos de {nombre} es de " + str(int(Nomina*0.92*0.000001)) + "millones de pesos")
        elif s =="total":
            print(f"el salario neto de {nombre} es de " + str(int(Nomina*0.000001)) + "millones de pesos")
        elif s =="subsidio":
            print(f"los subsidios de transporte son los siguientes:\n"+ "\n".join(str(sub).split(",")))
            print("en total suman "+ str(sum(sub.values())) + "pesos")
    elif nombre in sub.keys():
        for i in A:
            if nombre == i[1]:
                if s =="salario":
                    print(f"salario menos impuestos de {nombre} es de " + str(i[4]*0.92) + " pesos")
                elif s =="subsido":
                    print(f"el subsidio de transporte de {nombre} es de " + str(sub[nombre]) + " pesos")
                elif s =="total":
                    print(f"salario neto de {nombre} es de " + str(i[4]) + " pesos")
                return
    else:
        print("no se encontro nadie con ese nombre pa")
#ajustar salario minimo y subsidio de transporte:
def ajustarCant(texto):
    if texto == "sal":
        global smmv
        smmv = int(input("valor a colocar para el salario mínimo: "))
    elif texto == "trans":
        global subsidioTransporte
        subsidioTransporte = int(input("valor a colocar para el subsidio de transporte: "))
    actualizaMatriz(A)
#agregar o borrar n cantidad de empleados:
def editarEmpleados(numero):
    if numero > 0:
        for i in range(numero):
            l = []
            #id
            a = int(input("cedula: "))
            #nombre
            b = input("nombre:")
            c = int(input("salario base(#salarios minimos):"))
            #por si lo colocan en pesos en vez de salarios minimos:
            if c > 10000:
                c /=smmv
            d = int(input("dias trabajados:"))
            l +=a,b,c,d,0
            A.append(l)
            actualizaMatriz(A)
            print(l)
    elif numero < 0:
        numero *=-1
        pregunta = input("a continuacion borraras un usuario, seleccionar metodo de busqueda \npor nombre o id: ")
        ind = 0
        if pregunta == ("nombre"):
            print("buscando por nombre")
            ind += 1
        elif pregunta == ("id"):
            pass
        else:
            print("no se que dices asi que lo buscaré por nombre")
            pregunta = "nombre"
            ind +=1
        for i in range(numero):
            buscador = input(pregunta + ": ")
            #recorrer una matriz y borrar una fila buscando por su 1er o 2do elemento:
            cont = 0
            b = []
            for registro in A:
                print(str(registro[ind]) + "---" + buscador)
                if str(registro[ind])== buscador:
                    b.append(registro)
                    cont +=1
            print(f"ha(n) coincidido {cont} elemento(s)")
            if cont == 0:
                print("no se encontro la persona que buscaste")
            elif cont == 1:
                A.remove(b[0])
                print(f"se ha removido el usuario {b[0]} exitosamente")
            elif cont>1:
                print(f"seleciona cual de los {cont} es:")
                print(b)
                talk = int(input(f"digita cual de los {cont} elementos borrar:"))-1
                A.remove(b[talk])
                print(f"se ha removido un usuario {b[talk]} exitosamente")
    else:
        print("???")
    actualizaMatriz(A)
# todo entra aquí:
def trabajoFinal():
    owo = 0
    while owo !="x":
        actualizaMatriz(A)
        print(f"""--------------------------------------------------------------------------
        \n------------------------------bienvenido----------------------------------
        \nsalario minimo : ${smmv} pesos    subsidio de transporte: ${subsidioTransporte} pesos
        comandos:\npara salir escriba X
        \ncambiar el salario minimo: sal               cambiar el subsidio de transporte: trans
        \nimprimir la matriz de los empleados: mat       imprimir la nomina: nom
        \nsalario que obtiene un empleado: salario + espacio +(nombre)
        \nsubsidio de transporte de un empleado: subsidio + espacio +(nombre)
        \nsalario total de un empleado: total + espacio +(nombre) 
        para editar empleados:\nagregar o borrar empleados: emp + espacio +(numero de empleados positivo o negativo)""")
        owo = input("que accion deseas realizar\n").lower()
        if (owo == "sal") or (owo == "trans"):
            ajustarCant(owo)
        elif owo == "mat":
            print("matriz: \n [cedula,nombre,salarios base, dias trabajados,sueldo]")
            print(matrix)
            time.sleep(5)
        elif owo == "nom":
            print("nómina:")
            p = Nomina/1000000
            print("la nomina es de "+ str(int(p)) + " millon(es) de pesos")
            print("de ésta, se debe pagar en seguridad social "+ str(int(Nomina*0.08)) + " pesos")
            time.sleep(5)
        elif owo == "x":
            print("ok")
            time.sleep(2)
        elif " " in owo:
            frase = owo.split(" ")
            if frase[0] == "emp":
                editarEmpleados(int(frase[1]))
                time.sleep(3)
            elif frase[0] == "salario" or "subsidio" or "total":
                sIndividual(frase[1], frase[0])
                time.sleep(3)
            else:
                print("ejecuta nuevamente, evita usar espacios si no son necesarios")
        else:
            print("no se de que hablas")
            time.sleep(2)
    print("hasta pronto!")
#espacio de chequeo y pruebas:
trabajoFinal()