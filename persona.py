Class Persona:
    def __init__(self, num_llegada cedula, tramite):
        self.num_llegada = num_llegada
        self.cedula = cedula
        self.tramite = tramite
    
    def __str__(self):
        return f"{self.num_llegada} Persona {self.cedula} ({self.tramite})"