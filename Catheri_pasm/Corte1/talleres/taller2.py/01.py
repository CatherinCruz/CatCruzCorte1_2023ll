letra=input('ingrese la letra del abecedario:')
letra=letra.lower()
if letra =='a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'la letra {letra} es una vocal.')
else:
   print(f'la letra {letra} es una consonante.')