import sys
import csv

total = 0
valores_estudiantes = []
print("Ingrese el nombre del archivo [Clase2],[Tarea2],[Tarea2SinCeros]")
nombre = input() + ".csv"

try:
    archivo_valores = open(nombre, "r")
    reader = csv.reader(archivo_valores)
    for i in reader:
        valores_estudiantes.append(i)
    archivo_valores.close()

except IOError:
    print("Error al abrir el archivo")
    sys.exit(1)

demandas = []
for i in range(len(valores_estudiantes)-1):
    demandas.append(int(valores_estudiantes[0][i]))


eliminacion = 0
valores_estudiantes.pop(eliminacion)

datos = [[0 for x in range(len(valores_estudiantes)+2)] for y in range(len(valores_estudiantes))]

for i in range(len(valores_estudiantes)):
    for j in range(len(valores_estudiantes)+2):
        datos[i][j] = int(valores_estudiantes[i][j])

for i in range(len(valores_estudiantes)):
    if(datos[i][-2] == 0):
        datos[i][-2] = 1

taken = [[]for i in range(len(valores_estudiantes))]
max_controller = []
for i in range(len(valores_estudiantes)):
    max_controller.append(datos[i][-1])

contador = [0 for i in range(len(valores_estudiantes))]

for i in range(len(valores_estudiantes)):
    for w in range(datos[i][-2]):
        for j in range(len(valores_estudiantes)):
            if not(j in taken[i]) and(datos[i][j] != 0) and(demandas[j] != 0):
                menor1 = datos[i][j]
                qwer = j
                break
        for z in range(len(valores_estudiantes)):
            if((datos[i][z] < menor1 ) and not(z in taken[i]) and(datos[i][z] != 0) and(demandas[z] != 0)):
                menor1 = datos[i][z]
                qwer = z
        demandas[qwer] -= 1
        total += menor1
        taken[i].append(qwer)
        contador[i] += 1

demand_controller = 0
for i in range(len(demandas)):
    demand_controller += demandas[i]

if(demand_controller != 0):
    for i in range(len(valores_estudiantes)):
        for w in range(demandas[i]):
            for j in range(len(valores_estudiantes)):
                if(demandas[i] != 0) and(datos[j][i] != 0) and not(i in taken[j]) and(max_controller[j] > contador[j]):
                    menor1 = datos[j][i]
                    qwer = j
                    break
            for z in range(len(valores_estudiantes)):
                if(datos[z][i] < menor1) and not(i in taken[z]) and(datos[z][i] != 0) and(max_controller[z] > contador[z]):
                    menor1 = datos[z][i]
                    qwer = z
            total += menor1
            taken[qwer].append(i)
            contador[qwer] += 1

for i in range(len(taken)):
    for j in range(len(taken[i])):
        print("Al estudiante " + str(i+1) + " Se le asigna la tarea " + str(taken[i][j]+1))

print("\n Dando un tiempo factible de " + str(total))
