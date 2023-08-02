from ubicacion import Ubicacion
from destino import Destino
from datos import Data

def leer_destinos():
    destinos = Data('destinos.json')
    return destinos.leer_json()

def leer_ubicaciones():
    ubicaciones = Data('ubicaciones.json')
    return ubicaciones.leer_json()

def leer_actividades():
    actividades = Data('actividad.json')
    return actividades.leer_json()

def crear_destino(id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen):
    destino = Destino(
        id=id,
        nombre=nombre,
        tipo_cocina=tipo_cocina,
        ingredientes=ingredientes,
        precio_minimo=precio_minimo,
        precio_maximo=precio_maximo,
        popularidad=popularidad,
        disponibilidad=disponibilidad,
        id_ubicacion=id_ubicacion,
        imagen=imagen
    )
    return destino

def crear_ubicacion(id, direccion, coordenadas, imagen):
    ubicacion = Ubicacion(
        id=id,
        direccion=direccion,
        coordenadas=coordenadas,
        imagen=imagen
    )
    return ubicacion


