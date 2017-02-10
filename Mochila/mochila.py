import sys
import csv
import time

start_time = time.clock()
print("\nIngrese el nombre del archivo [Clase],[Caso1],[Caso2]....[Caso'n']")
nombre = input() + ".csv"
valores_objetos = []
try:
    archivo_valores = open(nombre, "r")
    reader = csv.reader(archivo_valores)
    for i in reader:
        valores_objetos.append(i)
    archivo_valores.close()

except IOError:
    print("Error al abrir el archivo")
    sys.exit(1)

valores_objetos[0].pop(0)
capacidad = int(valores_objetos[0][0])

for i in range(2):
    valores_objetos.pop(0)

objetos = [["." for i in range(3)] for i in range(len(valores_objetos))]
for i in range(len(valores_objetos)):
    objetos[i][0] = str("Objeto N")

for i in range(len(valores_objetos)):
    objetos[i][0] = valores_objetos[i][0]
    for j in range(2):
        objetos[i][j+1] = int(valores_objetos[i][j+1])

promedio = 0
for i in range(len(objetos)):
    promedio += objetos[i][1]
promedio = promedio / (len(objetos))
print("La capacidad máxima es: " + str(capacidad))
lista_no_excede = []
lista_excede_promedio= []
for i in range(len(objetos)):
    if(objetos[i][1] <= promedio):
        valor = objetos[i]
        lista_no_excede.append(valor)
    else:
        valor = objetos[i]
        lista_excede_promedio.append(valor)
lista_reordenada = []
taken = []
rango = len(lista_no_excede)
indicador = 0
while(rango != 0):
    for i in range(len(lista_no_excede)):
        mayor = 0
        for j in range(len(lista_no_excede)):
            if(lista_no_excede[j][2] > mayor) and not(j in taken):
                indicador = j
                mayor = lista_no_excede[j][2]
                valor = lista_no_excede[j]
    taken.append(indicador)
    lista_reordenada.append(valor)
    rango -= 1
rango = len(lista_excede_promedio)
indicador = 0
taken2 = []
menor = 0
while(rango != 0):
    for i in range(len(lista_excede_promedio)):
        for w in range(len(lista_excede_promedio)):
            if not(w in taken2):
                menor = lista_excede_promedio[w][1]
                valor = lista_excede_promedio[w]
                indicador = w

        for j in range(len(lista_excede_promedio)):
            if(lista_excede_promedio[j][1] < menor) and not(j in taken2):
                indicador = j
                menor = lista_excede_promedio[j][1]
                valor = lista_excede_promedio[j]
    taken2.append(indicador)
    lista_reordenada.append(valor)
    rango -= 1

peso = 0
beneficio = 0
aceptados = 0
contador = 0
for i in range(len(lista_reordenada)):
    if(peso <= capacidad):
        contador += 1
        peso += lista_reordenada[i][1]
    else:
        break
contador -= 1
peso = 0
for i in range(contador):
    peso += lista_reordenada[i][1]
    beneficio += lista_reordenada[i][2]
print("Los objetos en la mochila son: \n")
for i in range(contador):
    print(lista_reordenada[i][0] + " con un peso de objeto de " + str(lista_reordenada[i][1]) + " y con un beneficio de " + str(lista_reordenada[i][2]))
print("\n Con un peso en la mochila de " + str(peso) + " y un beneficio maximo de " + str(beneficio))
tiempo = time.clock() - start_time
print ("Tiempo de ejecución : " + str(tiempo))
