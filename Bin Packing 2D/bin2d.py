import sys
import csv
import random


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

solucion_secciones = []
anchura = 24
iteraciones = 0
taken = []
mayor = 0
altura1 = 0
lista_ordenada = []
taken_secciones = []
seccion = []
contador = 1
solucion_movimiento = []
anchura_disponible_secciones = []
soluciones_multiarranque = []


def iniciación():
    global lista_ordenada
    ###Definición de ancho del bin ###

    ancho = 90

    ### Etapa de ordenamiento y reacomodo  ###

    for i in range(5):
        valores_objetos.pop(0)
    lista_ordenada = [[] for i in range(len(valores_objetos))]
    valores_formato = [[0 for j in range(2)]for x in range(len(valores_objetos))]

    for i in range(len(valores_objetos)):
        for j in range(2):
            valores_formato[i][j] = int(valores_objetos[i][j])

    for i in range(len(valores_formato)):
        if(valores_formato[i][0] < valores_formato[i][1]):
            valores_formato[i][0] = int(valores_objetos[i][1])
            valores_formato[i][1] = int(valores_objetos[i][0])

    for i in range(len(valores_objetos)):
        for j in range(len(valores_objetos)):
            if not (j in taken):
                mayor = valores_formato[j][1]
                indice_mayor = j
                break
        for j in range(len(valores_formato)):
            if(valores_formato[j][1] > mayor) and not(j in taken):
                mayor = valores_formato[j][1]
                indice_mayor = j
        taken.append(indice_mayor)
        lista_ordenada[i] = valores_formato[indice_mayor]

def generador():
    global anchura, taken_secciones, lista_ordenada, solucion_movimiento,altura1, anchura_disponible_secciones
    altura1 = 0
    while(len(taken_secciones) < len(lista_ordenada)):
        seccion = []
        anchura_disponible = anchura
        for i in range(len(lista_ordenada)):
            if(lista_ordenada[i][0] < anchura_disponible) and not(i in taken_secciones):
                a_agregar = lista_ordenada[i]
                seccion.append(a_agregar)
                taken_secciones.append(i)
                anchura_disponible -= lista_ordenada[i][0]
        solucion_secciones.append(seccion)
        solucion_movimiento.append(seccion)
        anchura_disponible_secciones.append(anchura_disponible)
        altura1 += seccion[0][1]
        print(seccion)
    print("La altura utilizada en el constructivo fue " + str(altura1))


def movement():
    global solucion_secciones, solucion_movimiento, anchura,anchura_disponible_secciones,altura1
    iterar = True
    contador = 0
    breaker = False
    altura2 = 0
    for i in range(len(solucion_movimiento)-1):   #i son mis secciones
        # INDICADOR DE LA ALTURA MAS GRANDE DE LA SECCION
        indicador = (i+1) * -1
        mayor_altura = solucion_movimiento[indicador][0][1]
        movidos = []
        if(breaker == True):
            break
        for j in range(len(solucion_secciones[i])):    #j son mis tablas
            if(solucion_movimiento[indicador][j][1] == mayor_altura) and (solucion_movimiento[indicador][j][0] <= anchura_disponible_secciones[indicador-1]):
                variable = solucion_movimiento[indicador][j]
                solucion_movimiento[indicador-1].append(variable)
                anchura_disponible_secciones[indicador-1] -= solucion_movimiento[indicador][j][0]
                movidos.append(j)
            else:
                contador += 1
                break
        for m in range(len(movidos)):
            valor = movidos[m]
            solucion_movimiento[indicador].pop(valor)
        if(contador == 100):
            breaker = True
    for i in range(len(solucion_movimiento)):
        altura2 += solucion_movimiento[i][0][1]
    if(altura2 < altura1):
        print("Se encontró mejora con movimiento")
        print("Nueva Altura: " + str(altura2))
        for i in range(len(solucion_movimiento)):
            print(solucion_movimiento[i])
    else:
        print("Movement no mejoró nada")

def multiarranque():
    global lista_ordenada,anchura, altura1,soluciones_multiarranque
    for i in range(len(lista_ordenada)):
        lista_ordenada[i].append(i)
    altura_multiarranque = []
    local_taken_secciones = []
    #while(len(soluciones_multiarranque) < 200):
    # Comienzan a generarse las soluciones
    solucion = []
    solucion_multi_move = []
    anchura_disponible_secciones = []
    seccion = []
    anchura_disponible = anchura
    while(len(local_taken_secciones) != len(lista_ordenada)):
        posibles_inserts = []
        #Sección vacia
        #Posibles candidatos
        for i in range(len(lista_ordenada)):
            if(len(posibles_inserts) == 3):
                break
            if not(i in local_taken_secciones):
                insercion = lista_ordenada[i]
                posibles_inserts.append(insercion)
        #Selecciono al candidato
        aleatorio = random.randrange(len(posibles_inserts))
        #Creacion de secciones
        if(posibles_inserts[aleatorio][0] <= anchura_disponible) and not(posibles_inserts[aleatorio][2] in local_taken_secciones):
            valor = posibles_inserts[aleatorio]
            seccion.append(valor)
            anchura_disponible -= posibles_inserts[aleatorio][0]
            valor = posibles_inserts[aleatorio][2]
            local_taken_secciones.append(valor)
        else:
            solucion.append(seccion)
            seccion = []
            anchura_disponible_secciones.append(anchura_disponible)
            anchura_disponible = anchura
    print("")
    print("La solucion multiarranque es")
    print(solucion)




"""
            iterar = True
            contador = 0
            breaker = False
            altura2 = 0
            for i in range(len(solucion_multi_move)-1):   #i son mis secciones
                # INDICADOR DE LA ALTURA MAS GRANDE DE LA SECCION
                indicador = (i+1) * -1
                mayor_altura = solucion_multi_move[indicador][0][1]
                movidos = []
                if(breaker == True):
                    break
                for j in range(len(solucion[i])):    #j son mis tablas
                    if(solucion_multi_move[indicador][j][1] == mayor_altura) and (solucion_multi_move[indicador][j][0] <= anchura_disponible_secciones[indicador-1]):
                        variable = solucion_multi_move[indicador][j]
                        solucion_multi_move[indicador-1].append(variable)
                        anchura_disponible_secciones[indicador-1] -= solucion_multi_move[indicador][j][0]
                        movidos.append(j)
                    else:
                        contador += 1
                        break
                for m in range(len(movidos)):
                    valor = movidos[m]
                    solucion_multi_move[indicador].pop(valor)
                if(contador == 100):
                    breaker = True
        soluciones_multiarranque.append(solucion_multi_move)

"""
### MAIN ###
iniciación()
generador()
movement()
multiarranque()
