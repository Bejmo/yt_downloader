import os
import requests
from ytmusicapi import YTMusic
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

def buscar_miniatura_youtube_music(query):
    # Inicializa YTMusic
    ytmusic = YTMusic()

    # Busca canciones en YouTube Music
    resultados = ytmusic.search(query, filter='songs', limit=1)

    if resultados:
        cancion = resultados[0]
        if 'thumbnails' in cancion:
            # La miniatura se encuentra en la lista 'thumbnails'
            thumbnail_url = cancion['thumbnails'][-1]['url']  # La más grande es la última
            return thumbnail_url
    return None

def descargar_imagen(url, ruta):
    response = requests.get(url)
    if response.status_code == 200:
        with open(ruta, 'wb') as f:
            f.write(response.content)

def agregar_miniatura_a_mp3(mp3_path, image_path):
    try:
        # Cargar el archivo .mp3 y su metadata
        audio = MP3(mp3_path, ID3=ID3)

        # Si el archivo no tiene una etiqueta ID3, se la añadimos
        try:
            audio.add_tags()
        except error:
            pass

        # Cargar la imagen descargada
        with open(image_path, 'rb') as img:
            # Añadir la imagen a la metadata del archivo .mp3
            audio.tags.add(
                APIC(
                    encoding=3,  # UTF-8
                    mime='image/jpeg',  # Tipo MIME de la imagen
                    type=3,  # Tipo 3 es la portada frontal
                    desc='Cover',
                    data=img.read()  # Cargar los datos de la imagen
                )
            )

        # Guardar los cambios en el archivo .mp3
        audio.save()
        print(f'Miniatura añadida a {mp3_path}')

    except Exception as e:
        print(f'Error al agregar la miniatura a {mp3_path}: {e}')

def eliminar_imagen(image_path):
    try:
        os.remove(image_path)
        print(f'Imagen {image_path} eliminada.')
    except Exception as e:
        print(f'Error al eliminar {image_path}: {e}')

def obtener_archivos_mp3(carpeta):
    return [f for f in os.listdir(carpeta) if f.endswith('.mp3')]

# FUNCIÓN QUE SE LLAMA DESDE funciones_yt.py
def download_thumnail(archivo_mp3):
    carpeta = os.path.dirname(archivo_mp3)
    nombre_archivo, _ = os.path.splitext(archivo_mp3)
    query = nombre_archivo  # Usamos el nombre del archivo .mp3 como búsqueda
    thumbnail_url = buscar_miniatura_youtube_music(query)

    if thumbnail_url:
        # Descargar la miniatura
        ruta_imagen = os.path.join(carpeta, f'{nombre_archivo}.jpg')
        descargar_imagen(thumbnail_url, ruta_imagen)

        # Agregar la miniatura al archivo .mp3
        ruta_mp3 = os.path.join(carpeta, archivo_mp3)
        agregar_miniatura_a_mp3(ruta_mp3, ruta_imagen)

        # Eliminar la miniatura después de haberla añadido al archivo .mp3
        eliminar_imagen(ruta_imagen)
    else:
        print(f'No se encontró miniatura para {archivo_mp3}')

def main(carpeta):
    archivos_mp3 = obtener_archivos_mp3(carpeta)

    for archivo_mp3 in archivos_mp3:
        nombre_archivo, _ = os.path.splitext(archivo_mp3)
        query = nombre_archivo  # Usamos el nombre del archivo .mp3 como búsqueda
        thumbnail_url = buscar_miniatura_youtube_music(query)

        if thumbnail_url:
            # Descargar la miniatura
            ruta_imagen = os.path.join(carpeta, f'{nombre_archivo}.jpg')
            descargar_imagen(thumbnail_url, ruta_imagen)

            # Agregar la miniatura al archivo .mp3
            ruta_mp3 = os.path.join(carpeta, archivo_mp3)
            agregar_miniatura_a_mp3(ruta_mp3, ruta_imagen)

            # Eliminar la miniatura después de haberla añadido al archivo .mp3
            eliminar_imagen(ruta_imagen)
        else:
            print(f'No se encontró miniatura para {archivo_mp3}')

if __name__ == '__main__':
    carpeta = input("Introduce la ruta de la carpeta con los archivos .mp3: ")
    main(carpeta)
