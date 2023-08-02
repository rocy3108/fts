from pathlib import Path
import os
from tkinter import Toplevel, Label
from PIL import Image, ImageTk
import requests
from io import BytesIO

class PopupImage:
    def __init__(self, root, destino, actividades=None):
        self.destino = destino
        self.dialog = None
        self.root = root
        self.actividades = actividades
        self.BASE = Path(__file__).resolve().parent
        if destino['imagen'][0:5] == 'https':
            self.img = destino['imagen']
        else:
            self.img = os.path.join(self.BASE, 'components', 'frames', destino['imagen'])
        self.get_dialog()
    def get_dialog(self, event=None):
        if self.dialog is not None:
            return

        self.dialog = Toplevel()
        self.dialog.protocol("WM_DELETE_WINDOW", self.on_dialog_close)


        if self.img.startswith('https'):
            response = requests.get(self.img)
            image = Image.open(BytesIO(response.content))
        else:
            image = Image.open(self.img)

        photo = ImageTk.PhotoImage(image)

        photo = ImageTk.PhotoImage(image)

        background_label = Label(self.dialog, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.dialog.geometry("400x400")
        x, y = self.root.winfo_pointerxy()
        self.dialog.geometry("+%d+%d" % (x, y))

        label = Label(self.dialog, text=self.destino['nombre'], foreground='Black', font='Arial 20')
        label.pack()

        label2 = Label(self.dialog, text=f"{self.destino['tipo_cocina']}", foreground='blue', font='Arial 12')
        label2.pack()

        estrellas = self.destino['popularidad']

        label3 = Label(self.dialog, text='✪'*int(estrellas), foreground='yellow', bg='red', font='Arial')
        label3.pack()

        if self.actividades:
            for actividad in self.actividades:
                labels = Label(self.dialog, text=f'Actividad: {actividad["nombre"]}', foreground='red', bg='white', font='Arial')
                labels.pack()

        self.dialog.mainloop()

    def on_dialog_close(self):

        self.dialog.destroy()
        self.dialog = None

