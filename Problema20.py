## Econtrar a soma dos dígitos de 100!

a = 1
for i in range(1,100):
    a = a * i

a = str(a)
b = 0
for j in a:
    b = b + int(j)

print(b)