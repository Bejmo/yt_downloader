from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, error

# Modifica la metadafa del archivo "mp3_file", que es la dirección del archivo
def modificar_metadata(mp3_file, title, artist):
    # Esperar por seguridad

    # Cargar los metadatos del archivo MP3
    metadata = EasyID3(mp3_file)

    # Modificar los metadatos
    metadata['title'] = title
    metadata['artist'] = artist
    
    # Añadir el álbum de la canción
    # if (album): metadata['album'] = album
    
    # Añadir la letra a la canción
    # if (letra): metadata['USLT'] = USLT(encoding=Encoding.UTF8, lang='spa', desc='Letra', text=letra)
    
    # Agregar o reemplazar la carátula
    # with open(cover_image, 'rb') as albumart:
    #     metadata['APIC'] = APIC(
    #         encoding=3,  # UTF-8
    #         mime='image/jpeg',  # Tipo MIME de la imagen
    #         type=3,  # 3 significa carátula frontal
    #         desc='Cover',
    #         data=albumart.read()  # Leer los bytes de la imagen
    #     )

    metadata.save()

# PRUEBAS
# file_name = "Reality_Replay.mp3"
# current_directory = os.getcwd()

# mp3_file = os.path.join(current_directory, file_name)
# title = "Replay"
# artist = "Reality"
# modificar_metadata(mp3_file, title, artist, "", "")