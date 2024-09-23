import sys
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel

class DescargarVideoThread(QThread):
    progreso_actualizado = pyqtSignal(int)
    descarga_completada = pyqtSignal()
    descarga_cancelada = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._cancelar = False

    def run(self):
        for i in range(100):
            if self._cancelar:
                self.descarga_cancelada.emit()
                return
            self.sleep(1)  # Simulando la descarga
            self.progreso_actualizado.emit(i + 1)
        
        self.descarga_completada.emit()

    def cancelar(self):
        self._cancelar = True

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        self.hilo_descarga = DescargarVideoThread()
        self.hilo_descarga.progreso_actualizado.connect(self.actualizar_progreso)
        self.hilo_descarga.descarga_completada.connect(self.descarga_completada)
        self.hilo_descarga.descarga_cancelada.connect(self.descarga_cancelada)

    def initUI(self):
        self.boton_descargar = QPushButton('Descargar Vídeo', self)
        self.boton_descargar.clicked.connect(self.iniciar_descarga)
        
        self.boton_cancelar = QPushButton('Cancelar Descarga', self)
        self.boton_cancelar.clicked.connect(self.cancelar_descarga)

        self.etiqueta_progreso = QLabel('Progreso: 0%', self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.boton_descargar)
        layout.addWidget(self.boton_cancelar)
        layout.addWidget(self.etiqueta_progreso)
        
        self.setLayout(layout)
        self.setWindowTitle('Descargador de Vídeos')
        self.show()

    def iniciar_descarga(self):
        self.etiqueta_progreso.setText('Progreso: 0%')
        self.hilo_descarga.start()

    def cancelar_descarga(self):
        self.hilo_descarga.cancelar()

    @pyqtSlot(int)
    def actualizar_progreso(self, progreso):
        self.etiqueta_progreso.setText(f'Progreso: {progreso}%')
        
    @pyqtSlot()
    def descarga_completada(self):
        self.etiqueta_progreso.setText('Descarga completada')

    @pyqtSlot()
    def descarga_cancelada(self):
        self.etiqueta_progreso.setText('Descarga cancelada')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(app.exec_())
