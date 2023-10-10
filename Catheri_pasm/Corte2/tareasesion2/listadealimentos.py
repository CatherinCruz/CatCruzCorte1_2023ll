# Leer el archivo Alimentos.txt y organizar los artículos según el valor del IVA
with open("Alimentos.txt", "r") as archivo:
    lineas = archivo.readlines()
    alimentos = {}
    for linea in lineas:
        nombre, iva = linea.strip().split(",")
        alimentos[nombre] = float(iva)

def calcular_valor_bruto(producto, valor_neto):
    iva = alimentos[producto]
    valor_base = valor_neto / (1 + iva)
    valor_iva = valor_neto - valor_base
    return valor_base, valor_iva

while True:
    producto = input("Ingrese un producto del listado (o escriba 'salir' para terminar): ")
    if producto == "salir":
        break
    elif producto not in alimentos:
        print("El producto ingresado no se encuentra en el listado.")
        continue
    else:
        while True:
            try:
                valor_neto = float(input("Ingrese el valor neto del mercado actual: "))
                break
            except ValueError:
                print("El valor ingresado no es válido. Intente nuevamente.")
        valor_base, valor_iva = calcular_valor_bruto(producto, valor_neto)
        print(f"El valor base del producto es: {valor_base:.2f}")
        print(f"El valor del IVA es: {valor_iva:.2f}")