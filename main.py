print("\t\t\tMULTIPLICACIÓN DE MATRICES")
print("Kevin Daniel Pulupa")
#Numero de filas de las matrices deben ser iguales
filas =int(input("ingresa el numero de filas: "))
#Columna de la matriz 1
colum1= int(input("Ingrese el numero de columnas de la matriz 1: "))
#Columna de la matriz 1
colum2 =int (input("Ingrese el numero de columnas de la matriz 2: "))
#Creacion de la Matriz 1
print ("\t\t\t\t Matriz 1 ")
M1=[]
for i in range (filas):
    M1.append ([0]*colum1)
    print (M1[i])
#Creacion de la Matriz 2 
print ("\t\t\t\t Matriz 2 ")

M2=[]
for i in range (colum1):
    M2.append ([0]*colum2)
    print (M2[i])

print ("Ingresa los valores de la primera matriz")

#Intercambio de valores en la primera matriz 1
for i in range (filas):
    for j in range (colum1):
        M1[i][j]=float(input("Llena los datos de la posición (%d, %d): "  %(i,j)))
print("\t\t\t\t matriz1")
for i in range (filas):
    print (M1[i])

print ("Ingresa los valores de la segunda matriz") 

#Intercambio de valores en la primera matriz 2

for i in range (colum1):
    for j in range (colum2):
        M2[i][j]=float(input("Ingrese los valores en (%d,%d) : " %(i,j)))

print ("\t\t\t\t Matriz 2")
for i in range (colum1):
    print (M2[i])

print ("\t\t\t\t MULTIPLICACIÓN") 
#Matriz de resultado
R=[]
for i in range (filas):
    R.append([0]*colum2)
    
#MULTIPLICACION
for i in range (filas):
    for j in range (colum2):
            for k in range (colum1):
                R[i][j] += M1 [i] [k] * M2 [k] [j]

for i in range (filas):
    M=[]
    for j in range (colum2):
        M.append(R[i][j])
    print (M)
