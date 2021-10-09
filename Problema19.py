## Quantos domingos aconteceram no primeiro dia do mês no século XX

Dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

posicao= 0
passos = 0

def IsDomingo(x):
    a = False
    if x == "Domingo":
        a = True
    return a

final = 1

for i in range(1901, 2001):
    for j in range(1,13):
        if (i%4 == 0) and (j == 2) and (i != 100):
            passos = 1

        elif (i%4 != 0) and (j == 2):
            passos = 0

        elif (j in [1, 3, 5, 7, 8, 10, 12]) == True:
            passos = 3

        elif (j in [4, 6, 9, 11]) == True:
            passos = 2

        if posicao + passos > 6:
            posicao = posicao + passos - 7
        else:
            posicao = posicao + passos 

        if IsDomingo(Dias[posicao]) == True:
            final = final + 1


print(final)
