import random as r 

def app():
    pal=''
    nombre='QUE PONEMOS'
    while pal !='exit':
       x=r.choice(nombre)
       #x=r.randint(100,180)
       #x=r.uniform(100,180)
       print(x)
       pal=input ("para salir oprima exit:-->")

if __name__=="__main__":
    app()