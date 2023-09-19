#recursion en factorial
def factorial(x):
    if x>0:
      fac=x*factorial(x-1)
      print(fac)
    else:
        return 1
    return fac 

def main():
    num=int(input('ingrese el numero: '))
    resultado=factorial(num)
    print(f'el resultadoes: {resultado}')
    factorial(num)

if __name__=='__main__':
    main()