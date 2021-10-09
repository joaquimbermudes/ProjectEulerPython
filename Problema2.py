# Problema 2
# Encontrar a soma de todos os valores pares de uma sequencia de Fibonacci até 4.000.000

x1 = 1
x2 = 1
x = 0
s = 0

while x < 4000000:
    x = x1 + x2
    x2 = x1
    x1 = x
    if x % 2 == 0:
        s = s + x

print(s)
