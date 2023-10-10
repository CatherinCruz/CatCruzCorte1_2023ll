def archivo():
    lista = []
    with open('wcm.csv', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines[1:]:  
            dato = line.strip('\n').split(',')
            lista.append(dato)
    return lista

def diferencia_de_goles_en_el_mundial(listado):
    diferencia_de_goles_por_equipo = {}

    for partido in listado:
        equipo_local = partido[0]
        equipo_visitante = partido[1]
        goles_local = int(partido[2])
        goles_visitante = int(partido[4])

        
        if equipo_local not in diferencia_de_goles_por_equipo:
            diferencia_de_goles_por_equipo[equipo_local] = 0
        if equipo_visitante not in diferencia_de_goles_por_equipo:
            diferencia_de_goles_por_equipo[equipo_visitante] = 0
            
        diferencia_local = goles_local - goles_visitante
        diferencia_visitante = goles_visitante - goles_local
        diferencia_de_goles_por_equipo[equipo_local] += diferencia_local
        diferencia_de_goles_por_equipo[equipo_visitante] += diferencia_visitante

    return diferencia_de_goles_por_equipo

def main():
    listado = archivo()

    equipo_consultado = input('Ingrese el nombre del país que desea consultar: ')

    diferencia_de_goles_por_equipo = diferencia_de_goles_en_el_mundial(listado)

    if equipo_consultado in diferencia_de_goles_por_equipo:
        diferencia_de_goles = diferencia_de_goles_por_equipo[equipo_consultado]
        print(f'{equipo_consultado} tiene una diferencia de goles total de {diferencia_de_goles} en todos los mundiales.')
    else:
        print(f'{equipo_consultado} no ha participado en ningún mundial.')

if __name__ == '__main__':
    main()
