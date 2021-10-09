# Problema 5
# Menor número que pode ser dividido por 1:20

import numpy as np

x = np.ones(20)*2520
y = np.arange(1,21)
z = np.zeros(20)

while any(x % y != z):
    x = x + 20

print(x)

# resp = 2.3279256e+08
