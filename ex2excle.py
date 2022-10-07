k = r"C:\Users\lenovo\Desktop\Exercice2python.xlsx"
import numpy as np
import pandas as pd
import math
i=0
data = pd.read_excel(k)
val = len(data.a) - 1

while i <= val:
    DH = 6009.5
    R = 8.314
    DC = 37.87
    lndea = ((-DH / R) * ((1 / data.a[i]) - (1 / 273.15))) - ((DC / R) * ((data.a[i] - 273.15) / data.a[i]) - (math.log(data.a[i] / 273.15)))
    print("pour la temperature",data.a[i] )
    print("ln(alfa)=",-lndea)
    alfa = math.exp(lndea)
    print("alfa est de ",alfa)
    print('')
    i = i + 1