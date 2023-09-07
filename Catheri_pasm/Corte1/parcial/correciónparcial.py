from random import choice as c 

def repartir():
    deck='A23456789JQK'
    card=r.c(deck)
    return card

def  conteo(mano):
    card=[]
    for i in range(len(mano)):
        card.append(valor(mano[i]))
        print(card)
        if 'A' in mano:
            conteo=sum(card)
            while conteo>21 and 'A'in mano:
                indise=mano.index('A')
            card[indise] = 1
            conteo=sum(card)
    return sum(card) 
                
def valor(nuevamano):
        jack=['J','Q','K']

        if nuevamano in jack:
            nuevamano=10
        if nuevamano=='A':
            nuevamano=11
        else: 
            nuevamano=int(nuevamano)
        return nuevamano
        

  

def inicio():
    mano=[]
    mano.append((repartir()))
    mano.append((repartir()))
    print(mano)
    total=conteo(mano)
    print(f'conteo{total}')
    if total>21:
         print('__busted__')
         if total==21:
             print('blackjack')
    
    
    opc='y'
    while opc=='y':
        if opc=='y':
         opc=input('quiere otra carta?(y/n)')
         mano.append((repartir()))
         print(mano)
         total=conteo(mano)
         print(f'conteo{total}')
         if total>21:
             print('__busted__')
             break 
         if total==21:
             print('__blackjack__')
             break
         print(mano)
        elif opc=='n':
            break
        else: 
            print('opcion invalida')
            opc='y'


  




if __name__=='__main__':
    inicio()