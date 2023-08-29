def main(milista):
    num=int(input('que numero dese agregar'))
    milista.append(num)
    print(milista)

def agregar(milista):
    num=int(input('que numero dese agregar'))
    milista.append(num)
    print(milista)

def insertar(milista):
    var=int(input('que numero dese agregar'))
    idx=int(input('en que posicion'))
    milista.insert(idx,var)
    print(milista) 

def borrar(milista):
    milista.clear()
    print(milista)

def remover(milista):
    print(milista)
    var=int(input('que numero dese agregar'))
    milista.remover(var)
    print(milista)

def index(milista):
    milista.index()
    print(milista)


def main():
    milista=[2,4,7,8]
    opc=''
    while opc!='exit':
        print('seleccion una de las siguientes opciones:\n',\
            'l.agregar\n 2.insertar\n 3. borrar')
        opc=input('=>')

        if opc=='1':
            agregar(milista)
        elif opc=='2':
            insertar(milista)
        elif opc=='3':
            borrar(milista)
        elif opc=='4':
            remover(milista)





if __name__=='main_':
    main()