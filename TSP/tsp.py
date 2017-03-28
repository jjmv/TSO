import time
import math

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

#Ejecucion del método para sacar distancias euclidianas
for i in range(len(valores_objetos)):
    for j in range(len(valores_objetos)):
        euclidiana(i,j)

#Calcular promedios de distancias correspondiente a cada nodo
"""
promedios = []
for i in range(len(distancias)):
    suma = 0
    for j in range(len(distancias[i])):
        suma += distancias[i][j]
    promedio = suma / len(distancias[i])
    promedios.append(promedio)


#Sacar el promedio mas feo (el mas grande en este caso)
ciudad_inicial = 0
promedio_feo = promedios[0]
for i in range(len(promedios)):
    if(promedios[i] > promedio_feo):
        promedio_feo = promedios[i]
        ciudad_inicial = i
"""
ciudad_inicial = 0

solucion_inicial = []
solucion_inicial.append(ciudad_inicial)
taken = []
taken.append(ciudad_inicial)
indice = ciudad_inicial

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
solucion_inicial.append(ciudad_inicial)

###########################################################
aristas = []
print(solucion_inicial)
suma_distancia_inicial = 0
for i in range(len(solucion_inicial)-1):
    suma_distancia_inicial += distancias[solucion_inicial[i]][solucion_inicial[i+1]]
    aristas.append(distancias[solucion_inicial[i]][solucion_inicial[i+1]])



mayor = aristas[1]
nodo1 = 0
nodo2 = 0
cambio_nodos = []
indice1 = 0
indice2 = 0

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

contador = 0
arista_max()
nuevas_aristas = []
suma_vieja = suma_distancia_inicial
breaker = False
#Inicio del movement
while(contador < 1000):
    for i in range(len(distancias)-2):
        for j in range(len(distancias)-2):
            nueva_suma = 0
            nuevas_aristas = []
            cambio_nodos.insert(i+1,nodo1)
            cambio_nodos.insert(j+1,nodo2)
            for k in range(len(distancias)):
                nueva_suma += distancias[cambio_nodos[k]][cambio_nodos[k+1]]
                nuevas_aristas.append(distancias[cambio_nodos[k]][cambio_nodos[k+1]])
            if(nueva_suma < suma_distancia_inicial):
                suma_distancia_inicial = nueva_suma
                aristas = nuevas_aristas
                solucion_inicial = cambio_nodos
                arista_max()
                contador = 0
            else:
                contador += 1
                arista_max()
                if(contador == 1000):
                    break
                    breaker = True
        if(breaker == True):
            break

tiempo = time.clock() - start_time
print("La distancia encontrada es:" + str(suma_distancia_inicial))
if(suma_distancia_inicial < suma_vieja):
    print("Se encontró una mejora con una distancia de: " + str(suma_distancia_inicial))
else:
    print("No se encontró ninguna mejora")
print("Tiempo de ejecución:" + str(tiempo))
