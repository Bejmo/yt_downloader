import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import QThread, pyqtSignal

class Worker(QThread):
    progress = pyqtSignal(int)
    
    def __init__(self, stop_flag, func):
        super().__init__()
        self.stop_flag = stop_flag
        self.func = func

    def run(self):
        for i in range(1, 11):
            if self.stop_flag['stop']:
                break
            self.func()  # Ejecutar la función pasada como parámetro
            self.progress.emit(i)
            time.sleep(1)  # Simula una tarea larga

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('Presiona el botón para empezar la tarea', self)
        
        self.start_button = QPushButton('Iniciar tarea', self)
        self.start_button.clicked.connect(self.startTask)
        
        self.stop_button = QPushButton('Detener tarea', self)
        self.stop_button.clicked.connect(self.stopTask)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        self.setWindowTitle('QThread Ejemplo con Función')
        self.setGeometry(300, 300, 300, 200)

        self.stop_flag = {'stop': False}

    def startTask(self, func):
        self.stop_flag['stop'] = False
        self.thread = Worker(self.stop_flag, func)
        self.thread.progress.connect(self.updateLabel)
        self.thread.start()

    def stopTask(self):
        self.stop_flag['stop'] = True
        self.label.setText('Tarea detenida.')

    def updateLabel(self, progress):
        self.label.setText(f'Progreso: {progress}/10')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    def my_function():
        print("Ejecutando mi función.")
    ex.startTask(my_function)
    ex.show()
    sys.exit(app.exec_())
