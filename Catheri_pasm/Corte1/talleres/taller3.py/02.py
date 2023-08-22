numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

producto = 0
if numero1 == 0 or numero2 == 0:
    producto = 0
else:
    for _ in range(abs(numero2)):
        producto += abs(numero1)

if (numero1 < 0 and numero2 > 0) or (numero1 > 0 and numero2 < 0):
    producto = -producto

print("El producto de", numero1, "y", numero2, "es:", producto)