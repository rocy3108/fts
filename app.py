from tkinter import *
import tkintermapview
from funciones import *
from tkinter import messagebox
from PIL import Image
from top_level import PopupImage

# Funciones
#


def ver_puntos_mapa(mapa):
    lista_datos = leer_ubicaciones()
    for coord in lista_datos:
        mapa.set_marker(coord['coordenadas'][0], coord['coordenadas'][1])


def ver_destinos():
    lista_destinos = leer_destinos()
    texto = ''
    for destino in lista_destinos:
        texto += str(destino['id'])+') ' + destino['nombre'] + '\n'
    return texto


def boton_destinos(id_destino, mapa, root):
    lista_destinos = leer_destinos()
    lista_ubicaciones = leer_ubicaciones()
    lista_actividades = leer_actividades()
    for ubicacion in lista_ubicaciones:
        if ubicacion['id'] == id_destino:
            mapa.set_marker(ubicacion['coordenadas'][0],
                            ubicacion['coordenadas'][1])
            
    for destino in lista_destinos:
        if destino['id'] == id_destino:
            actividades_encontradas = []
            for actividad in lista_actividades:
                if actividad['destino_id'] == id_destino:
                    actividades_encontradas.append(actividad)
            
            PopupImage(root, destino, actividades_encontradas)


ventana_principal = Tk()

# Variables
destinos = StringVar()
destinos.set(ver_destinos())

id_destino = IntVar()

# define ancho y alto de la ventana principal
ventana_principal.geometry('800x600')

caja1 = Frame(ventana_principal)
caja1.grid(row=0, column=0)

titulo = Label(caja1, text='BIENVENIDOS AL MAPA DE CIUDAD DE SALTA',
               foreground='white', bg='black', font='Arial 12')
titulo.grid(row=0, column=1)

caja = Frame(ventana_principal)
caja.grid(row=1, column=0)

caja_botones = Frame(caja)
caja_botones.grid(row=0, column=0)

boton = Button(caja_botones, text='BUSCAR', foreground='white', bg='violet', font='Arial 10', command=lambda: boton_destinos(
    int(id_destino.get()), map_widget, ventana_principal))
boton.grid(row=1, column=0)

entry = Entry(caja_botones, textvariable=id_destino)
entry.grid(row=0, column=0)

map_widget = tkintermapview.TkinterMapView(
    caja, width=500, height=500, corner_radius=0)
map_widget.grid(row=0, column=1)
map_widget.set_position(-24.789124241917268, -65.41029074730143)
map_widget.set_zoom(15)
# ver_puntos_mapa(map_widget)

texto_destinos = Label(caja, textvariable=destinos)
texto_destinos.grid(row=0, column=2)
ver_destinos()


ventana_principal.mainloop()
