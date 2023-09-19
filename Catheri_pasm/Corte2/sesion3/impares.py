#se llama varias veces ella misma.lista de recursion
def impar(x):
    if x>0:
        num=(2*x+1)+impar(x-1)
        return num
    else:
        return 1

def main ():
    num=int(input('ingrese el numero: '))
    resultado=impar(num)
    print(f'el resultadoes: {resultado}')
    #impar(num)

if __name__=='__main__':
    main()