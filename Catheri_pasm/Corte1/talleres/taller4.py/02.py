def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    divisores = calcular_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero

numeros_perfectos_esperados = [6, 28, 496, 8128]
numeros_perfectos_encontrados = []

print("Números perfectos encontrados:")
for numero in numeros_perfectos_esperados:
    if es_numero_perfecto(numero):
        numeros_perfectos_encontrados.append(numero)
        print(numero)

print("\nProceso finalizado.")

