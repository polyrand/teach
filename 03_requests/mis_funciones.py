import json
import os

def guardar_json(datos, nombre_archivo):
    """
    Guarda datos en formato JSON si no existe el archivo.
    
    Si existe, devuelve una lista de los archivos en el directorio y un error que podemos
    mostrar usando `raise`.
    """
    
    error = None
    
    if os.path.exists(nombre_archivo):
        print("el archivo ya existe")
        error = FileExistsError
        return [archivo for archivo in os.listdir() if not archivo.startswith(".") and not archivo.startswith("_")], error

    string_json = json.dumps(datos)

    with open(nombre_archivo, "w") as f:
        f.write(string_json)

    return nombre_archivo, error