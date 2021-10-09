# Problema 4
# Encontrar o maior número palindromo que seja produto de dois números de 3 dígitos

def invert(texto):
    return texto[::-1]

c = 0

x = []

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        x.append(j*i)

v = 0

for i in x:
    if str(i) == invert(str(i)):
        v = max(v, i)


print(v)