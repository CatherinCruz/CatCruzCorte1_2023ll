def archivo():
    f=open('wcm.csv','r',encoding='utf8')
    documento=f.readlines()
    f.close()
    lista=[]
    for valor in documento:
        dato=valor.strip('\n').split(',')
        lista.append(dato)
    print(lista)
    for valor in lista:
    #     pass
    # #print (valor)
     return lista 


