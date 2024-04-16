import tkinter as tk
from pytube import YouTube
from pytube import Playlist
import pandas as pd
import os
import subprocess

# CONVERTIR AUDIO
def convert_to_audio(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Success.")
    except subprocess.CalledProcessError as e:
        print("Conversion failed.")

# ------------------------------------------------ #

# INICIALIZACIÓN AUDIO_YT
# Crear directorio de "metadata" donde se encuentra el directorio "root".
directorio_actual = os.path.dirname(__file__)
directorio_metadata = os.path.join(directorio_actual, 'metadata')
nombre_archivo = 'ruta.txt'
ruta_archivo = os.path.join(directorio_metadata, nombre_archivo)
root = "" # Directorio que contiene la ruta donde se guardarán las descargas.

# Crear directorio de "root"
if not os.path.exists(directorio_metadata): # No existe "root": se crea.
    os.makedirs(directorio_metadata)
    root = os.path.join(directorio_actual, 'downloads')
    
    # Escribir el default path en el archivo
    with open(ruta_archivo, 'w') as archivo:
        directorio_descargas = os.path.join(directorio_actual, 'downloads')
        if not os.path.exists(root):
            os.makedirs(root)
        archivo.write(root)

# ------------------------------------------------ #

# FUNCIONES AUDIO_YT
        
# Descarga el audio de un vídeo de YouTube a través de la URL.
# actualizar indica si es una actualización de playlist (1) o no (0)
def descargar_audio_youtube(yt, destino, actualizar):
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destino)
    # AÑADIR CONVESION DE AUDIO
    # base, ext = os.path.splitext(out_file) # Separa la extensión del nombre
    # new_file = base + '.mp3'
    # try: # Soluciona error de tener un nombre raro y no detectarlo con yt.title en "actualizar_playlist"
    #     os.rename(out_file, new_file)
    #     name_file = yt.title + '.mp3'
    #     if (actualizar == 1):
    #         texto_imprimir.insert(tk.END, "Actualizando. Añadiendo: ", name_file, "\n")
    #     else:
    #         texto_imprimir.insert(tk.END, "Descargando: ", str(name_file), "\n")
    # except:
    #     os.remove(out_file)
    texto_imprimir.insert(tk.END, "Descargado.\n")

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

# ------------------------------------------------ #

# FUNCIONES BOTONES

# Variable global para saber el estado del programa.
# estado == 0 -> Ningún botón pulsado
# estado == 1 -> descargar vídeo
# estado == 2 -> descargar playlist
# estado == 3 -> modificar playlist
# estado == 4 -> modificar root path
estado = 0

def enviar():
    global estado, root, ruta_archivo
    # Cargar directorio de root (por si se ha modificado)
    with open(ruta_archivo, 'r') as archivo:
        root = archivo.read()
    url = entrada_enlace.get()
    directorio = entrada_directorio.get()
    directorio = os.path.join(root, directorio)

    # Ver el estado en el que se encuentra y actuar en consecuencia.
    if (estado == 0):
        texto_imprimir.insert(tk.END, "No hay ningúna opción pulsada.\n")
        return
    elif (estado == 1):
        yt = YouTube(url)
        descargar_audio_youtube(yt, directorio, 0)
    elif (estado == 2):
        p = Playlist(url)
        descargar_playlist(p, directorio)
    elif (estado == 3):
        p = Playlist(url)
        actualizar_playlist(p, directorio)
    elif (estado == 4):
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(url) # Se guarda la entrada de la url.
            texto_imprimir.insert(tk.END, "Root modificado.\n")

    estado = 0
    borrar_contenido_button()

def descargar_video_button():
    global estado
    estado = 1
    texto_imprimir.insert(tk.END, "Descargar vídeo.\n")

def descargar_playlist_button():
    global estado
    estado = 2
    texto_imprimir.insert(tk.END, "Descargar playlist.\n")

def actualizar_playlist_button():
    global estado
    estado = 3
    texto_imprimir.insert(tk.END, "Actualizar playlist.\n")

def modificar_root_button():
    global estado
    estado = 4
    texto_imprimir.insert(tk.END, "Modificar root path.\nIntroduzca el valor de la nueva ruta en la barra de URL (tiene que ser válida para su sitema operativo) y pulse el botón de enviar.\n")

def borrar_contenido_button():
    entrada_enlace.delete(0, tk.END)
    entrada_directorio.delete(0, tk.END)

def borrar_contenido_salida_button():
    texto_imprimir.delete(1.0, tk.END)

# ------------------------------------------------ #

# BOTONES

# Crear ventana principal
ventana = tk.Tk()
ventana.title("YouTube MP3")
# Cambiar el icono de la ventana
ventana.iconbitmap("yt.ico")

# Crear barra de entrada del enlace
entrada_enlace = tk.Entry(ventana, width=100)  # Ajusta el tamaño según lo necesites
entrada_enlace.grid(row=0, column=0, columnspan=2)  # Usamos columnspan para que ocupe dos columnas

# Crear barra de entrada del directorio
entrada_directorio = tk.Entry(ventana, width=100)
entrada_directorio.grid(row=1, column=0, columnspan=2)  # Usamos columnspan para que ocupe dos columnas


# Crear botones
enviar = tk.Button(ventana, text="Enviar", command=enviar, width=10, height=2)
enviar.grid(row=2, column=0, sticky="ew")  # Usamos sticky="ew" para que el botón se expanda horizontalmente

# Botón para borrar contenido de la barra de entrada
boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_contenido_button, width=10, height=2)
boton_borrar.grid(row=2, column=1, sticky="ew")

descargar_video = tk.Button(ventana, text="Descargar Vídeo", command=descargar_video_button, width=10, height=2)
descargar_video.grid(row=3, column=0, sticky="ew")

descargar_playlist = tk.Button(ventana, text="Descargar Playlist", command=descargar_playlist_button, width=10, height=2)
descargar_playlist.grid(row=3, column=1, sticky="ew")

actualizar_playlist = tk.Button(ventana, text="Actualizar Playlist", command=actualizar_playlist_button, width=10, height=2)
actualizar_playlist.grid(row=4, column=0, sticky="ew")

modificar_root = tk.Button(ventana, text="Modificar Root Path", command=modificar_root_button, width=10, height=2)
modificar_root.grid(row=4, column=1, sticky="ew")

# Crear zona de texto para imprimir
texto_imprimir = tk.Text(ventana, height=20, width=100)
texto_imprimir.grid(row=5, column=0, columnspan=2)  # Usamos columnspan para que ocupe dos columnas

# Botón para limpiar la salida.
boton_clear_salida = tk.Button(ventana, text="Clear", command=borrar_contenido_salida_button, width=10, height=2)
boton_clear_salida.grid(row=6, column=0, columnspan=2, sticky="ew")

ventana.mainloop()