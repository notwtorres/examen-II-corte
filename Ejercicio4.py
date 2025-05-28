# Ejercicio4

class Cola:
  def __init__():
    self.items = ()
    self.ciudadano = 0
    self.siguiente = None

  def esta_vacia(self):
    return len(self.items) == 0

  def añadir(self, ciudadano):
    self.items.append(ciudadano)

  def extraer(self, ciudadano):
    self.items.remove(ciudadano)
  
  def mostrar(self, ciudadano):
    print(self.items)

  def atender(self, ciudadano):
    mostrar(ciudadano)
    extraer(ciudadano)

  def siguiente(self, ciudadano):
    self.ciudadano = self.siguiente

class Pila:
  from Cola import Cola
  def __init__():
    self.items = []

  def mostrar_historial(self, tramite):
    print(self.items)

  def añadir_tramite(self, tramite):
    self.items.append(tramite)

def main():
  from Cola import Cola
  from Pila import Pila

  ciudadano = input(print("Ingrese su nombre: "))
  Cola.añadir(ciudadano)

  tramite = input(print("Que tramite desea realizar: "))
  Pila.añadir_tramite(tramite)

  print("Cola de espera")
  print(Cola.mostrar)

  print("Historial")
  print(Pila.mostrar_historial)

  respuesta = input(print("Desea atender al ciudadano {Cola.ciudadano}"))
  Cola.extraer(ciudadano)

if __name__ = "__main__":
  main()
