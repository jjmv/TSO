import time
import math
import sys

solucion_inicial = []
suma_distancia_inicial = 0
breaker = False
movimiento = []
contador = 0

print("\nIngrese el nombre del archivo [Clase],[Caso1],[Caso2]....[Caso'n']")
nombre = input() + ".txt"
valores_objetos = []

try:
    archivo_valores = open(nombre, "r")
    reader = archivo_valores.readlines()
    reader.pop(0)
    for i in reader:
        var = i.split()
        valores_objetos.append(var)
    archivo_valores.close()

except IOError:
    print("Error al abrir el archivo")
    sys.exit(1)
start_time = time.clock()

#Lista vacia con distancias en 0
distancias = [[float(0) for i in range(len(valores_objetos))]for j in range(len(valores_objetos))]

#Declarar función para sacar distancia euclidiana
def euclidiana(i,j):
    if(i != j):
        cua= float(0)
        suma = float(0)
        distancia = float(0)
        for x in range(len(valores_objetos[0])-1):
            resta = float(valores_objetos[i][x+1]) - float(valores_objetos[j][x+1])
            cua = resta ** 2
            suma = suma + cua
        suma = math.sqrt(suma)
        distancias[i][j] = suma

"""
#Función para calcular la arista mas pesada
def arista_max():
    global mayor,nodo1,nodo2,cambio_nodos,indice1,indice2
    mayor = aristas[1]
    for x in range(len(aristas)-3):
        if(aristas[x+2] > mayor):
            mayor = aristas[x+2]
            nodo1 = solucion_inicial[x+2]
            nodo2 = solucion_inicial[x+3]
            indice1 = x+2
            indice2 = x+3
    cambio_nodos = solucion_inicial
    cambio_nodos.pop(indice2)
    cambio_nodos.pop(indice1)

"""

def vecino_cercano():
    global solucion_inicial
    solucion_inicial.append(0)
    taken = []
    taken.append(0)
    indice = 0
    vecino = 0
    #Calculo de la solucion inicial (aun sin hacer el movement)
    for i in range(len(distancias)):
        menor = max(distancias[indice])
        for j in range(len(distancias)):
            if(distancias[indice][j] < menor) and(j not in taken) and (distancias[indice][j] != 0):
                menor = distancias[indice][j]
                vecino = j
        if(i == (len(distancias)-1)):
            break
        indice = vecino
        taken.append(vecino)
        solucion_inicial.append(vecino)
    solucion_inicial.append(0)

def movement():
    global solucion_inicial,movimiento, contador
    movimiento = solucion_inicial
    while(contador < 1000):
        








#Ejecucion de la función para calcular distancias
for i in range(len(valores_objetos)):
    for j in range(len(valores_objetos)):
        euclidiana(i,j)
#Ejecucion de funcion para el método vecino mas cercano e impresión de la solución inicial.
vecino_cercano()
movement()
print(movimiento)
print(solucion_inicial)
