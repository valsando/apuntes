import random

numero = input("dime un numero del 1- 10:")
print("dejame pensar")
numcomp = random.randint(1,10)
if numero == numcomp:
       print("le pegó esta gurrupleta")
else: print(f"nonas, yo pensaba que era el {numcomp}")
