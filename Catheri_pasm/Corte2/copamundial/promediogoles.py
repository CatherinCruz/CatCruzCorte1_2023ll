def archivo():
    lista = []
    with open('wcm.csv', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines[1:]: 
            dato = line.strip('\n').split(',')
            lista.append(dato)
    return lista

def promedio_de_goles_a_favor_por_pais(listado, equipo_consultado):
    total_goles_a_favor = 0
    total_partidos = 0

    for partido in listado:
        equipo_local = partido[0]
        equipo_visitante = partido[1]
        goles_local = int(partido[2])
        goles_visitante = int(partido[4])

        if equipo_local == equipo_consultado:
            total_goles_a_favor += goles_local
            total_partidos += 1

        if equipo_visitante == equipo_consultado:
            total_goles_a_favor += goles_visitante
            total_partidos += 1

    if total_partidos > 0:
        promedio = total_goles_a_favor / total_partidos
        return promedio
    else:
        return 0

def main():
    listado = archivo()

    equipo_consultado = input('Ingrese el nombre del país para calcular el promedio de goles a favor: ')

    promedio_goles_a_favor = promedio_de_goles_a_favor_por_pais(listado, equipo_consultado)

    if promedio_goles_a_favor > 0:
        print(f'El promedio de goles a favor de {equipo_consultado} en todos los mundiales es de {promedio_goles_a_favor:.2f} goles por partido.')
    else:
        print(f'{equipo_consultado} no ha participado en ningún mundial o no ha anotado goles.')

if __name__ == '__main__':
    main()
