#herencia y jerarquia atributos que se dan desde un punto inicial padre y tienen varias clasificaciones parecidas pero no iguales.
class deportista:
  def __init__(self, nombre:str , documento:str, edad:str):
    
      self.__nombre=nombre
      self.__documento=documento
      self.__edad=edad 

  def setNombre (self ,nombre:str):
    self.__nombre= nombre 

  def getNombre(self):
          return self.__nombre
  def setDocumento  (self ,documento:str):
    self.__documento= documento 

  def getDocumento(self):
          return self.__documento 
  def setEdad (self ,edad:str):
    self.__edad= edad 

  def getEdad(self):
          return self.__edad 
class futbolista(deportista):
  def __init__(self, nombre: str, documento: str, edad: str, \
                  goles:int, equipo:str):
    super().__init__(nombre, documento, edad)
    self.__goles=goles
    self.equipo=equipo
  def setGoles(self,goles:int):
      self.__goles=goles
  def setEquipo(self,equipo:str):
      self.equipo=equipo
  def getGoles(self):
      return self.__goles
  def getEquipos(self):
      return self.equipo
  
  def anotar(self):
      return f'el jugador {self.getNombre()} ha anotado{self.getGoles()} en el equipo{self.getEquipos()} '
  
def main():
     inscrito=deportista('Juan','23456890',23)

if __name__=='__main__':
     main()