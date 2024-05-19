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

# ------------------------------------------------ #

# - INICIALIZACIÓN - #

# Crear directorio de "metadata" donde se encuentra el directorio "root".
directorio_actual = os.path.dirname(__file__)
directorio_metadata = os.path.join(directorio_actual, 'metadata')
ruta_archivo = os.path.join(directorio_metadata, "ruta.txt")
directorio_descargas = "" # Directorio donde se descargan los archivos.
# root = "" # Directorio que contiene la ruta donde se guardarán las descargas.

# Asigna el valor default al archivo que contiene el directorio de descargas.
def default_root():
    global ruta_archivo, directorio_descargas, directorio_actual
    # Escribir el default path de descargas en el archivo.
    with open(ruta_archivo, 'w') as archivo:
        directorio_descargas = os.path.join(directorio_actual, 'downloads')
        if not os.path.exists(directorio_descargas): # Si no existe /downloads, lo crea.
            os.makedirs(directorio_descargas)
        archivo.write(directorio_descargas)

# Crear directorio de "root"
if not os.path.exists(directorio_metadata): # Si no existe carpeta de metadata con el root se crea
    os.makedirs(directorio_metadata)
    root = os.path.join(directorio_actual, 'downloads')
    
    default_root()
else:
    # Cargar directorio de root (por si se ha modificado)
    with open(ruta_archivo, 'r') as archivo:
        root = archivo.read()

# ------------------------------------------------ #

# - FUNCIONES - #

def convert_to_audio(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",                      # Eliminar vídeo
        "-acodec", "libmp3lame",    # Seleccionasr codec
        "-ab", "192k",              # Bit rate
        "-ar", "44100",             # Sampling rate (Hz)
        "-y",                       # sobreescribir archivos
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Success.")
    except subprocess.CalledProcessError as e:
        print("Conversion failed.")

# ------------------------------------------------ #

# FUNCIONES AUDIO_YT
        
# Descarga el audio de un vídeo de YouTube a través de la URL.
# actualizar indica si es una actualización de playlist (1) o no (0)
def descargar_audio_youtube(yt, destino, actualizar):
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file) # Separa la extensión del nombre
    new_file = base + '.mp3'

    if (actualizar == 1):
        window.ui.terminal.append("Actualizando. Añadiendo: " + os.path.basename(new_file))
        # texto_imprimir.insert(tk.END, "Actualizando. Añadiendo: ", str(new_file), "\n")
    else:
        window.ui.terminal.append("Descargando: " + os.path.basename(new_file))
        # texto_imprimir.insert(tk.END, "Descargando: ", str(new_file), "\n")

    # Conversión a audio.
    convert_to_audio(out_file, new_file)
    os.remove(out_file)
    
    window.ui.terminal.append("Descargado.\n")

# Descarga la playlist de la url indicada.
def descargar_playlist(playlist, destino):
    counter = 0
    for yt in playlist.videos:
        descargar_audio_youtube(yt, destino, 0)
        counter += 1

    window.ui.terminal.append("Descarga de la playlist completada.\n" + "Descargados: " + str(counter) + " archivos.\n")

# Actualiza la playlist de la url indicada.
# Va descargando canciones de la playlist hasta encontrar una que ya existe (o acaba la playlist).
# Es útil cuando tienes la platlist ordenada con el filtro: fecha de inclusión más reciente.
def actualizar_playlist(playlist, destino):
    archivos_en_directorio = os.listdir(destino)
    window.ui.terminal.append("Se está actualizando, espere unos instantes.\n")

    counter = 0
    for yt in playlist.videos:
        name_file = yt.title + '.mp3'
        if not (name_file in archivos_en_directorio): # Si no está en la playlist, se descarga.
            descargar_audio_youtube(yt, destino, 1)
            counter += 1
        else:
            break
    window.ui.terminal.append("Actualización completada.\n" + "Descargados: " + str(counter) + " archivos.\n")


# # Actualiza la playlist COMPLETAMENTE.
# def actualizar_playlist(playlist, destino):
#     archivos_en_directorio = os.listdir(destino)
#     texto_imprimir.insert(tk.END, "Se está actualizando, espere unos instantes.\n")
#     for yt in playlist.videos:
#         name_file = yt.title + '.mp3'
#         if not (name_file in archivos_en_directorio):
#             descargar_audio_youtube(yt, destino, 1)
#     texto_imprimir.insert(tk.END, "Actualización completada.\n")

# ------------------------------------------------ #

# - MAIN - #

class MyApp(QWidget):
    # Estado del programa.
    # estado == 0 -> Ningún botón pulsado
    # estado == 1 -> descargar vídeo
    # estado == 2 -> descargar playlist
    # estado == 3 -> modificar playlist
    # estado == 4 -> modificar root path
    estado = 0

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
        global ruta_archivo

        url = self.ui.cambiar_root_line.text()
        with open(ruta_archivo, 'w') as archivo:
                archivo.write(url) # Se guarda la entrada de la url.
                self.ui.terminal.append("Root modificado.\n")

        self.ui.cambiar_root_line.clear()

    def set_default_root(self):
        default_root()

        self.ui.terminal.append("Se ha modificado el root al default:\ncarpeta_actual/downloads")

    def borrar_contenido_button(self):
        self.ui.url_line.clear()
        self.ui.carpeta_line.clear()

    def borrar_contenido_salida_button(self):
        self.ui.terminal.clear()

    def imprimir_root_actual(self):
        global root, ruta_archivo
        with open(ruta_archivo, 'r') as archivo:
            root = archivo.read()
        self.ui.terminal.append("Root actual: " + root + "\n")

    def enviar(self):
        url = self.ui.url_line.text()
        directorio = self.ui.carpeta_line.text()
        directorio = os.path.join(root, directorio)

        # Ver el estado en el que se encuentra y actuar en consecuencia.
        if (self.estado == 0):
            self.ui.terminal.append("No hay ningúna opción pulsada.\n")
            return
        elif (self.estado == 1):
            yt = YouTube(url)
            descargar_audio_youtube(yt, directorio, 0)
        elif (self.estado == 2):
            p = Playlist(url)
            descargar_playlist(p, directorio)
        elif (self.estado == 3):
            p = Playlist(url)
            actualizar_playlist(p, directorio)

        self.borrar_contenido_button()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())