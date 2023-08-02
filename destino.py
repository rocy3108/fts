class Destino:
    def __init__(
        self,
        nombre,
        tipo_cocina,
        ingredientes,
        precio_minimo,
        precio_maximo,
        popularidad,
        disponibilidad,
        id_ubicacion,
        imagen
    ):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo_cocina": self.tipo_cocina,
            "ingredientes": self.ingredientes,
            "precio_minimo": self.precio_minimo,
            "precio_maximo": self.precio_maximo,
            "popularidad": self.popularidad,
            "disponibilidad": self.disponibilidad,
            "id_ubicacion": self.id_ubicacion,
            "imagen": self.imagen
        }
