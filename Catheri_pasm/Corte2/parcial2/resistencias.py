def resistencias(bandas):
    print(bandas)
    n1=banda1*banda3
    n2=banda2*banda3
    total=n1*n2
    banda1=[0,1,2,3,4,5,6,7,8,9]and[negro,cafe,rojo,naranja,amarillo,verde,azul,morado,gris,blanco]
    banda2=[0,1,2,3,4,5,6,7,8,9]and[negro,cafe,rojo,naranja,amarillo,verde,azul,morado,gris,blanco]
    banda3=[negro*1,cafe*10,rojo*100,naranja*1000,amarillo*10000,verde*100000,azul*1000000,morado*10000000,gris*100000000,blanco*1000000000]#and[negro,cafe,rojo,naranja,amarillo,verde,azul,morado,gris,blanco]
    negro=0
    cafe=1
    rojo=2
    naranja=3
    amarillo=4
    verde=5
    azul=6
    morado=7
    gris=8
    blanco=9
    #n1=banda1*banda3
    #n2=banda2*banda3
    
    #banda_colores=(input('ingrese el color de la primera banda?'))
    #print(f'{banda_colores}')
 

if __name__=='__main__':
    banda_colores=[]
    for i in range(3):
        banda_colores.append(input(f'color {i+1}:'))
    resistencias(banda_colores)