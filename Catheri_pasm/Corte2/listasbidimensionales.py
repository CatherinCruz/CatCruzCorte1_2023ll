from random import randint as r

def main(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(r(1,10))

        print(matriz[i])




if __name__=='__main__':
    filas=int(input('ingrese el numero de filas:'))
    columnas=int(input('ingrese el numero de columnas:'))
    main(filas, columnas)