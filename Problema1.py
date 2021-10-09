# Problema 1
# Encontrar a soma de todos o naturais multiplos de 3 ou 5 menores que 1000

s = 0

for i in range(1000):
    if (i % 3) == 0 or (i % 5) == 0:
        s = s + i

print(s)