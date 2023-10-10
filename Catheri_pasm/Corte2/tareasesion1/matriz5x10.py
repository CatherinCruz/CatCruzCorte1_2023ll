#  matriz de 5x10 https://www.youtube.com/watch?v=FdP0Yz1TaPs 
matriz = [[0] * 10 for _ in range(5)]

matriz[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matriz[1] = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
matriz[2] = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
matriz[3] = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
matriz[4] = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

print("Matriz creada:")
for fila in matriz:
    print(fila)

numero_mas_alto = float('-inf')
numero_mas_bajo = float('inf')
posicion_mas_alto = None
posicion_mas_bajo = None

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > numero_mas_alto:
            numero_mas_alto = matriz[i][j]
            posicion_mas_alto = (i,j)
        if matriz[i][j] < numero_mas_bajo:
            numero_mas_bajo = matriz[i][j]
            posicion_mas_bajo = (i,j)

print(f"\nNúmero más alto: {numero_mas_alto} en la posición {posicion_mas_alto}")
print(f"Número más bajo: {numero_mas_bajo} en la posición {posicion_mas_bajo}")

matriz_organizada = sorted([num for fila in matriz for num in fila], reverse=True)
matriz_organizada = [matriz_organizada[i:i+10] for i in range(0,len(matriz_organizada),10)]

print("\nMatriz organizada:")
for fila in matriz_organizada:
    print(fila)