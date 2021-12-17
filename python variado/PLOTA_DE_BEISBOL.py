import math
# Vo = 30   son ejemplos de en ejercicio ya resuelto
# gr = 36.9

Vo = 11.135
gr = 60
w = math.radians(gr)
voy = Vo * math.sin(w)
vox = Vo * math.cos(w)
g = 9.8
ts = voy/g
T = 2 * ts
D = vox * T
Hmax = voy**2 / (2 * g)
print("la altura maxima es" + str(Hmax))
hwili = 3.05
H = hwili-1.55
while not(H < Hmax):
    H = float(input("uno menor pendejo"))
else:
    X1 = (voy - math.sqrt((voy**2) - (2 * g * H)))/ (g)
    X2 = (voy + math.sqrt((voy**2) - (2 * g * H)))/ ( g)
print(X1)
print(X2)
D = vox * X2
print(str(D) + "metros")
corredor = float(input("corredor"))
di = D - corredor
difinal= di/X2
print("el corredor requiere correr a" +str(difinal) + "metros por segundo")
