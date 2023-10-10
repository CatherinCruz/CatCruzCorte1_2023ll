def archivo():
    lista = []
    with open('wcm.csv', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines[1:]:  
            dato = line.strip('\n').split(',')
            lista.append(dato)
    return lista

def enfrentamientos_entre_equipos(listado, equipo1, equipo2):
    enfrentamientos = enfrentamientos_entre_equipos

    for partido in listado:
        equipo_local = partido[0]
        equipo_visitante = partido[1]

        if (equipo_local == equipo1 and equipo_visitante == equipo2) or (equipo_local == equipo2 and equipo_visitante == equipo1):
            enfrentamientos =+ 1

    return enfrentamientos

def main():
    listado = archivo()

    equipo1 = input('Ingrese el nombre del primer equipo: ')
    equipo2 = input('Ingrese el nombre del segundo equipo: ')

    enfrentamientos = enfrentamientos_entre_equipos(listado, equipo1, equipo2)

    print(f'{equipo1} y {equipo2} se han enfrentado {enfrentamientos} veces en los mundiales.')

if __name__ == '__main__':
    main()
