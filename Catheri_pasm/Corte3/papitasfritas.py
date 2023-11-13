def te_gustan_las_papas_fritas_con_malteada():
    respuesta=input('¿Te gustan las papas fritas con malteada?')
    if respuesta.lower=='si':
        print('¡Genial nos podemos casar!')
    elif respuesta.lower()=='no':
        print('Vamos y sabes que es lo bueno!')
    else:
        print('respuesta no valida revisate por deos!!!')
   
    if __name__=='__main__':
        te_gustan_las_papas_fritas_con_malteada()