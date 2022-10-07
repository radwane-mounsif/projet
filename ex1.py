
import numpy as np
i = 1
n=int(input("DONNER N  "))
while i <= n:
    c = input("le nom de gaz ")
    a = float(input("dooner a "))
    b = float(input("dooner b "))
    T = 500
    P = 200
    R = 0.082
    B = -(P * b + R * T)
    C = -(a * b)
    coeff = [P, B, a, C]
    sol = np.roots(coeff)
    b = sol[0].real
    print('le volume molaire de gaz', c, 'est', b)
    i = i + 1

