from cola import Cola
from persona import Persona
class CitizenHandler:
  def __init__(self):
    self.citizens = Cola()

  def agregar_ciudadano(self, ciudadano):
    self.citizens.enqueue(ciudadano)
  
  def desencolar_ciudadno(self):
    self.citizens.dequeue()
  
  def mostrar_ciudadano(self):
    self.citizens.peek()