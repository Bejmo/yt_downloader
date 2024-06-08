from PyQt5.QtWidgets import QApplication
import os
import re
import subprocess

# Limpiar el nombre del archivo (NO USAR CON EL PATH).
def clean_filename(filename):
    # Chars no permitidos por los archivos de Windows.
    caracteres_a_eliminar = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for caracter in caracteres_a_eliminar:
        filename = filename.replace(caracter, "")

    # Eliminar "(visualizer)" y similares
    palabras_eliminadas = ["(Visualizer)","(visualizer)","Visualizer","visualizer","[visualizer]","[Visualizer]",
                            "videoclip","Videoclip","(videoclip)","(Videoclip)", "(Official Video)",
                            "(Official Audio)",
                            ]

    for palabra in palabras_eliminadas:
        filename = filename.replace(" " + palabra, "")

    return filename

# Convierte a audio un vídeo.
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

# Descarga el audio de un vídeo de YouTube a través de la URL.
# actualizar indica si es una actualización de playlist (1) o no (0)
def descargar_audio_youtube(yt, destino, actualizar, window):
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file) # Separa la extensión del nombre
    new_file = base + ".mp3"
    # Cambiar nombre.
    file_name = yt.author + " - " + yt.title + ".mp3"
    file_name = clean_filename(file_name)
    print(file_name)
    new_name = os.path.join(os.path.dirname(new_file), file_name)

    if (actualizar == 1):
        window.ui.terminal.append("Actualizando. Añadiendo: " + os.path.basename(new_name))
    else:
        window.ui.terminal.append("Descargando: " + os.path.basename(new_name))

    QApplication.processEvents()  # Allow UI to update

    # Conversión a audio.
    convert_to_audio(out_file, new_file)
    os.remove(out_file)

    # Renombrar archio (da error si lo hago antes).
    os.rename(new_file, new_name)
    
    window.ui.terminal.append("Descargado.\n")

# Descarga la playlist de la url indicada.
def descargar_playlist(playlist, destino, window):
    counter = 0
    for yt in playlist.videos:
        descargar_audio_youtube(yt, destino, 0, window)
        counter += 1

    window.ui.terminal.append("Descarga de la playlist completada.\n" + "Descargados: " + str(counter) + " archivos.\n")

# Actualiza la playlist de la url indicada.
# Va descargando canciones de la playlist hasta encontrar una que ya existe (o acaba la playlist).
# Es útil cuando tienes la platlist ordenada con el filtro: fecha de inclusión más reciente.
def actualizar_playlist(playlist, destino, window):
    archivos_en_directorio = os.listdir(destino)
    window.ui.terminal.append("Se está actualizando, espere unos instantes.\n")

    counter = 0
    for yt in playlist.videos:
        name_file = yt.title + ".mp3"
        if not (name_file in archivos_en_directorio): # Si no está en la playlist, se descarga.
            descargar_audio_youtube(yt, destino, 1, window)
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
#             descargar_audio_youtube(yt, destino, 1, window)
#     texto_imprimir.insert(tk.END, "Actualización completada.\n")