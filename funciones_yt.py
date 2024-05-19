import os
import subprocess

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
def descargar_playlist(playlist, destino, window):
    counter = 0
    for yt in playlist.videos:
        descargar_audio_youtube(yt, destino, 0)
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