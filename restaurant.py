class Restaurant:
    
    def __init__(self, id, nombre, ubicacion_id, calificacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion_id = ubicacion_id
        self.calificacion = calificacion
    
    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "ubicacion": self.ubicacion_id,
            "calificacion": self.calificacion
        }
    