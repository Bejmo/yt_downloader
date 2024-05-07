all:

interface: interface.ui
	pyuic5 interface.ui -o interface.py

exe: audio_yt.py
	pyinstaller --clean --onefile --windowed audio_yt.py