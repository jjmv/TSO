import sys
import csv

total = 0
valores_estudiantes =[]

try:
    archivo_valores = open("Tarea.csv","r") #Se abre el archivo que contiene los datos
    reader = csv.reader(archivo_valores)
    for i in reader:
        valores_estudiantes.append(i)
    archivo_valores.close()

except IOError:
    print("Error al abrir el archivo")
    sys.exit(1)

combinacion_optima = []
datos = [[0 for x in range(len(valores_estudiantes))] for y in range(len(valores_estudiantes))]

for i in range(len(valores_estudiantes)):
    for j in range(len(valores_estudiantes)):
        datos[i][j] = int(valores_estudiantes[i][j])

reacomodo = []
chosen_list = []

for i in range(len(valores_estudiantes)):
    for j in range(len(valores_estudiantes)):
        if(datos[i][j] == 0):
            nuevalista = datos[i]
            reacomodo.append(nuevalista)
            if not(i in chosen_list):
                chosen_list.append(i)
                break
            break
j = 0

for i in range(len(valores_estudiantes)):
    j = 0
    for t in range(len(chosen_list)):
        if(datos[i] == reacomodo[t]):
            j = j + 1
    if(j == 0):
        reacomodo.append(datos[i])

if(len(reacomodo) != 0):
    datos = reacomodo

taken = []

for i in range(len(valores_estudiantes)):
    for j in range(len(valores_estudiantes)):
        if not(j in taken) and(datos[i][j] != 0):
            menor = datos[i][j]
            qwer = j
            break
    for j in range(len(valores_estudiantes)):
        if((datos[i][j] < menor ) and not(j in taken) and(datos[i][j] != 0)):
            menor = datos[i][j]
            qwer = j

    total += menor
    combinacion_optima.append(menor)
    taken.append(qwer)
    print("Al estudiante " + str(i + 1) + " se le asgina la tarea " + str(qwer + 1))
print("El tiempo optimo es " + str(total))
