def dos():
    for i in range (len(cadena)):
        print(cadena[i],'valor de i:', i)
def main2(cadena):
    for i in cadena:
        print(i)

def main3(cadena):
    i=0
    while i<(cadena):
        print(f'{cadena[i]}, valor de i:{i}')
        i+=1

if __name__=='__main__':
    cadena='Hola Mundo!'
    main2(cadena)
    main3(cadena)
    dos(cadena)