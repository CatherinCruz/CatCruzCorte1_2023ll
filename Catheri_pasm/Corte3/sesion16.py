class Personas:
    def __init__(self):
        self.nombre=None
        self.altura=None
        self.peso=None
        






def main():
    pacientes=[]
    while 1:
        usuario=Personas()
        usuario.nombre=input('Nombre:')
        usuario.altura=input('altura(cm):')
        usuario.peso=input('peso(kg):')

        pacientes.append(usuario)


        print(f'Nombre: {usuario.nombre}\n
              f'altura:{usuario.altura}(cm)\n
              f'peso:{usuario.peso}(kg)')


if __name__=='__main__':
    main()
