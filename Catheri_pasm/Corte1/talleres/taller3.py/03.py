n = int(input("Ingrese la cantidad de números de la serie de Fibonacci a mostrar: "))

fibonacci = [0, 1]

if n >= 2:
    while len(fibonacci) < n:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)

    print("Serie de Fibonacci:")
    for num in fibonacci:
        print(num, end=" ")
else:
    print("Debe ingresar un número mayor o igual a 2 para mostrar la serie de Fibonacci.")






