from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from pytube import YouTube
import sys

class FetchChannelNameThread(QThread):
    channel_name_fetched = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            yt = YouTube(self.url)
            channel_name = yt.author
        except Exception as e:
            channel_name = str(e)
        self.channel_name_fetched.emit(channel_name)

class YouTubeChannelNameApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Obtener nombre del canal de YouTube')

        self.layout = QVBoxLayout()

        self.url_label = QLabel('URL del video de YouTube:')
        self.layout.addWidget(self.url_label)

        self.url_entry = QLineEdit(self)
        self.layout.addWidget(self.url_entry)

        self.fetch_button = QPushButton('Obtener nombre del canal', self)
        self.fetch_button.clicked.connect(self.on_fetch_button_click)
        self.layout.addWidget(self.fetch_button)

        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def on_fetch_button_click(self):
        url = self.url_entry.text()
        if not url:
            QMessageBox.critical(self, 'Error', 'Por favor, introduce una URL de YouTube.')
            return

        self.thread = FetchChannelNameThread(url)
        self.thread.channel_name_fetched.connect(self.on_channel_name_fetched)
        self.thread.start()

    def on_channel_name_fetched(self, channel_name):
        self.result_label.setText(f'Nombre del canal: {channel_name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YouTubeChannelNameApp()
    ex.show()
    sys.exit(app.exec_())
