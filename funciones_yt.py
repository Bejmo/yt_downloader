import os
import re
import subprocess
import sys
from metadata_mp3 import *
from download_thumnails import download_thumnail
from PyQt5.QtWidgets import QApplication

# Limpiar el nombre del archivo (NO USAR CON EL PATH)
def clean_filename(filename):
    # Chars no permitidos por los archivos de Windows
    caracteres_a_eliminar = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for caracter in caracteres_a_eliminar:
        filename = filename.replace(caracter, '')

    # Eliminar '(visualizer)' y similares
    palabras_eliminadas = [
        ' (Visualizer)', ' (visualizer)', ' Visualizer', ' visualizer', ' [Visualizer]', ' [visualizer]',
        ' videoclip', ' Videoclip', ' (videoclip)', ' (Videoclip)', ' (Official Video)', ' (Official Audio)',
        'Topic', ' (Video Oficial)', ' [Official Video]', ' (Videoclip Oficial)', ' (Vídeo Oficial)',
        ' [Visualizer Video]', ' [visualizer video]', ' (Visualizer Video)', ' (visualizer video)',
        ' Official Video', ' official video', ' Official Audio', ' official audio', ' [Official Audio]',
        ' (Official Video)', ' (official video)', ' (Official Audio)', ' (official audio)',
        ' [Official Music Video]', ' [official music video]', ' (Official Music Video)', ' (official music video)',
        ' Video Oficial', ' video oficial', ' (Vídeo Oficial)', ' (vídeo oficial)', ' (Video Oficial)', ' (video oficial)',
        ' [Vídeo Oficial]', ' [vídeo oficial]', ' [Video Oficial]', ' [video oficial]', 
        ' (Vídeo)', ' (video)', ' (Vídeo Oficial)', ' (Video Oficial)', ' [Vídeo Oficial]', ' [Video Oficial]',
        ' (Audio Oficial)', ' (audio oficial)', ' [Audio Oficial]', ' [audio oficial]',
        ' (Lyric Video)', ' (lyric video)', ' Lyric Video', ' lyric video', ' [Lyric Video]', ' [lyric video]',
        ' (Official Lyric Video)', ' (official lyric video)', ' [Official Lyric Video]', ' [official lyric video]',
        ' (En Vivo)', ' (en vivo)', ' [En Vivo]', ' [en vivo]', ' En Vivo', ' en vivo',
        ' (Live)', ' (live)', ' [Live]', ' [live]', ' Live', ' live',
        ' (Live Performance)', ' (live performance)', ' [Live Performance]', ' [live performance]',
        ' Performance', ' performance', ' (Performance)', ' (performance)', ' [Performance]', ' [performance]',
        ' (Music Video)', ' (music video)', ' Music Video', ' music video', ' [Music Video]', ' [music video]',
        ' (Oficial)', ' (oficial)', ' [Oficial]', ' [oficial]', ' Oficial', ' oficial',
        ' (Video)', ' (video)', ' [Video]', ' [video]', ' Video', ' video',
        ' (Vídeo)', ' (vídeo)', ' [Vídeo]', ' [vídeo]', ' Vídeo', ' vídeo',
        ' [Lyrics]', ' [lyrics]', ' (Lyrics)', ' (lyrics)', ' Lyrics', ' lyrics',
        ' (Official Visualizer)', ' (official visualizer)', ' [Official Visualizer]', ' [official visualizer]',
        ' (Official)', ' (official)', ' [Official]', ' [official]'
    ]
    for palabra in palabras_eliminadas:
        filename = filename.replace(palabra, '')

    # Quitar posible espacio final
    filename = filename.replace(' .mp3', '.mp3')

    return filename

# Limpia el nombre del autor (mejorar nombre de los vídeos de YouTube Music)
def clean_author_name(author):
    author = author.replace(' - Topic', '')
    return author

# Devuelve si el vídeo indicado proviene de YouTube Music o no
def video_from_yt_music(yt):
    return ("Provided to YouTube" in yt.description)

# Obtener el path de ffmpeg
def get_ffmpeg_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'ffmpeg.exe')
    else:
        return os.path.join(os.path.dirname(__file__), 'bin', 'ffmpeg.exe')

# Convierte a audio un vídeo
def convert_to_audio(input_file, output_file):
    ffmpeg_cmd = [
        get_ffmpeg_path(),
        '-i', input_file,
        '-vn',                      # Eliminar vídeo
        '-acodec', 'libmp3lame',    # Seleccionasr codec
        '-ab', '192k',              # Bit rate
        '-ar', '44100',             # Sampling rate (Hz)
        '-y',                       # sobreescribir archivos
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True, creationflags=subprocess.CREATE_NO_WINDOW) # Flag para que no se abra el terminal
        print('Success.')
    except subprocess.CalledProcessError as e:
        print('Conversion failed.')

# Descarga un vídeo de YouTube a través de la URL
# actualizar indica si es una actualización de playlist (1) o no (0)
def descargar_video_youtube(yt, destino, actualizar, esVideo, window):
    if (esVideo): archivo = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() # Se descarga con menos calidad
    else: archivo = yt.streams.filter(only_audio=True).first()
    out_file = archivo.download(output_path=destino)
    base, ext = os.path.splitext(out_file) # Separa la extensión del nombre

    if (esVideo): ext = '.mp4'
    else: ext = '.mp3'

    # Mejorar nombre (si está indicado)
    if (window.ui.mejorar_nombres.isChecked()):
        if (video_from_yt_music(yt)):
            file_name = yt.author + yt.title + ext
        else:
            file_name = yt.title + ext
        file_name = clean_filename(file_name)
    else:
        file_name = yt.title + ext
    
    new_name = os.path.join(os.path.dirname(base + ext), file_name)

    if (actualizar):
        window.ui.terminal.append('Actualizando. Añadiendo: ' + os.path.basename(new_name))
    else:
        window.ui.terminal.append('Descargando: ' + os.path.basename(new_name))

    # Conversión a audio (en caso de que sea audio)
    if (not esVideo):
        convert_to_audio(out_file, new_name)
        os.remove(out_file)
    else:
        # Renombrar vídeo
        os.rename(out_file, new_name)

    # Añadir metada al archivo convertido
    if (video_from_yt_music(yt)):
        modificar_metadata(new_name, yt.title, clean_author_name(yt.author))
        download_thumnail(yt, new_name)
    
    window.ui.terminal.append('Descargado.\n')

# Descarga la playlist de la url indicada (LA PLAYLIST TIENE QUE ESTAR EN "OCULTO" O "PÚBLICO")
def descargar_playlist(playlist, destino, esVideo, window):
    index = 1 - 1 # Índice que indica a partir de qué canción debe empezar a descargar 
    counter = 0

    if (window.ui.download_whole_playlist.isChecked()):
        for i in range(index, len(playlist)):
            yt = playlist.videos[i]
            descargar_video_youtube(yt, destino, False, esVideo, window)
            counter += 1
            QApplication.processEvents()
    else:
        num_downloads = window.ui.numero_descargas.value()
        for i in range(index, len(playlist)):
            yt = playlist.videos[i]
            descargar_video_youtube(yt, destino, False, esVideo, window)
            counter += 1
            if (counter == num_downloads): break # Parar cuando tengas el número de videos indicados
            QApplication.processEvents()

    if (counter == 0):
        window.ui.terminal.append('Puede que se haya producido un error: no hay elementos en la playlist indicada.\n')
    else:
        window.ui.terminal.append('Descarga de la playlist completada.\n' + 'Descargados: ' + str(counter) + ' archivos.\n')

# Actualiza la playlist de la url indicada
# Va descargando canciones de la playlist hasta encontrar una que ya existe (o acaba la playlist)
# Es útil cuando tienes la platlist ordenada con el filtro: fecha de inclusión más reciente
def actualizar_playlist(playlist, destino, esVideo, window):
    archivos_en_directorio = os.listdir(destino)
    window.ui.terminal.append('Se está actualizando, espere unos instantes.\n')

    if (window.ui.MP3.currentText() == 'MP4'): ext = '.mp4'
    else: ext = '.mp3'

    counter = 0
    for yt in playlist.videos:
        # Obtener el nombre que debería de tener el archivo
        if (window.ui.mejorar_nombres.isChecked()):
            if (video_from_yt_music(yt)):
                file_name = yt.author + yt.title + ext
            else:
                file_name = yt.title + ext
            file_name = clean_filename(file_name)
        else:
            file_name = yt.title + ext

        # Si no está en la playlist, se descarga
        if not (file_name in archivos_en_directorio): 
            descargar_video_youtube(yt, destino, True, esVideo, window)
            counter += 1
            QApplication.processEvents()
        else:
            break
    
    if (counter == 0):
        window.ui.terminal.append('Puede que se haya producido un error: no hay elementos en la playlist indicada.\n')
    else:
        window.ui.terminal.append('Actualización completada.\n' + 'Descargados: ' + str(counter) + ' archivos.\n')