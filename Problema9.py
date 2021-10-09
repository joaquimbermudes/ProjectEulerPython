# Problema 9
# Encontrar 3 naturais triplo pitagórico que somem 1000 e multiplica-los
#ab(1000-a-b) = ab1000 - ba**2 - ab**2
#a**2 + b**2 - a**2 - 2ab + 2000a - b**2 + 2000b - 1000000 = 0


for a in range(1000):
    for b in range(1000):
        if (a**2 + b**2 == (1000 - a - b)**2):
            print(a*b*1000 - b*(a**2) - a*(b**2))


