with open("alimentos.txt", "r") as formato:
    productos = {}
    for i in formato:
        item, descripcion, iva = i.strip().split(",")
        productos[descripcion.lower()] = float(iva)
while True:
    opc = input("ingrese el nombre del producto: ").lower()
    neto = float(input("ingrese el valor neto: "))
    if opc in productos:
        iva=productos[opc]
    total=neto / (1 + iva)
    valorf=neto - total

    print(f"valordel producto: {total}")
    print(f"valor del iva del producto: {valorf}")