# Problema 3
# Qual o maior fator primo de 600851475143

import numpy as np

x = 600851475143
a = 2
p = np.zeros(1)

while x != 1:
    a = 2
    while x % a != 0:
        a = a + 1
    p = np.append(p, a)
    x = x/a

print(max(p))
