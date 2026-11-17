#Array
precio= [0] * 7

#Limpiar Array precio
for j in range(7):
    precio[j] = 0

#Cargar datos Precio Producto Tecnológicos
j=0

while j < 7:
    pre= float(input("Ingrese precio: "))
    precio[j]= pre
    j= j + 1

#Descarga del array
i=0

while i < 7:
    print(i + 1,precio[i])
    i = i + 1

