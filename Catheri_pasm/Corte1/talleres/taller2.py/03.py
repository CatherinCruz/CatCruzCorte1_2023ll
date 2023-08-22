lado_a=float(input('ingrese la longitud del primer lado:'))
lado_b=float(input('ingrese la longitud del primer lado:'))
lado_c=float(input('ingrese la longitud del primer lado:'))
if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
    if lado_a==lado_b==lado_c:
     tipo_triangulo = 'equilatero'
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c: 
     tipo_triangulo='isoseles'
    else:   
     tipo_triangulo='escaleno'
    print(f'se puede formar un triangulo {tipo_triangulo}.')
else: 
  print('No se puede formar el triangulo con esas longitudes.')


