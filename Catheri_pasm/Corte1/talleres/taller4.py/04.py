import math 

def calcular_combinaciones_binomiales(n, r):
    combinaciones = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    return combinaciones

n = int(input("Ingresa el número total de elementos (n): "))
r = int(input("Ingresa el número de elementos en cada muestra (r): "))

if n >= r >= 2:
    combinaciones = calcular_combinaciones_binomiales(n, r)
    print(f"El número de combinaciones binomiales de {n} elementos tomados de {r} en {r} es {combinaciones:.0f}.")
else:
    print("Asegúrate de que 2 <= r <= n.")