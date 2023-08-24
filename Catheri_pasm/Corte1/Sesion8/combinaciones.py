from factorial import factorial as f   

def combinacion():
    n=int(input('ingrese el numero de elementos:'))
    m=int(input('ingrese el numero de grupos:'))
    cmb=(f(n)/f(m)*f(n-m))
    print(f'el numero de combinaciones posibles es:{cmb}')




if __name__=='__main__':
    combinacion()