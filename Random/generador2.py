vector = [827 , 941, 1123 , 1373, 379 , 431 ,541]
n = 100
m = 98257
numeros = []
index = 0
for i in range(n):
    if(index != 5):
        r = vector[index] * vector[index+1] % m
        vector[index] = r
        r /= m
        index += 1
        if not(r in numeros):
            print(r)
            numeros.append(r)
        else:
            print("Se repitieron despues de " + str(i) + " numeros generados")
            break
    else:
        r = vector[index]* vector[0] % m
        vector[index] = r
        r /= m
        index = 0
        if not(r in numeros):
            print(r)
            numeros.append(r)
        else:
            print("Se repitieron despues de " + str(i) + " numeros generados")
            break
