# array de cantidad de personas por 25 distritos de Lima
pers_dist = [j]

# array con los nombres de los 25 distritos
Nomb = [j]

# carga del array de personas
for j in range(25):
    canti = int(input("Ingrese la cantidad de personas: "))
    pers_dist[j]=cant
    print(j+1, " : ", pers_dist[j])

# carga del array de nombres de distritos
for i in range(25):
    Nombre = input("Ingrese el nombre de cada distrito: ")
    Nomb[i]= Nombre
    print(i+1, " : ", Nomb[i])

# hallando el total de personas de los 25 distritos
Total_dist = 0
for j in range(25):
    canti=int(input("Ingrese la cantidad de personas"))
    pers_dist[j]=canti
    Total_dist = Total_dist + pers_dist[j]
print(j+1,"Total de personas por los 25 distritos: ", Total_dist)

# TAREA 2: descargar (mostrar) el array de personas por 25 distritos
print("Personas por distrito:")
for j in range(25):
    print(j+1, " - ", Nomb[j], " : ", pers_dist[j])

# TAREA 3: distrito con más y con menos población
mayor = pers_dist[0]
menor = pers_dist[0]
pos_mayor = 0
pos_menor = 0

for j in range(25):
    if pers_dist[j] > mayor:
        mayor = pers_dist[j]
        pos_mayor = j
    if pers_dist[j] < menor:
        menor = pers_dist[j]
        pos_menor = j

print("Distrito con más población: ", Nomb[pos_mayor], " con ", mayor, " personas")
print("Distrito con menos población: ", Nomb[pos_menor], " con ", menor, " personas")