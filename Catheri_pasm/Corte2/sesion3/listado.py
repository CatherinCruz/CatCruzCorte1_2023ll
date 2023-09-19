#el diccionario es como una lista pero son pequeñas bases de datos
def inscripcion():
    estudiantes={}
    datos={}
    while 1:
        opc=input('desea inscribir un estudiante (y/n):')

        if opc=='y':
            nombre=input('Nombre:')
            edad=input('Edad:')
            codigo=input('Codigo:')
            genero=input('Genero:')
            datos['edad']=edad
            datos['codigo']=codigo
            datos['genero']=genero
            estudiantes[nombre]=datos
            print(estudiantes)
        elif opc=='n':
            for key,value in estudiantes.items():
                print(f'Estudiante:{key}')
                print(estudiantes[key]['edad'])
                print(estudiantes[key]['codigo'])
                print(estudiantes[key]['genero'])
            break 
        else:
            print('Opcion invalida')

def main():
    inscripcion()




if __name__=='__main__':
    main()