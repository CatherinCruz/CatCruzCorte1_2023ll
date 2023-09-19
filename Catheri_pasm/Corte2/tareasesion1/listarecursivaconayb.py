def posiciones_de(a, b):
    if len(a) < len(b):
        return [1]
    elif a[:len(b)] == b:
        return [0] + [i + len(b) for i in posiciones_de(a[len(b):], b)]
    else:
        return [i + 1 for i in posiciones_de(a[1:], b)]

a = "Hola soy yo haahaha"
b = "yeye"
posiciones = posiciones_de(a, b)
print(f"Las posiciones en donde se encuentra '{b}' dentro de '{a}' son: {posiciones}")