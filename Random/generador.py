# GENERADOR CONGRUENIAL LINEAL
n = 100 #Cantidad de números a generar
a = 23 #Numero impar que no sea multiplo de 3 o 5
m = 7883
x = 787
c = 7
numeros = []
for i in range(n):
    r = (a*x + c)
    r = r % m
    x = r
    r = r / m
    if not(r in numeros):
        print(r)
        numeros.append(r)
    else:
        print("Se repitio despues de " + str(i))
        break
