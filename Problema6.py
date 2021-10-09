# Problema 6
# Encontrar a diferença entre o quadrado da soma e a soma dos quadrados dos 100 primeiros números

import numpy as np

x = ((100**2 + 100)/2)**2
y = sum(np.arange(101)**2)

print(x - y)

