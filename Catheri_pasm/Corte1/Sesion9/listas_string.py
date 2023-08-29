#los arreglos son inalterables y las lustas si se pueden alterar.
#los arreglos inician desde 1 y las listas desde 0.
def dos():
    for i in range (len(cadena)):
        print(cadena[i],'valor de i:', i)
def main2(cadena):
    for i in cadena:
        print(i)


if __name__=='__main__':
    cadena='Hola Mundo!'
    #main2(cadena)
    dos(cadena)