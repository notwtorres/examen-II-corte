import menu
from controllers import citizenHandler
import Persona

handler = citizenHandler.CitizenHandler()
while True:
  menu.menu()

  user_input = input("ingrese una opcion")
  match user_input:
    case "1":
      cedula = input("cedula => ")
      tramite = input("trámite => ")
      ciudadano = Persona(cedula, tramite)
      handler.agregar_ciudadano(ciudadano)
    
    case "2": 
      handler.desencolar_ciudadno()
