print('figuras validas:\n',\
      '1.calcule el area de un circulo\n',\
      '2.calcule el area de un rectangulo\n',\
        '3.calcule el area de un triangulo')
            

fig=input('Ingrese el nombre de una figura para calcular su area: ')
A='NAN'
if(fig=='circulo'):
    r=int(input('ingrese el valor del radio:'))
    A=3.1416*r**2
elif(fig=='rectangulo'):
    b=int (input('ingrese el valor de la base:'))
    h=int (input('ingrese el valor de la altura:'))
    A=b*h
elif(fig=='triangulo'):
    b=int (input('ingrese el valor de la base:'))
    h=int (input('ingrese el valor de la altura:'))
    A=b*h/2
else:
    print('ingrese una opcion invalida')
print('el valor del area es' , A)
