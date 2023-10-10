def archivo():
    lista = []
    with open('wcm.csv', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines[1:]:  
            dato = line.strip('\n').split(',')
            lista.append(dato)
    return lista

def goles_en_contra_en_el_mundial(listado):
    goles_contra_por_equipo = {}

    for partido in listado:
        equipo_local = partido[0]
        equipo_visitante = partido[1]
        goles_local = int(partido[2])
        goles_visitante = int(partido[4])

        if equipo_local not in goles_contra_por_equipo:
            goles_contra_por_equipo[equipo_local] = 0
        if equipo_visitante not in goles_contra_por_equipo:
            goles_contra_por_equipo[equipo_visitante] = 0

        goles_contra_por_equipo[equipo_local] += goles_visitante
        goles_contra_por_equipo[equipo_visitante] += goles_local

    return goles_contra_por_equipo

def main():
    listado = archivo()

    equipo_consultado = input('Ingrese el nombre del país que desea consultar: ')

    goles_contra_por_equipo = goles_en_contra_en_el_mundial(listado)

    total_goles_contra = goles_contra_por_equipo[equipo_consultado]

    print(f'{equipo_consultado} ha recibido un total de {total_goles_contra} goles en contra en todos los mundiales.')

if __name__ == '__main__':
    main()



