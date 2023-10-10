def archivo():
    f = open('wcm.csv', 'r', encoding='utf8')
    documento = f.readlines()[1:]  
    f.close()
    lista = []
    for valor in documento:
        dato = valor.strip('\n').split(',')
        lista.append(dato)
    return lista

def goles_en_el_mundial(listado):
    goles_por_equipo = {}

    for partido in listado:
        equipo_local = partido[0]
        equipo_visitante = partido[1]
        goles_local = int(partido[2])
        goles_visitante = int(partido[4])

        if equipo_local in goles_por_equipo:
            goles_por_equipo[equipo_local] += goles_local
        else:
            goles_por_equipo[equipo_local] = goles_local

        if equipo_visitante in goles_por_equipo:
            goles_por_equipo[equipo_visitante] += goles_visitante
        else:
            goles_por_equipo[equipo_visitante] = goles_visitante

    return goles_por_equipo

def main():
    partidos = archivo()

    equipo_consultado = input('Ingrese el nombre del país que desea consultar: ')

    goles_por_equipo = goles_en_el_mundial(partidos)

    total_goles = 0
    if equipo_consultado in goles_por_equipo:
        total_goles = goles_por_equipo[equipo_consultado]

    print(f'{equipo_consultado} ha anotado un total de {total_goles} goles en todos los mundiales.')

if __name__ == '__main__':
    main()
