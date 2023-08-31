import math as m 

x_origen = float(input("Ingresa la coordenada x del origen del vector: "))
y_origen = float(input("Ingresa la coordenada y del origen del vector: "))
x_fin = float(input("Ingresa la coordenada x del fin del vector: "))
y_fin = float(input("Ingresa la coordenada y del fin del vector: "))

componente_x = x_fin - x_origen
componente_y = y_fin - y_origen

modulo = m.sqrt(componente_x ** 2 + componente_y ** 2)

print("\nEl vector tiene las siguientes características:")
print(f"Componente x: {componente_x}")
print(f"Componente y: {componente_y}")
print(f"Módulo del vector: {modulo}")
