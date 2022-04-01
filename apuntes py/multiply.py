

print("---------for---------")
numero = int(input("¿De que número quieres ver la tabla?: "))
print(f"----Tabla del {numero}----")

# "range" es un objeto iterable, más sobre ello más adelante
for nume in range(1,11):
    print(f"{numero} x {nume} = {nume*numero}")
