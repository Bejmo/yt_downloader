from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from pytube import YouTube
import subprocess
import os
import sys

class DownloadThread(QThread):
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    finished = pyqtSignal()
    
    def __init__(self, url):
        super().__init__()
        self.url = url
        self._is_running = True

    def run(self):
        try:
            yt = YouTube(self.url, on_progress_callback=self.progress_callback)
            stream = yt.streams.filter(only_audio=True).first()
            self.status.emit(f"Descargando: {yt.title}")
            out_file = stream.download()
            if self._is_running:
                self.status.emit("Convirtiendo a audio...")
                output_mp3 = out_file.replace('.mp4', '.mp3')
                subprocess.run(['ffmpeg', '-i', out_file, output_mp3])
                self.status.emit("Conversión finalizada!")
                # Eliminamos el archivo original de vídeo si la conversión fue exitosa
                if os.path.exists(output_mp3):
                    os.remove(out_file)
        except Exception as e:
            self.status.emit(f"Error: {str(e)}")
        finally:
            self.finished.emit()

    def progress_callback(self, stream, chunk, bytes_remaining):
        if self._is_running:
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = int(bytes_downloaded / total_size * 100)
            self.progress.emit(percentage_of_completion)

    def stop(self):
        self._is_running = False

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.layout.addWidget(self.url_input)

        self.download_button = QPushButton('Descargar', self)
        self.download_button.clicked.connect(self.start_download)
        self.layout.addWidget(self.download_button)

        self.stop_button = QPushButton('Cancelar', self)
        self.stop_button.clicked.connect(self.stop_download)
        self.layout.addWidget(self.stop_button)

        self.progress_bar = QProgressBar(self)
        self.layout.addWidget(self.progress_bar)

        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)
        self.layout.addWidget(self.log_output)

        self.setLayout(self.layout)
        self.setWindowTitle('YouTube Downloader')

        self.download_thread = None

    @pyqtSlot()
    def start_download(self):
        url = self.url_input.text()
        if url:
            self.download_thread = DownloadThread(url)
            self.download_thread.progress.connect(self.update_progress_bar)
            self.download_thread.status.connect(self.update_log)
            self.download_thread.finished.connect(self.on_download_finished)
            self.download_thread.start()

    @pyqtSlot()
    def stop_download(self):
        if self.download_thread and self.download_thread.isRunning():
            self.download_thread.stop()
            self.download_thread.quit()
            self.download_thread.wait()
            self.log_output.append("Descarga cancelada.")
            self.progress_bar.setValue(0)

    @pyqtSlot(int)
    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    @pyqtSlot(str)
    def update_log(self, message):
        self.log_output.append(message)

    @pyqtSlot()
    def on_download_finished(self):
        self.download_thread = None
        self.log_output.append("Proceso finalizado.")
        self.progress_bar.setValue(0)

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
