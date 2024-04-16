from pytube import YouTube
from pytube import Playlist
import pandas as pd
import os

# Descarga el audio de un vídeo de YouTube a través de la URL.
# actualizar indica si es una actualización de playlist (1) o no (0)
def descargar_audio_youtube(yt, destino, actualizar):
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file) # Separa la extensión del nombre
    new_file = base + '.mp3'
    try: # Soluciona error de tener un nombre raro y no detectarlo con yt.title en "actualizar_playlist"
        os.rename(out_file, new_file)
        name_file = yt.title + '.mp3'
        if (actualizar == 1):
            texto_imprimir.insert(tk.END, "Actualizando. Añadiendo: ", name_file, "\n")
        else:
            texto_imprimir.insert(tk.END, "Descargando: ", name_file, "\n")
    except:
        os.remove(out_file)

# Descarga la playlist de la url indicada.
def descargar_playlist(playlist, destino):
    for yt in playlist.videos:
        descargar_audio_youtube(yt, destino, 0)
    texto_imprimir.insert(tk.END, "Descarga de la playlist completada.\n")

# Actualiza la playlist de la url indicada.
def actualizar_playlist(playlist, destino):
    archivos_en_directorio = os.listdir(destino)
    texto_imprimir.insert(tk.END, "Se está actualizando, espere unos instantes.\n")
    for yt in playlist.videos:
        name_file = yt.title + '.mp3'
        if not (name_file in archivos_en_directorio):
            descargar_audio_youtube(yt, destino, 1)
    texto_imprimir.insert(tk.END, "Actualización completada.\n")

# MAIN FUNCTION
def main():
    print("Programa para descargar audio de YouTube.")

    # Crear directorio de "metadata" donde se encuentra el directorio "root".
    directorio_actual = os.path.dirname(__file__)
    directorio_metadata = os.path.join(directorio_actual, 'metadata')
    nombre_archivo = 'ruta.txt'
    ruta_archivo = os.path.join(directorio_metadata, nombre_archivo)
    root = "" # Directorio que contiene la ruta donde se guardarán las descargas.
    
    if not os.path.exists(directorio_metadata): # No existe "root": se crea.
        os.makedirs(directorio_metadata)
        root = os.path.join(directorio_actual, 'downloads')
        
        # Escribir el default path en el archivo
        with open(ruta_archivo, 'w') as archivo:
            directorio_descargas = os.path.join(directorio_actual, 'downloads')
            if not os.path.exists(root):
                os.makedirs(root)
            archivo.write(root)
    else: # Guardar el root file guardado anteriormente.
        with open(ruta_archivo, 'r') as archivo:
            root = archivo.read()

    respuesta = int(input("Desea descargar un vídeo [1]\nUna playlist [2]\nActualizar una playlist [3]\nModificar el root path [4]\n"))
    if (1 <= respuesta and respuesta <= 4):
        url = input("Introduzca URL: ");
        destino = input("Introduzca el nombre de la carpeta destino (si no desea guardarlo en ninguna carpeta, pulse ENTER): ")
        destino = os.path.join(root, destino)

        try:    
            if (respuesta == 1):
                yt = YouTube(url)
                descargar_audio_youtube(yt, destino, 0)
            elif (respuesta == 2):
                p = Playlist(url)
                descargar_playlist(p, destino)
            elif (respuesta == 3):
                p = Playlist(url)
                actualizar_playlist(p, destino)
            elif (respuesta == 4):
                root = input("Introduzca el valor de la ruta completa (tiene que ser válida para su sistema operativo)")
                with open(root, 'w') as archivo:
                    archivo.write(root)
    
            texto_imprimir.insert(tk.END, "Solicitud completada correctamente.\n")
        
        except:
            texto_imprimir.insert(tk.END, "Se ha producido un error. Inténtelo más tarde.\n")

    else:
        texto_imprimir.insert(tk.END, "El número introducido es inválido. Inténtelo más tarde.\n")

# main()