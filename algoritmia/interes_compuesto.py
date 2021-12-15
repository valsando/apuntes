#1% sobre los cdt's, un inversionista decide depositarun valor determinado a 12 meses, para lo cual desea saber
#cuanto es el interes mnsual a retirar si no desea reinvertirlo, calcular capital ttal + interes acumulado
#
cap = float(input("capital a invertir"))
cap1 = cap
int = 0.01 * cap
meses = float(input("cuantos meses vas a calcular"))
c = 0
intt = int * meses
while c != meses:
    cap += int
    int = 0.01 * cap
    c += 1
    #final
inta = cap -cap1
print(f"el interes sin reinvertir cada mes es {intt} y el interes reinvertido es {inta}")
