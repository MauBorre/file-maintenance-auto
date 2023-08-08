import os
import shutil
from datetime import datetime, timedelta

# Establecer el directorio a trabajar
folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# Establecer a donde se moveran los archivos para su eliminacion
to_delete_folder_path = os.path.join(os.path.expanduser('~'), 'to_delete')

# Crear el directorio si no existe...
if not os.path.exists(to_delete_folder_path):
    os.makedirs(to_delete_folder_path)

# Lista de archivos en el directorio
files = os.listdir(folder_path)

# Obtener la fecha
now = datetime.now()

# Recorrer la lista de archivos
for file in files:
    # Obtener el directorio del archivo
    file_path = os.path.join(folder_path, file)

    # Obtener la fecha de modificacion del archivo
    modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))

    # Calcular la diferencia con respecto a la fecha actual
    time_difference = now - modified_date

    # Si el archivo se mantuvo sin modificar por 30 dias, mover al directorio correspondiente.
    if time_difference > timedelta(days=30):
        shutil.move(file_path, to_delete_folder_path)