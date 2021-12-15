cap = float(input("capital inicial: "))
p_int = float(input("porcentaje de interes: "))
int = cap * p_int/100

a = 8
for i in range(a):
    cap += int
    if int <0:
        int = 0
    elif int > 7:
        cap += int
        int = cap * p_int/100
        print(str(cap) + " es su capital")
    else:
        cap -= int
        print(str(cap) + "es su capital y "+ str(int) +" el interes mensual acumulado")
        int = (2 + i) * cap * p_int/100
