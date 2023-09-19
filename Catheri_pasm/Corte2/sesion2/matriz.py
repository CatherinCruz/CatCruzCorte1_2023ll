def main_read():
    f=open('matrizAsignacion.txt','rt')
    documento=f.read()
    f.close()
    print(documento)

def main_read2():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readline().strip('\n').split(',')
    while documento != ['']:
        print(documento)
        #input('presione enter')
        documento=f.readline().strip('\n').split(',')
    f.close()

def main_read3():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readlines()
    print(documento)
    lista=[]
    for i in documento:
        lista=i.strip('\n').split(',')
    print(lista)
    #suma(lista)

if __name__=='__main__':
    #main_read()
    #main_read2()
    main_read3()