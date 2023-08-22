numero = int(input("Ingrese un número: "))

if numero == 0:
    print("Ningún número es divisible entre cero")
else:
    print("Divisores positivos de", numero, ":")

    divisor = 1
    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
        divisor += 1

    print("Utilizando bucle for:")
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            print(divisor)