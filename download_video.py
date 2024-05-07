import tkinter as tk
from pytube import YouTube
from pytube import Playlist
import pandas as pd
import os
import subprocess

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

destino = "D:\Documents"
url = input("Enlace: ")
yt = YouTube(url)

video = yt.streams.filter(only_audio=True).first()
out_file = video.download(output_path=destino)
base, ext = os.path.splitext(out_file) # Separa la extensión del nombre
new_file = base + '.mp3'

# Conversión a audio.
convert_to_audio(out_file, new_file)
os.remove(out_file)