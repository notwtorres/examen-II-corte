class Stack:
    
    def __init__(self):
        self._items = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self._items[-1]

    def get_all(self):
        return list(self._items)

class Citizen:
    def __init__(self, ci: str, name: str):
        self.ci = ci            
        self.name = name
        self.history = Stack()  

    def __repr__(self):
        return f"<Ciudadano {self.ci}: {self.name}>"


class HistoryManager:
    def add_tramite(self, citizen: Citizen, tramite: str):
     
        citizen.history.push(tramite)
        print(f"Trámite '{tramite}' añadido al historial de {citizen.name}.")

    def ultimo_tramite(self, citizen: Citizen) -> str:
      
        return citizen.history.peek()

    def mostrar_historial(self, citizen: Citizen) -> list:
   
        return citizen.history.get_all()



