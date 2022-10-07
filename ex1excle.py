k = r"C:\Users\lenovo\Desktop\EX1Python.xlsx"
import numpy as np
import pandas as pd
i = 0
data = pd.read_excel(k)
print(data)
print(data.b[0])
val = len(data.gaz) - 1

while i <= val:
    T = 500
    R = 0.082
    P = 200
    B = -(P * data.b[i] + R * T)
    C = -(data.a[i] * data.b[i])
    coeff = [P, B, data.a[i], C]
    volm = np.roots(coeff)
    b = volm[0].real
    print('volume  de gaz', data.gaz[i], 'est', b, 'l')
    i = i + 1

