import pandas as pd
import numpy as np

s = np.arange(5)
poblacion = 5000#pd.Series(p)
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
                                                                                                                                                                                                                                        
