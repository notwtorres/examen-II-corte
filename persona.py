Class Persona:
    def __init__(self, cedula, tramite):
        self.cedula = cedula
        self.tramite = tramite
    
    def __str__(self):
        return f"(Persona {self.cedula} ({self.tramite})"