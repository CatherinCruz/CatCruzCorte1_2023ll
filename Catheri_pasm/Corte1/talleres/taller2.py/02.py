tiempoparqueo=int(input('ingrese el tiempo de parqueo en minutos:'))
costosinIVA=tiempoparqueo*139
IVA=costosinIVA*0.19
costototal=costosinIVA+IVA
resto=costototal %50
if resto !=0:
    costototalaprox=costototal + (50 - resto)
else:
    costototalaprox=costototal
print(f'costo de parqueo sin IVA:${costosinIVA:2f}')
print(f'IVA (19%):${IVA:2f}')
print(f'costo total con IVA:${costototal:2f}')
print(f'costo total aproximado a multiplo de $50 :${costototalaprox:2f}')