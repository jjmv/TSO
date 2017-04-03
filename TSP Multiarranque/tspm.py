import time
import math
import sys
import random

solucion_inicial = []
suma_distancia_inicial = 0
suma_evaluadora = 0
movimiento = []
contador = 0
soluciones_sumas = [0 for i in range(200)]
soluciones_multiarranque = [[] for i in range(200)]
solucion_multiarranque_menor = 0
movimiento = solucion_inicial

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

def vecino_cercano():
    global solucion_inicial, suma_distancia_inicial
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
    for j in range(len(solucion_inicial)-1):
        suma_distancia_inicial += distancias[solucion_inicial[j]][solucion_inicial[j+1]]
    print(suma_distancia_inicial)



def movement():
    global solucion_inicial, suma_evaluadora, suma_distancia_inicial,movimiento
    terminar = False
    iterar = True
    contador = 0
    while(iterar == True):
        for i in range(len(distancias)-2):
            for j in range(len(distancias)-2):
                #indicador1 = movimiento[i+1]
                #indicador2 = movimiento[i+2]
                indicadores = []
                indicadores.append(movimiento[i+1])
                indicadores.append(movimiento[i+2])
                #print(indicadores)
                movimiento.pop(i+1)
                movimiento.pop(i+1)
                #movimiento.insert(j+1, indicador2)
                #movimiento.insert(j+1, indicador1)
                movimiento[j+1:j+1] = indicadores
                suma_evaluadora = 0
                #print(movimiento)
                for k in range(len(movimiento)-1):
                    suma_evaluadora += distancias[movimiento[k]][movimiento[k+1]]
                #print(suma_evaluadora)
                if(suma_evaluadora < suma_distancia_inicial):
                    suma_distancia_inicial = suma_evaluadora
                    #solucion_inicial = movimiento
                    contador = 0
                else:
                    contador += 1
                    #movimiento = solucion_inicial
                    print(solucion_inicial)
                    if(contador == 10):
                        terminar = True
                        break
            if(terminar == True):
                break
        iterar = False


def multiarranque():
    global solucion_inicial, solucion_multiarranque_menor
    for i in range(200):
        soluciones_multiarranque[i].append(0)
    for q in range(200):
        while(len(soluciones_multiarranque[q]) < len(distancias)):
            posibles_vecinos = []
            for i in range(len(distancias)):
                if not(i in soluciones_multiarranque[q]):
                    menor = distancias[soluciones_multiarranque[q][len(soluciones_multiarranque[q])-1]][i]
                    mayor = menor
                    break
            for i in range(len(distancias)):
                if not(i in soluciones_multiarranque[q]) and(distancias[soluciones_multiarranque[q][len(soluciones_multiarranque[q])-1]][i] < menor):
                    menor = distancias[soluciones_multiarranque[q][len(soluciones_multiarranque[q])-1]][i]
                if not(i in soluciones_multiarranque[q]) and(distancias[soluciones_multiarranque[q][len(soluciones_multiarranque[q])-1]][i] > mayor):
                    mayor = distancias[soluciones_multiarranque[q][len(soluciones_multiarranque[q])-1]][i]
            maximo = menor + .3 *(mayor - menor)
            for j in range(len(distancias)):
                if not(j in soluciones_multiarranque[q]) and(distancias[soluciones_multiarranque[q][len(soluciones_multiarranque[q])-1]][j] <= maximo):
                    posibles_vecinos.append(j)
            aleatorio = random.randint(0,len(posibles_vecinos)-1)
            soluciones_multiarranque[q].append(posibles_vecinos[aleatorio])
    for q in range(200):
        soluciones_multiarranque[q].append(0)
        for j in range(len(soluciones_multiarranque[q])-1):
            soluciones_sumas[q] += distancias[soluciones_multiarranque[q][j]][soluciones_multiarranque[q][j+1]]
    solucion_multiarranque_menor = min(soluciones_sumas)


#############################   Aqui comienza el "MAIN"   #############################
#Ejecucion de la función para calcular distancias
for i in range(len(valores_objetos)):
    for j in range(len(valores_objetos)):
        euclidiana(i,j)
############################# Necesario para correr las pruebas ########################
#Ejecucion de funcion para el método vecino mas cercano e impresión de la solución inicial.
vecino_cercano()
movement()
#multiarranque()
print("La distancia inicial con movimimiento es: " + str(suma_distancia_inicial))
#if(solucion_multiarranque_menor < suma_distancia_inicial):
#    print("Se encontró mejora con multiarranque con distancia: " + str(solucion_multiarranque_menor))
#else:
#    print("Nel")
