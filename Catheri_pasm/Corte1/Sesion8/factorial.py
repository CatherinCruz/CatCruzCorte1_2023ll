
def factorial(x):
    a=1
    for i in range(x):
        a*=i+1 #i=i*
        #print(a)
    return a 

if __name__=='__main__':
    a=factorial(4)
    print(f'resultado{a}')