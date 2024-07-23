import base64

# Lee el archivo de icono y codifícalo en base64
with open('yt.ico', 'rb') as file:
    icon_data = file.read()

# Codifica los datos en base64 para incluirlos en el código fuente
encoded_icon_data = base64.b64encode(icon_data).decode('utf-8')

# Escribe el código fuente que puede ser utilizado para acceder al icono
with open('icon_data.py', 'w') as file:
    file.write(f"""
ICON_DATA = b'{encoded_icon_data}'
""")