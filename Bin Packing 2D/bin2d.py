import sys
import csv
import random
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

solucion_secciones = []
anchura = 90
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
solucion_multi_move = []

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
        if(contador == 1000):
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
    altura_multiarranque = []
    local_taken_secciones = []
    while(len(soluciones_multiarranque) < 200):
        # Comienzan a generarse las soluciones
        solucion = []
        solucion_multi_move = []
        anchura_disponible_secciones = []
        anchura_disponible = anchura
        local_taken_secciones = []
        seccion = []
        while(len(local_taken_secciones) < len(lista_ordenada)):
            mayor = 0
            id_candidatos = []
            posibles_inserts = []
            #Sección vacia
            #Posibles candidatos
            for i in range(len(lista_ordenada)):
                if(len(posibles_inserts) == 3):
                    break
                if not(i in local_taken_secciones):
                    insercion = lista_ordenada[i]
                    posibles_inserts.append(insercion)
                    id_candidatos.append(i)
            #Selecciono al candidato
            aleatorio = random.randrange(len(posibles_inserts))
            #Creacion de secciones
            if(posibles_inserts[aleatorio][0] <= anchura_disponible) and not(id_candidatos[aleatorio] in local_taken_secciones):
                valor1 = id_candidatos[aleatorio]
                valor = posibles_inserts[aleatorio]
                seccion.append(valor)
                anchura_disponible -= posibles_inserts[aleatorio][0]
                local_taken_secciones.append(valor1)
                if(len(local_taken_secciones) == len(lista_ordenada)):
                    st = []
                    seccion_ordenada = []
                    for i in range(len(seccion)):
                        for j in range(len(seccion)):
                            if not (j in st):
                                mayor = seccion[j][1]
                                indice_mayor = j
                                break
                        for j in range(len(seccion)):
                            if(seccion[j][1] > mayor) and not(j in st):
                                mayor = seccion[j][1]
                                indice_mayor = j
                        add = seccion[indice_mayor]
                        seccion_ordenada.append(add)
                        st.append(indice_mayor)
                    solucion.append(seccion_ordenada)
                    solucion_multi_move.append(seccion_ordenada)
            else:
                st = []
                seccion_ordenada = []
                for i in range(len(seccion)):
                    for j in range(len(seccion)):
                        if not (j in st):
                            mayor = seccion[j][1]
                            indice_mayor = j
                            break
                    for j in range(len(seccion)):
                        if(seccion[j][1] > mayor) and not(j in st):
                            mayor = seccion[j][1]
                            indice_mayor = j
                    add = seccion[indice_mayor]
                    seccion_ordenada.append(add)
                    st.append(indice_mayor)

                solucion.append(seccion_ordenada)
                solucion_multi_move.append(seccion_ordenada)
                seccion = []
                anchura_disponible_secciones.append(anchura_disponible)
                anchura_disponible = anchura
        soluciones_multiarranque.append(solucion)

    menor_altura = 0
    menor_indice = 0
    for i in range(len(soluciones_multiarranque[0])):
        menor_altura += soluciones_multiarranque[0][i][0][1]

    for i in range(len(soluciones_multiarranque)):
        altura = 0
        for j in range(len(soluciones_multiarranque[i])):
            altura = altura + soluciones_multiarranque[i][j][0][1]
        if(altura < menor_altura):
            menor_altura = altura
            menor_indice = i

    if(menor_altura < altura1):
        print("Se encontró mejora en la solucion: " + str(menor_indice+1))
        for j in range(len(soluciones_multiarranque[menor_indice])):
            print(soluciones_multiarranque[menor_indice][j])
        print("Altura encontrada fue :" +str(menor_altura))
    else:
        print("La mejor altura encontrada fue con multiarranque fue: " + str(altura1))

### MAIN ###
start_time = time.clock()
iniciación()
generador()
tiempo_constructivo = time.clock() - start_time
movement()
tiempo_movimiento = time.clock() - start_time
multiarranque()
tiempo_multiarranque = time.clock() - start_time

print("")
print("El tiempo en el constructivo fue: " + str(tiempo_constructivo))
print("El tiempo en el movimiento fue: " + str(tiempo_movimiento))
print("El tiempo en el multiarranque fue: " + str(tiempo_multiarranque))
