def Saludo():
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    mensaje = f"Bienvenido {nombre_usuario} al curso de Programación aplicada."
    print(mensaje)

if __name__=='__main__':
    Saludo()