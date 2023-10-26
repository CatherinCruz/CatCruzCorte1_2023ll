# Definir la clase Ciudadano TareaPOO
class Ciudadano:
   
    def _init_(self, nombre, cedula, edad):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad

    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    
    def get_nombre(self):
        return self.__nombre

    
    def set_cedula(self, cedula):
       
        if len(str(cedula)) >= 8 and len(str(cedula)) <= 10:
            self.__cedula = cedula
        else:
            print("La cédula debe tener entre 8 y 10 dígitos")

   
    def get_cedula(self):
        return self.__cedula

    
    def set_edad(self, edad):
        
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo mayor que cero")

   
    def get_edad(self):
        return self.__edad

    
    def mostrar(self):
        print(f"Nombre: {self._nombre} - Edad: {self.edad} - CC: {self._cedula}")

    
    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return True
        else:
            return False


if __name__ == '_main_':
 
    ciudadano1 = Ciudadano("Catherin", 1023944703, 28)

    ciudadano1.mostrar()

    if ciudadano1.esMayorDeEdad():
        print("El ciudadano1 es mayor de edad")
    else:
        print("El ciudadano1 no es mayor de edad")