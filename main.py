# Interfaz
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from interface import Ui_Form
import sys

# Otras funcionalidades
from pytube import YouTube
from pytube import Playlist
import pandas as pd
import os
import subprocess
from funciones_yt import *

# - MAIN - #

class MyApp(QWidget):
    # Estado del programa.
    # estado == 0 -> Ningún botón pulsado
    # estado == 1 -> descargar vídeo
    # estado == 2 -> descargar playlist
    # estado == 3 -> modificar playlist
    estado = 0

    directorio_actual = os.path.dirname(__file__)
    directorio_metadata = os.path.join(directorio_actual, 'metadata')
    ruta_archivo = os.path.join(directorio_metadata, "ruta.txt")
    directorio_descargas = "" # Directorio donde se descargan los archivos.

    # Asigna el valor default al archivo que contiene el directorio de descargas.
    # Se encapsula en una función para poder usarse más adelante.
    def default_descargas(self):
        # Escribir el default path de descargas en el archivo.
        with open(self.ruta_archivo, 'w') as archivo:
            self.directorio_descargas = os.path.join(self.directorio_actual, 'downloads')
            if not os.path.exists(self.directorio_descargas): # Si no existe /downloads, lo crea.
                os.makedirs(self.directorio_descargas)
            archivo.write(self.directorio_descargas)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("YT MP3") # Cambiar título ventana
        self.resize(800, 500)

        # Icono de aplicación
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, 'icons', 'yt.ico')
        self.setWindowIcon(QIcon(icon_path))

        # Asignar funciones a los botones
        self.ui.enviar_button.pressed.connect(self.enviar)
        self.ui.descargar_video_radio_button.toggled.connect(self.descargar_video_button)
        self.ui.descargar_playlist_radio_button.toggled.connect(self.descargar_playlist_button)
        self.ui.actualizar_playlist_radio_button.toggled.connect(self.actualizar_playlist_button)
        self.ui.set_default_root.pressed.connect(self.set_default_root)
        self.ui.cambiar_root_button.pressed.connect(self.modificar_root_button)
        self.ui.imprimir_root_actual.pressed.connect(self.imprimir_root_actual)

        # - Inicialización programa - #
        
        # Crear directorio de metadata si no existe.
        if not os.path.exists(self.directorio_metadata):
            os.makedirs(self.directorio_metadata)
            
            self.default_descargas()
        # Si existe, carga el directorio de descargas de "metadata".
        else:
            with open(self.ruta_archivo, 'r') as archivo:
                directorio_descargas = archivo.read()


    # - Funciones de Botones - #

    def descargar_video_button(self):
        self.estado = 1
        # self.ui.terminal.append("Descargar vídeo.\n")

    def descargar_playlist_button(self):
        self.estado = 2
        # self.ui.terminal.append("Descargar playlist.\n")

    def actualizar_playlist_button(self):
        self.estado = 3
        # self.ui.terminal.append("Actualizar playlist.\n")

    def modificar_root_button(self):
        url = self.ui.cambiar_root_line.text()
        with open(self.ruta_archivo, 'w') as archivo:
                # Si la entrada no es vacía.
                if (url != ""):
                    archivo.write(url) # Se guarda la entrada de la url.
                    self.ui.terminal.append("Root modificado.\n")
                    self.ui.cambiar_root_line.clear()
                # Si la entrada es vacía.
                else:
                    self.ui.terminal.append("No se ha podido modificar el root.\n")


    def set_default_root(self):
        self.default_descargas()

        self.ui.terminal.append("Se ha modificado el root al default:\n" + self.directorio_descargas)

    def borrar_contenido_button(self):
        self.ui.url_line.clear()
        self.ui.carpeta_line.clear()

    def borrar_contenido_salida_button(self):
        self.ui.terminal.clear()

    def imprimir_root_actual(self):
        with open(self.ruta_archivo, 'r') as archivo:
            directorio_descargas = archivo.read()
        self.ui.terminal.append("Root actual: " + directorio_descargas + "\n")

    def enviar(self):
        url = self.ui.url_line.text()
        directorio = self.ui.carpeta_line.text()
        directorio = os.path.join(self.directorio_descargas, directorio)

        # Ver el estado en el que se encuentra y actuar en consecuencia.
        if (self.estado == 0):
            self.ui.terminal.append("No hay ningúna opción pulsada.\n")
            return
        elif (self.estado == 1):
            yt = YouTube(url)
            descargar_audio_youtube(yt, directorio, 0, self)
        elif (self.estado == 2):
            p = Playlist(url)
            descargar_playlist(p, directorio, self)
        elif (self.estado == 3):
            p = Playlist(url)
            actualizar_playlist(p, directorio, self)

        self.borrar_contenido_button()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())