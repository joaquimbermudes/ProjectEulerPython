# Problema 7
# Qual o primo número 10001?

import numpy as np

p = np.array([2, 3, 5, 7, 11, 13])
n = np.ones(6)*15
z = np.zeros(6)

while len(p) != 10001:
    if all(n % p != z):
        p = np.append(p, n[0])
        n = n + 2
        n = np.append(n, n[0])
        z = np.append(z, 0)
    else:
        n = n + 2

print(max(p))