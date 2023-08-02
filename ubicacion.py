
class Ubicacion:
    
    def __init__(self, id,nombre, direccion, coordenadas= None):
        self.id = id
        self.nombre= nombre
        self.direccion = direccion
        self.coordenadas = coordenadas
        if not (coordenadas is None):
            self.coordenadas= coordenadas
        else:
            self.coordenadas= [] 
    
    
    def to_json(self):
        return {
            "id": self.id,
            "direccion": self.direccion,
            "coordenadas": self.coordenadas,
        }
    
    @classmethod
    def from_json(cls,data):
        return cls(data["id"],data["nombre"],data["direccion"],data["coordenadas"])