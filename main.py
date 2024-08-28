import sys
import os
import base64
from pathlib import Path

# Interfaz
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QByteArray, QCoreApplication
# from PyQt5.QtCore import QThread, pyqtSignal ([*] falta por acabar de implementar)
from interface import Ui_Form

# Icono
from icons.icon_data import ICON_DATA

# PyTube
from pytubefix import YouTube
from pytubefix import Playlist
from funciones_yt import *

class MyApp(QWidget):
    # Estado del programa.
    # estado == 0 -> Ningún botón pulsado
    # estado == 1 -> descargar vídeo
    # estado == 2 -> descargar playlist
    # estado == 3 -> modificar playlist
    estado = 0

    # Atributos de directorios

    # Directorio actual si se usa un ejecutable (if) o el archivo de python (else)
    if getattr(sys, 'frozen', False):
        directorio_actual = os.path.dirname(sys.executable)
    else:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

    directorio_metadata = os.path.join(directorio_actual, 'metadata')
    ruta_archivo = os.path.join(directorio_metadata, 'ruta.txt')
    root = '' # Directorio donde se descargan los archivos

    # Asigna el valor default al archivo que contiene el root
    # Se encapsula en una función para poder usarse más adelante
    def default_root(self):
        # Escribir el default path de descargas en el archivo
        with open(self.ruta_archivo, 'w') as archivo:
            self.root = str(Path.home() / 'Downloads')
            print(self.root)
            archivo.write(self.root)
    
    def leer_root(self):
        with open(self.ruta_archivo, 'r') as archivo:
            self.root = archivo.read()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('YT MP3') # Cambiar título ventana
        self.resize(800, 500)

        # Decodifica los datos del icono
        icon_data = base64.b64decode(ICON_DATA)
        icon_qbytearray = QByteArray(icon_data)
        icon_pixmap = QPixmap()
        icon_pixmap.loadFromData(icon_qbytearray)

        # Icono de aplicación
        self.setWindowIcon(QIcon(icon_pixmap))

        # Asignar funciones a los botones
        self.ui.descargar_button.pressed.connect(self.descargar)
        self.ui.descargar_video_radio_button.toggled.connect(self.descargar_video_button)
        self.ui.descargar_playlist_radio_button.toggled.connect(self.descargar_playlist_button)
        self.ui.actualizar_playlist_radio_button.toggled.connect(self.actualizar_playlist_button)
        self.ui.set_default_root.pressed.connect(self.set_default_root)
        self.ui.modificar_root_button.pressed.connect(self.modificar_root_button)
        self.ui.imprimir_root_actual.pressed.connect(self.imprimir_root_actual)
        self.ui.usage_button.pressed.connect(self.imprimir_usage)

        # - Inicialización programa - #
        
        # Crear directorio de metadata si no existe
        if not os.path.exists(self.directorio_metadata):
            os.makedirs(self.directorio_metadata)
            
            self.default_root()
        # Si existe, carga el root que está en 'metadata'
        else:
            self.leer_root()

    # - Funciones de Botones - #

    def descargar_video_button(self):
        self.estado = 1
        # self.ui.terminal.append('Descargar vídeo.\n')

    def descargar_playlist_button(self):
        self.estado = 2
        # self.ui.terminal.append('Descargar playlist.\n')

    def actualizar_playlist_button(self):
        self.estado = 3
        # self.ui.terminal.append('Actualizar playlist.\n')

    def modificar_root_button(self):
        url = self.ui.modificar_root_line.text()
        with open(self.ruta_archivo, 'w') as archivo:
                # Si la entrada no es vacía
                if (url):
                    archivo.write(url) # Se guarda la entrada de la url
                    self.ui.terminal.append('Root modificado.\n')
                    self.ui.terminal.append('Root actual:\n' + url + '\n')
                    self.ui.modificar_root_line.clear()
                # Si la entrada es vacía
                else:
                    self.ui.terminal.append('No se ha podido modificar el root.\n')

        self.leer_root()
    
    def set_default_root(self):
        # Crear el cuadro de diálogo de confirmación
        reply = QMessageBox.question(self, 'Confirmación', '¿Estás seguro de que deseas establecer el directorio raíz predeterminado?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.default_root()
            self.ui.terminal.append('Se ha modificado el root al default:\n' + self.root + '\n')
        else:
            self.ui.terminal.append('No se ha modificado el default root\n')
    
    def borrar_contenido_button(self):
        self.ui.url_line.clear()
        self.ui.carpeta_line.clear()

    def borrar_contenido_salida_button(self):
        self.ui.terminal.clear()

    def imprimir_root_actual(self):
        self.ui.terminal.append('Root actual:\n' + self.root + '\n')

    def imprimir_usage(self):
        self.ui.terminal.append(
            'Usage:\n' + 
            'Seleccione la opción que desee e introduzca la URL de YouTube y, opcionalmente, el nombre de la carpeta donde quiera guardar los archivos descargados (dentro del ROOT). Finalmente, pulse DESCARGAR para empezar la descarga.\n' +
            'Si necesita más detalles de las opciones que se ofrecen, deje el ratón encima de estas para ver una descripción más detallada.\n\n' +
            'NOTA: El ROOT es el directorio donde se descarga todo por defecto. Puede modificarlo introduciendo la dirección del directorio y pulsando el botón CAMBIAR ROOT. También puede asignar la ruta por defecto pulsando el botón SET DEFAULT ROOT. El ROOT por defecto es la carpeta DOWNLOADS que se encuentra en el directorio de este programa.\n'
        )

    def descargar(self):
        formato = self.ui.MP3.currentText() # Puede ser MP3 o MP4
        esVideo = (formato == 'MP4')

        url = self.ui.url_line.text()
        directorio = self.ui.carpeta_line.text()
        # Si no hay directorio indicado, se guarda en el root
        if (directorio == ''): directorio = self.root
        else: directorio = os.path.join(self.root, directorio)

        # Solo borrar el contenido del botón si hay alguna acción indicada
        if (self.estado != 0): self.borrar_contenido_button()
        else: # estado == 0
            self.ui.terminal.append('No hay ningúna opción pulsada.\n')
            return

        # Ver el estado en el que se encuentra y actuar en consecuencia
        url_correcta = True
        if (self.estado == 1):
            try:
                yt = YouTube(url)
            except:
                url_correcta = False
                self.ui.terminal.append('La URL no es correcta.\n')

            try:
                if (url_correcta): descargar_video_youtube(yt, directorio, False, esVideo, self.directorio_actual, self) # Actualizar = True
            except:
                self.ui.terminal.append('Error al descargar.\n')

        elif (self.estado == 2):
            try:
                p = Playlist(url)
            except:
                url_correcta = False
                self.ui.terminal.append('La URL no es correcta.\n')
            
            try:
                if (url_correcta): descargar_playlist(p, directorio, esVideo, self.directorio_actual, self)
            except:
                self.ui.terminal.append('Error al descargar.\n')

        elif (self.estado == 3):
            try:
                p = Playlist(url)
            except:
                url_correcta = False
                self.ui.terminal.append('La URL no es correcta.\n')

            try:
                if (url_correcta): actualizar_playlist(p, directorio, esVideo, self.directorio_actual, self)
            except:
                self.ui.terminal.append('Error al descargar.\n')

    def closeEvent(self, event):
        # Asegurar el cierre de la aplicación principal
        sys.exit(app.exec_())
        # QCoreApplication.quit()  # Termina el bucle principal de la aplicación
        # event.accept()  # Aceptar el evento de cierre de la ventana

# - MAIN - #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())