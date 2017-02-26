import sys
import csv
import time

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

start_time = time.clock()

capacidad = int(valores_objetos[0][1])
valores_objetos.pop(0)
valores_objetos.pop(0)

objetos = [[0 for i in range(2)] for i in range(len(valores_objetos))]
for i in range(len(valores_objetos)):
    for j in range(2):
        objetos[i][j] = int(valores_objetos[i][j])
lista_reaordenada = []
taken = []
for w in range(len(objetos)):
    for i in range(len(objetos)):
        if not(i in taken):
            mayor = objetos[i][1]
            indice_mayor = i
            break
    for i in range(len(objetos)):
        if(objetos[i][1]>mayor) and not(i in taken):
            mayor = objetos[i][1]
            indice_mayor = i
    taken.append(indice_mayor)

for i in range(len(objetos)):
    valor = objetos[taken[i]]
    lista_reaordenada.append(valor)

discos = []
taken = []
while(len(taken) < len(lista_reaordenada)):
    auxiliar = []
    peso_usado = 0
    peso_disponible = capacidad
    for w in range(len(lista_reaordenada)):
        if(lista_reaordenada[w][1] <= peso_disponible)and not(w in taken):
            valor = lista_reaordenada[w]
            auxiliar.append(valor)
            peso_usado += auxiliar[w][1]
            peso_disponible -= lista_reaordenada[w][1]
            taken.append(w)
        else:
            
            break
    discos.append(auxiliar)

print(discos)
