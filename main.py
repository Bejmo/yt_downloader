import sys
import os
import base64
from pathlib import Path

# Interfaz
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QByteArray, QEventLoop, QThread, pyqtSignal, pyqtSlot
from interface import Ui_Form

# Icono
from icons.icon_data import ICON_DATA

# PyTube
from pytubefix import YouTube
from pytubefix import Playlist
# Importar funciones de descarga
from funciones_yt import *

# Clase para ejecutar las funciones en paralelo
# class DownloadThread(QThread):
#     status = pyqtSignal(str) # Indica si ha ocurrido algún error
#     # progreso_actualizado = pyqtSignal(str)
#     descarga_completada = pyqtSignal()
#     descarga_cancelada = pyqtSignal()
    
#     def __init__(self, task_function, *args, **kwargs):
#         super().__init__()
#         # Para ejecutar la función en paralelo
#         self.task_function = task_function
#         self.args = args
#         self.kwargs = kwargs

#         # self._loop = QEventLoop() # Bucle en el que se ejecuta la tarea, esperando un signal de parada en cualquier momento
#         self._is_running = True

#     def run(self):
#         try:
#             self.task_function(*self.args, **self.kwargs)
#         # except Exception as e:
#             # self.status.emit(f"Error: {str(e)}")
#         finally:
#             self.descarga_completada.emit()

#     def stop(self):
#         self._is_running = False

class MyApp(QWidget):
    # Atributos de directorios

    # Directorio actual si se usa un ejecutable (if) o el archivo de python (else)
    if getattr(sys, 'frozen', False):
        directorio_actual = os.path.dirname(sys.executable)
    else:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

    directorio_metadata = os.path.join(directorio_actual, 'metadata')
    ruta_archivo = os.path.join(directorio_metadata, 'ruta.txt')
    root = '' # Directorio donde se descargan los archivos

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
        self.ui.descargar_button.clicked.connect(self.descargar)
        self.ui.set_default_root_button.clicked.connect(self.set_default_root)
        self.ui.modificar_root_button.clicked.connect(self.modificar_root)
        self.ui.imprimir_root_actual_button.clicked.connect(self.imprimir_root_actual)
        self.ui.usage_button.clicked.connect(self.imprimir_usage)
        # self.ui.stop_descarga_button.clicked.connect(self.cancelar_descarga)
        # STOP DESCARGA -> stop_descarga_button

        # Configuración de visibilidad de algunos botones
        self.ui.numero_descargas.setVisible(False)
        self.ui.download_whole_playlist.setVisible(False)

        # - Inicialización programa - #

        self.download_thread = None
        
        # Crear directorio de metadata si no existe
        if not os.path.exists(self.directorio_metadata):
            os.makedirs(self.directorio_metadata)
            
            self.default_root()
        # Si existe, carga el root que está en 'metadata'
        else:
            self.leer_root()

    # Asigna el valor default al archivo que contiene el ROOT, llamado metadata
    def default_root(self):
        with open(self.ruta_archivo, 'w') as archivo:
            self.root = str(Path.home() / 'Downloads')
            print(self.root)
            archivo.write(self.root)
    
    # Lee el contenido de "metadata" para obtener el ROOT
    def leer_root(self):
        with open(self.ruta_archivo, 'r') as archivo:
            self.root = archivo.read()

    # - Funciones de Botones - #

    def modificar_root(self):
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
    
    def borrar_contenido(self):
        self.ui.url_line.clear()
        self.ui.carpeta_line.clear()

    def borrar_contenido_salida(self):
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

    # def cerrar_thread(self):
        # if self.download_thread and self.download_thread.isRunning():
        #     self.download_thread.stop()
        #     self.download_thread.quit()
        #     self.download_thread.wait()
        #     self.ui.terminal.append("Descarga cancelada.\n")
        # else:
        #     self.ui.terminal.append("No había ninguna descarga en proceso.\n")


    def descargar(self):
        formato = self.ui.MP3.currentText() # Puede ser MP3 o MP4
        esVideo = (formato == 'MP4')

        # Obtener la URL
        url = self.ui.url_line.text()
        directorio = self.ui.carpeta_line.text()
        # Si no hay directorio indicado, se guarda en el root
        if (directorio == ''): directorio = self.root
        else: directorio = os.path.join(self.root, directorio)

        url_correcta = True # Se presupone correcta hasta que se encuentra un error

        # - Ver la opción seleccionada - #
        # Descargar vídeo
        if (self.ui.descargar_video_radio_button.isChecked()):
            self.borrar_contenido()
            try:
                yt = YouTube(url)
            except Exception as e:
                url_correcta = False
                self.ui.terminal.append(f"Error: {str(e)}")

            try:
                if (url_correcta):
                    descargar_video_youtube(yt, directorio, False, esVideo, self)
                    # self.download_thread = DownloadThread(descargar_video_youtube, yt, directorio, False, esVideo, self) # Actualizar = False
                    
                    # # Asignar slots
                    # self.download_thread.status.connect(self.update_terminal) # Para imprimir en terminal
                    # self.download_thread.descarga_completada.connect(self.finalizar_descarga) # Para finalizar el proceso
                    
                    # self.download_thread.start()
            except Exception as e:
                self.ui.terminal.append(f"Error: {str(e)}")

        # Descargar playlist
        elif (self.ui.descargar_playlist_radio_button.isChecked()):
            self.borrar_contenido()
            try:
                p = Playlist(url)
            except Exception as e:
                url_correcta = False
                self.ui.terminal.append(f"Error: {str(e)}")
            
            try:
                if (url_correcta):
                    descargar_playlist(p, directorio, esVideo, self)
                    # self.download_thread = DownloadThread(descargar_playlist, p, directorio, esVideo, self)

                    # # Asignar slots
                    # self.download_thread.status.connect(self.update_terminal) # Para notificar errores
                    # self.download_thread.descarga_completada.connect(self.finalizar_descarga) # Para finalizar el proceso

                    # self.download_thread.start()
            except Exception as e:
                self.ui.terminal.append(f"Error: {str(e)}")

        # Actualizar playlist
        elif (self.ui.actualizar_playlist_radio_button.isChecked()):
            self.borrar_contenido()
            try:
                p = Playlist(url)
            except Exception as e:
                url_correcta = False
                self.ui.terminal.append(f"Error: {str(e)}")

            try:
                if (url_correcta):
                    actualizar_playlist(p, directorio, esVideo, self)
                    # self.download_thread = DownloadThread(actualizar_playlist, p, directorio, esVideo, self)

                    # # Asignar slots
                    # self.download_thread.status.connect(self.update_terminal) # Para notificar errores
                    # self.download_thread.descarga_completada.connect(self.finalizar_descarga) # Para finalizar el proceso

                    # self.download_thread.start()
            except Exception as e:
                self.ui.terminal.append(f"Error: {str(e)}")

        else:
            self.ui.terminal.append('No hay ningúna opción pulsada.\n')

    # - Slots - #

    # @pyqtSlot(str)
    # def update_terminal(self, message):
    #     self.ui.terminal.append(message)
    
    # @pyqtSlot()
    # def finalizar_descarga(self):
    #     # self.download_thread.stop()
    #     self.download_thread = None

# - MAIN - #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())