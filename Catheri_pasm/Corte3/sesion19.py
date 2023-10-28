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
  def presentacion(self):
    return f'{self.getNombre()} es un gran deportista'
  
        
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
      return f'el jugador {self.getNombre()} ha anotado{self.getGoles()} en el equipo{self.getEquipos()} goles'
  def presentacion(self):
    return f'{self.getNombre()} es un gran futbolista'
  
  class tenista(deportista):
    def __init__(self, nombre: str, documento: str, edad: str):
        super().__init__(nombre, documento, edad)
        self.__games=games
        self.__sets=sets
    def setGames(self,games:int):
      self.__games=games 
    def getGames(self):
      return self.__games
    def setSets(self,sets:int):
      self.__sets=sets
    def getSets(self):
      return self.__sets
    def ace(self):
      return f'el jugador {self.getNombre()} ha ganado {self.getGames()} games'
    def presentacion(self):
       return f'{self.getNombre()}es un gran tenista'
        
  
def main():
    inscrito=futbolista('Falcao García',35,'38763284',34,'Seleccion Colombia')
    print(f'Nombre: {inscrito.getNombre()}\n',\
            f'Edad: {inscrito.getEdad()}\n',\
                f'Documento: {inscrito.getDocumento()}\n',\
                    f'#Goles: {inscrito.getGoles()}\n',\
                    f'Equipo: {inscrito.getEquipo()}\n')
    print(inscrito.anotar())
    print(inscrito.presentacion())
    print('\n------------------------------------')
    inscrito2=tenista('Roger Federer','897234923',4,12)
    print(f'Nombre: {inscrito2.getNombre()}\n',\
        f'Edad: {inscrito2.getEdad()}\n',\
            f'Documento: {inscrito2.getDocumento()}\n',\
                f'#Games: {inscrito2.getGames()}\n',\
                f'#sets: {inscrito2.getSets()}\n')
    print(inscrito2.ace())
    print(inscrito2.presentacion())
    print('\n------------------------------------')
    inscrito3=deportista('Magnus Carlsen','2387623',32)
    print(inscrito3.presentacion())

if __name__=='__main__':
     main()